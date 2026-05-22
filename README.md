# analytics-baas

Analytics instrumentation and metric queries for **BaaS (BukuSimpan)**.

| | |
|---|---|
| **Design doc** | [BaaS Analytics Design Doc v1.0](https://bukuwarung.atlassian.net/wiki/x/AYCCmw) |
| **ERS Spec** | [Google Sheets — 68 events](https://docs.google.com/spreadsheets/d/1v2P1qLUeZuZ1nmy3PuEzUBlxBgqek0cCR171MD_iHhA/edit) |

## Contents

```
ers/
  baas-ers.csv                    Source-of-truth ERS spec (68 events, P0: 34 / P1: 24 / P2: 10)
instrumentation/
  python/instrumentation.py       Mixpanel Python SDK — typed functions for all P0+P1 events
  swift/instrumentation.swift     Mixpanel Swift SDK — iOS
  kotlin/instrumentation.kt       Mixpanel Kotlin SDK — Android
queries/
  metrics.sql                     BigQuery queries: conversion rates, SLA p50/p90/p99, error breakdown
tests/
  validation_test.py              pytest schema compliance suite (TDD)
```

## Quick start

```bash
# Re-generate all code from the ERS spec
python scripts/generate_code.py --ers-input ers/baas-ers.csv --prefix baas_ --feature "BaaS" --output-dir .

# Validate the ERS spec
python scripts/validate_ers.py --input ers/baas-ers.csv --prefix baas_

# Run schema tests (TDD — tests fail until events are implemented, that's correct)
pip install pytest mixpanel
pytest tests/validation_test.py

# Validate live data post-launch
export MIXPANEL_PROJECT_ID=your_project_id
export MIXPANEL_SERVICE_ACCOUNT_SECRET=your_secret
python scripts/validate_data.py --ers-input ers/baas-ers.csv --prefix baas_ --lookback-days 1
```

## Naming convention

Prefix: `baas_` &nbsp; Pattern: `{prefix}_{object}_{action}` &nbsp; All lowercase snake_case
