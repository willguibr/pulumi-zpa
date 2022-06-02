# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetZPAProvisioningKeyResult',
    'AwaitableGetZPAProvisioningKeyResult',
    'get_zpa_provisioning_key',
    'get_zpa_provisioning_key_output',
]

@pulumi.output_type
class GetZPAProvisioningKeyResult:
    """
    A collection of values returned by getZPAProvisioningKey.
    """
    def __init__(__self__, app_connector_group_id=None, app_connector_group_name=None, association_type=None, creation_time=None, enabled=None, enrollment_cert_id=None, enrollment_cert_name=None, expiration_in_epoch_sec=None, id=None, ip_acls=None, max_usage=None, modified_time=None, modifiedby=None, name=None, provisioning_key=None, ui_config=None, usage_count=None, zcomponent_id=None, zcomponent_name=None):
        if app_connector_group_id and not isinstance(app_connector_group_id, str):
            raise TypeError("Expected argument 'app_connector_group_id' to be a str")
        pulumi.set(__self__, "app_connector_group_id", app_connector_group_id)
        if app_connector_group_name and not isinstance(app_connector_group_name, str):
            raise TypeError("Expected argument 'app_connector_group_name' to be a str")
        pulumi.set(__self__, "app_connector_group_name", app_connector_group_name)
        if association_type and not isinstance(association_type, str):
            raise TypeError("Expected argument 'association_type' to be a str")
        pulumi.set(__self__, "association_type", association_type)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if enrollment_cert_id and not isinstance(enrollment_cert_id, str):
            raise TypeError("Expected argument 'enrollment_cert_id' to be a str")
        pulumi.set(__self__, "enrollment_cert_id", enrollment_cert_id)
        if enrollment_cert_name and not isinstance(enrollment_cert_name, str):
            raise TypeError("Expected argument 'enrollment_cert_name' to be a str")
        pulumi.set(__self__, "enrollment_cert_name", enrollment_cert_name)
        if expiration_in_epoch_sec and not isinstance(expiration_in_epoch_sec, str):
            raise TypeError("Expected argument 'expiration_in_epoch_sec' to be a str")
        pulumi.set(__self__, "expiration_in_epoch_sec", expiration_in_epoch_sec)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_acls and not isinstance(ip_acls, list):
            raise TypeError("Expected argument 'ip_acls' to be a list")
        pulumi.set(__self__, "ip_acls", ip_acls)
        if max_usage and not isinstance(max_usage, str):
            raise TypeError("Expected argument 'max_usage' to be a str")
        pulumi.set(__self__, "max_usage", max_usage)
        if modified_time and not isinstance(modified_time, str):
            raise TypeError("Expected argument 'modified_time' to be a str")
        pulumi.set(__self__, "modified_time", modified_time)
        if modifiedby and not isinstance(modifiedby, str):
            raise TypeError("Expected argument 'modifiedby' to be a str")
        pulumi.set(__self__, "modifiedby", modifiedby)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_key and not isinstance(provisioning_key, str):
            raise TypeError("Expected argument 'provisioning_key' to be a str")
        pulumi.set(__self__, "provisioning_key", provisioning_key)
        if ui_config and not isinstance(ui_config, str):
            raise TypeError("Expected argument 'ui_config' to be a str")
        pulumi.set(__self__, "ui_config", ui_config)
        if usage_count and not isinstance(usage_count, str):
            raise TypeError("Expected argument 'usage_count' to be a str")
        pulumi.set(__self__, "usage_count", usage_count)
        if zcomponent_id and not isinstance(zcomponent_id, str):
            raise TypeError("Expected argument 'zcomponent_id' to be a str")
        pulumi.set(__self__, "zcomponent_id", zcomponent_id)
        if zcomponent_name and not isinstance(zcomponent_name, str):
            raise TypeError("Expected argument 'zcomponent_name' to be a str")
        pulumi.set(__self__, "zcomponent_name", zcomponent_name)

    @property
    @pulumi.getter(name="appConnectorGroupId")
    def app_connector_group_id(self) -> str:
        return pulumi.get(self, "app_connector_group_id")

    @property
    @pulumi.getter(name="appConnectorGroupName")
    def app_connector_group_name(self) -> str:
        return pulumi.get(self, "app_connector_group_name")

    @property
    @pulumi.getter(name="associationType")
    def association_type(self) -> str:
        return pulumi.get(self, "association_type")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="enrollmentCertId")
    def enrollment_cert_id(self) -> str:
        return pulumi.get(self, "enrollment_cert_id")

    @property
    @pulumi.getter(name="enrollmentCertName")
    def enrollment_cert_name(self) -> str:
        return pulumi.get(self, "enrollment_cert_name")

    @property
    @pulumi.getter(name="expirationInEpochSec")
    def expiration_in_epoch_sec(self) -> str:
        return pulumi.get(self, "expiration_in_epoch_sec")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAcls")
    def ip_acls(self) -> Sequence[str]:
        return pulumi.get(self, "ip_acls")

    @property
    @pulumi.getter(name="maxUsage")
    def max_usage(self) -> str:
        return pulumi.get(self, "max_usage")

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
    @pulumi.getter(name="provisioningKey")
    def provisioning_key(self) -> str:
        return pulumi.get(self, "provisioning_key")

    @property
    @pulumi.getter(name="uiConfig")
    def ui_config(self) -> str:
        return pulumi.get(self, "ui_config")

    @property
    @pulumi.getter(name="usageCount")
    def usage_count(self) -> str:
        return pulumi.get(self, "usage_count")

    @property
    @pulumi.getter(name="zcomponentId")
    def zcomponent_id(self) -> str:
        return pulumi.get(self, "zcomponent_id")

    @property
    @pulumi.getter(name="zcomponentName")
    def zcomponent_name(self) -> str:
        return pulumi.get(self, "zcomponent_name")


