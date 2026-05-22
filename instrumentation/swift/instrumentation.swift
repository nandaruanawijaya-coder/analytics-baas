// AUTO-GENERATED — do not edit manually.
// Feature: BaaS (BukuSimpan) | Prefix: baas_ | Generated: 2026-05-22

import Mixpanel

extension Analytics {

    /// [P0] User taps any BukuSimpan activate CTA
    static func trackActivateCtaClicked(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_activate_cta_clicked", properties: properties)
    }

    /// [P1] User taps BukuSimpan promo/marketing banner
    static func trackPromoBannerClicked(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_promo_banner_clicked", properties: properties)
    }

    /// [P1] BukuSimpan activation overlay appears
    static func trackOverlayViewed(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_overlay_viewed", properties: properties)
    }

    /// [P0] User taps Aktifkan Sekarang on overlay
    static func trackRegisterStarted(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_register_started", properties: properties)
    }

    /// [P0] User taps Verifikasi Akun (new user requiring KYC)
    static func trackKycVerifyStarted(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kyc_verify_started", properties: properties)
    }

    /// [P1] EDC user sees mobile-only notice and backs out
    static func trackMobileRequiredDismissed(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_mobile_required_dismissed", properties: properties)
    }

    /// [P1] User sees temporary closed notice and backs out
    static func trackTempClosedDismissed(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_temp_closed_dismissed", properties: properties)
    }

    /// [P1] Registration form screen appears
    static func trackRegistrationFormViewed(
        userId: String,
        sourceTouchpoint: String,
        stepName: String,
        stepNumber: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "step_name": stepName,
            "step_number": stepNumber,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_registration_form_viewed", properties: properties)
    }

    /// [P1] User confirms phone change (taps Ubah Nomor in popup)
    static func trackPhoneChangeConfirmed(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_phone_change_confirmed", properties: properties)
    }

    /// [P1] User submits new phone number
    static func trackPhoneChangeSubmitted(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_phone_change_submitted", properties: properties)
    }

    /// [P0] User taps Upload Kartu Keluarga
    static func trackKkUploadStarted(
        userId: String,
        sourceTouchpoint: String,
        stepName: String,
        stepNumber: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "step_name": stepName,
            "step_number": stepNumber,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_upload_started", properties: properties)
    }

    /// [P1] User selects camera in upload popup
    static func trackKkCameraSelected(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_camera_selected", properties: properties)
    }

    /// [P1] User selects file in upload popup
    static func trackKkFileSelected(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_file_selected", properties: properties)
    }

    /// [P0] User takes KK photo via camera
    static func trackKkPhotoCaptured(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String,
        attemptNumber: String? = nil
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        if let attemptNumber = attemptNumber { properties["attempt_number"] = attemptNumber }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_photo_captured", properties: properties)
    }

    /// [P1] User taps Foto Ulang on KK confirmation
    static func trackKkPhotoRetaken(
        userId: String,
        attemptNumber: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "attempt_number": attemptNumber,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_photo_retaken", properties: properties)
    }

    /// [P0] User taps Lanjut on KK photo confirmation
    static func trackKkPhotoConfirmed(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_photo_confirmed", properties: properties)
    }

    /// [P0] KK photo upload fails (format or server error)
    static func trackKkUploadFailed(
        userId: String,
        errorCode: String,
        errorMessage: String,
        platform: String,
        appVersion: String,
        sessionId: String,
        attemptNumber: String? = nil
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        if let attemptNumber = attemptNumber { properties["attempt_number"] = attemptNumber }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kk_upload_failed", properties: properties)
    }

    /// [P1] Family card information form appears
    static func trackFamilyCardFormViewed(
        userId: String,
        stepName: String,
        stepNumber: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "step_name": stepName,
            "step_number": stepNumber,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_family_card_form_viewed", properties: properties)
    }

    /// [P0] User taps Lanjut submitting family card form
    static func trackFamilyCardFormSubmitted(
        userId: String,
        stepName: String,
        stepNumber: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "step_name": stepName,
            "step_number": stepNumber,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_family_card_form_submitted", properties: properties)
    }

    /// [P0] User taps Ya Lanjut agreeing to T&C
    static func trackTncAgreed(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_tnc_agreed", properties: properties)
    }

    /// [P0] Registration received by bank — Finished Registration page loads
    static func trackRegistrationSubmitted(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_registration_submitted", properties: properties)
    }

    /// [P1] User taps Mengerti on Finished Registration
    static func trackRegistrationAcknowledged(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_registration_acknowledged", properties: properties)
    }

    /// [P0] Registration submission fails (server error)
    static func trackRegistrationFailed(
        userId: String,
        errorCode: String,
        errorMessage: String
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_registration_failed", properties: properties)
    }

