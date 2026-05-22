# AUTO-GENERATED — do not edit manually.
# Feature: BaaS (BukuSimpan) | Prefix: baas_ | Generated: 2026-05-22
# Re-generate with: python scripts/generate_code.py --ers-input ers.csv --prefix baas_

import os
import mixpanel
from typing import Optional

mp = mixpanel.Mixpanel(os.getenv('MIXPANEL_TOKEN', ''))

# ─── Standard properties ──────────────────────────────────────────────────────
# Include these on every track() call via a wrapper or super-properties:
# platform, app_version, session_id

def track_activate_cta_clicked(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps any BukuSimpan activate CTA
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_activate_cta_clicked", properties)

def track_promo_banner_clicked(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps BukuSimpan promo/marketing banner
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_promo_banner_clicked", properties)

def track_overlay_viewed(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] BukuSimpan activation overlay appears
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_overlay_viewed", properties)

def track_register_started(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Aktifkan Sekarang on overlay
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_register_started", properties)

def track_kyc_verify_started(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Verifikasi Akun (new user requiring KYC)
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kyc_verify_started", properties)

def track_mobile_required_dismissed(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] EDC user sees mobile-only notice and backs out
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_mobile_required_dismissed", properties)

def track_temp_closed_dismissed(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User sees temporary closed notice and backs out
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_temp_closed_dismissed", properties)

def track_registration_form_viewed(
    user_id: str,
    source_touchpoint: str,
    step_name: str,
    step_number: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] Registration form screen appears
    Required:  user_id, source_touchpoint, step_name, step_number, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "step_name": step_name,
        "step_number": step_number,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_registration_form_viewed", properties)

def track_phone_change_confirmed(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User confirms phone change (taps Ubah Nomor in popup)
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_phone_change_confirmed", properties)

def track_phone_change_submitted(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User submits new phone number
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_phone_change_submitted", properties)

def track_kk_upload_started(
    user_id: str,
    source_touchpoint: str,
    step_name: str,
    step_number: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Upload Kartu Keluarga
    Required:  user_id, source_touchpoint, step_name, step_number, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "step_name": step_name,
        "step_number": step_number,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kk_upload_started", properties)

def track_kk_camera_selected(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User selects camera in upload popup
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kk_camera_selected", properties)

def track_kk_file_selected(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User selects file in upload popup
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kk_file_selected", properties)

def track_kk_photo_captured(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
    attempt_number: Optional[str] = None,
) -> None:
    """
    [P0] User takes KK photo via camera
    Required:  user_id, platform, app_version, session_id
    Optional:  attempt_number
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    if attempt_number is not None:
        properties["attempt_number"] = attempt_number
    mp.track(user_id, "baas_kk_photo_captured", properties)

def track_kk_photo_retaken(
    user_id: str,
    attempt_number: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Foto Ulang on KK confirmation
    Required:  user_id, attempt_number, platform, app_version, session_id
    """
    properties = {
        "attempt_number": attempt_number,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kk_photo_retaken", properties)

def track_kk_photo_confirmed(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Lanjut on KK photo confirmation
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kk_photo_confirmed", properties)

def track_kk_upload_failed(
    user_id: str,
    error_code: str,
    error_message: str,
    platform: str,
    app_version: str,
    session_id: str,
    attempt_number: Optional[str] = None,
) -> None:
    """
    [P0] KK photo upload fails (format or server error)
    Required:  user_id, error_code, error_message, platform, app_version, session_id
    Optional:  attempt_number
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    if attempt_number is not None:
        properties["attempt_number"] = attempt_number
    mp.track(user_id, "baas_kk_upload_failed", properties)

def track_family_card_form_viewed(
    user_id: str,
    step_name: str,
    step_number: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] Family card information form appears
    Required:  user_id, step_name, step_number, platform, app_version, session_id
    """
    properties = {
        "step_name": step_name,
        "step_number": step_number,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_family_card_form_viewed", properties)

def track_family_card_form_submitted(
    user_id: str,
    step_name: str,
    step_number: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Lanjut submitting family card form
    Required:  user_id, step_name, step_number, platform, app_version, session_id
    """
    properties = {
        "step_name": step_name,
        "step_number": step_number,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_family_card_form_submitted", properties)

def track_tnc_agreed(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Ya Lanjut agreeing to T&C
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_tnc_agreed", properties)

def track_registration_submitted(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] Registration received by bank — Finished Registration page loads
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_registration_submitted", properties)

def track_registration_acknowledged(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Mengerti on Finished Registration
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_registration_acknowledged", properties)

def track_registration_failed(
    user_id: str,
    error_code: str,
    error_message: str,
) -> None:
    """
    [P0] Registration submission fails (server error)
    Required:  user_id, error_code, error_message
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
    }
    mp.track(user_id, "baas_registration_failed", properties)

def track_kyc_approved(
    user_id: str,
    processing_duration_ms: str,
    session_id: str,
    sla_breach: Optional[str] = None,
) -> None:
    """
    [P0] KYC review passes — account approved by bank
    Required:  user_id, processing_duration_ms, session_id
    Optional:  sla_breach
    """
    properties = {
        "processing_duration_ms": processing_duration_ms,
        "session_id": session_id,
    }
    if sla_breach is not None:
        properties["sla_breach"] = sla_breach
    mp.track(user_id, "baas_kyc_approved", properties)

def track_kyc_rejected(
    user_id: str,
    rejection_reason: str,
    processing_duration_ms: str,
    error_code: Optional[str] = None,
    sla_breach: Optional[str] = None,
) -> None:
    """
    [P0] KYC fails — soft rejection (can re-register)
    Required:  user_id, rejection_reason, processing_duration_ms
    Optional:  error_code, sla_breach
    """
    properties = {
        "rejection_reason": rejection_reason,
        "processing_duration_ms": processing_duration_ms,
    }
    if error_code is not None:
        properties["error_code"] = error_code
    if sla_breach is not None:
        properties["sla_breach"] = sla_breach
    mp.track(user_id, "baas_kyc_rejected", properties)

def track_kyc_hard_rejected(
    user_id: str,
    rejection_reason: str,
    processing_duration_ms: str,
    error_code: Optional[str] = None,
) -> None:
    """
    [P0] KYC fails — hard rejection (cannot re-register)
    Required:  user_id, rejection_reason, processing_duration_ms
    Optional:  error_code
    """
    properties = {
        "rejection_reason": rejection_reason,
        "processing_duration_ms": processing_duration_ms,
    }
    if error_code is not None:
        properties["error_code"] = error_code
    mp.track(user_id, "baas_kyc_hard_rejected", properties)

def track_kyc_rejected_acknowledged(
    user_id: str,
    rejection_reason: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Mengerti on rejection page
    Required:  user_id, rejection_reason, platform, app_version, session_id
    """
    properties = {
        "rejection_reason": rejection_reason,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_kyc_rejected_acknowledged", properties)

def track_reregister_started(
    user_id: str,
    attempt_number: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] Soft-rejected user taps Daftar Ulang
    Required:  user_id, attempt_number, platform, app_version, session_id
    """
    properties = {
        "attempt_number": attempt_number,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_reregister_started", properties)

def track_reregister_failed(
    user_id: str,
    error_code: str,
    error_message: str,
    attempt_number: str,
) -> None:
    """
    [P0] Re-registration submission fails
    Required:  user_id, error_code, error_message, attempt_number
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
        "attempt_number": attempt_number,
    }
    mp.track(user_id, "baas_reregister_failed", properties)

def track_link_account_cta_clicked(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] Approved user taps Hubungkan Rekening or Hubungkan Sekarang
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_link_account_cta_clicked", properties)

def track_link_account_started(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps Hubungkan Akun on Registration Success page
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_link_account_started", properties)

def track_webview_entered(
    user_id: str,
    webview_name: str,
    destination: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User leaves BW app into Nobu webview
    Required:  user_id, webview_name, destination, platform, app_version, session_id
    """
    properties = {
        "webview_name": webview_name,
        "destination": destination,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_webview_entered", properties)

def track_webview_returned(
    user_id: str,
    webview_name: str,
    outcome: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User returns from Nobu webview to BW
    Required:  user_id, webview_name, outcome, platform, app_version, session_id
    """
    properties = {
        "webview_name": webview_name,
        "outcome": outcome,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_webview_returned", properties)

def track_account_linked(
    user_id: str,
    processing_duration_ms: str,
    session_id: str,
    sla_breach: Optional[str] = None,
) -> None:
    """
    [P0] BukuSimpan account linked — backend confirmed
    Required:  user_id, processing_duration_ms, session_id
    Optional:  sla_breach
    """
    properties = {
        "processing_duration_ms": processing_duration_ms,
        "session_id": session_id,
    }
    if sla_breach is not None:
        properties["sla_breach"] = sla_breach
    mp.track(user_id, "baas_account_linked", properties)

def track_link_account_failed(
    user_id: str,
    error_code: str,
    error_message: str,
    processing_duration_ms: str,
) -> None:
    """
    [P0] Account linking fails
    Required:  user_id, error_code, error_message, processing_duration_ms
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
        "processing_duration_ms": processing_duration_ms,
    }
    mp.track(user_id, "baas_link_account_failed", properties)

def track_setup_default_cta_clicked(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User taps to set BukuSimpan as default account
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_setup_default_cta_clicked", properties)

def track_default_account_setup_succeeded(
    user_id: str,
    processing_duration_ms: str,
    session_id: str,
    sla_breach: Optional[str] = None,
) -> None:
    """
    [P0] Auto-setup of BukuSimpan as default succeeds
    Required:  user_id, processing_duration_ms, session_id
    Optional:  sla_breach
    """
    properties = {
        "processing_duration_ms": processing_duration_ms,
        "session_id": session_id,
    }
    if sla_breach is not None:
        properties["sla_breach"] = sla_breach
    mp.track(user_id, "baas_default_account_setup_succeeded", properties)

def track_default_account_setup_failed(
    user_id: str,
    error_code: str,
    error_message: str,
    processing_duration_ms: str,
) -> None:
    """
    [P0] Auto-setup fails
    Required:  user_id, error_code, error_message, processing_duration_ms
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
        "processing_duration_ms": processing_duration_ms,
    }
    mp.track(user_id, "baas_default_account_setup_failed", properties)

def track_setup_error_retry_clicked(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Coba Ulang after default setup error
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_setup_error_retry_clicked", properties)

def track_page_viewed(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User opens the BukuSimpan main page
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_page_viewed", properties)

def track_check_balance_clicked(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Cek Saldo or eye button
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_check_balance_clicked", properties)

def track_transaction_history_clicked(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Riwayat Transaksi
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_transaction_history_clicked", properties)

def track_account_detail_clicked(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Detail Akun
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_account_detail_clicked", properties)

def track_transfer_bank_clicked(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Transfer Bank — enters Payment Out flow
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_transfer_bank_clicked", properties)

def track_komisi_cairkan_clicked(
    user_id: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Cairkan Komisi Agen
    Required:  user_id, platform, app_version, session_id
    """
    properties = {
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_komisi_cairkan_clicked", properties)

def track_source_account_selected(
    user_id: str,
    account_type: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User selects Tabungan or Giro as source account
    Required:  user_id, account_type, platform, app_version, session_id
    """
    properties = {
        "account_type": account_type,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_source_account_selected", properties)

def track_komisi_amount_submitted(
    user_id: str,
    amount: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User taps Lanjut submitting komisi amount
    Required:  user_id, amount, platform, app_version, session_id
    """
    properties = {
        "amount": amount,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_komisi_amount_submitted", properties)

def track_komisi_amount_failed(
    user_id: str,
    error_code: str,
    error_message: str,
    amount: Optional[str] = None,
) -> None:
    """
    [P0] Komisi transfer submission fails
    Required:  user_id, error_code, error_message
    Optional:  amount
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
    }
    if amount is not None:
        properties["amount"] = amount
    mp.track(user_id, "baas_komisi_amount_failed", properties)

def track_payment_started(
    user_id: str,
    source_touchpoint: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User enters the Payment Out flow
    Required:  user_id, source_touchpoint, platform, app_version, session_id
    """
    properties = {
        "source_touchpoint": source_touchpoint,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_payment_started", properties)

def track_payment_bank_selected(
    user_id: str,
    bank_name: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User selects destination bank
    Required:  user_id, bank_name, platform, app_version, session_id
    """
    properties = {
        "bank_name": bank_name,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_payment_bank_selected", properties)

def track_payment_account_number_entered(
    user_id: str,
    bank_name: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User inputs destination bank account number
    Required:  user_id, bank_name, platform, app_version, session_id
    """
    properties = {
        "bank_name": bank_name,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_payment_account_number_entered", properties)

def track_payment_amount_entered(
    user_id: str,
    amount: str,
    currency: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User inputs payment amount
    Required:  user_id, amount, currency, platform, app_version, session_id
    """
    properties = {
        "amount": amount,
        "currency": currency,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_payment_amount_entered", properties)

def track_payment_method_selected(
    user_id: str,
    payment_method: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User selects payment method from drawer
    Required:  user_id, payment_method, platform, app_version, session_id
    """
    properties = {
        "payment_method": payment_method,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_payment_method_selected", properties)

def track_insufficient_balance_viewed(
    user_id: str,
    amount: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P0] User sees insufficient balance notice
    Required:  user_id, amount, platform, app_version, session_id
    """
    properties = {
        "amount": amount,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_insufficient_balance_viewed", properties)

def track_payment_processing_viewed(
    user_id: str,
    amount: str,
    payment_method: str,
    platform: str,
    app_version: str,
    session_id: str,
) -> None:
    """
    [P1] User sees payment processing screen
    Required:  user_id, amount, payment_method, platform, app_version, session_id
    """
    properties = {
        "amount": amount,
        "payment_method": payment_method,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    mp.track(user_id, "baas_payment_processing_viewed", properties)

def track_payment_confirmed(
    user_id: str,
    amount: str,
    payment_method: str,
    platform: str,
    app_version: str,
    session_id: str,
    bank_name: Optional[str] = None,
) -> None:
    """
    [P0] User submits PIN confirming payment intent
    Required:  user_id, amount, payment_method, platform, app_version, session_id
    Optional:  bank_name
    """
    properties = {
        "amount": amount,
        "payment_method": payment_method,
        "platform": platform,
        "app_version": app_version,
        "session_id": session_id,
    }
    if bank_name is not None:
        properties["bank_name"] = bank_name
    mp.track(user_id, "baas_payment_confirmed", properties)

def track_payment_success(
    user_id: str,
    amount: str,
    payment_method: str,
    processing_duration_ms: str,
    currency: str,
    sla_breach: Optional[str] = None,
) -> None:
    """
    [P0] Payment completes successfully
    Required:  user_id, amount, payment_method, processing_duration_ms, currency
    Optional:  sla_breach
    """
    properties = {
        "amount": amount,
        "payment_method": payment_method,
        "processing_duration_ms": processing_duration_ms,
        "currency": currency,
    }
    if sla_breach is not None:
        properties["sla_breach"] = sla_breach
    mp.track(user_id, "baas_payment_success", properties)

def track_payment_failed(
    user_id: str,
    error_code: str,
    error_message: str,
    payment_method: str,
    processing_duration_ms: str,
    amount: Optional[str] = None,
    sla_breach: Optional[str] = None,
) -> None:
    """
    [P0] Payment fails
    Required:  user_id, error_code, error_message, payment_method, processing_duration_ms
    Optional:  amount, sla_breach
    """
    properties = {
        "error_code": error_code,
        "error_message": error_message,
        "payment_method": payment_method,
        "processing_duration_ms": processing_duration_ms,
    }
    if amount is not None:
        properties["amount"] = amount
    if sla_breach is not None:
        properties["sla_breach"] = sla_breach
    mp.track(user_id, "baas_payment_failed", properties)

# ─── P2 events (not generated — instrument when bandwidth allows) ─────────────
# baas_learn_more_clicked — User taps Pelajari Tentang BukuSimpan
# baas_overlay_dismissed — User taps close on activation overlay
# baas_home_popup_dismissed — User taps close on homepage popup
# baas_phone_change_clicked — User taps Ubah on phone number field
# baas_tnc_link_clicked — User taps T&C / Privacy Policy link
# baas_registration_form_abandoned — User backs out during registration
# baas_debit_card_clicked — User taps Kartu Debit
# baas_change_pin_clicked — User taps Ubah Pin
# baas_reset_pin_clicked — User taps Reset Pin
# baas_payment_detail_clicked — User taps Lihat Detail Pembayaran
