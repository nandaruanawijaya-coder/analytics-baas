-- AUTO-GENERATED metrics queries — BigQuery compatible.
-- Feature: BaaS (BukuSimpan) | Prefix: baas_ | Generated: 2026-05-22
-- Variables: @start_date DATE, @end_date DATE, @project STRING

-- ──────────────────────────────────────────────────────────
-- Metric: Kk Upload Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_kk_upload_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Registration Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_registration_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Kyc Rejected — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_kyc_rejected'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Kyc Hard Rejected — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_kyc_hard_rejected'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Reregister Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_reregister_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Link Account Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_link_account_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Default Account Setup Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_default_account_setup_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Komisi Amount Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_komisi_amount_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- Metric: Payment Failed — count and breakdown by error_code
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                       AS event_date,
  JSON_EXTRACT_SCALAR(properties, '$.error_code')        AS error_code,
  JSON_EXTRACT_SCALAR(properties, '$.rejection_reason')  AS rejection_reason,
  COUNT(*)                                               AS occurrences,
  COUNT(DISTINCT user_id)                               AS affected_users
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_payment_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1, 2, 3
ORDER BY occurrences DESC;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Kyc Approved — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_kyc_approved'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Kyc Rejected — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_kyc_rejected'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Kyc Hard Rejected — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_kyc_hard_rejected'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Account Linked — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_account_linked'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Link Account Failed — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_link_account_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Default Account Setup Succeeded — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_default_account_setup_succeeded'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Default Account Setup Failed — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_default_account_setup_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Payment Success — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_payment_success'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;

-- ──────────────────────────────────────────────────────────
-- SLA Metric: Payment Failed — p50, p90, p99 processing time
-- ──────────────────────────────────────────────────────────
SELECT
  DATE(event_time)                                                  AS event_date,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(50)]   AS p50_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(90)]   AS p90_ms,
  APPROX_QUANTILES(CAST(JSON_EXTRACT_SCALAR(properties, '$.processing_duration_ms') AS INT64), 100)[OFFSET(99)]   AS p99_ms,
  COUNTIF(JSON_EXTRACT_SCALAR(properties, '$.sla_breach') = 'true') AS sla_breaches,
  COUNT(*)                                                           AS total_events
FROM `@project.mixpanel_events.events`
WHERE event_name = 'baas_payment_failed'
  AND DATE(event_time) BETWEEN @start_date AND @end_date
GROUP BY 1
ORDER BY 1;
