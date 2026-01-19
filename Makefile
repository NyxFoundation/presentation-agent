# Global configuration
PROMPTS_DIR ?= prompts
OUTPUT_DIR ?= outputs
LOG_DIR ?= $(OUTPUT_DIR)/logs

# Input variables for prompts (many are overridden from 00_audience/00_contents outputs)
PERSON_NAME ?= Taro Yamada
COMPANY ?= Company Name
INTRODUCTION ?= inputs/introduction.md
CONSTRAINTS ?= 10 slides, 5-minute briefing, internal audience
TONE ?= Internal, formal
SLIDEV_THEME ?= default
FONT ?= BIZ UDPMincho
BACKGROUND_COLOR ?= White
LANGUAGE ?= English

# Output files
AUDIENCE_OUT := $(OUTPUT_DIR)/00_audience.json
CONTENTS_OUT := $(OUTPUT_DIR)/00_contents.json
SUMMARY_OUT := $(OUTPUT_DIR)/01_decision_brief.json
GOV_OUT := $(OUTPUT_DIR)/02_governing_thought.json
SPINE_OUT := $(OUTPUT_DIR)/03_narrative_spine.json
TOC_OUT := $(OUTPUT_DIR)/04_toc_argument_tree.json
PLAN_OUT := $(OUTPUT_DIR)/05_slide_plan.json
DRAFT_OUT := $(OUTPUT_DIR)/06_slide_drafts.json
CHART_OUT := $(OUTPUT_DIR)/07_chart_edits.json
EDITS_OUT := $(OUTPUT_DIR)/08_edits.json
MANIFEST_OUT := $(OUTPUT_DIR)/09_slidev_manifest.json

# Claude configuration
export CLAUDE_CODE_PERMISSIONS := bypassPermissions
export CLAUDE_CODE_MAX_OUTPUT_TOKENS := 100000
CLAUDE_FLAGS ?= --dangerously-skip-permissions --output-format json

.PHONY: all init clean audience contents summary governing_thought narrative_spine toc_tree slide_plan slide_drafts visuals approval_edit export_slidev help

all: export_slidev

help:
	@echo "Presentation pipeline targets:"
	@echo "  audience          - Run prompts/00_audience.md"
	@echo "  contents          - Run prompts/00_contents.md"
	@echo "  summary           - Run prompts/01_summary.md"
	@echo "  governing_thought - Run prompts/02_governing_thought.md"
	@echo "  narrative_spine   - Run prompts/03_narrative_spine.md"
	@echo "  toc_tree          - Run prompts/04_toc_tree.md"
	@echo "  slide_plan        - Run prompts/05_slide_plan.md"
	@echo "  slide_drafts      - Run prompts/06_slide_drafts.md"
	@echo "  visuals           - Run prompts/07_visuals.md"
	@echo "  approval_edit     - Run prompts/08_approval_edit.md"
	@echo "  export_slidev     - Run prompts/09_export_slidev.md"
	@echo ""
	@echo "Inputs are controlled via variables (DOC_TYPE, AUDIENCE, DECISION_NEEDED, CONSTRAINTS, CONTEXT,"
	@echo "RAW_IDEAS, GOVERNING_THOUGHT, KEY_CLAIMS, AVAILABLE_FACTS, TONE, RAW_DATA_OR_CHARTS, SLIDEV_THEME)."

init:
	@mkdir -p $(OUTPUT_DIR)
	@mkdir -p $(LOG_DIR)

clean:
	@echo "Cleaning outputs..."
	@rm -rf $(OUTPUT_DIR)
	@echo "Clean completed"

# -------------------------------------------------------------------
# Helper to render a prompt with placeholder replacement via Python.
# Each target defines its own replacements.
# -------------------------------------------------------------------
define render_prompt
python - <<'PY'
from pathlib import Path
tpl = Path("$(1)").read_text()
repls = $(2)
for k, v in repls.items():
    tpl = tpl.replace(k, v)
print(tpl)
PY
endef

