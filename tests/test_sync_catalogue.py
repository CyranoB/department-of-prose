"""Regression tests for catalogue version and evidence provenance."""

import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
HELPERS = runpy.run_path(str(ROOT / "scripts/sync-catalogue.py"))
SPEC = (ROOT / "docs/pattern-catalogue-spec.md").read_text(encoding="utf-8")
AUDIT = (ROOT / "docs/pattern-catalogue-source-audit.md").read_text(
    encoding="utf-8"
)


class CatalogueSyncTests(unittest.TestCase):
    def test_version_change_reaches_catalogue_and_evidence_notes(self):
        revised = SPEC.replace("version `1.0.0`", "version `1.0.1`")
        version, reviewed = HELPERS["catalogue_metadata"](revised, AUDIT)
        catalogue = HELPERS["render"](revised, AUDIT, version, reviewed)
        rows, sections = HELPERS["read_entries"](revised, AUDIT)
        note = HELPERS["render_deep_dive"](rows[0], sections[1], version)

        self.assertIn("Catalogue version: **1.0.1**", catalogue)
        self.assertIn("Version 1.0.1 includes", catalogue)
        self.assertIn("Catalogue version **1.0.1**", note)

    def test_vocabulary_version_must_match(self):
        revised = SPEC.replace(
            "Status: implemented catalogue policy, version `1.0.0`",
            "Status: implemented catalogue policy, version `1.0.1`",
        )
        with self.assertRaisesRegex(ValueError, "vocabulary version"):
            HELPERS["catalogue_metadata"](revised, AUDIT)

    def test_indirect_studies_do_not_gain_pattern_specific_support(self):
        _, sections = HELPERS["read_entries"](SPEC, AUDIT)
        for number in (34, 36):
            with self.subTest(number=number):
                _, _, evidence_type, strength = HELPERS["source_lines"](
                    sections[number]
                )
                self.assertEqual((evidence_type, strength), ("empirical", "unsubstantiated"))

    def test_missing_evidence_decision_is_rejected(self):
        _, sections = HELPERS["read_entries"](SPEC, AUDIT)
        section = sections[34].replace("- **Evidence strength:** unsubstantiated.\n", "")
        with self.assertRaisesRegex(ValueError, "evidence type, and strength"):
            HELPERS["source_lines"](section)


if __name__ == "__main__":
    unittest.main()
