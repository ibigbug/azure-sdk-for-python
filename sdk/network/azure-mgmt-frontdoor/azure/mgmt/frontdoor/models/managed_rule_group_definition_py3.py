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

from msrest.serialization import Model


class ManagedRuleGroupDefinition(Model):
    """Describes a managed rule group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar rule_group_name: Name of the managed rule group.
    :vartype rule_group_name: str
    :ivar description: Description of the managed rule group.
    :vartype description: str
    :ivar rules: List of rules within the managed rule group.
    :vartype rules: list[~azure.mgmt.frontdoor.models.ManagedRuleDefinition]
    """

    _validation = {
        'rule_group_name': {'readonly': True},
        'description': {'readonly': True},
        'rules': {'readonly': True},
    }

    _attribute_map = {
        'rule_group_name': {'key': 'ruleGroupName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'rules': {'key': 'rules', 'type': '[ManagedRuleDefinition]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ManagedRuleGroupDefinition, self).__init__(**kwargs)
        self.rule_group_name = None
        self.description = None
        self.rules = None
