"""Lock the contributor-facing docs added for outside contributors."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_contributor_docs_match_the_readiness_plan():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "AUDIO_TOOLS_EDITION" in readme
    assert "mixer-build" in readme
    top = readme.split("## Tester", 1)[0]
    assert "CONTRIBUTING.md" in top
    assert "DESKTOP.md" in top
    assert "DEPLOY.md" in top
    assert "3.11" in top

    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    for heading in (
        "Setup",
        "Tests",
        "Two products",
        "Where to start",
        "Committed frontends",
        "Never commit",
    ):
        assert f"## {heading}" in contributing
    assert "region-picker-build" in contributing
    assert "mix-tabs-build" in contributing
    assert "npm test" in contributing
    assert "click_times_1x" not in contributing

    conduct = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
    assert "Contributor Covenant" in conduct
    assert "2.1" in conduct
    assert conduct.count("[MAINTAINER_EMAIL]") == 1

    security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
    assert "[MAINTAINER_EMAIL]" in security
    assert "public issue" in security
    for scope in ("uploads", "auth", "YouTube fetch", "desktop packaging"):
        assert scope in security
    assert "respond within" not in security.lower()
    assert "24/7" in security

    bug = (ROOT / ".github" / "ISSUE_TEMPLATE" / "bug.yml").read_text(encoding="utf-8")
    assert "name:" in bug
    assert "description:" in bug
    assert "Desktop" in bug and "Website" in bug
    assert "OS" in bug
    assert "CPU/GPU" in bug

    feature = (ROOT / ".github" / "ISSUE_TEMPLATE" / "feature.yml").read_text(encoding="utf-8")
    assert "name:" in feature
    assert "description:" in feature
    assert "Desktop" in feature and "Website" in feature

    config = (ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text(encoding="utf-8")
    assert "blank_issues_enabled: false" in config
    assert "security/policy" in config
    assert "Security" in config

    pr = (ROOT / ".github" / "pull_request_template.md").read_text(encoding="utf-8")
    assert "frontend/src/" in pr
    assert "npm test" in pr
