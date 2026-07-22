import tempfile
import unittest
from pathlib import Path

from check_scenario_artifact import validate_artifact


class ScenarioArtifactValidationTest(unittest.TestCase):
    def write_artifact(self, directory: Path, body: str) -> Path:
        target = directory / "scenario.md"
        target.write_text(body, encoding="utf-8")
        (directory / "implementation.kt").write_text("class Implementation", encoding="utf-8")
        (directory / "test.kt").write_text("class Test", encoding="utf-8")
        return target

    def valid_artifact(self) -> str:
        return """---
status: 'done'
---

### S1: automated behavior

- **Verification:** auto

### S2: manual behavior

- **Verification:** manual - device observation

## Coverage Map

| Scenario | Verification | Status | Test | Implementation |
|----------|--------------|--------|------|----------------|
| S1 | auto | verified | test | implementation |
| S2 | manual | verified | walkthrough | implementation |

## Verification Log

- S2 device observation completed.

## Scenario Traceability

| Scenario | Verified by | Implementation |
|----------|-------------|----------------|
| S1: automated behavior | [test](test.kt#L1) | [implementation](implementation.kt#L1) |
| S2: manual behavior | manual walkthrough (see Verification Log) | [implementation](implementation.kt#L1) |
"""

    def test_accepts_completed_artifact_with_traceability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact = self.write_artifact(Path(temporary_directory), self.valid_artifact())
            self.assertEqual([], validate_artifact(artifact, require_done=True))

    def test_rejects_completed_artifact_without_traceability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact = self.write_artifact(
                Path(temporary_directory),
                self.valid_artifact().split("## Scenario Traceability", 1)[0],
            )
            self.assertIn(
                "Scenario Traceability section is missing",
                validate_artifact(artifact, require_done=True),
            )

    def test_rejects_manual_scenario_without_walkthrough_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact = self.write_artifact(
                Path(temporary_directory),
                self.valid_artifact().replace("S2 device observation completed.", "No device observation."),
            )
            self.assertIn(
                "S2 manual walkthrough is missing from Verification Log",
                validate_artifact(artifact, require_done=True),
            )


if __name__ == "__main__":
    unittest.main()
