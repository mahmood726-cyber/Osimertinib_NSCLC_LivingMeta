# Osimertinib_NSCLC_LivingMeta

Osimertinib in EGFR-Mutant NSCLC: a living meta-analysis of randomized trials.

Single-file, offline HTML review dashboard (`OSIMERTINIB_NSCLC_REVIEW.html`; `index.html` redirects to it). Pooling, heterogeneity, prediction-interval and diagnostic panels run client-side from the bundled `assets/` JS engines and the review's own extracted trial data — no server or external data source at view time.

Smoke test: `python -m pytest -q test_smoke.py` (checks structural integrity of the shipped HTML).
