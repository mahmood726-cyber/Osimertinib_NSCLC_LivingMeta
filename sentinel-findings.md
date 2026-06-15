# sentinel-findings.md

*Written by Sentinel — WARN-tier findings.*

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:16159`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:22994`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.205829+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:31.408166+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:29984`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:35247`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36933`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36936`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43901`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43945`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44007`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:33.898532+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:16159`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:22994`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.509630+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:48.801303+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:29984`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:35247`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36933`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36936`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43901`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43945`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44007`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:45:52.460004+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:16159`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:22994`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.391026+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:45:58.572743+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:29984`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:35247`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36933`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36936`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43901`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43945`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44007`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:46:00.719533+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:8`
- **Detail:** pattern matched: - no unfilled template placeholders ({{...}}, REPLACE_ME, __PLACEHOLDER__);
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:48:48.834290+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:48`
- **Detail:** pattern matched: for tok in ("REPLACE_ME", "__PLACEHOLDER__"):
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:48:48.834370+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:16159`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:22994`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.452664+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:48:50.832578+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:29984`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:35247`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36933`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36936`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43901`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43945`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44007`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:48:55.837356+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:8`
- **Detail:** pattern matched: - no unfilled template placeholders ({{...}}, REPLACE_ME, __PLACEHOLDER__);
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:49:14.440064+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:48`
- **Detail:** pattern matched: for tok in ("REPLACE_ME", "__PLACEHOLDER__"):
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:49:14.440143+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:16159`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:22994`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:16.768734+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:17.348713+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:29984`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:35247`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36933`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36936`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43901`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43945`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44007`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:28.389822+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:16159`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:22994`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.426820+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:49:50.779221+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:29984`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:35247`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36933`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:36936`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43901`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:43945`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44007`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44339`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `OSIMERTINIB_NSCLC_REVIEW.html:44357`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:49:57.688467+00:00
