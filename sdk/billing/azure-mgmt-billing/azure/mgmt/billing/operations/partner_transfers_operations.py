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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class PartnerTransfersOperations(object):
    """PartnerTransfersOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def initiate(
            self, billing_account_name, billing_profile_name, customer_name, recipient_email_id=None, reseller_id=None, custom_headers=None, raw=False, **operation_config):
        """Initiates the request to transfer the legacy subscriptions or RIs.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param billing_profile_name: Billing Profile Id.
        :type billing_profile_name: str
        :param customer_name: Customer name.
        :type customer_name: str
        :param recipient_email_id: Email Id of recipient for transfer.
        :type recipient_email_id: str
        :param reseller_id: Optional reseller Id for transfer.
        :type reseller_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TransferDetails or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.TransferDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        parameters = models.InitiateTransferRequest(recipient_email_id=recipient_email_id, reseller_id=reseller_id)

        # Construct URL
        url = self.initiate.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'customerName': self._serialize.url("customer_name", customer_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'InitiateTransferRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TransferDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    initiate.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/initiateTransfer'}

    def get(
            self, billing_account_name, billing_profile_name, customer_name, transfer_name, custom_headers=None, raw=False, **operation_config):
        """Gets the transfer details for given transfer Id.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param billing_profile_name: Billing Profile Id.
        :type billing_profile_name: str
        :param customer_name: Customer name.
        :type customer_name: str
        :param transfer_name: Transfer Name.
        :type transfer_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TransferDetails or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.TransferDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'customerName': self._serialize.url("customer_name", customer_name, 'str'),
            'transferName': self._serialize.url("transfer_name", transfer_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TransferDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName}'}

    def cancel(
            self, billing_account_name, billing_profile_name, customer_name, transfer_name, custom_headers=None, raw=False, **operation_config):
        """Cancels the transfer for given transfer Id.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param billing_profile_name: Billing Profile Id.
        :type billing_profile_name: str
        :param customer_name: Customer name.
        :type customer_name: str
        :param transfer_name: Transfer Name.
        :type transfer_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TransferDetails or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.TransferDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.cancel.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'customerName': self._serialize.url("customer_name", customer_name, 'str'),
            'transferName': self._serialize.url("transfer_name", transfer_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TransferDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    cancel.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers/{customerName}/transfers/{transferName}'}