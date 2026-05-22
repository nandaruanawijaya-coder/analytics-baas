# AUTO-GENERATED validation tests — run: pytest validation_test.py
# Feature: BaaS (BukuSimpan) | Prefix: baas_ | Generated: 2026-05-22
# These tests define the contract. They WILL FAIL until events are instrumented.

import re
import inspect
import pytest
import unittest.mock as mock
from instrumentation import track_activate_cta_clicked, track_register_started, track_kyc_verify_started, track_kk_upload_started, track_kk_photo_captured, ...

EVENT_NAME_PATTERN = re.compile(r'^[a-z][a-z0-9_]{2,254}$')
AGREED_PREFIX = 'baas_'

ALL_P0_EVENTS = [
    "baas_activate_cta_clicked",
    "baas_register_started",
    "baas_kyc_verify_started",
    "baas_kk_upload_started",
    "baas_kk_photo_captured",
    "baas_kk_photo_confirmed",
    "baas_kk_upload_failed",
    "baas_family_card_form_submitted",
    "baas_tnc_agreed",
    "baas_registration_submitted",
    "baas_registration_failed",
    "baas_kyc_approved",
    "baas_kyc_rejected",
    "baas_kyc_hard_rejected",
    "baas_kyc_rejected_acknowledged",
    "baas_reregister_started",
    "baas_reregister_failed",
    "baas_link_account_cta_clicked",
    "baas_link_account_started",
    "baas_webview_entered",
    "baas_webview_returned",
    "baas_account_linked",
    "baas_link_account_failed",
    "baas_setup_default_cta_clicked",
    "baas_default_account_setup_succeeded",
    "baas_default_account_setup_failed",
    "baas_page_viewed",
    "baas_komisi_amount_failed",
    "baas_payment_started",
    "baas_payment_method_selected",
    "baas_insufficient_balance_viewed",
    "baas_payment_confirmed",
    "baas_payment_success",
    "baas_payment_failed",
]

class TestNamingConvention:
    def test_all_event_names_match_snake_case(self):
        for name in ALL_P0_EVENTS:
            assert EVENT_NAME_PATTERN.match(name), \
                f"Event '{name}' does not match snake_case pattern"

    def test_all_event_names_have_correct_prefix(self):
        for name in ALL_P0_EVENTS:
            assert name.startswith(AGREED_PREFIX), \
                f"Event '{name}' missing prefix '{AGREED_PREFIX}'"

    def test_no_event_name_exceeds_255_chars(self):
        for name in ALL_P0_EVENTS:
            assert len(name) <= 255, f"Event '{name}' exceeds 255 characters"

