"""Regression tests for marketplace packaging and shared plugin versions."""

import json
import runpy
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
HELPERS = runpy.run_path(str(ROOT / "scripts/plugin_version.py"))


class PluginVersionTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.repository = Path(self.temporary_directory.name)
        for folder in (
            ".claude-plugin",
            ".codex-plugin",
            ".agents/plugins",
            "skills/example",
        ):
            (self.repository / folder).mkdir(parents=True, exist_ok=True)
        self.write_json(
            ".claude-plugin/plugin.json",
            {"name": "department-of-prose", "version": "2.1.0", "skills": ["./skills/example"]},
        )
        self.write_json(
            ".claude-plugin/marketplace.json",
            {
                "name": "department-of-prose",
                "metadata": {"version": "2.1.0"},
                "plugins": [
                    {
                        "name": "department-of-prose",
                        "source": "./",
                        "version": "2.1.0",
                    }
                ],
            },
        )
        self.write_json(
            ".codex-plugin/plugin.json",
            {"name": "department-of-prose", "version": "2.1.0", "skills": "./skills/"},
        )
        self.write_json(
            ".agents/plugins/marketplace.json",
            {
                "name": "department-of-prose",
                "plugins": [
                    {
                        "name": "department-of-prose",
                        "source": {"source": "local", "path": "./"},
                        "policy": {
                            "installation": "AVAILABLE",
                            "authentication": "ON_INSTALL",
                        },
                        "category": "Productivity",
                    }
                ],
            },
        )
        (self.repository / "skills/example/SKILL.md").write_text("---\nname: example\n---\n")
        self.git("init")
        self.git("add", ".")
        self.git(
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.com",
            "-c",
            "commit.gpgsign=false",
            "commit",
            "-m",
            "base",
        )

    def tearDown(self):
        self.temporary_directory.cleanup()

    def write_json(self, relative_path, value):
        (self.repository / relative_path).write_text(json.dumps(value) + "\n")

    def git(self, *args):
        subprocess.run(
            ["git", *args],
            cwd=self.repository,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_current_repository_packaging_is_valid(self):
        self.assertEqual(HELPERS["check"](ROOT), "3.1.1")

    def test_plugin_change_requires_bump(self):
        (self.repository / "skills/example/SKILL.md").write_text("updated\n")
        with self.assertRaisesRegex(ValueError, "greater than"):
            HELPERS["check"](self.repository, "HEAD")
        HELPERS["bump"](self.repository, "2.2.0")
        self.assertEqual(HELPERS["check"](self.repository, "HEAD"), "2.2.0")

    def test_unrelated_change_needs_no_bump(self):
        (self.repository / "README.md").write_text("documentation\n")
        self.assertEqual(HELPERS["check"](self.repository, "HEAD"), "2.1.0")

    def test_invalid_or_non_increasing_bump_is_rejected(self):
        for value in ("2.1.0", "1.0.0", "02.2.0", "banana"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                HELPERS["bump"](self.repository, value)

    def test_manifest_drift_is_rejected(self):
        manifest_path = self.repository / ".codex-plugin/plugin.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["version"] = "2.2.0"
        manifest_path.write_text(json.dumps(manifest) + "\n")
        with self.assertRaisesRegex(ValueError, "versions differ"):
            HELPERS["check"](self.repository)

    def test_bump_repairs_drift_only_with_a_higher_version(self):
        manifest_path = self.repository / ".codex-plugin/plugin.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["version"] = "2.2.0"
        manifest_path.write_text(json.dumps(manifest) + "\n")
        with self.assertRaisesRegex(ValueError, "greater than"):
            HELPERS["bump"](self.repository, "2.2.0")
        HELPERS["bump"](self.repository, "2.3.0")
        self.assertEqual(HELPERS["check"](self.repository), "2.3.0")


if __name__ == "__main__":
    unittest.main()
