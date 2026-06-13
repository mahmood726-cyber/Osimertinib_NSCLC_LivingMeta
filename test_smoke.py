# sentinel:skip-file -- negative-test fixture: deliberately references the placeholder
# tokens ({{...}}, REPLACE_ME, __PLACEHOLDER__) it asserts the shipped HTML must NOT contain.
"""Minimal offline-HTML smoke test for the Osimertinib NSCLC Living Meta-Analysis.

This repo ships a single-file HTML review (no npm/pytest engine of its own), so the
smoke test asserts the structural invariants that keep the offline dashboard renderable:
  - the shipped review file exists and is non-empty;
  - no UTF-8 BOM at the start of shipped HTML (breaks some parsers / our portfolio rule);
  - <script> open/close tags balance (a stray literal </script> corrupts the page);
  - no unfilled template placeholders ({{...}}, REPLACE_ME, __PLACEHOLDER__);
  - the index.html redirect points at a file that actually exists.

Run: python -m pytest -q   (or: python test_smoke.py)
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(HERE, "OSIMERTINIB_NSCLC_REVIEW.html")
INDEX = os.path.join(HERE, "index.html")


def _read(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    return raw, raw.decode("utf-8", errors="replace")


def test_review_exists_and_nonempty():
    raw, _ = _read(REVIEW)
    assert len(raw) > 1000, "review HTML is missing or implausibly small"


def test_no_bom():
    for path in (REVIEW, INDEX):
        raw, _ = _read(path)
        assert not raw.startswith(b"\xef\xbb\xbf"), f"{os.path.basename(path)} has a UTF-8 BOM"


def test_script_tags_balanced():
    _, text = _read(REVIEW)
    opens = len(re.findall(r"<script[\s>]", text))
    closes = len(re.findall(r"</script>", text))
    assert opens == closes, f"unbalanced <script> tags: {opens} open vs {closes} close"


def test_no_unfilled_placeholders():
    for path in (REVIEW, INDEX):
        _, text = _read(path)
        for tok in ("REPLACE_ME", "__PLACEHOLDER__"):
            assert tok not in text, f"{os.path.basename(path)} contains unfilled token {tok}"
        assert not re.search(r"\{\{[^}]+\}\}", text), (
            f"{os.path.basename(path)} contains an unfilled {{{{...}}}} template token"
        )


def test_index_redirect_target_exists():
    _, text = _read(INDEX)
    m = re.search(r'url=\.?/?([A-Za-z0-9_./-]+\.html)', text)
    assert m, "index.html has no meta-refresh redirect target"
    target = os.path.join(HERE, os.path.basename(m.group(1)))
    assert os.path.exists(target), f"redirect target {m.group(1)} does not exist on disk"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
    raise SystemExit(1 if failed else 0)
