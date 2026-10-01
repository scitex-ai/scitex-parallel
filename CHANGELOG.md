# Changelog

All notable changes to `scitex-parallel` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.9] - 2026-10-02

- Correct tuple-argument examples and include the native ordered fan-out/gather workflow.
- Repair release SIF execution with verified images and job-owned temporary paths.
- Execute the owning end-to-end workflow during release validation.


## [0.1.8] — 2025-10-01

- Untrack `_sphinx_html/` build artifacts from git.
- Refresh docs from CI build.
- Resync integrated release pipeline from scitex-dev v0.11.20.
- Resync canonical PyPI/RTD-sphinx workflows from scitex-dev.

## [0.1.7] — 2025-08-01

- Clear PA-306 + PA-307 test-quality violations.
- Normalize workflow filenames and README badges (PS-164).

## [0.1.6] — 2025-07-01

- Add subprocess-coverage wiring and PA-303 test guard.
- Add `codecov.yml` and install-test workflow.
- Recommend `uv pip install <pkg>[all]` in README.
- Bump scitex-dev pin floor to 0.11.7.
- Add from_umbrella.tar.gz archive test.
- Add weekly doc-quality workflow (pinned to newb==0.25.0).
- Add ## Architecture and ## Demo sections to README (PS141/PS142).
- Add CHANGELOG.md (audit-project PS134/PS135).
- Integrate audit-all into the test suite.
- Add mandatory installation/quick-start/python-api skill leaves.
- Adopt inline [WHAT]/[WHEN]/[HOW] marker standard in skills.
- Adopt canonical README (PS204x2, PS107/110/112/113).
- Mirror test layout + example stubs for audit-project compliance.
- Add release-safety opt-in for publish-pypi (workflow_dispatch).
- Add canonical SKILL.md frontmatter (name, description, tags).
- Fix PA501 + PA201 — `from __future__ import annotations` and `__version__` in `__all__`.

## [0.1.5]

- Initial CHANGELOG entry — see git log for prior history.
