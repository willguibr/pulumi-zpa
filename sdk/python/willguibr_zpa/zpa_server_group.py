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

__all__ = ['ZPAServerGroupArgs', 'ZPAServerGroup']

@pulumi.input_type
class ZPAServerGroupArgs:
    def __init__(__self__, *,
                 app_connector_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dynamic_discovery: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_anchored: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 servers: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]]] = None):
        """
        The set of arguments for constructing a ZPAServerGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]] app_connector_groups: List of app-connector IDs.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]] applications: This field is a json array of app-connector-id only.
        :param pulumi.Input[str] description: This field is the description of the server group.
        :param pulumi.Input[bool] dynamic_discovery: This field controls dynamic discovery of the servers.
        :param pulumi.Input[bool] enabled: This field defines if the server group is enabled or disabled.
        :param pulumi.Input[str] name: This field defines the name of the server group.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]] servers: This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
               only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        if app_connector_groups is not None:
            pulumi.set(__self__, "app_connector_groups", app_connector_groups)
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if config_space is not None:
            pulumi.set(__self__, "config_space", config_space)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dynamic_discovery is not None:
            pulumi.set(__self__, "dynamic_discovery", dynamic_discovery)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if ip_anchored is not None:
            pulumi.set(__self__, "ip_anchored", ip_anchored)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if servers is not None:
            pulumi.set(__self__, "servers", servers)

    @property
    @pulumi.getter(name="appConnectorGroups")
    def app_connector_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]]]:
        """
        List of app-connector IDs.
        """
        return pulumi.get(self, "app_connector_groups")

    @app_connector_groups.setter
    def app_connector_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]]]):
        pulumi.set(self, "app_connector_groups", value)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]]]:
        """
        This field is a json array of app-connector-id only.
        """
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]]]):
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
        This field is the description of the server group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dynamicDiscovery")
    def dynamic_discovery(self) -> Optional[pulumi.Input[bool]]:
        """
        This field controls dynamic discovery of the servers.
        """
        return pulumi.get(self, "dynamic_discovery")

    @dynamic_discovery.setter
    def dynamic_discovery(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dynamic_discovery", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        This field defines if the server group is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="ipAnchored")
    def ip_anchored(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ip_anchored")

    @ip_anchored.setter
    def ip_anchored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ip_anchored", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the name of the server group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]]]:
        """
        This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
        only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        return pulumi.get(self, "servers")

    @servers.setter
    def servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]]]):
        pulumi.set(self, "servers", value)


@pulumi.input_type
class _ZPAServerGroupState:
    def __init__(__self__, *,
                 app_connector_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dynamic_discovery: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_anchored: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 servers: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]]] = None):
        """
        Input properties used for looking up and filtering ZPAServerGroup resources.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]] app_connector_groups: List of app-connector IDs.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]] applications: This field is a json array of app-connector-id only.
        :param pulumi.Input[str] description: This field is the description of the server group.
        :param pulumi.Input[bool] dynamic_discovery: This field controls dynamic discovery of the servers.
        :param pulumi.Input[bool] enabled: This field defines if the server group is enabled or disabled.
        :param pulumi.Input[str] name: This field defines the name of the server group.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]] servers: This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
               only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        if app_connector_groups is not None:
            pulumi.set(__self__, "app_connector_groups", app_connector_groups)
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if config_space is not None:
            pulumi.set(__self__, "config_space", config_space)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dynamic_discovery is not None:
            pulumi.set(__self__, "dynamic_discovery", dynamic_discovery)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if ip_anchored is not None:
            pulumi.set(__self__, "ip_anchored", ip_anchored)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if servers is not None:
            pulumi.set(__self__, "servers", servers)

    @property
    @pulumi.getter(name="appConnectorGroups")
    def app_connector_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]]]:
        """
        List of app-connector IDs.
        """
        return pulumi.get(self, "app_connector_groups")

    @app_connector_groups.setter
    def app_connector_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupAppConnectorGroupArgs']]]]):
        pulumi.set(self, "app_connector_groups", value)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]]]:
        """
        This field is a json array of app-connector-id only.
        """
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupApplicationArgs']]]]):
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
        This field is the description of the server group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dynamicDiscovery")
    def dynamic_discovery(self) -> Optional[pulumi.Input[bool]]:
        """
        This field controls dynamic discovery of the servers.
        """
        return pulumi.get(self, "dynamic_discovery")

    @dynamic_discovery.setter
    def dynamic_discovery(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dynamic_discovery", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        This field defines if the server group is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="ipAnchored")
    def ip_anchored(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ip_anchored")

    @ip_anchored.setter
    def ip_anchored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ip_anchored", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the name of the server group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]]]:
        """
        This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
        only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        return pulumi.get(self, "servers")

    @servers.setter
    def servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAServerGroupServerArgs']]]]):
        pulumi.set(self, "servers", value)


class ZPAServerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_connector_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupAppConnectorGroupArgs']]]]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupApplicationArgs']]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dynamic_discovery: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_anchored: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupServerArgs']]]]] = None,
                 __props__=None):
        """
        Create a ZPAServerGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupAppConnectorGroupArgs']]]] app_connector_groups: List of app-connector IDs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupApplicationArgs']]]] applications: This field is a json array of app-connector-id only.
        :param pulumi.Input[str] description: This field is the description of the server group.
        :param pulumi.Input[bool] dynamic_discovery: This field controls dynamic discovery of the servers.
        :param pulumi.Input[bool] enabled: This field defines if the server group is enabled or disabled.
        :param pulumi.Input[str] name: This field defines the name of the server group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupServerArgs']]]] servers: This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
               only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ZPAServerGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZPAServerGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZPAServerGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZPAServerGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_connector_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupAppConnectorGroupArgs']]]]] = None,
                 applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupApplicationArgs']]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dynamic_discovery: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 ip_anchored: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupServerArgs']]]]] = None,
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
            __props__ = ZPAServerGroupArgs.__new__(ZPAServerGroupArgs)

            __props__.__dict__["app_connector_groups"] = app_connector_groups
            __props__.__dict__["applications"] = applications
            __props__.__dict__["config_space"] = config_space
            __props__.__dict__["description"] = description
            __props__.__dict__["dynamic_discovery"] = dynamic_discovery
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["ip_anchored"] = ip_anchored
            __props__.__dict__["name"] = name
            __props__.__dict__["servers"] = servers
        super(ZPAServerGroup, __self__).__init__(
            'zpa:index/zPAServerGroup:ZPAServerGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_connector_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupAppConnectorGroupArgs']]]]] = None,
            applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupApplicationArgs']]]]] = None,
            config_space: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dynamic_discovery: Optional[pulumi.Input[bool]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            ip_anchored: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupServerArgs']]]]] = None) -> 'ZPAServerGroup':
        """
        Get an existing ZPAServerGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupAppConnectorGroupArgs']]]] app_connector_groups: List of app-connector IDs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupApplicationArgs']]]] applications: This field is a json array of app-connector-id only.
        :param pulumi.Input[str] description: This field is the description of the server group.
        :param pulumi.Input[bool] dynamic_discovery: This field controls dynamic discovery of the servers.
        :param pulumi.Input[bool] enabled: This field defines if the server group is enabled or disabled.
        :param pulumi.Input[str] name: This field defines the name of the server group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAServerGroupServerArgs']]]] servers: This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
               only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZPAServerGroupState.__new__(_ZPAServerGroupState)

        __props__.__dict__["app_connector_groups"] = app_connector_groups
        __props__.__dict__["applications"] = applications
        __props__.__dict__["config_space"] = config_space
        __props__.__dict__["description"] = description
        __props__.__dict__["dynamic_discovery"] = dynamic_discovery
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["ip_anchored"] = ip_anchored
        __props__.__dict__["name"] = name
        __props__.__dict__["servers"] = servers
        return ZPAServerGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appConnectorGroups")
    def app_connector_groups(self) -> pulumi.Output[Sequence['outputs.ZPAServerGroupAppConnectorGroup']]:
        """
        List of app-connector IDs.
        """
        return pulumi.get(self, "app_connector_groups")

    @property
    @pulumi.getter
    def applications(self) -> pulumi.Output[Sequence['outputs.ZPAServerGroupApplication']]:
        """
        This field is a json array of app-connector-id only.
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="configSpace")
    def config_space(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "config_space")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        This field is the description of the server group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dynamicDiscovery")
    def dynamic_discovery(self) -> pulumi.Output[Optional[bool]]:
        """
        This field controls dynamic discovery of the servers.
        """
        return pulumi.get(self, "dynamic_discovery")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        This field defines if the server group is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="ipAnchored")
    def ip_anchored(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "ip_anchored")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        This field defines the name of the server group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def servers(self) -> pulumi.Output[Sequence['outputs.ZPAServerGroupServer']]:
        """
        This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
        only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
        """
        return pulumi.get(self, "servers")

