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
    'GetZPAPolicyTypeResult',
    'AwaitableGetZPAPolicyTypeResult',
    'get_zpa_policy_type',
    'get_zpa_policy_type_output',
]

@pulumi.output_type
class GetZPAPolicyTypeResult:
    """
    A collection of values returned by getZPAPolicyType.
    """
    def __init__(__self__, creation_time=None, description=None, enabled=None, id=None, modified_time=None, modifiedby=None, name=None, policy_type=None, rules=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
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
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)

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
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> str:
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetZPAPolicyTypeRuleResult']:
        return pulumi.get(self, "rules")


class AwaitableGetZPAPolicyTypeResult(GetZPAPolicyTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPAPolicyTypeResult(
            creation_time=self.creation_time,
            description=self.description,
            enabled=self.enabled,
            id=self.id,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            policy_type=self.policy_type,
            rules=self.rules)


def get_zpa_policy_type(id: Optional[str] = None,
                        policy_type: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPAPolicyTypeResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['policyType'] = policy_type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPAPolicyType:getZPAPolicyType', __args__, opts=opts, typ=GetZPAPolicyTypeResult).value

    return AwaitableGetZPAPolicyTypeResult(
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        enabled=__ret__.enabled,
        id=__ret__.id,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        policy_type=__ret__.policy_type,
        rules=__ret__.rules)


@_utilities.lift_output_func(get_zpa_policy_type)
def get_zpa_policy_type_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                               policy_type: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPAPolicyTypeResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...