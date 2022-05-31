# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetZPACloudConnectorGroupResult',
    'AwaitableGetZPACloudConnectorGroupResult',
    'get_zpa_cloud_connector_group',
    'get_zpa_cloud_connector_group_output',
]

@pulumi.output_type
class GetZPACloudConnectorGroupResult:
    """
    A collection of values returned by getZPACloudConnectorGroup.
    """
    def __init__(__self__, cloud_connectors=None, creation_time=None, description=None, enabled=None, geolocation_id=None, id=None, modified_time=None, modifiedby=None, name=None, zia_cloud=None, zia_org_id=None):
        if cloud_connectors and not isinstance(cloud_connectors, list):
            raise TypeError("Expected argument 'cloud_connectors' to be a list")
        pulumi.set(__self__, "cloud_connectors", cloud_connectors)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if geolocation_id and not isinstance(geolocation_id, str):
            raise TypeError("Expected argument 'geolocation_id' to be a str")
        pulumi.set(__self__, "geolocation_id", geolocation_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if modified_time and not isinstance(modified_time, str):
            raise TypeError("Expected argument 'modified_time' to be a str")
        pulumi.set(__self__, "modified_time", modified_time)
        if modifiedby and not isinstance(modifiedby, str):
            raise TypeError("Expected argument 'modifiedby' to be a str")
        pulumi.set(__self__, "modifiedby", modifiedby)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if zia_cloud and not isinstance(zia_cloud, str):
            raise TypeError("Expected argument 'zia_cloud' to be a str")
        pulumi.set(__self__, "zia_cloud", zia_cloud)
        if zia_org_id and not isinstance(zia_org_id, str):
            raise TypeError("Expected argument 'zia_org_id' to be a str")
        pulumi.set(__self__, "zia_org_id", zia_org_id)

    @property
    @pulumi.getter(name="cloudConnectors")
    def cloud_connectors(self) -> Sequence['outputs.GetZPACloudConnectorGroupCloudConnectorResult']:
        return pulumi.get(self, "cloud_connectors")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="geolocationId")
    def geolocation_id(self) -> str:
        return pulumi.get(self, "geolocation_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modifiedTime")
    def modified_time(self) -> str:
        return pulumi.get(self, "modified_time")

    @property
    @pulumi.getter
    def modifiedby(self) -> str:
        return pulumi.get(self, "modifiedby")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ziaCloud")
    def zia_cloud(self) -> str:
        return pulumi.get(self, "zia_cloud")

    @property
    @pulumi.getter(name="ziaOrgId")
    def zia_org_id(self) -> str:
        return pulumi.get(self, "zia_org_id")


class AwaitableGetZPACloudConnectorGroupResult(GetZPACloudConnectorGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPACloudConnectorGroupResult(
            cloud_connectors=self.cloud_connectors,
            creation_time=self.creation_time,
            description=self.description,
            enabled=self.enabled,
            geolocation_id=self.geolocation_id,
            id=self.id,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            zia_cloud=self.zia_cloud,
            zia_org_id=self.zia_org_id)


def get_zpa_cloud_connector_group(id: Optional[str] = None,
                                  name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPACloudConnectorGroupResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPACloudConnectorGroup:getZPACloudConnectorGroup', __args__, opts=opts, typ=GetZPACloudConnectorGroupResult).value

    return AwaitableGetZPACloudConnectorGroupResult(
        cloud_connectors=__ret__.cloud_connectors,
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        enabled=__ret__.enabled,
        geolocation_id=__ret__.geolocation_id,
        id=__ret__.id,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        zia_cloud=__ret__.zia_cloud,
        zia_org_id=__ret__.zia_org_id)


@_utilities.lift_output_func(get_zpa_cloud_connector_group)
def get_zpa_cloud_connector_group_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                         name: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPACloudConnectorGroupResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
