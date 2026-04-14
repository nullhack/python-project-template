# Feature: Auto-Publish Documentation on Merge to Main

## User Stories
- As a maintainer, I want documentation to be automatically built and published to GitHub Pages every time a PR is merged to main, so that the published docs are always in sync with the latest code.

## Acceptance Criteria

- `e9b6be8c-c786-4113-9920-f098a954869d`: Docs publish job only runs on push to main.
  Given: A workflow event is triggered
  When: The event is a pull_request (not a merge to main)
  Then: The docs publish job is skipped
  Test strategy: integration

- `75619a7d-7eb8-45ac-901c-b86486c30690`: Docs are built before publishing.
  Given: A commit is merged to main
  When: The publish job runs
  Then: `task doc-build` runs successfully and produces output in `docs/api/` and `docs/coverage/`
  Test strategy: integration

- `23cf4a4e-3960-458d-994d-efea5d854895`: Docs are published to GitHub Pages.
  Given: The doc-build step succeeded
  When: The publish step runs
  Then: `ghp-import` (or equivalent) deploys the `docs/` directory to the `gh-pages` branch
  Test strategy: integration

- `c580dcb9-00c7-4124-9762-70ff1192bd09`: Publish job runs only after quality and tests pass.
  Given: The quality or test job fails
  When: The CI workflow runs on main
  Then: The publish job does not execute
  Test strategy: integration

- `c942990a-a69c-473e-a820-8ce51e337262`: Workflow has least-privilege permissions for Pages deployment.
  Given: The publish job needs to write to GitHub Pages
  When: The job is defined
  Then: It has `contents: write` (or `pages: write` + `id-token: write`) and no broader permissions
  Test strategy: integration

## Notes
- GitHub Pages must be configured on the repo (source: `gh-pages` branch or GitHub Actions deployment)
- The existing `task doc-publish` already runs `ghp-import -n -p -f docs` — reuse it or inline the equivalent steps
- Out of scope: publishing on tags/releases (covered by git-release skill), PR preview deployments
- Out of scope: changing the docs toolchain (pdoc stays)
- Priority: Must