# Helpers to read values from JSON outputs with fallbacks
define json_or_default
python - <<'PY'
import json, sys, pathlib
path = pathlib.Path("$(1)")
fallback = $(2)
try:
    data = json.loads(path.read_text())
    val = data
    for part in "$(3)".split("."):
        if isinstance(val, dict):
            val = val.get(part, "")
        else:
            val = ""
    if isinstance(val, (list, dict)):
        import json as j
        print(j.dumps(val, ensure_ascii=False))
    elif isinstance(val, str) and val.strip():
        print(val.strip())
    else:
        print(fallback)
except Exception:
    print(fallback)
PY
endef

# -------------------------------------------------------------------
# Pipeline steps
# -------------------------------------------------------------------

audience: $(AUDIENCE_OUT)
$(AUDIENCE_OUT): $(PROMPTS_DIR)/00_audience.md | init
	@echo "Running 00_audience..."
	@START_TIME=$$(date +%s); \
	prompt="$$( $(call render_prompt,$<,{ '{{PERSON_NAME}}': \"$(PERSON_NAME)\", '{{COMPANY}}': \"$(COMPANY)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/00_audience.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/00_audience.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/00_audience.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/00_audience.json | head -1 | cut -d: -f2); \
	if [ -f "$(AUDIENCE_OUT)" ]; then \
		echo "Finished 00_audience (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(AUDIENCE_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

contents: $(CONTENTS_OUT)
$(CONTENTS_OUT): $(PROMPTS_DIR)/00_contents.md | init
	@echo "Running 00_contents..."
	@START_TIME=$$(date +%s); \
	prompt="$$( $(call render_prompt,$<,{ '{{INTRODUCTION}}': \"$(INTRODUCTION)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/00_contents.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/00_contents.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/00_contents.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/00_contents.json | head -1 | cut -d: -f2); \
	if [ -f "$(CONTENTS_OUT)" ]; then \
		echo "Finished 00_contents (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(CONTENTS_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

summary: $(SUMMARY_OUT)
$(SUMMARY_OUT): $(PROMPTS_DIR)/01_summary.md $(AUDIENCE_OUT) $(CONTENTS_OUT) | init
	@echo "Running 01_summary..."
	@START_TIME=$$(date +%s); \
	doc_type="$$( $(call json_or_default,$(AUDIENCE_OUT),"\"Proposal deck\"","proposal_inputs.doc_type") )"; \
	audience="$$( $(call json_or_default,$(AUDIENCE_OUT),"\"Executive reviewers\"","proposal_inputs.audience") )"; \
	decision_needed="$$( $(call json_or_default,$(AUDIENCE_OUT),"\"Approval for PoC\"","proposal_inputs.decision_needed") )"; \
	context="$$( $(call json_or_default,$(CONTENTS_OUT),"\"Describe the background, problem, and urgency\"","proposal_inputs.context") )"; \
	prompt="$$( $(call render_prompt,$<,{ '{{AUDIENCE_BRIEF}}': \"$(AUDIENCE_OUT)\", '{{CONTENT_BRIEF}}': \"$(CONTENTS_OUT)\", '{{CONSTRAINTS}}': \"$(CONSTRAINTS)\" }) )"; \
	prompt="$$prompt\n\nAudience defaults (from $(AUDIENCE_OUT)): doc_type=$$doc_type; audience=$$audience; decision_needed=$$decision_needed\nContent defaults (from $(CONTENTS_OUT)): context=$$context"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/01_summary.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/01_summary.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/01_summary.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/01_summary.json | head -1 | cut -d: -f2); \
	if [ -f "$(SUMMARY_OUT)" ]; then \
		echo "Finished 01_summary (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(SUMMARY_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

governing_thought: $(GOV_OUT)
$(GOV_OUT): $(PROMPTS_DIR)/02_governing_thought.md $(SUMMARY_OUT) $(CONTENTS_OUT) | init
	@echo "Running 02_governing_thought..."
	@START_TIME=$$(date +%s); \
	raw_ideas="$$( $(call json_or_default,$(CONTENTS_OUT),"\"Key idea fragments for the governing thought\"","proposal_inputs.raw_ideas") )"; \
	prompt="$$( $(call render_prompt,$<,{ '{{DECISION_BRIEF}}': \"$(SUMMARY_OUT)\", '{{CONTENT_BRIEF}}': \"$(CONTENTS_OUT)\" }) )"; \
	prompt="$$prompt\n\nRaw ideas (from $(CONTENTS_OUT)): $$raw_ideas"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/02_governing_thought.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/02_governing_thought.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/02_governing_thought.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/02_governing_thought.json | head -1 | cut -d: -f2); \
	if [ -f "$(GOV_OUT)" ]; then \
		echo "Finished 02_governing_thought (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(GOV_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

narrative_spine: $(SPINE_OUT)
$(SPINE_OUT): $(PROMPTS_DIR)/03_narrative_spine.md $(SUMMARY_OUT) $(GOV_OUT) $(CONTENTS_OUT) | init
	@echo "Running 03_narrative_spine..."
	@START_TIME=$$(date +%s); \
	gov="$$( $(call json_or_default,$(CONTENTS_OUT),"\"One-sentence governing thought\"","proposal_inputs.governing_thought_seed") )"; \
	key_claims="$$( $(call json_or_default,$(CONTENTS_OUT),"[\\\"Claim 1\\\", \\\"Claim 2\\\", \\\"Claim 3\\\"]","proposal_inputs.key_claims_seed") )"; \
	prompt="$$( $(call render_prompt,$<,{ '{{DECISION_BRIEF}}': \"$(SUMMARY_OUT)\", '{{GOVERNING_THOUGHT}}': \"$$gov\", '{{KEY_CLAIMS}}': \"$$key_claims\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/03_narrative_spine.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/03_narrative_spine.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/03_narrative_spine.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/03_narrative_spine.json | head -1 | cut -d: -f2); \
	if [ -f "$(SPINE_OUT)" ]; then \
		echo "Finished 03_narrative_spine (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(SPINE_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

toc_tree: $(TOC_OUT)
$(TOC_OUT): $(PROMPTS_DIR)/04_toc_tree.md $(SPINE_OUT) | init
	@echo "Running 04_toc_tree..."
	@START_TIME=$$(date +%s); \
	prompt="$$( $(call render_prompt,$<,{ '{{NARRATIVE_SPINE}}': \"$(SPINE_OUT)\", '{{GOVERNING_THOUGHT}}': \"$(GOVERNING_THOUGHT)\", '{{KEY_CLAIMS}}': \"$(KEY_CLAIMS)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/04_toc_tree.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/04_toc_tree.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/04_toc_tree.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/04_toc_tree.json | head -1 | cut -d: -f2); \
	if [ -f "$(TOC_OUT)" ]; then \
		echo "Finished 04_toc_tree (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(TOC_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

slide_plan: $(PLAN_OUT)
$(PLAN_OUT): $(PROMPTS_DIR)/05_slide_plan.md $(TOC_OUT) | init
	@echo "Running 05_slide_plan..."
	@START_TIME=$$(date +%s); \
	prompt="$$( $(call render_prompt,$<,{ '{{TOC_TREE}}': \"$(TOC_OUT)\", '{{CONSTRAINTS}}': \"$(CONSTRAINTS)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/05_slide_plan.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/05_slide_plan.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/05_slide_plan.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/05_slide_plan.json | head -1 | cut -d: -f2); \
	if [ -f "$(PLAN_OUT)" ]; then \
		echo "Finished 05_slide_plan (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(PLAN_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

slide_drafts: $(DRAFT_OUT)
$(DRAFT_OUT): $(PROMPTS_DIR)/06_slide_drafts.md $(PLAN_OUT) $(CONTENTS_OUT) | init
	@echo "Running 06_slide_drafts..."
	@START_TIME=$$(date +%s); \
	avail="$$( $(call json_or_default,$(CONTENTS_OUT),"\"\"","proposal_inputs.available_facts") )"; \
	prompt="$$( $(call render_prompt,$<,{ '{{SLIDE_PLAN}}': \"$(PLAN_OUT)\", '{{AVAILABLE_FACTS}}': \"$$avail\", '{{TONE}}': \"$(TONE)\", '{{LANGUAGE}}': \"$(LANGUAGE)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/06_slide_drafts.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/06_slide_drafts.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/06_slide_drafts.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/06_slide_drafts.json | head -1 | cut -d: -f2); \
	if [ -f "$(DRAFT_OUT)" ]; then \
		echo "Finished 06_slide_drafts (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(DRAFT_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

visuals: $(CHART_OUT)
$(CHART_OUT): $(PROMPTS_DIR)/07_visuals.md $(DRAFT_OUT) $(CONTENTS_OUT) | init
	@echo "Running 07_visuals..."
	@START_TIME=$$(date +%s); \
	raw_data="$$( $(call json_or_default,$(CONTENTS_OUT),"\"\"","proposal_inputs.raw_data_or_charts") )"; \
	prompt="$$( $(call render_prompt,$<,{ '{{SLIDE_DRAFTS}}': \"$(DRAFT_OUT)\", '{{RAW_DATA_OR_CHARTS}}': \"$$raw_data\", '{{LANGUAGE}}': \"$(LANGUAGE)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/07_visuals.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/07_visuals.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/07_visuals.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/07_visuals.json | head -1 | cut -d: -f2); \
	if [ -f "$(CHART_OUT)" ]; then \
		echo "Finished 07_visuals (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(CHART_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

approval_edit: $(EDITS_OUT)
$(EDITS_OUT): $(PROMPTS_DIR)/08_approval_edit.md $(PLAN_OUT) $(DRAFT_OUT) | init
	@echo "Running 08_approval_edit..."
	@START_TIME=$$(date +%s); \
	prompt="$$( $(call render_prompt,$<,{ '{{SLIDE_PLAN}}': \"$(PLAN_OUT)\", '{{SLIDE_DRAFTS}}': \"$(DRAFT_OUT)\", '{{CONSTRAINTS}}': \"$(CONSTRAINTS)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/08_approval_edit.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/08_approval_edit.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/08_approval_edit.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/08_approval_edit.json | head -1 | cut -d: -f2); \
	if [ -f "$(EDITS_OUT)" ]; then \
		echo "Finished 08_approval_edit (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(EDITS_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

export_slidev: $(MANIFEST_OUT)
$(MANIFEST_OUT): $(PROMPTS_DIR)/09_export_slidev.md $(EDITS_OUT) $(DRAFT_OUT) $(CHART_OUT) | init
	@echo "Running 09_export_slidev..."
	@START_TIME=$$(date +%s); \
	prompt="$$( $(call render_prompt,$<,{ '{{REVISED_SLIDE_PLAN}}': \"$(EDITS_OUT)\", '{{SLIDE_DRAFTS}}': \"$(DRAFT_OUT)\", '{{CHART_EDITS}}': \"$(CHART_OUT)\", '{{SLIDEV_THEME}}': \"$(SLIDEV_THEME)\", '{{FONT}}': \"$(FONT)\", '{{BACKGROUND_COLOR}}': \"$(BACKGROUND_COLOR)\", '{{LANGUAGE}}': \"$(LANGUAGE)\" }) )"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/09_export_slidev.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/09_export_slidev.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/09_export_slidev.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/09_export_slidev.json | head -1 | cut -d: -f2); \
	if [ -f "$(MANIFEST_OUT)" ]; then \
		echo "Finished 09_export_slidev (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(MANIFEST_OUT) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi
# Provide fallbacks for governing thought and key claims in 02/03 if seeds are empty
EMPTY_GOV_SEED := "One-sentence governing thought"
EMPTY_KEY_CLAIMS := "[\"Claim 1\", \"Claim 2\", \"Claim 3\"]"
