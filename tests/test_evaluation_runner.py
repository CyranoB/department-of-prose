from contextlib import redirect_stdout
import importlib.util
from io import StringIO
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "evaluation/run.py"
SPEC = importlib.util.spec_from_file_location("evaluation_runner", RUNNER_PATH)
assert SPEC is not None and SPEC.loader is not None
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


class ExpectedFailureTests(unittest.TestCase):
    def test_documented_behavioral_mismatch_is_an_expected_failure(self):
        output = StringIO()
        with redirect_stdout(output):
            result = RUNNER.run_all("DET-EXTRACT-002")

        self.assertEqual(result, 0)
        self.assertIn("XFAIL DET-EXTRACT-002", output.getvalue())

    def test_execution_error_cannot_replace_expected_behavioral_failure(self):
        output = StringIO()
        with (
            patch.object(
                RUNNER.RHYTHM,
                "strip_markdown",
                side_effect=RuntimeError("synthetic parser crash"),
            ),
            redirect_stdout(output),
        ):
            result = RUNNER.run_all("DET-EXTRACT-002")

        self.assertEqual(result, 1)
        self.assertIn("unexpected RuntimeError: synthetic parser crash", output.getvalue())
        self.assertNotIn("XFAIL DET-EXTRACT-002", output.getvalue())

    def test_unrelated_assertion_path_does_not_match_exemption(self):
        fixture = {
            "status": "xfail",
            "expected_failure": {
                "path": "stdout.not_contains",
                "contains": "known phrase",
            },
        }

        self.assertFalse(
            RUNNER.matches_expected_failure(
                fixture,
                RUNNER.FixtureMismatch("returncode.equals", "known phrase"),
            )
        )
        self.assertFalse(
            RUNNER.matches_expected_failure(
                fixture,
                RUNNER.FixtureMismatch("stdout.not_contains", "different failure"),
            )
        )


if __name__ == "__main__":
    unittest.main()
