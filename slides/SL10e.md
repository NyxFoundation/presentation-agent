---
layout: default
---

<div class="nx-kicker">OSS ／ Eris Agent Simulator</div>

<div class="os-wrap"><div class="os-card"><div class="os-left"><div class="os-id"><svg class="os-gh" viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg><span class="os-org">NyxFoundation /</span><span class="os-repo">eris-agent-simulator</span></div><div class="os-desc">本発表の実験環境そのもの。この模擬経済を、手元のマシンでそのまま再現できる。</div><div class="os-qr-row"><img class="os-qr" src="/images/qr_eris_repo.svg" alt="QR: eris-agent-simulator" /><div class="os-qr-t">リポジトリは<br/>こちらから</div></div></div><div class="os-right"><div class="os-f"><span class="os-fn">01</span><div><div class="os-fh">実プロトコルを統合</div><div class="os-fe">Uniswap・Balancer・Curve・Aave・GMX の5つ</div></div></div><div class="os-f"><span class="os-fn">02</span><div><div class="os-fh">マルチエージェント競争</div><div class="os-fe">独立プロセスのAI群が、同一メンプールで利益を競う</div></div></div><div class="os-f"><span class="os-fn">03</span><div><div class="os-fh">LLM 駆動の戦略</div><div class="os-fe">戦略は自然言語で書き、LLM が各判断を生成する</div></div></div><div class="os-f"><span class="os-fn">04</span><div><div class="os-fh">決定論的リプレイ</div><div class="os-fe">シード固定でシナリオを再現、同一条件で反復検証</div></div></div></div></div></div>

<style>
.os-wrap { display: flex; justify-content: center; margin-top: 1.1rem; }
.os-card { width: 100%; max-width: 860px; background: #fff; border: 1px solid var(--line-strong); border-radius: 12px; box-shadow: 0 2px 10px rgba(24,24,26,0.06); display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; padding: 1.5rem 1.8rem; }
.os-id { display: flex; align-items: center; gap: 8px; }
.os-gh { width: 24px; height: 24px; color: var(--ink); flex-shrink: 0; }
.os-org { font-family: var(--font-mono); font-size: 14px; color: var(--ink-dim); }
.os-repo { font-family: var(--font-mono); font-size: 16px; font-weight: 700; color: var(--accent); }
.os-desc { font-family: var(--font-jp-serif); font-size: 14.5px; line-height: 1.7; color: var(--ink-dim); margin-top: 0.6rem; }
.os-qr-row { display: flex; align-items: center; gap: 1rem; margin-top: 1rem; }
.os-qr { width: 148px; height: 148px; border: 1px solid var(--line); border-radius: 8px; display: block; }
.os-qr-t { font-family: var(--font-jp-serif); font-size: 14px; line-height: 1.7; color: var(--ink-dim); }
.os-right { border-left: 1px solid var(--line); padding-left: 2rem; display: flex; flex-direction: column; justify-content: center; gap: 0.9rem; }
.os-f { display: flex; gap: 0.75rem; align-items: flex-start; }
.os-fn { font-family: var(--font-mono); font-size: 15px; font-weight: 700; color: var(--accent); line-height: 1.5; flex-shrink: 0; }
.os-fh { font-family: var(--font-jp-serif); font-size: 15.5px; font-weight: 800; color: var(--ink); }
.os-fe { font-family: var(--font-jp-serif); font-size: 13px; line-height: 1.6; color: var(--ink-dim); margin-top: 0.12rem; }
</style>

<!--
Speaker Notes:
- ここまで見せた実験環境は、そのまま OSS として公開している（github.com/NyxFoundation/eris-agent-simulator）
- Uniswap V3 / Balancer v2 / Curve / Aave v3 / GMX v2 をフォークなしでローカル Anvil に一括デプロイ
- 複数の AI エージェントが独立プロセスとして同一メンプールで競争。戦略は prompt.md の自然言語で定義し、LLM が判断
- コーディネーターがフェアプライスを決定論的に生成 → シード固定で同一条件のバックテストを反復できる
- 監査チェックリストでは見つからない弱点を、実際に競わせて観測する PoC。研究・実験用（本番運用は想定しない）
- QR からリポジトリへ。手元で動かして、次の ASCON へ
-->
