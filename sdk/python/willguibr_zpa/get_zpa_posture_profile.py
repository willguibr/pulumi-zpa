# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetZPAPostureProfileResult',
    'AwaitableGetZPAPostureProfileResult',
    'get_zpa_posture_profile',
    'get_zpa_posture_profile_output',
]

@pulumi.output_type
class GetZPAPostureProfileResult:
    """
    A collection of values returned by getZPAPostureProfile.
    """
    def __init__(__self__, creation_time=None, domain=None, id=None, master_customer_id=None, modified_time=None, modifiedby=None, name=None, posture_udid=None, zscaler_cloud=None, zscaler_customer_id=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if master_customer_id and not isinstance(master_customer_id, str):
            raise TypeError("Expected argument 'master_customer_id' to be a str")
        pulumi.set(__self__, "master_customer_id", master_customer_id)
        if modified_time and not isinstance(modified_time, str):
            raise TypeError("Expected argument 'modified_time' to be a str")
        pulumi.set(__self__, "modified_time", modified_time)
        if modifiedby and not isinstance(modifiedby, str):
            raise TypeError("Expected argument 'modifiedby' to be a str")
        pulumi.set(__self__, "modifiedby", modifiedby)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if posture_udid and not isinstance(posture_udid, str):
            raise TypeError("Expected argument 'posture_udid' to be a str")
        pulumi.set(__self__, "posture_udid", posture_udid)
        if zscaler_cloud and not isinstance(zscaler_cloud, str):
            raise TypeError("Expected argument 'zscaler_cloud' to be a str")
        pulumi.set(__self__, "zscaler_cloud", zscaler_cloud)
        if zscaler_customer_id and not isinstance(zscaler_customer_id, str):
            raise TypeError("Expected argument 'zscaler_customer_id' to be a str")
        pulumi.set(__self__, "zscaler_customer_id", zscaler_customer_id)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def domain(self) -> str:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="masterCustomerId")
    def master_customer_id(self) -> str:
        return pulumi.get(self, "master_customer_id")

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
    @pulumi.getter(name="postureUdid")
    def posture_udid(self) -> str:
        return pulumi.get(self, "posture_udid")

    @property
    @pulumi.getter(name="zscalerCloud")
    def zscaler_cloud(self) -> str:
        return pulumi.get(self, "zscaler_cloud")

    @property
    @pulumi.getter(name="zscalerCustomerId")
    def zscaler_customer_id(self) -> str:
        return pulumi.get(self, "zscaler_customer_id")


class AwaitableGetZPAPostureProfileResult(GetZPAPostureProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPAPostureProfileResult(
            creation_time=self.creation_time,
            domain=self.domain,
            id=self.id,
            master_customer_id=self.master_customer_id,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            posture_udid=self.posture_udid,
            zscaler_cloud=self.zscaler_cloud,
            zscaler_customer_id=self.zscaler_customer_id)


def get_zpa_posture_profile(name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPAPostureProfileResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPAPostureProfile:getZPAPostureProfile', __args__, opts=opts, typ=GetZPAPostureProfileResult).value

    return AwaitableGetZPAPostureProfileResult(
        creation_time=__ret__.creation_time,
        domain=__ret__.domain,
        id=__ret__.id,
        master_customer_id=__ret__.master_customer_id,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        posture_udid=__ret__.posture_udid,
        zscaler_cloud=__ret__.zscaler_cloud,
        zscaler_customer_id=__ret__.zscaler_customer_id)


@_utilities.lift_output_func(get_zpa_posture_profile)
def get_zpa_posture_profile_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPAPostureProfileResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
