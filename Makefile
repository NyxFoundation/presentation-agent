# Configuration variables
CONFERENCE_URL ?= https://agentwild-workshop.github.io/
CONFERENCE_TITLE ?= "Agents in the Wild: Safety, Security, and Beyond"
RESEARCH_NOTES ?= inputs/research_notes.md
TARGET_CONFERENCE ?= inputs/target_conference.md
OUTPUT_DIR ?= outputs
LOG_DIR ?= outputs/logs

# Output files
CONTRIBUTION ?= $(OUTPUT_DIR)/00_contribution.md
ABSTRACT ?= $(OUTPUT_DIR)/10_abstract.md
INTRODUCTION ?= $(OUTPUT_DIR)/20_introduction.md
RELATED_WORK ?= $(OUTPUT_DIR)/30_related_work.md
METHODOLOGY ?= $(OUTPUT_DIR)/40_methodology.md
EVALUATION ?= $(OUTPUT_DIR)/50_evaluation.md
CONCLUSION ?= $(OUTPUT_DIR)/60_conclusion.md
PAPER ?= $(OUTPUT_DIR)/99_full_paper.md

# Claude environment
export CLAUDE_CODE_PERMISSIONS := bypassPermissions
export CLAUDE_CODE_MAX_OUTPUT_TOKENS := 100000

# Claude configuration
CLAUDE_FLAGS ?= --dangerously-skip-permissions --output-format json

.PHONY: all preparation writing refinement init clean help
.PHONY: 00_conference 00_contribution
.PHONY: 10_abstract 20_introduction 30_related_work 40_methodology 50_evaluation 60_conclusion
.PHONY: 99_refine_paper

# Default target: run full pipeline
all: preparation writing refinement
	@echo "Full pipeline completed! Check $(OUTPUT_DIR)/"

# Phase targets
preparation: 00_contribution
	@echo "Preparation phase completed!"

writing: 10_abstract 20_introduction 30_related_work 40_methodology 50_evaluation 60_conclusion
	@echo "Writing phase completed!"

refinement: 99_refine_paper
	@echo "Refinement phase completed!"

# ------------------------------------------------------
# Utilities
# ------------------------------------------------------

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Configuration Variables:"
	@echo "  CONFERENCE_URL    - Target conference URL"
	@echo "  CONFERENCE_TITLE  - Conference name for web searches"
	@echo "  RESEARCH_NOTES    - Path to research notes (default: inputs/research_notes.md)"
	@echo ""
	@echo "Phase Targets:"
	@echo "  all         - Run full pipeline (preparation + writing + refinement)"
	@echo "  preparation - Run preparation phase"
	@echo "  writing     - Run writing phase (all sections)"
	@echo "  refinement  - Run refinement phase (final paper)"
	@echo ""
	@echo "Preparation Steps:"
	@echo "  00_conference   - Define target conference    -> inputs/target_conference.md"
	@echo "  00_contribution - Define research contribution -> outputs/00_contribution.md"
	@echo ""
	@echo "Writing Steps:"
	@echo "  10_abstract     - Write abstract              -> outputs/10_abstract.md"
	@echo "  20_introduction - Write introduction          -> outputs/20_introduction.md"
	@echo "  30_related_work - Write related work          -> outputs/30_related_work.md"
	@echo "  40_methodology  - Write methodology           -> outputs/40_methodology.md"
	@echo "  50_evaluation   - Write evaluation            -> outputs/50_evaluation.md"
	@echo "  60_conclusion   - Write conclusion            -> outputs/60_conclusion.md"
	@echo ""
	@echo "Refinement Steps:"
	@echo "  99_refine_paper - Integrate and refine        -> outputs/99_paper.md"
	@echo ""
	@echo "Utilities:"
	@echo "  clean - Remove generated outputs"
	@echo ""
	@echo "Example:"
	@echo "  make 00_conference CONFERENCE_URL=https://example.com CONFERENCE_TITLE=\"Conf 2026\""
	@echo "  make all"

init:
	@echo "Initializing workspace..."
	mkdir -p $(OUTPUT_DIR)
	mkdir -p $(LOG_DIR)
	mkdir -p inputs
	@echo "Workspace ready"

