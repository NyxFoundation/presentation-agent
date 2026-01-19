# Configuration
PROMPTS_DIR ?= prompts
OUTPUT_DIR ?= outputs
LOG_DIR ?= $(OUTPUT_DIR)/logs

# Inputs (edit here)
PERSON_NAME ?= 礒津政明
COMPANY ?= ソニーグループ株式会社,株式会社ソニー・グローバルエデュケーション,ソニーネットワークコミュニケーションズ株式会社,S.BLOX株式会社,Soneium,Startale
INTRODUCTION ?= inputs/introduction.md
CONSTRAINTS ?= 15 slides, 15-minute
TONE ?= casual
SLIDEV_THEME ?= default
FONT ?= BIZ UDPMincho
BACKGROUND_COLOR ?= White
LANGUAGE ?= English

# Outputs
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
REVIEW_OUT := $(OUTPUT_DIR)/10_executive_review.json

# Claude configuration
export CLAUDE_CODE_PERMISSIONS := bypassPermissions
export CLAUDE_CODE_MAX_OUTPUT_TOKENS := 100000
CLAUDE_FLAGS ?= --dangerously-skip-permissions --output-format json

.PHONY: all init clean audience contents summary governing_thought narrative_spine toc_tree slide_plan slide_drafts visuals approval_edit export_slidev executive_review help

all: executive_review

help:
	@echo "Targets: audience, contents, summary, governing_thought, narrative_spine, toc_tree, slide_plan, slide_drafts, visuals, approval_edit, export_slidev, executive_review"
	@echo "Edit Makefile variables (PERSON_NAME, COMPANY, INTRODUCTION, CONSTRAINTS, TONE, LANGUAGE, FONT, BACKGROUND_COLOR, SLIDEV_THEME) before running."
	@echo ""
	@echo "Pipeline: audience -> contents -> summary -> governing_thought -> narrative_spine -> toc_tree -> slide_plan -> slide_drafts -> visuals -> approval_edit -> export_slidev -> executive_review"

init:
	@mkdir -p $(OUTPUT_DIR) $(LOG_DIR)

clean:
	@rm -rf $(OUTPUT_DIR)

# -------------------------------------------------------------------
# Steps
# -------------------------------------------------------------------

audience: $(AUDIENCE_OUT)
$(AUDIENCE_OUT): $(PROMPTS_DIR)/00_audience.md | init
	@echo "Running 00_audience..."
	@prompt="$$(sed -e 's|{{PERSON_NAME}}|$(PERSON_NAME)|g' -e 's|{{COMPANY}}|$(COMPANY)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/00_audience.json; \
	if [ -f "$(AUDIENCE_OUT)" ]; then echo "Finished 00_audience"; else echo "Warning: $(AUDIENCE_OUT) not found"; fi

contents: $(CONTENTS_OUT)
$(CONTENTS_OUT): $(PROMPTS_DIR)/00_contents.md | init
	@echo "Running 00_contents..."
	@prompt="$$(sed -e 's|{{INTRODUCTION}}|$(INTRODUCTION)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/00_contents.json; \
	if [ -f "$(CONTENTS_OUT)" ]; then echo "Finished 00_contents"; else echo "Warning: $(CONTENTS_OUT) not found"; fi

summary: $(SUMMARY_OUT)
$(SUMMARY_OUT): $(PROMPTS_DIR)/01_summary.md $(AUDIENCE_OUT) $(CONTENTS_OUT) | init
	@echo "Running 01_summary..."
	@prompt="$$(sed -e 's|{{AUDIENCE_BRIEF}}|$(AUDIENCE_OUT)|g' -e 's|{{CONTENT_BRIEF}}|$(CONTENTS_OUT)|g' -e 's|{{CONSTRAINTS}}|$(CONSTRAINTS)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/01_summary.json; \
	if [ -f "$(SUMMARY_OUT)" ]; then echo "Finished 01_summary"; else echo "Warning: $(SUMMARY_OUT) not found"; fi

governing_thought: $(GOV_OUT)
$(GOV_OUT): $(PROMPTS_DIR)/02_governing_thought.md $(SUMMARY_OUT) $(CONTENTS_OUT) | init
	@echo "Running 02_governing_thought..."
	@prompt="$$(sed -e 's|{{DECISION_BRIEF}}|$(SUMMARY_OUT)|g' -e 's|{{CONTENT_BRIEF}}|$(CONTENTS_OUT)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/02_governing_thought.json; \
	if [ -f "$(GOV_OUT)" ]; then echo "Finished 02_governing_thought"; else echo "Warning: $(GOV_OUT) not found"; fi

narrative_spine: $(SPINE_OUT)
$(SPINE_OUT): $(PROMPTS_DIR)/03_narrative_spine.md $(SUMMARY_OUT) $(GOV_OUT) $(CONTENTS_OUT) | init
	@echo "Running 03_narrative_spine..."
	@prompt="$$(sed -e 's|{{DECISION_BRIEF}}|$(SUMMARY_OUT)|g' -e 's|{{GOVERNING_THOUGHT}}|$(GOV_OUT)|g' -e 's|{{KEY_CLAIMS}}|$(CONTENTS_OUT)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/03_narrative_spine.json; \
	if [ -f "$(SPINE_OUT)" ]; then echo "Finished 03_narrative_spine"; else echo "Warning: $(SPINE_OUT) not found"; fi

