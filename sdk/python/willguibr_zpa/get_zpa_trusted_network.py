# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetZPATrustedNetworkResult',
    'AwaitableGetZPATrustedNetworkResult',
    'get_zpa_trusted_network',
    'get_zpa_trusted_network_output',
]

@pulumi.output_type
class GetZPATrustedNetworkResult:
    """
    A collection of values returned by getZPATrustedNetwork.
    """
    def __init__(__self__, creation_time=None, domain=None, id=None, modified_time=None, modifiedby=None, name=None, network_id=None, zscaler_cloud=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
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
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if zscaler_cloud and not isinstance(zscaler_cloud, str):
            raise TypeError("Expected argument 'zscaler_cloud' to be a str")
        pulumi.set(__self__, "zscaler_cloud", zscaler_cloud)

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
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="zscalerCloud")
    def zscaler_cloud(self) -> str:
        return pulumi.get(self, "zscaler_cloud")


class AwaitableGetZPATrustedNetworkResult(GetZPATrustedNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPATrustedNetworkResult(
            creation_time=self.creation_time,
            domain=self.domain,
            id=self.id,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            network_id=self.network_id,
            zscaler_cloud=self.zscaler_cloud)


def get_zpa_trusted_network(id: Optional[str] = None,
                            name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPATrustedNetworkResult:
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
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPATrustedNetwork:getZPATrustedNetwork', __args__, opts=opts, typ=GetZPATrustedNetworkResult).value

    return AwaitableGetZPATrustedNetworkResult(
        creation_time=__ret__.creation_time,
        domain=__ret__.domain,
        id=__ret__.id,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        network_id=__ret__.network_id,
        zscaler_cloud=__ret__.zscaler_cloud)


@_utilities.lift_output_func(get_zpa_trusted_network)
def get_zpa_trusted_network_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                   name: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPATrustedNetworkResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
