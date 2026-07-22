import argparse
import re
from pathlib import Path


def extract_section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    return match.group(1) if match else ""


def extract_table_rows(section: str) -> list[list[str]]:
    rows = []
    for line in section.splitlines():
        if not line.startswith("|") or re.match(r"^\|[-\s|]+\|$", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] != "Scenario":
            rows.append(cells)
    return rows


def validate_relative_links(row: str, artifact: Path) -> list[str]:
    errors = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", row):
        path_text = target.split("#", 1)[0]
        if not path_text or "://" in path_text or path_text.startswith("#"):
            continue
        if not (artifact.parent / path_text).resolve().exists():
            errors.append(f"traceability link target does not exist: {target}")
    return errors


def validate_artifact(artifact: Path, require_done: bool) -> list[str]:
    text = artifact.read_text(encoding="utf-8")
    errors = []
    if require_done and not re.search(r"^status:\s*['\"]done['\"]\s*$", text, re.MULTILINE):
        errors.append("frontmatter status must be done")

    scenario_ids = re.findall(r"^### (S\d+):", text, re.MULTILINE)
    if not scenario_ids:
        return ["no scenarios found"]

    coverage_rows = extract_table_rows(extract_section(text, "Coverage Map"))
    coverage = {row[0]: row for row in coverage_rows if len(row) >= 3 and re.fullmatch(r"S\d+", row[0])}
    traceability = extract_section(text, "Scenario Traceability")
    if not traceability:
        errors.append("Scenario Traceability section is missing")
        trace_rows = {}
    else:
        trace_rows = {
            match.group(1): line
            for line in traceability.splitlines()
            if (match := re.match(r"^\|\s*(S\d+):", line))
        }

    verification_log = extract_section(text, "Verification Log")
    for scenario_id in scenario_ids:
        row = coverage.get(scenario_id)
        if row is None:
            errors.append(f"{scenario_id} is missing from Coverage Map")
            continue
        if row[2] != "verified":
            errors.append(f"{scenario_id} is not verified")
        trace_row = trace_rows.get(scenario_id)
        if trace_row is None:
            errors.append(f"{scenario_id} is missing from Scenario Traceability")
        else:
            errors.extend(validate_relative_links(trace_row, artifact))
        if row[1] == "manual" and not re.search(
            rf"(?<![A-Za-z0-9]){re.escape(scenario_id)}(?![A-Za-z0-9])",
            verification_log,
        ):
            errors.append(f"{scenario_id} manual walkthrough is missing from Verification Log")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--require-done", action="store_true")
    arguments = parser.parse_args()
    errors = validate_artifact(arguments.artifact, arguments.require_done)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"scenario artifact valid: {arguments.artifact}")


if __name__ == "__main__":
    main()
