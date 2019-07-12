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

from .proxy_resource_py3 import ProxyResource


class Build(ProxyResource):
    """Build resource properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param build_id: The unique identifier for the build.
    :type build_id: str
    :param status: The current status of the build. Possible values include:
     'Queued', 'Started', 'Running', 'Succeeded', 'Failed', 'Canceled',
     'Error', 'Timeout'
    :type status: str or
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.BuildStatus
    :param last_updated_time: The last updated time for the build.
    :type last_updated_time: datetime
    :param build_type: The type of build. Possible values include:
     'AutoBuild', 'QuickBuild'
    :type build_type: str or
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.BuildType
    :param create_time: The time the build was created.
    :type create_time: datetime
    :param start_time: The time the build started.
    :type start_time: datetime
    :param finish_time: The time the build finished.
    :type finish_time: datetime
    :param output_images: The list of all images that were generated from the
     build.
    :type output_images:
     list[~azure.mgmt.containerregistry.v2018_02_01_preview.models.ImageDescriptor]
    :param build_task: The build task with which the build was started.
    :type build_task: str
    :param image_update_trigger: The image update trigger that caused the
     build.
    :type image_update_trigger:
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.ImageUpdateTrigger
    :param git_commit_trigger: The git commit trigger that caused the build.
    :type git_commit_trigger:
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.GitCommitTrigger
    :param is_archive_enabled: The value that indicates whether archiving is
     enabled or not. Default value: False .
    :type is_archive_enabled: bool
    :param platform: The platform properties against which the build will
     happen.
    :type platform:
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.PlatformProperties
    :param provisioning_state: The provisioning state of a build. Possible
     values include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Failed',
     'Canceled'
    :type provisioning_state: str or
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'build_id': {'key': 'properties.buildId', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
        'build_type': {'key': 'properties.buildType', 'type': 'str'},
        'create_time': {'key': 'properties.createTime', 'type': 'iso-8601'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'finish_time': {'key': 'properties.finishTime', 'type': 'iso-8601'},
        'output_images': {'key': 'properties.outputImages', 'type': '[ImageDescriptor]'},
        'build_task': {'key': 'properties.buildTask', 'type': 'str'},
        'image_update_trigger': {'key': 'properties.imageUpdateTrigger', 'type': 'ImageUpdateTrigger'},
        'git_commit_trigger': {'key': 'properties.gitCommitTrigger', 'type': 'GitCommitTrigger'},
        'is_archive_enabled': {'key': 'properties.isArchiveEnabled', 'type': 'bool'},
        'platform': {'key': 'properties.platform', 'type': 'PlatformProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, build_id: str=None, status=None, last_updated_time=None, build_type=None, create_time=None, start_time=None, finish_time=None, output_images=None, build_task: str=None, image_update_trigger=None, git_commit_trigger=None, is_archive_enabled: bool=False, platform=None, provisioning_state=None, **kwargs) -> None:
        super(Build, self).__init__(**kwargs)
        self.build_id = build_id
        self.status = status
        self.last_updated_time = last_updated_time
        self.build_type = build_type
        self.create_time = create_time
        self.start_time = start_time
        self.finish_time = finish_time
        self.output_images = output_images
        self.build_task = build_task
        self.image_update_trigger = image_update_trigger
        self.git_commit_trigger = git_commit_trigger
        self.is_archive_enabled = is_archive_enabled
        self.platform = platform
        self.provisioning_state = provisioning_state