clean:
	@echo "Cleaning outputs..."
	rm -rf $(OUTPUT_DIR)/*.md
	rm -rf $(OUTPUT_DIR)/*.json
	rm -rf $(LOG_DIR)/*.json
	@echo "Clean completed"

# ------------------------------------------------------
# Helper function for running Claude prompts
# ------------------------------------------------------
define run_claude
	@echo "Running $(1)..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$(2)" > $(LOG_DIR)/$(3).json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/$(3).json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/$(3).json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/$(3).json | head -1 | cut -d: -f2); \
	if [ -f "$(4)" ]; then \
		echo "Finished $(1) (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(4) not generated"; exit 1; \
	fi
endef

# ------------------------------------------------------
# Preparation Steps
# ------------------------------------------------------

# Step 00_conference: Define Target Conference
00_conference: | init
	@echo "Running 00_define_target_conference.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/00_define_target_conference.md | sed 's|{{URL}}|$(CONFERENCE_URL)|g' | sed 's|{{TITLE}}|$(CONFERENCE_TITLE)|g')" > $(LOG_DIR)/00_conference.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/00_conference.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/00_conference.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/00_conference.json | head -1 | cut -d: -f2); \
	if [ -f "$(TARGET_CONFERENCE)" ]; then \
		echo "Finished 00_define_target_conference.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Warning: $(TARGET_CONFERENCE) not found (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	fi

# Step 00_contribution: Define Research Contribution
00_contribution: $(CONTRIBUTION)
$(CONTRIBUTION): prompts/00_define_contribution.md $(TARGET_CONFERENCE) $(RESEARCH_NOTES) | init
	@echo "Running 00_define_contribution.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/00_define_contribution.md | sed 's|{{RESEARCH_NOTES}}|$(RESEARCH_NOTES)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g')" > $(LOG_DIR)/00_contribution.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/00_contribution.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/00_contribution.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/00_contribution.json | head -1 | cut -d: -f2); \
	if [ -f "$(CONTRIBUTION)" ]; then \
		echo "Finished 00_define_contribution.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(CONTRIBUTION) not generated"; exit 1; \
	fi

# ------------------------------------------------------
# Writing Steps
# ------------------------------------------------------

# Step 10_abstract: Write Abstract
10_abstract: $(ABSTRACT)
$(ABSTRACT): prompts/10_write_abstract.md $(CONTRIBUTION) $(TARGET_CONFERENCE) | init
	@echo "Running 10_write_abstract.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/10_write_abstract.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g')" > $(LOG_DIR)/10_abstract.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/10_abstract.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/10_abstract.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/10_abstract.json | head -1 | cut -d: -f2); \
	if [ -f "$(ABSTRACT)" ]; then \
		echo "Finished 10_write_abstract.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(ABSTRACT) not generated"; exit 1; \
	fi

# Step 20_introduction: Write Introduction
20_introduction: $(INTRODUCTION)
$(INTRODUCTION): prompts/20_write_introduction.md $(CONTRIBUTION) $(TARGET_CONFERENCE) $(RESEARCH_NOTES) | init
	@echo "Running 20_write_introduction.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/20_write_introduction.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g' | sed 's|{{RESEARCH_NOTES}}|$(RESEARCH_NOTES)|g')" > $(LOG_DIR)/20_introduction.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/20_introduction.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/20_introduction.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/20_introduction.json | head -1 | cut -d: -f2); \
	if [ -f "$(INTRODUCTION)" ]; then \
		echo "Finished 20_write_introduction.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(INTRODUCTION) not generated"; exit 1; \
	fi

# Step 30_related_work: Write Related Work
30_related_work: $(RELATED_WORK)
$(RELATED_WORK): prompts/30_write_related_work.md $(CONTRIBUTION) $(TARGET_CONFERENCE) $(RESEARCH_NOTES) | init
	@echo "Running 30_write_related_work.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/30_write_related_work.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g' | sed 's|{{RESEARCH_NOTES}}|$(RESEARCH_NOTES)|g')" > $(LOG_DIR)/30_related_work.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/30_related_work.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/30_related_work.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/30_related_work.json | head -1 | cut -d: -f2); \
	if [ -f "$(RELATED_WORK)" ]; then \
		echo "Finished 30_write_related_work.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(RELATED_WORK) not generated"; exit 1; \
	fi

# Step 40_methodology: Write Methodology
40_methodology: $(METHODOLOGY)
$(METHODOLOGY): prompts/40_write_methodology.md $(CONTRIBUTION) $(TARGET_CONFERENCE) $(RESEARCH_NOTES) | init
	@echo "Running 40_write_methodology.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/40_write_methodology.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g' | sed 's|{{RESEARCH_NOTES}}|$(RESEARCH_NOTES)|g')" > $(LOG_DIR)/40_methodology.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/40_methodology.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/40_methodology.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/40_methodology.json | head -1 | cut -d: -f2); \
	if [ -f "$(METHODOLOGY)" ]; then \
		echo "Finished 40_write_methodology.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(METHODOLOGY) not generated"; exit 1; \
	fi

# Step 50_evaluation: Write Evaluation
50_evaluation: $(EVALUATION)
$(EVALUATION): prompts/50_write_evaluation.md $(CONTRIBUTION) $(TARGET_CONFERENCE) $(RESEARCH_NOTES) $(METHODOLOGY) | init
	@echo "Running 50_write_evaluation.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/50_write_evaluation.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g' | sed 's|{{RESEARCH_NOTES}}|$(RESEARCH_NOTES)|g' | sed 's|{{METHODOLOGY}}|$(METHODOLOGY)|g')" > $(LOG_DIR)/50_evaluation.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/50_evaluation.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/50_evaluation.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/50_evaluation.json | head -1 | cut -d: -f2); \
	if [ -f "$(EVALUATION)" ]; then \
		echo "Finished 50_write_evaluation.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(EVALUATION) not generated"; exit 1; \
	fi

# Step 60_conclusion: Write Conclusion
60_conclusion: $(CONCLUSION)
$(CONCLUSION): prompts/60_write_conclusion.md $(CONTRIBUTION) $(TARGET_CONFERENCE) $(EVALUATION) | init
	@echo "Running 60_write_conclusion.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/60_write_conclusion.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g' | sed 's|{{EVALUATION}}|$(EVALUATION)|g')" > $(LOG_DIR)/60_conclusion.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/60_conclusion.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/60_conclusion.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/60_conclusion.json | head -1 | cut -d: -f2); \
	if [ -f "$(CONCLUSION)" ]; then \
		echo "Finished 60_write_conclusion.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(CONCLUSION) not generated"; exit 1; \
	fi

# ------------------------------------------------------
# Refinement Steps
# ------------------------------------------------------

# Step 99_refine_paper: Integrate and Refine Paper
99_refine_paper: $(PAPER)
$(PAPER): prompts/99_refine_paper.md $(CONTRIBUTION) $(ABSTRACT) $(INTRODUCTION) $(RELATED_WORK) $(METHODOLOGY) $(EVALUATION) $(CONCLUSION) $(TARGET_CONFERENCE) | init
	@echo "Running 99_refine_paper.md..."; \
	START_TIME=$$(date +%s); \
	claude $(CLAUDE_FLAGS) -p "$$(cat prompts/99_refine_paper.md | sed 's|{{CONTRIBUTION}}|$(CONTRIBUTION)|g' | sed 's|{{ABSTRACT}}|$(ABSTRACT)|g' | sed 's|{{INTRO}}|$(INTRODUCTION)|g' | sed 's|{{RELATED}}|$(RELATED_WORK)|g' | sed 's|{{METHOD}}|$(METHODOLOGY)|g' | sed 's|{{EVAL}}|$(EVALUATION)|g' | sed 's|{{CONCLUSION}}|$(CONCLUSION)|g' | sed 's|{{CONFERENCE}}|$(TARGET_CONFERENCE)|g')" > $(LOG_DIR)/99_refine_paper.json; \
	END_TIME=$$(date +%s); \
	DURATION=$$((END_TIME - START_TIME)); \
	INPUT_TOKENS=$$(grep -o '"input_tokens":[0-9]*' $(LOG_DIR)/99_refine_paper.json | head -1 | cut -d: -f2); \
	OUTPUT_TOKENS=$$(grep -o '"output_tokens":[0-9]*' $(LOG_DIR)/99_refine_paper.json | head -1 | cut -d: -f2); \
	COST=$$(grep -o '"total_cost_usd":[0-9.]*' $(LOG_DIR)/99_refine_paper.json | head -1 | cut -d: -f2); \
	if [ -f "$(PAPER)" ]; then \
		echo "Finished 99_refine_paper.md (Time: $${DURATION}s | Tokens: In=$$INPUT_TOKENS, Out=$$OUTPUT_TOKENS | Cost: \$$$$COST)"; \
	else \
		echo "Error: $(PAPER) not generated"; exit 1; \
	fi
