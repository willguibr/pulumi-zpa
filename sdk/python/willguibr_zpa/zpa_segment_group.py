# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ZPASegmentGroupArgs', 'ZPASegmentGroup']

@pulumi.input_type
class ZPASegmentGroupArgs:
    def __init__(__self__, *,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input['ZPASegmentGroupApplicationArgs']]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_migrated: Optional[pulumi.Input[bool]] = None,
                 tcp_keep_alive_enabled: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZPASegmentGroup resource.
        :param pulumi.Input[str] description: Description of the app group.
        :param pulumi.Input[bool] enabled: Whether this app group is enabled or not.
        :param pulumi.Input[str] name: Name of the app group.
        """
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if config_space is not None:
            pulumi.set(__self__, "config_space", config_space)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_migrated is not None:
            pulumi.set(__self__, "policy_migrated", policy_migrated)
        if tcp_keep_alive_enabled is not None:
            pulumi.set(__self__, "tcp_keep_alive_enabled", tcp_keep_alive_enabled)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPASegmentGroupApplicationArgs']]]]:
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPASegmentGroupApplicationArgs']]]]):
        pulumi.set(self, "applications", value)

    @property
    @pulumi.getter(name="configSpace")
    def config_space(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_space")

    @config_space.setter
    def config_space(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_space", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the app group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this app group is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the app group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyMigrated")
    def policy_migrated(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "policy_migrated")

    @policy_migrated.setter
    def policy_migrated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "policy_migrated", value)

    @property
    @pulumi.getter(name="tcpKeepAliveEnabled")
    def tcp_keep_alive_enabled(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tcp_keep_alive_enabled")

    @tcp_keep_alive_enabled.setter
    def tcp_keep_alive_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tcp_keep_alive_enabled", value)


@pulumi.input_type
class _ZPASegmentGroupState:
    def __init__(__self__, *,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input['ZPASegmentGroupApplicationArgs']]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_migrated: Optional[pulumi.Input[bool]] = None,
                 tcp_keep_alive_enabled: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZPASegmentGroup resources.
        :param pulumi.Input[str] description: Description of the app group.
        :param pulumi.Input[bool] enabled: Whether this app group is enabled or not.
        :param pulumi.Input[str] name: Name of the app group.
        """
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if config_space is not None:
            pulumi.set(__self__, "config_space", config_space)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_migrated is not None:
            pulumi.set(__self__, "policy_migrated", policy_migrated)
        if tcp_keep_alive_enabled is not None:
            pulumi.set(__self__, "tcp_keep_alive_enabled", tcp_keep_alive_enabled)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPASegmentGroupApplicationArgs']]]]:
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPASegmentGroupApplicationArgs']]]]):
        pulumi.set(self, "applications", value)

    @property
    @pulumi.getter(name="configSpace")
    def config_space(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "config_space")

    @config_space.setter
    def config_space(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_space", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the app group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this app group is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the app group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyMigrated")
    def policy_migrated(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "policy_migrated")

    @policy_migrated.setter
    def policy_migrated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "policy_migrated", value)

    @property
    @pulumi.getter(name="tcpKeepAliveEnabled")
    def tcp_keep_alive_enabled(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tcp_keep_alive_enabled")

    @tcp_keep_alive_enabled.setter
    def tcp_keep_alive_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tcp_keep_alive_enabled", value)


class ZPASegmentGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPASegmentGroupApplicationArgs']]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_migrated: Optional[pulumi.Input[bool]] = None,
                 tcp_keep_alive_enabled: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZPASegmentGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the app group.
        :param pulumi.Input[bool] enabled: Whether this app group is enabled or not.
        :param pulumi.Input[str] name: Name of the app group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ZPASegmentGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZPASegmentGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZPASegmentGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZPASegmentGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPASegmentGroupApplicationArgs']]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_migrated: Optional[pulumi.Input[bool]] = None,
                 tcp_keep_alive_enabled: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZPASegmentGroupArgs.__new__(ZPASegmentGroupArgs)

            __props__.__dict__["applications"] = applications
            __props__.__dict__["config_space"] = config_space
            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["policy_migrated"] = policy_migrated
            __props__.__dict__["tcp_keep_alive_enabled"] = tcp_keep_alive_enabled
        super(ZPASegmentGroup, __self__).__init__(
            'zpa:index/zPASegmentGroup:ZPASegmentGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPASegmentGroupApplicationArgs']]]]] = None,
            config_space: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_migrated: Optional[pulumi.Input[bool]] = None,
            tcp_keep_alive_enabled: Optional[pulumi.Input[str]] = None) -> 'ZPASegmentGroup':
        """
        Get an existing ZPASegmentGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the app group.
        :param pulumi.Input[bool] enabled: Whether this app group is enabled or not.
        :param pulumi.Input[str] name: Name of the app group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZPASegmentGroupState.__new__(_ZPASegmentGroupState)

        __props__.__dict__["applications"] = applications
        __props__.__dict__["config_space"] = config_space
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["policy_migrated"] = policy_migrated
        __props__.__dict__["tcp_keep_alive_enabled"] = tcp_keep_alive_enabled
        return ZPASegmentGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def applications(self) -> pulumi.Output[Sequence['outputs.ZPASegmentGroupApplication']]:
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="configSpace")
    def config_space(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "config_space")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the app group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this app group is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the app group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyMigrated")
    def policy_migrated(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "policy_migrated")

    @property
    @pulumi.getter(name="tcpKeepAliveEnabled")
    def tcp_keep_alive_enabled(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "tcp_keep_alive_enabled")

