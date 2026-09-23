#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "SOURCE_CORPUS.md",
    ROOT / "references" / "social-model.md",
    ROOT / "references" / "modern-principles.md",
    ROOT / "references" / "language-pragmatics.md",
    ROOT / "references" / "action-policy.md",
    ROOT / "references" / "guides" / "INDEX.md",
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
if 'executable-guides: "460"' not in skill:
    errors.append("SKILL.md must declare 460 executable guides")

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

guide_dir = ROOT / "references" / "guides"
guide_files = sorted(
    p for p in guide_dir.glob("*.md")
    if p.name != "INDEX.md"
)
guide_ids = []
for path in guide_files:
    content = path.read_text(encoding="utf-8")
    guide_ids.extend(re.findall(r"^## (CSI-G\d{3})｜", content, flags=re.MULTILINE))

if len(guide_files) != 23:
    errors.append(f"expected 23 guide modules, got {len(guide_files)}")
if len(guide_ids) != 460:
    errors.append(f"expected 460 executable guides, got {len(guide_ids)}")
if len(set(guide_ids)) != len(guide_ids):
    errors.append("duplicate guide ids detected")
expected_ids = {f"CSI-G{i:03d}" for i in range(1, 461)}
missing_ids = sorted(expected_ids - set(guide_ids))
extra_ids = sorted(set(guide_ids) - expected_ids)
if missing_ids:
    errors.append(f"missing guide ids: {missing_ids[:10]}")
if extra_ids:
    errors.append(f"unexpected guide ids: {extra_ids[:10]}")

digest_files = sorted((ROOT / "references" / "book-digests").glob("*.md"))
if len(digest_files) < 6:
    errors.append(f"expected at least 6 book digest files, got {len(digest_files)}")

if rules_count < 20:
    errors.append(f"expected at least 20 machine-readable core rules, got {rules_count}")
if eval_count < 20:
    errors.append(f"expected at least 20 eval cases, got {eval_count}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    raise SystemExit(1)

print(
    f"VALIDATION PASS: {len(guide_ids)} guides / {len(guide_files)} modules, "
    f"{len(digest_files)} book digests, {rules_count} core rules, {eval_count} eval cases"
)
