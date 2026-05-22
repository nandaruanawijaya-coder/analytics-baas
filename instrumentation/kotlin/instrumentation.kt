// AUTO-GENERATED — do not edit manually.
// Feature: BaaS (BukuSimpan) | Prefix: baas_ | Generated: 2026-05-22

import com.mixpanel.android.mpmetrics.MixpanelAPI
import org.json.JSONObject

object Analytics {
    private lateinit var mp: MixpanelAPI
    fun init(api: MixpanelAPI) { mp = api }

    /** [P0] User taps any BukuSimpan activate CTA */
    fun trackActivateCtaClicked(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_activate_cta_clicked", props)
    }

    /** [P1] User taps BukuSimpan promo/marketing banner */
    fun trackPromoBannerClicked(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_promo_banner_clicked", props)
    }

    /** [P1] BukuSimpan activation overlay appears */
    fun trackOverlayViewed(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_overlay_viewed", props)
    }

    /** [P0] User taps Aktifkan Sekarang on overlay */
    fun trackRegisterStarted(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_register_started", props)
    }

    /** [P0] User taps Verifikasi Akun (new user requiring KYC) */
    fun trackKycVerifyStarted(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kyc_verify_started", props)
    }

    /** [P1] EDC user sees mobile-only notice and backs out */
    fun trackMobileRequiredDismissed(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_mobile_required_dismissed", props)
    }

    /** [P1] User sees temporary closed notice and backs out */
    fun trackTempClosedDismissed(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_temp_closed_dismissed", props)
    }

    /** [P1] Registration form screen appears */
    fun trackRegistrationFormViewed(userId: String, sourceTouchpoint: String, stepName: String, stepNumber: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("step_name", stepName)
        props.put("step_number", stepNumber)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_registration_form_viewed", props)
    }

    /** [P1] User confirms phone change (taps Ubah Nomor in popup) */
    fun trackPhoneChangeConfirmed(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_phone_change_confirmed", props)
    }

    /** [P1] User submits new phone number */
    fun trackPhoneChangeSubmitted(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_phone_change_submitted", props)
    }

    /** [P0] User taps Upload Kartu Keluarga */
    fun trackKkUploadStarted(userId: String, sourceTouchpoint: String, stepName: String, stepNumber: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("step_name", stepName)
        props.put("step_number", stepNumber)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kk_upload_started", props)
    }

    /** [P1] User selects camera in upload popup */
    fun trackKkCameraSelected(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kk_camera_selected", props)
    }

    /** [P1] User selects file in upload popup */
    fun trackKkFileSelected(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kk_file_selected", props)
    }