toc_tree: $(TOC_OUT)
$(TOC_OUT): $(PROMPTS_DIR)/04_toc_tree.md $(SPINE_OUT) $(CONTENTS_OUT) | init
	@echo "Running 04_toc_tree..."
	@prompt="$$(sed -e 's|{{NARRATIVE_SPINE}}|$(SPINE_OUT)|g' -e 's|{{GOVERNING_THOUGHT}}|$(GOV_OUT)|g' -e 's|{{KEY_CLAIMS}}|$(CONTENTS_OUT)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/04_toc_tree.json; \
	if [ -f "$(TOC_OUT)" ]; then echo "Finished 04_toc_tree"; else echo "Warning: $(TOC_OUT) not found"; fi

slide_plan: $(PLAN_OUT)
$(PLAN_OUT): $(PROMPTS_DIR)/05_slide_plan.md $(TOC_OUT) | init
	@echo "Running 05_slide_plan..."
	@prompt="$$(sed -e 's|{{TOC_TREE}}|$(TOC_OUT)|g' -e 's|{{CONSTRAINTS}}|$(CONSTRAINTS)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/05_slide_plan.json; \
	if [ -f "$(PLAN_OUT)" ]; then echo "Finished 05_slide_plan"; else echo "Warning: $(PLAN_OUT) not found"; fi

slide_drafts: $(DRAFT_OUT)
$(DRAFT_OUT): $(PROMPTS_DIR)/06_slide_drafts.md $(PLAN_OUT) $(CONTENTS_OUT) | init
	@echo "Running 06_slide_drafts..."
	@prompt="$$(sed -e 's|{{SLIDE_PLAN}}|$(PLAN_OUT)|g' -e 's|{{AVAILABLE_FACTS}}|$(CONTENTS_OUT)|g' -e 's|{{TONE}}|$(TONE)|g' -e 's|{{LANGUAGE}}|$(LANGUAGE)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/06_slide_drafts.json; \
	if [ -f "$(DRAFT_OUT)" ]; then echo "Finished 06_slide_drafts"; else echo "Warning: $(DRAFT_OUT) not found"; fi

visuals: $(CHART_OUT)
$(CHART_OUT): $(PROMPTS_DIR)/07_visuals.md $(DRAFT_OUT) $(CONTENTS_OUT) | init
	@echo "Running 07_visuals..."
	@prompt="$$(sed -e 's|{{SLIDE_DRAFTS}}|$(DRAFT_OUT)|g' -e 's|{{RAW_DATA_OR_CHARTS}}|$(CONTENTS_OUT)|g' -e 's|{{LANGUAGE}}|$(LANGUAGE)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/07_visuals.json; \
	if [ -f "$(CHART_OUT)" ]; then echo "Finished 07_visuals"; else echo "Warning: $(CHART_OUT) not found"; fi

approval_edit: $(EDITS_OUT)
$(EDITS_OUT): $(PROMPTS_DIR)/08_approval_edit.md $(PLAN_OUT) $(DRAFT_OUT) | init
	@echo "Running 08_approval_edit..."
	@prompt="$$(sed -e 's|{{SLIDE_PLAN}}|$(PLAN_OUT)|g' -e 's|{{SLIDE_DRAFTS}}|$(DRAFT_OUT)|g' -e 's|{{CONSTRAINTS}}|$(CONSTRAINTS)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/08_approval_edit.json; \
	if [ -f "$(EDITS_OUT)" ]; then echo "Finished 08_approval_edit"; else echo "Warning: $(EDITS_OUT) not found"; fi

export_slidev: $(MANIFEST_OUT)
$(MANIFEST_OUT): $(PROMPTS_DIR)/09_export_slidev.md $(EDITS_OUT) $(DRAFT_OUT) $(CHART_OUT) | init
	@echo "Running 09_export_slidev..."
	@prompt="$$(sed -e 's|{{REVISED_SLIDE_PLAN}}|$(EDITS_OUT)|g' -e 's|{{SLIDE_DRAFTS}}|$(DRAFT_OUT)|g' -e 's|{{CHART_EDITS}}|$(CHART_OUT)|g' -e 's|{{SLIDEV_THEME}}|$(SLIDEV_THEME)|g' -e 's|{{FONT}}|$(FONT)|g' -e 's|{{BACKGROUND_COLOR}}|$(BACKGROUND_COLOR)|g' -e 's|{{LANGUAGE}}|$(LANGUAGE)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/09_export_slidev.json; \
	if [ -f "$(MANIFEST_OUT)" ]; then echo "Finished 09_export_slidev"; else echo "Warning: $(MANIFEST_OUT) not found"; fi

executive_review: $(REVIEW_OUT)
$(REVIEW_OUT): $(PROMPTS_DIR)/10_executive_review.md $(MANIFEST_OUT) $(DRAFT_OUT) $(GOV_OUT) $(AUDIENCE_OUT) | init
	@echo "Running 10_executive_review..."
	@prompt="$$(sed -e 's|{{SLIDEV_MANIFEST}}|$(MANIFEST_OUT)|g' -e 's|{{SLIDE_DRAFTS}}|$(DRAFT_OUT)|g' -e 's|{{GOVERNING_THOUGHT}}|$(GOV_OUT)|g' -e 's|{{AUDIENCE_BRIEF}}|$(AUDIENCE_OUT)|g' $<)"; \
	claude $(CLAUDE_FLAGS) -p "$$prompt" > $(LOG_DIR)/10_executive_review.json; \
	if [ -f "$(REVIEW_OUT)" ]; then echo "Finished 10_executive_review"; else echo "Warning: $(REVIEW_OUT) not found"; fi
