# Contributing

Thanks for considering a contribution. This project is an opinionated agent
pipeline for generating Slidev presentations, and PRs are welcome on the
agent itself: prompts under `prompts/`, the `Makefile` pipeline, the Slidev
theme, layouts, components, and documentation.

## Before you start

- For non-trivial changes (new pipeline stages, prompt rewrites, breaking
  changes), please open an issue first to discuss the approach. For small
  fixes — typos, doc edits, obvious bugs — open a PR directly.
- Contributions are accepted under the project's [MIT License](LICENSE).

## Working locally

`outputs/` and `slides/` are gitignored. The pipeline produces them locally
for you to inspect, but they should not appear in commits on contributor PRs.

```bash
# Install dependencies
bun i

# Run the pipeline against your own inputs/introduction.md
make all

# Preview the generated deck
bun dev            # http://localhost:3030

# Export a PDF (requires Playwright Chromium)
bun export
```

The pipeline shells out to the `claude` CLI, so you need an authenticated
Claude Code session on the machine running `make all`. See the
[Quick Start](README.md#quick-start) in the README for the input format.

## Branch conventions

| Branch in this repo | Who can push                | Cloudflare Pages |
|---------------------|-----------------------------|------------------|
| `main`              | maintainers (via merge)     | production       |
| `presentation/*`    | maintainers + pipeline bot  | preview          |
| all other branches  | maintainers only            | not deployed     |

External contributors open PRs from their own forks. Forks never publish to
the upstream Cloudflare Pages project — `presentation/*` is reserved for
decks the maintainers have explicitly approved for publication. To preview
your changes, run `bun dev` locally.

## Pull requests

- Keep each PR focused on a single change.
- Include a short summary of *why* the change is needed, not just *what*
  it does.
- Rebase onto the latest `main` before requesting review.
- Verify that `outputs/` and `slides/` are not in your diff:
  `git diff --stat origin/main...HEAD` should not list them.
- Fill in the PR template — it exists to make review faster.

## Reporting bugs and requesting features

Use the templates under `.github/ISSUE_TEMPLATE/`. For bugs, the most
helpful thing you can include is a minimal `inputs/introduction.md` that
reproduces the issue, plus the relevant log from `outputs/logs/`.
