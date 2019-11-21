# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class NetworkOperationStatus(str, Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"


class NetworkExperimentResourceState(str, Enum):

    creating = "Creating"
    enabling = "Enabling"
    enabled = "Enabled"
    disabling = "Disabling"
    disabled = "Disabled"
    deleting = "Deleting"


class State(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class AggregationInterval(str, Enum):

    hourly = "Hourly"
    daily = "Daily"


class TimeseriesType(str, Enum):

    measurement_counts = "MeasurementCounts"
    latency_p50 = "LatencyP50"
    latency_p75 = "LatencyP75"
    latency_p95 = "LatencyP95"


class EndpointType(str, Enum):

    afd = "AFD"
    azure_region = "AzureRegion"
    cdn = "CDN"
    atm = "ATM"


class FrontDoorResourceState(str, Enum):

    creating = "Creating"
    enabling = "Enabling"
    enabled = "Enabled"
    disabling = "Disabling"
    disabled = "Disabled"
    deleting = "Deleting"


class CustomHttpsProvisioningState(str, Enum):

    enabling = "Enabling"
    enabled = "Enabled"
    disabling = "Disabling"
    disabled = "Disabled"
    failed = "Failed"


class CustomHttpsProvisioningSubstate(str, Enum):

    submitting_domain_control_validation_request = "SubmittingDomainControlValidationRequest"
    pending_domain_control_validation_request_approval = "PendingDomainControlValidationREquestApproval"
    domain_control_validation_request_approved = "DomainControlValidationRequestApproved"
    domain_control_validation_request_rejected = "DomainControlValidationRequestRejected"
    domain_control_validation_request_timed_out = "DomainControlValidationRequestTimedOut"
    issuing_certificate = "IssuingCertificate"
    deploying_certificate = "DeployingCertificate"
    certificate_deployed = "CertificateDeployed"
    deleting_certificate = "DeletingCertificate"
    certificate_deleted = "CertificateDeleted"


class FrontDoorCertificateSource(str, Enum):

    azure_key_vault = "AzureKeyVault"
    front_door = "FrontDoor"


class MinimumTLSVersion(str, Enum):

    one_full_stop_zero = "1.0"
    one_full_stop_two = "1.2"


class FrontDoorCertificateType(str, Enum):

    dedicated = "Dedicated"


class EnforceCertificateNameCheckEnabledState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class FrontDoorEnabledState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class FrontDoorProtocol(str, Enum):

    http = "Http"
    https = "Https"


class RoutingRuleEnabledState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class FrontDoorForwardingProtocol(str, Enum):

    http_only = "HttpOnly"
    https_only = "HttpsOnly"
    match_request = "MatchRequest"


class FrontDoorQuery(str, Enum):

    strip_none = "StripNone"
    strip_all = "StripAll"


class DynamicCompressionEnabled(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class FrontDoorRedirectType(str, Enum):

    moved = "Moved"
    found = "Found"
    temporary_redirect = "TemporaryRedirect"
    permanent_redirect = "PermanentRedirect"


class FrontDoorRedirectProtocol(str, Enum):

    http_only = "HttpOnly"
    https_only = "HttpsOnly"
    match_request = "MatchRequest"


class BackendEnabledState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class FrontDoorHealthProbeMethod(str, Enum):

    get = "GET"
    head = "HEAD"


class HealthProbeEnabled(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class SessionAffinityEnabledState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class HeaderActionType(str, Enum):

    append = "Append"
    delete = "Delete"
    overwrite = "Overwrite"


class RulesEngineMatchVariable(str, Enum):

    is_mobile = "IsMobile"
    remote_addr = "RemoteAddr"
    request_method = "RequestMethod"
    query_string = "QueryString"
    post_args = "PostArgs"
    request_uri = "RequestUri"
    request_path = "RequestPath"
    request_filename = "RequestFilename"
    request_filename_extension = "RequestFilenameExtension"
    request_header = "RequestHeader"
    request_body = "RequestBody"
    request_scheme = "RequestScheme"


class RulesEngineOperator(str, Enum):

    any = "Any"
    ip_match = "IPMatch"
    geo_match = "GeoMatch"
    equal = "Equal"
    contains = "Contains"
    less_than = "LessThan"
    greater_than = "GreaterThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than_or_equal = "GreaterThanOrEqual"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"


class Transform(str, Enum):

    lowercase = "Lowercase"
    uppercase = "Uppercase"
    trim = "Trim"
    url_decode = "UrlDecode"
    url_encode = "UrlEncode"
    remove_nulls = "RemoveNulls"


class MatchProcessingBehavior(str, Enum):

    continue_enum = "Continue"
    stop = "Stop"


class ResourceType(str, Enum):

    microsoft_networkfront_doors = "Microsoft.Network/frontDoors"
    microsoft_networkfront_doorsfrontend_endpoints = "Microsoft.Network/frontDoors/frontendEndpoints"


class Availability(str, Enum):

    available = "Available"
    unavailable = "Unavailable"


class PolicyEnabledState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class PolicyMode(str, Enum):

    prevention = "Prevention"
    detection = "Detection"


class CustomRuleEnabledState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class RuleType(str, Enum):

    match_rule = "MatchRule"
    rate_limit_rule = "RateLimitRule"


class MatchVariable(str, Enum):

    remote_addr = "RemoteAddr"
    request_method = "RequestMethod"
    query_string = "QueryString"
    post_args = "PostArgs"
    request_uri = "RequestUri"
    request_header = "RequestHeader"
    request_body = "RequestBody"
    cookies = "Cookies"
    socket_addr = "SocketAddr"


class Operator(str, Enum):

    any = "Any"
    ip_match = "IPMatch"
    geo_match = "GeoMatch"
    equal = "Equal"
    contains = "Contains"
    less_than = "LessThan"
    greater_than = "GreaterThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than_or_equal = "GreaterThanOrEqual"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    reg_ex = "RegEx"


class TransformType(str, Enum):

    lowercase = "Lowercase"
    uppercase = "Uppercase"
    trim = "Trim"
    url_decode = "UrlDecode"
    url_encode = "UrlEncode"
    remove_nulls = "RemoveNulls"


class ActionType(str, Enum):

    allow = "Allow"
    block = "Block"
    log = "Log"
    redirect = "Redirect"


class ManagedRuleExclusionMatchVariable(str, Enum):

    request_header_names = "RequestHeaderNames"
    request_cookie_names = "RequestCookieNames"
    query_string_arg_names = "QueryStringArgNames"
    request_body_post_arg_names = "RequestBodyPostArgNames"


class ManagedRuleExclusionSelectorMatchOperator(str, Enum):

    equals = "Equals"
    contains = "Contains"
    starts_with = "StartsWith"
    ends_with = "EndsWith"
    equals_any = "EqualsAny"


class ManagedRuleEnabledState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class PolicyResourceState(str, Enum):

    creating = "Creating"
    enabling = "Enabling"
    enabled = "Enabled"
    disabling = "Disabling"
    disabled = "Disabled"
    deleting = "Deleting"


class LatencyScorecardAggregationInterval(str, Enum):

    daily = "Daily"
    weekly = "Weekly"
    monthly = "Monthly"


class TimeseriesAggregationInterval(str, Enum):

    hourly = "Hourly"
    daily = "Daily"