    /// [P0] KYC review passes — account approved by bank
    static func trackKycApproved(
        userId: String,
        processingDurationMs: String,
        sessionId: String,
        slaBreach: String? = nil
    ) {
        var properties: Properties = [
            "processing_duration_ms": processingDurationMs,
            "session_id": sessionId,
        ]
        if let slaBreach = slaBreach { properties["sla_breach"] = slaBreach }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kyc_approved", properties: properties)
    }

    /// [P0] KYC fails — soft rejection (can re-register)
    static func trackKycRejected(
        userId: String,
        rejectionReason: String,
        processingDurationMs: String,
        errorCode: String? = nil,
        slaBreach: String? = nil
    ) {
        var properties: Properties = [
            "rejection_reason": rejectionReason,
            "processing_duration_ms": processingDurationMs,
        ]
        if let errorCode = errorCode { properties["error_code"] = errorCode }
        if let slaBreach = slaBreach { properties["sla_breach"] = slaBreach }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kyc_rejected", properties: properties)
    }

    /// [P0] KYC fails — hard rejection (cannot re-register)
    static func trackKycHardRejected(
        userId: String,
        rejectionReason: String,
        processingDurationMs: String,
        errorCode: String? = nil
    ) {
        var properties: Properties = [
            "rejection_reason": rejectionReason,
            "processing_duration_ms": processingDurationMs,
        ]
        if let errorCode = errorCode { properties["error_code"] = errorCode }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kyc_hard_rejected", properties: properties)
    }

    /// [P0] User taps Mengerti on rejection page
    static func trackKycRejectedAcknowledged(
        userId: String,
        rejectionReason: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "rejection_reason": rejectionReason,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_kyc_rejected_acknowledged", properties: properties)
    }

    /// [P0] Soft-rejected user taps Daftar Ulang
    static func trackReregisterStarted(
        userId: String,
        attemptNumber: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "attempt_number": attemptNumber,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_reregister_started", properties: properties)
    }

    /// [P0] Re-registration submission fails
    static func trackReregisterFailed(
        userId: String,
        errorCode: String,
        errorMessage: String,
        attemptNumber: String
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
            "attempt_number": attemptNumber,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_reregister_failed", properties: properties)
    }

    /// [P0] Approved user taps Hubungkan Rekening or Hubungkan Sekarang
    static func trackLinkAccountCtaClicked(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_link_account_cta_clicked", properties: properties)
    }

    /// [P0] User taps Hubungkan Akun on Registration Success page
    static func trackLinkAccountStarted(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_link_account_started", properties: properties)
    }

    /// [P0] User leaves BW app into Nobu webview
    static func trackWebviewEntered(
        userId: String,
        webviewName: String,
        destination: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "webview_name": webviewName,
            "destination": destination,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_webview_entered", properties: properties)
    }

    /// [P0] User returns from Nobu webview to BW
    static func trackWebviewReturned(
        userId: String,
        webviewName: String,
        outcome: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "webview_name": webviewName,
            "outcome": outcome,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_webview_returned", properties: properties)
    }

    /// [P0] BukuSimpan account linked — backend confirmed
    static func trackAccountLinked(
        userId: String,
        processingDurationMs: String,
        sessionId: String,
        slaBreach: String? = nil
    ) {
        var properties: Properties = [
            "processing_duration_ms": processingDurationMs,
            "session_id": sessionId,
        ]
        if let slaBreach = slaBreach { properties["sla_breach"] = slaBreach }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_account_linked", properties: properties)
    }

    /// [P0] Account linking fails
    static func trackLinkAccountFailed(
        userId: String,
        errorCode: String,
        errorMessage: String,
        processingDurationMs: String
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
            "processing_duration_ms": processingDurationMs,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_link_account_failed", properties: properties)
    }

    /// [P0] User taps to set BukuSimpan as default account
    static func trackSetupDefaultCtaClicked(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_setup_default_cta_clicked", properties: properties)
    }

    /// [P0] Auto-setup of BukuSimpan as default succeeds
    static func trackDefaultAccountSetupSucceeded(
        userId: String,
        processingDurationMs: String,
        sessionId: String,
        slaBreach: String? = nil
    ) {
        var properties: Properties = [
            "processing_duration_ms": processingDurationMs,
            "session_id": sessionId,
        ]
        if let slaBreach = slaBreach { properties["sla_breach"] = slaBreach }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_default_account_setup_succeeded", properties: properties)
    }

    /// [P0] Auto-setup fails
    static func trackDefaultAccountSetupFailed(
        userId: String,
        errorCode: String,
        errorMessage: String,
        processingDurationMs: String
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
            "processing_duration_ms": processingDurationMs,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_default_account_setup_failed", properties: properties)
    }

    /// [P1] User taps Coba Ulang after default setup error
    static func trackSetupErrorRetryClicked(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_setup_error_retry_clicked", properties: properties)
    }

    /// [P0] User opens the BukuSimpan main page
    static func trackPageViewed(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_page_viewed", properties: properties)
    }

