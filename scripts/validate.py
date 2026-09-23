#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "references" / "social-model.md",
    ROOT / "references" / "classics-to-rules.md",
    ROOT / "references" / "modern-principles.md",
    ROOT / "references" / "language-pragmatics.md",
    ROOT / "references" / "scenario-playbook.md",
    ROOT / "references" / "action-policy.md",
    ROOT / "data" / "rules.jsonl",
    ROOT / "evals" / "cases.jsonl",
    ROOT / "dist" / "chinese-social-intelligence.system.md",
]

errors = []

for path in required:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")
if "name: chinese-social-intelligence" not in skill:
    errors.append("SKILL.md missing expected name")
if "description:" not in skill:
    errors.append("SKILL.md missing description")

def validate_jsonl(path: Path, required_keys):
    count = 0
    seen = set()
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            if not line.strip():
                continue
            count += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"{path.relative_to(ROOT)}:{lineno}: invalid JSON: {e}")
                continue
            missing = required_keys - set(obj)
            if missing:
                errors.append(f"{path.relative_to(ROOT)}:{lineno}: missing keys {sorted(missing)}")
            item_id = obj.get("id")
            if item_id in seen:
                errors.append(f"{path.relative_to(ROOT)}:{lineno}: duplicate id {item_id}")
            seen.add(item_id)
    return count

rules_count = validate_jsonl(
    ROOT / "data" / "rules.jsonl",
    {"id", "source", "principle", "when", "do", "avoid", "guardrail"},
)
eval_count = validate_jsonl(
    ROOT / "evals" / "cases.jsonl",
    {"id", "category", "scenario", "expected", "forbidden"},
)

if rules_count < 20:
    errors.append(f"expected at least 20 rules, got {rules_count}")
if eval_count < 20:
    errors.append(f"expected at least 20 eval cases, got {eval_count}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    raise SystemExit(1)

print(f"VALIDATION PASS: {rules_count} rules, {eval_count} eval cases")
