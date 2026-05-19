#!/usr/bin/env node
// Applies one refinement iteration: pulls the five-persona panel review out of
// the Claude stream-json log, records it, and signals the loop via exit code:
//
//   0  applied — keep iterating
//   10 applied — panel reports convergence, stop
//   20 stop — the deck score (weakest persona) stopped rising
//   1  error — model output unusable
//
// Usage: node scripts/refine-step.mjs <events.jsonl> <runDir> <ii>
//
// The slide files are edited in place by the model itself (Edit/Write tools),
// so this helper only handles the review, not the deck.

import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const [eventsPath, runDir, ii] = process.argv.slice(2);
if (!eventsPath || !runDir || !ii) {
  console.error('usage: node scripts/refine-step.mjs <events.jsonl> <runDir> <ii>');
  process.exit(1);
}

const fail = (msg) => {
  console.error(`  ✗ ${msg}`);
  process.exit(1);
};

const PERSONAS = ['donor', 'sponsor', 'researcher', 'layperson', 'design_critic'];

// --- pull the final assistant message out of the stream-json log -----------
let result = '';
for (const line of readFileSync(eventsPath, 'utf8').trim().split('\n')) {
  try {
    const o = JSON.parse(line);
    if (o.type === 'result' && typeof o.result === 'string') result = o.result;
  } catch {
    /* skip non-JSON lines */
  }
}
if (!result.trim()) fail('no final message in the model event log');
writeFileSync(join(runDir, `iter-${ii}-message.txt`), result);

// --- extract the JSON review (balanced-brace, string-aware) ----------------
const extractJson = (text) => {
  const start = text.indexOf('{');
  if (start === -1) return null;
  let depth = 0, inStr = false, esc = false;
  for (let i = start; i < text.length; i++) {
    const c = text[i];
    if (inStr) {
      if (esc) esc = false;
      else if (c === '\\') esc = true;
      else if (c === '"') inStr = false;
    } else if (c === '"') inStr = true;
    else if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) return text.slice(start, i + 1); }
  }
  return null;
};

const jsonText = extractJson(result);
if (!jsonText) fail('no JSON review object in the final message');

let review;
try {
  review = JSON.parse(jsonText);
} catch (e) {
  fail(`review JSON did not parse: ${e.message}`);
}

// --- validate the panel ----------------------------------------------------
const panel = review.panel || {};
const missing = PERSONAS.filter(
  (p) => !panel[p] || typeof panel[p].score !== 'number',
);
if (missing.length) fail(`panel is missing scored personas: ${missing.join(', ')}`);

const scores = PERSONAS.map((p) => panel[p].score);
const deckScore = Math.min(...scores);
const weakest = PERSONAS[scores.indexOf(deckScore)];

// --- compare with the previous iteration -----------------------------------
const prevPath = join(runDir, 'last-review.json');
let prevScore = null;
try {
  prevScore = Number(JSON.parse(readFileSync(prevPath, 'utf8')).deck_score);
} catch {
  /* first iteration */
}

writeFileSync(join(runDir, `iter-${ii}-review.json`), JSON.stringify(review, null, 2));
writeFileSync(prevPath, JSON.stringify(review, null, 2));

// --- report ----------------------------------------------------------------
console.log('  panel: ' + PERSONAS.map((p) => `${p} ${panel[p].score.toFixed(1)}`).join(' · '));
console.log(
  `  deck score: ${deckScore.toFixed(2)}/5  (weakest: ${weakest})` +
    (Number.isFinite(prevScore) ? `  prev ${prevScore.toFixed(2)}` : ''),
);
for (const d of panel[weakest].demands || []) console.log(`  · ${weakest} wants: ${d}`);
for (const c of review.changelog || []) console.log(`  + ${c}`);
for (const g of review.remaining_gaps || []) console.log(`  · gap: ${g}`);

// --- loop control ----------------------------------------------------------
if (review.verdict === 'converged') process.exit(10);
if (Number.isFinite(prevScore) && deckScore <= prevScore + 0.01) {
  console.log('  (weakest persona did not improve — plateau)');
  process.exit(20);
}
process.exit(0);