    /// [P1] User taps Cek Saldo or eye button
    static func trackCheckBalanceClicked(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_check_balance_clicked", properties: properties)
    }

    /// [P1] User taps Riwayat Transaksi
    static func trackTransactionHistoryClicked(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_transaction_history_clicked", properties: properties)
    }

    /// [P1] User taps Detail Akun
    static func trackAccountDetailClicked(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_account_detail_clicked", properties: properties)
    }

    /// [P1] User taps Transfer Bank — enters Payment Out flow
    static func trackTransferBankClicked(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_transfer_bank_clicked", properties: properties)
    }

    /// [P1] User taps Cairkan Komisi Agen
    static func trackKomisiCairkanClicked(
        userId: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_komisi_cairkan_clicked", properties: properties)
    }

    /// [P1] User selects Tabungan or Giro as source account
    static func trackSourceAccountSelected(
        userId: String,
        accountType: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "account_type": accountType,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_source_account_selected", properties: properties)
    }

    /// [P1] User taps Lanjut submitting komisi amount
    static func trackKomisiAmountSubmitted(
        userId: String,
        amount: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "amount": amount,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_komisi_amount_submitted", properties: properties)
    }

    /// [P0] Komisi transfer submission fails
    static func trackKomisiAmountFailed(
        userId: String,
        errorCode: String,
        errorMessage: String,
        amount: String? = nil
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
        ]
        if let amount = amount { properties["amount"] = amount }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_komisi_amount_failed", properties: properties)
    }

    /// [P0] User enters the Payment Out flow
    static func trackPaymentStarted(
        userId: String,
        sourceTouchpoint: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "source_touchpoint": sourceTouchpoint,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_started", properties: properties)
    }

    /// [P1] User selects destination bank
    static func trackPaymentBankSelected(
        userId: String,
        bankName: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "bank_name": bankName,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_bank_selected", properties: properties)
    }

    /// [P1] User inputs destination bank account number
    static func trackPaymentAccountNumberEntered(
        userId: String,
        bankName: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "bank_name": bankName,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_account_number_entered", properties: properties)
    }

    /// [P1] User inputs payment amount
    static func trackPaymentAmountEntered(
        userId: String,
        amount: String,
        currency: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "amount": amount,
            "currency": currency,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_amount_entered", properties: properties)
    }

    /// [P0] User selects payment method from drawer
    static func trackPaymentMethodSelected(
        userId: String,
        paymentMethod: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "payment_method": paymentMethod,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_method_selected", properties: properties)
    }

    /// [P0] User sees insufficient balance notice
    static func trackInsufficientBalanceViewed(
        userId: String,
        amount: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "amount": amount,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_insufficient_balance_viewed", properties: properties)
    }

    /// [P1] User sees payment processing screen
    static func trackPaymentProcessingViewed(
        userId: String,
        amount: String,
        paymentMethod: String,
        platform: String,
        appVersion: String,
        sessionId: String
    ) {
        var properties: Properties = [
            "amount": amount,
            "payment_method": paymentMethod,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_processing_viewed", properties: properties)
    }

    /// [P0] User submits PIN confirming payment intent
    static func trackPaymentConfirmed(
        userId: String,
        amount: String,
        paymentMethod: String,
        platform: String,
        appVersion: String,
        sessionId: String,
        bankName: String? = nil
    ) {
        var properties: Properties = [
            "amount": amount,
            "payment_method": paymentMethod,
            "platform": platform,
            "app_version": appVersion,
            "session_id": sessionId,
        ]
        if let bankName = bankName { properties["bank_name"] = bankName }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_confirmed", properties: properties)
    }

    /// [P0] Payment completes successfully
    static func trackPaymentSuccess(
        userId: String,
        amount: String,
        paymentMethod: String,
        processingDurationMs: String,
        currency: String,
        slaBreach: String? = nil
    ) {
        var properties: Properties = [
            "amount": amount,
            "payment_method": paymentMethod,
            "processing_duration_ms": processingDurationMs,
            "currency": currency,
        ]
        if let slaBreach = slaBreach { properties["sla_breach"] = slaBreach }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_success", properties: properties)
    }

    /// [P0] Payment fails
    static func trackPaymentFailed(
        userId: String,
        errorCode: String,
        errorMessage: String,
        paymentMethod: String,
        processingDurationMs: String,
        amount: String? = nil,
        slaBreach: String? = nil
    ) {
        var properties: Properties = [
            "error_code": errorCode,
            "error_message": errorMessage,
            "payment_method": paymentMethod,
            "processing_duration_ms": processingDurationMs,
        ]
        if let amount = amount { properties["amount"] = amount }
        if let slaBreach = slaBreach { properties["sla_breach"] = slaBreach }
        Mixpanel.mainInstance().identify(distinctId: userId)
        Mixpanel.mainInstance().track(event: "baas_payment_failed", properties: properties)
    }

}