class AwaitableGetZPAProvisioningKeyResult(GetZPAProvisioningKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPAProvisioningKeyResult(
            app_connector_group_id=self.app_connector_group_id,
            app_connector_group_name=self.app_connector_group_name,
            association_type=self.association_type,
            creation_time=self.creation_time,
            enabled=self.enabled,
            enrollment_cert_id=self.enrollment_cert_id,
            enrollment_cert_name=self.enrollment_cert_name,
            expiration_in_epoch_sec=self.expiration_in_epoch_sec,
            id=self.id,
            ip_acls=self.ip_acls,
            max_usage=self.max_usage,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            provisioning_key=self.provisioning_key,
            ui_config=self.ui_config,
            usage_count=self.usage_count,
            zcomponent_id=self.zcomponent_id,
            zcomponent_name=self.zcomponent_name)


def get_zpa_provisioning_key(association_type: Optional[str] = None,
                             id: Optional[str] = None,
                             name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPAProvisioningKeyResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['associationType'] = association_type
    __args__['id'] = id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPAProvisioningKey:getZPAProvisioningKey', __args__, opts=opts, typ=GetZPAProvisioningKeyResult).value

    return AwaitableGetZPAProvisioningKeyResult(
        app_connector_group_id=__ret__.app_connector_group_id,
        app_connector_group_name=__ret__.app_connector_group_name,
        association_type=__ret__.association_type,
        creation_time=__ret__.creation_time,
        enabled=__ret__.enabled,
        enrollment_cert_id=__ret__.enrollment_cert_id,
        enrollment_cert_name=__ret__.enrollment_cert_name,
        expiration_in_epoch_sec=__ret__.expiration_in_epoch_sec,
        id=__ret__.id,
        ip_acls=__ret__.ip_acls,
        max_usage=__ret__.max_usage,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        provisioning_key=__ret__.provisioning_key,
        ui_config=__ret__.ui_config,
        usage_count=__ret__.usage_count,
        zcomponent_id=__ret__.zcomponent_id,
        zcomponent_name=__ret__.zcomponent_name)


@_utilities.lift_output_func(get_zpa_provisioning_key)
def get_zpa_provisioning_key_output(association_type: Optional[pulumi.Input[str]] = None,
                                    id: Optional[pulumi.Input[Optional[str]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPAProvisioningKeyResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