class Test_TrackActivateCtaClicked:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_activate_cta_clicked(user_id="test_user_id", source_touchpoint="test_source_touchpoint", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackRegisterStarted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_register_started(user_id="test_user_id", source_touchpoint="test_source_touchpoint", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackKycVerifyStarted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_verify_started(user_id="test_user_id", source_touchpoint="test_source_touchpoint", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackKkUploadStarted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kk_upload_started(user_id="test_user_id", source_touchpoint="test_source_touchpoint", step_name="test_step_name", step_number="test_step_number", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'step_name' in props, 'step_name must be in properties'
            assert 'step_number' in props, 'step_number must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackKkPhotoCaptured:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kk_photo_captured(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kk_photo_captured(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'attempt_number' not in props, 'attempt_number must not be present when not supplied'

class Test_TrackKkPhotoConfirmed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kk_photo_confirmed(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackKkUploadFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kk_upload_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kk_upload_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'attempt_number' not in props, 'attempt_number must not be present when not supplied'

class Test_TrackFamilyCardFormSubmitted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_family_card_form_submitted(user_id="test_user_id", step_name="test_step_name", step_number="test_step_number", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'step_name' in props, 'step_name must be in properties'
            assert 'step_number' in props, 'step_number must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackTncAgreed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_tnc_agreed(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackRegistrationSubmitted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_registration_submitted(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackRegistrationFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_registration_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'

class Test_TrackKycApproved:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_approved(user_id="test_user_id", processing_duration_ms="test_processing_duration_ms", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_approved(user_id="test_user_id", processing_duration_ms="test_processing_duration_ms", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'sla_breach' not in props, 'sla_breach must not be present when not supplied'

    def test_has_processing_duration_ms_parameter(self):
        sig = inspect.signature(track_kyc_approved)
        assert 'processing_duration_ms' in sig.parameters, \
            'Backend event must accept processing_duration_ms for SLA tracking'

class Test_TrackKycRejected:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_rejected(user_id="test_user_id", rejection_reason="test_rejection_reason", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'rejection_reason' in props, 'rejection_reason must be in properties'
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_rejected(user_id="test_user_id", rejection_reason="test_rejection_reason", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' not in props, 'error_code must not be present when not supplied'
            assert 'sla_breach' not in props, 'sla_breach must not be present when not supplied'

class Test_TrackKycHardRejected:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_hard_rejected(user_id="test_user_id", rejection_reason="test_rejection_reason", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'rejection_reason' in props, 'rejection_reason must be in properties'
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_hard_rejected(user_id="test_user_id", rejection_reason="test_rejection_reason", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' not in props, 'error_code must not be present when not supplied'

class Test_TrackKycRejectedAcknowledged:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_kyc_rejected_acknowledged(user_id="test_user_id", rejection_reason="test_rejection_reason", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'rejection_reason' in props, 'rejection_reason must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackReregisterStarted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_reregister_started(user_id="test_user_id", attempt_number="test_attempt_number", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'attempt_number' in props, 'attempt_number must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackReregisterFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_reregister_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", attempt_number="test_attempt_number")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'
            assert 'attempt_number' in props, 'attempt_number must be in properties'

class Test_TrackLinkAccountCtaClicked:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_link_account_cta_clicked(user_id="test_user_id", source_touchpoint="test_source_touchpoint", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackLinkAccountStarted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_link_account_started(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackWebviewEntered:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_webview_entered(user_id="test_user_id", webview_name="test_webview_name", destination="test_destination", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'webview_name' in props, 'webview_name must be in properties'
            assert 'destination' in props, 'destination must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackWebviewReturned:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_webview_returned(user_id="test_user_id", webview_name="test_webview_name", outcome="test_outcome", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'webview_name' in props, 'webview_name must be in properties'
            assert 'outcome' in props, 'outcome must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackAccountLinked:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_account_linked(user_id="test_user_id", processing_duration_ms="test_processing_duration_ms", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_account_linked(user_id="test_user_id", processing_duration_ms="test_processing_duration_ms", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'sla_breach' not in props, 'sla_breach must not be present when not supplied'

class Test_TrackLinkAccountFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_link_account_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'

class Test_TrackSetupDefaultCtaClicked:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_setup_default_cta_clicked(user_id="test_user_id", source_touchpoint="test_source_touchpoint", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackDefaultAccountSetupSucceeded:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_default_account_setup_succeeded(user_id="test_user_id", processing_duration_ms="test_processing_duration_ms", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_default_account_setup_succeeded(user_id="test_user_id", processing_duration_ms="test_processing_duration_ms", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'sla_breach' not in props, 'sla_breach must not be present when not supplied'

class Test_TrackDefaultAccountSetupFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_default_account_setup_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'

class Test_TrackPageViewed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_page_viewed(user_id="test_user_id", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackKomisiAmountFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_komisi_amount_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_komisi_amount_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message")
            props = mp_mock.track.call_args[0][2]
            assert 'amount' not in props, 'amount must not be present when not supplied'

class Test_TrackPaymentStarted:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_started(user_id="test_user_id", source_touchpoint="test_source_touchpoint", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'source_touchpoint' in props, 'source_touchpoint must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackPaymentMethodSelected:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_method_selected(user_id="test_user_id", payment_method="test_payment_method", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'payment_method' in props, 'payment_method must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackInsufficientBalanceViewed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_insufficient_balance_viewed(user_id="test_user_id", amount="test_amount", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'amount' in props, 'amount must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

class Test_TrackPaymentConfirmed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_confirmed(user_id="test_user_id", amount="test_amount", payment_method="test_payment_method", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'amount' in props, 'amount must be in properties'
            assert 'payment_method' in props, 'payment_method must be in properties'
            assert 'platform' in props, 'platform must be in properties'
            assert 'app_version' in props, 'app_version must be in properties'
            assert 'session_id' in props, 'session_id must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_confirmed(user_id="test_user_id", amount="test_amount", payment_method="test_payment_method", platform="test_platform", app_version="test_app_version", session_id="test_session_id")
            props = mp_mock.track.call_args[0][2]
            assert 'bank_name' not in props, 'bank_name must not be present when not supplied'

class Test_TrackPaymentSuccess:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_success(user_id="test_user_id", amount="test_amount", payment_method="test_payment_method", processing_duration_ms="test_processing_duration_ms", currency="test_currency")
            props = mp_mock.track.call_args[0][2]
            assert 'amount' in props, 'amount must be in properties'
            assert 'payment_method' in props, 'payment_method must be in properties'
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'
            assert 'currency' in props, 'currency must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_success(user_id="test_user_id", amount="test_amount", payment_method="test_payment_method", processing_duration_ms="test_processing_duration_ms", currency="test_currency")
            props = mp_mock.track.call_args[0][2]
            assert 'sla_breach' not in props, 'sla_breach must not be present when not supplied'

    def test_has_processing_duration_ms_parameter(self):
        sig = inspect.signature(track_payment_success)
        assert 'processing_duration_ms' in sig.parameters, \
            'Backend event must accept processing_duration_ms for SLA tracking'

class Test_TrackPaymentFailed:
    def test_required_properties_present(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", payment_method="test_payment_method", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'error_code' in props, 'error_code must be in properties'
            assert 'error_message' in props, 'error_message must be in properties'
            assert 'payment_method' in props, 'payment_method must be in properties'
            assert 'processing_duration_ms' in props, 'processing_duration_ms must be in properties'

    def test_optional_properties_excluded_when_none(self):
        with mock.patch('instrumentation.mp') as mp_mock:
            track_payment_failed(user_id="test_user_id", error_code="test_error_code", error_message="test_error_message", payment_method="test_payment_method", processing_duration_ms="test_processing_duration_ms")
            props = mp_mock.track.call_args[0][2]
            assert 'amount' not in props, 'amount must not be present when not supplied'
            assert 'sla_breach' not in props, 'sla_breach must not be present when not supplied'