    /** [P0] User takes KK photo via camera */
    fun trackKkPhotoCaptured(userId: String, platform: String, appVersion: String, sessionId: String, attemptNumber: String? = null) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        attemptNumber?.let { props.put("attempt_number", it) }
        mp.identify(userId)
        mp.track("baas_kk_photo_captured", props)
    }

    /** [P1] User taps Foto Ulang on KK confirmation */
    fun trackKkPhotoRetaken(userId: String, attemptNumber: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("attempt_number", attemptNumber)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kk_photo_retaken", props)
    }

    /** [P0] User taps Lanjut on KK photo confirmation */
    fun trackKkPhotoConfirmed(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kk_photo_confirmed", props)
    }

    /** [P0] KK photo upload fails (format or server error) */
    fun trackKkUploadFailed(userId: String, errorCode: String, errorMessage: String, platform: String, appVersion: String, sessionId: String, attemptNumber: String? = null) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        attemptNumber?.let { props.put("attempt_number", it) }
        mp.identify(userId)
        mp.track("baas_kk_upload_failed", props)
    }

    /** [P1] Family card information form appears */
    fun trackFamilyCardFormViewed(userId: String, stepName: String, stepNumber: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("step_name", stepName)
        props.put("step_number", stepNumber)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_family_card_form_viewed", props)
    }

    /** [P0] User taps Lanjut submitting family card form */
    fun trackFamilyCardFormSubmitted(userId: String, stepName: String, stepNumber: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("step_name", stepName)
        props.put("step_number", stepNumber)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_family_card_form_submitted", props)
    }

    /** [P0] User taps Ya Lanjut agreeing to T&C */
    fun trackTncAgreed(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_tnc_agreed", props)
    }

    /** [P0] Registration received by bank — Finished Registration page loads */
    fun trackRegistrationSubmitted(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_registration_submitted", props)
    }

    /** [P1] User taps Mengerti on Finished Registration */
    fun trackRegistrationAcknowledged(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_registration_acknowledged", props)
    }

    /** [P0] Registration submission fails (server error) */
    fun trackRegistrationFailed(userId: String, errorCode: String, errorMessage: String) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        mp.identify(userId)
        mp.track("baas_registration_failed", props)
    }

    /** [P0] KYC review passes — account approved by bank */
    fun trackKycApproved(userId: String, processingDurationMs: String, sessionId: String, slaBreach: String? = null) {
        val props = JSONObject()
        props.put("processing_duration_ms", processingDurationMs)
        props.put("session_id", sessionId)
        slaBreach?.let { props.put("sla_breach", it) }
        mp.identify(userId)
        mp.track("baas_kyc_approved", props)
    }

    /** [P0] KYC fails — soft rejection (can re-register) */
    fun trackKycRejected(userId: String, rejectionReason: String, processingDurationMs: String, errorCode: String? = null, slaBreach: String? = null) {
        val props = JSONObject()
        props.put("rejection_reason", rejectionReason)
        props.put("processing_duration_ms", processingDurationMs)
        errorCode?.let { props.put("error_code", it) }
        slaBreach?.let { props.put("sla_breach", it) }
        mp.identify(userId)
        mp.track("baas_kyc_rejected", props)
    }

    /** [P0] KYC fails — hard rejection (cannot re-register) */
    fun trackKycHardRejected(userId: String, rejectionReason: String, processingDurationMs: String, errorCode: String? = null) {
        val props = JSONObject()
        props.put("rejection_reason", rejectionReason)
        props.put("processing_duration_ms", processingDurationMs)
        errorCode?.let { props.put("error_code", it) }
        mp.identify(userId)
        mp.track("baas_kyc_hard_rejected", props)
    }

    /** [P0] User taps Mengerti on rejection page */
    fun trackKycRejectedAcknowledged(userId: String, rejectionReason: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("rejection_reason", rejectionReason)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_kyc_rejected_acknowledged", props)
    }

    /** [P0] Soft-rejected user taps Daftar Ulang */
    fun trackReregisterStarted(userId: String, attemptNumber: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("attempt_number", attemptNumber)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_reregister_started", props)
    }

    /** [P0] Re-registration submission fails */
    fun trackReregisterFailed(userId: String, errorCode: String, errorMessage: String, attemptNumber: String) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        props.put("attempt_number", attemptNumber)
        mp.identify(userId)
        mp.track("baas_reregister_failed", props)
    }

    /** [P0] Approved user taps Hubungkan Rekening or Hubungkan Sekarang */
    fun trackLinkAccountCtaClicked(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_link_account_cta_clicked", props)
    }

    /** [P0] User taps Hubungkan Akun on Registration Success page */
    fun trackLinkAccountStarted(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_link_account_started", props)
    }

    /** [P0] User leaves BW app into Nobu webview */
    fun trackWebviewEntered(userId: String, webviewName: String, destination: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("webview_name", webviewName)
        props.put("destination", destination)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_webview_entered", props)
    }

    /** [P0] User returns from Nobu webview to BW */
    fun trackWebviewReturned(userId: String, webviewName: String, outcome: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("webview_name", webviewName)
        props.put("outcome", outcome)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_webview_returned", props)
    }

    /** [P0] BukuSimpan account linked — backend confirmed */
    fun trackAccountLinked(userId: String, processingDurationMs: String, sessionId: String, slaBreach: String? = null) {
        val props = JSONObject()
        props.put("processing_duration_ms", processingDurationMs)
        props.put("session_id", sessionId)
        slaBreach?.let { props.put("sla_breach", it) }
        mp.identify(userId)
        mp.track("baas_account_linked", props)
    }

    /** [P0] Account linking fails */
    fun trackLinkAccountFailed(userId: String, errorCode: String, errorMessage: String, processingDurationMs: String) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        props.put("processing_duration_ms", processingDurationMs)
        mp.identify(userId)
        mp.track("baas_link_account_failed", props)
    }

    /** [P0] User taps to set BukuSimpan as default account */
    fun trackSetupDefaultCtaClicked(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_setup_default_cta_clicked", props)
    }

    /** [P0] Auto-setup of BukuSimpan as default succeeds */
    fun trackDefaultAccountSetupSucceeded(userId: String, processingDurationMs: String, sessionId: String, slaBreach: String? = null) {
        val props = JSONObject()
        props.put("processing_duration_ms", processingDurationMs)
        props.put("session_id", sessionId)
        slaBreach?.let { props.put("sla_breach", it) }
        mp.identify(userId)
        mp.track("baas_default_account_setup_succeeded", props)
    }

    /** [P0] Auto-setup fails */
    fun trackDefaultAccountSetupFailed(userId: String, errorCode: String, errorMessage: String, processingDurationMs: String) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        props.put("processing_duration_ms", processingDurationMs)
        mp.identify(userId)
        mp.track("baas_default_account_setup_failed", props)
    }

    /** [P1] User taps Coba Ulang after default setup error */
    fun trackSetupErrorRetryClicked(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_setup_error_retry_clicked", props)
    }

    /** [P0] User opens the BukuSimpan main page */
    fun trackPageViewed(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_page_viewed", props)
    }

    /** [P1] User taps Cek Saldo or eye button */
    fun trackCheckBalanceClicked(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_check_balance_clicked", props)
    }

    /** [P1] User taps Riwayat Transaksi */
    fun trackTransactionHistoryClicked(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_transaction_history_clicked", props)
    }

    /** [P1] User taps Detail Akun */
    fun trackAccountDetailClicked(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_account_detail_clicked", props)
    }

    /** [P1] User taps Transfer Bank — enters Payment Out flow */
    fun trackTransferBankClicked(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_transfer_bank_clicked", props)
    }

    /** [P1] User taps Cairkan Komisi Agen */
    fun trackKomisiCairkanClicked(userId: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_komisi_cairkan_clicked", props)
    }

    /** [P1] User selects Tabungan or Giro as source account */
    fun trackSourceAccountSelected(userId: String, accountType: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("account_type", accountType)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_source_account_selected", props)
    }

    /** [P1] User taps Lanjut submitting komisi amount */
    fun trackKomisiAmountSubmitted(userId: String, amount: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("amount", amount)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_komisi_amount_submitted", props)
    }

    /** [P0] Komisi transfer submission fails */
    fun trackKomisiAmountFailed(userId: String, errorCode: String, errorMessage: String, amount: String? = null) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        amount?.let { props.put("amount", it) }
        mp.identify(userId)
        mp.track("baas_komisi_amount_failed", props)
    }

    /** [P0] User enters the Payment Out flow */
    fun trackPaymentStarted(userId: String, sourceTouchpoint: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("source_touchpoint", sourceTouchpoint)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_payment_started", props)
    }

    /** [P1] User selects destination bank */
    fun trackPaymentBankSelected(userId: String, bankName: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("bank_name", bankName)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_payment_bank_selected", props)
    }

    /** [P1] User inputs destination bank account number */
    fun trackPaymentAccountNumberEntered(userId: String, bankName: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("bank_name", bankName)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_payment_account_number_entered", props)
    }

    /** [P1] User inputs payment amount */
    fun trackPaymentAmountEntered(userId: String, amount: String, currency: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("amount", amount)
        props.put("currency", currency)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_payment_amount_entered", props)
    }

    /** [P0] User selects payment method from drawer */
    fun trackPaymentMethodSelected(userId: String, paymentMethod: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("payment_method", paymentMethod)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_payment_method_selected", props)
    }

    /** [P0] User sees insufficient balance notice */
    fun trackInsufficientBalanceViewed(userId: String, amount: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("amount", amount)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_insufficient_balance_viewed", props)
    }

    /** [P1] User sees payment processing screen */
    fun trackPaymentProcessingViewed(userId: String, amount: String, paymentMethod: String, platform: String, appVersion: String, sessionId: String) {
        val props = JSONObject()
        props.put("amount", amount)
        props.put("payment_method", paymentMethod)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        mp.identify(userId)
        mp.track("baas_payment_processing_viewed", props)
    }

    /** [P0] User submits PIN confirming payment intent */
    fun trackPaymentConfirmed(userId: String, amount: String, paymentMethod: String, platform: String, appVersion: String, sessionId: String, bankName: String? = null) {
        val props = JSONObject()
        props.put("amount", amount)
        props.put("payment_method", paymentMethod)
        props.put("platform", platform)
        props.put("app_version", appVersion)
        props.put("session_id", sessionId)
        bankName?.let { props.put("bank_name", it) }
        mp.identify(userId)
        mp.track("baas_payment_confirmed", props)
    }

    /** [P0] Payment completes successfully */
    fun trackPaymentSuccess(userId: String, amount: String, paymentMethod: String, processingDurationMs: String, currency: String, slaBreach: String? = null) {
        val props = JSONObject()
        props.put("amount", amount)
        props.put("payment_method", paymentMethod)
        props.put("processing_duration_ms", processingDurationMs)
        props.put("currency", currency)
        slaBreach?.let { props.put("sla_breach", it) }
        mp.identify(userId)
        mp.track("baas_payment_success", props)
    }

    /** [P0] Payment fails */
    fun trackPaymentFailed(userId: String, errorCode: String, errorMessage: String, paymentMethod: String, processingDurationMs: String, amount: String? = null, slaBreach: String? = null) {
        val props = JSONObject()
        props.put("error_code", errorCode)
        props.put("error_message", errorMessage)
        props.put("payment_method", paymentMethod)
        props.put("processing_duration_ms", processingDurationMs)
        amount?.let { props.put("amount", it) }
        slaBreach?.let { props.put("sla_breach", it) }
        mp.identify(userId)
        mp.track("baas_payment_failed", props)
    }

}