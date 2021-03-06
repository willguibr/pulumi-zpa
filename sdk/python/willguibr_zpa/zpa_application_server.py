# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ZPAApplicationServerArgs', 'ZPAApplicationServer']

@pulumi.input_type
class ZPAApplicationServerArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 app_server_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZPAApplicationServer resource.
        :param pulumi.Input[str] address: This field defines the domain or IP address of the server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_server_group_ids: This field defines the list of server groups IDs.
        :param pulumi.Input[str] description: This field defines the description of the server.
        :param pulumi.Input[bool] enabled: This field defines the status of the server.
        :param pulumi.Input[str] name: This field defines the name of the server.
        """
        pulumi.set(__self__, "address", address)
        if app_server_group_ids is not None:
            pulumi.set(__self__, "app_server_group_ids", app_server_group_ids)
        if config_space is not None:
            pulumi.set(__self__, "config_space", config_space)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        This field defines the domain or IP address of the server.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="appServerGroupIds")
    def app_server_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        This field defines the list of server groups IDs.
        """
        return pulumi.get(self, "app_server_group_ids")

    @app_server_group_ids.setter
    def app_server_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "app_server_group_ids", value)

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
        This field defines the description of the server.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        This field defines the status of the server.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the name of the server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ZPAApplicationServerState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 app_server_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZPAApplicationServer resources.
        :param pulumi.Input[str] address: This field defines the domain or IP address of the server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_server_group_ids: This field defines the list of server groups IDs.
        :param pulumi.Input[str] description: This field defines the description of the server.
        :param pulumi.Input[bool] enabled: This field defines the status of the server.
        :param pulumi.Input[str] name: This field defines the name of the server.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if app_server_group_ids is not None:
            pulumi.set(__self__, "app_server_group_ids", app_server_group_ids)
        if config_space is not None:
            pulumi.set(__self__, "config_space", config_space)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the domain or IP address of the server.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="appServerGroupIds")
    def app_server_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        This field defines the list of server groups IDs.
        """
        return pulumi.get(self, "app_server_group_ids")

    @app_server_group_ids.setter
    def app_server_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "app_server_group_ids", value)

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
        This field defines the description of the server.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        This field defines the status of the server.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the name of the server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ZPAApplicationServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 app_server_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZPAApplicationServer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: This field defines the domain or IP address of the server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_server_group_ids: This field defines the list of server groups IDs.
        :param pulumi.Input[str] description: This field defines the description of the server.
        :param pulumi.Input[bool] enabled: This field defines the status of the server.
        :param pulumi.Input[str] name: This field defines the name of the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZPAApplicationServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZPAApplicationServer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZPAApplicationServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZPAApplicationServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 app_server_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_space: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ZPAApplicationServerArgs.__new__(ZPAApplicationServerArgs)

            if address is None and not opts.urn:
                raise TypeError("Missing required property 'address'")
            __props__.__dict__["address"] = address
            __props__.__dict__["app_server_group_ids"] = app_server_group_ids
            __props__.__dict__["config_space"] = config_space
            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
        super(ZPAApplicationServer, __self__).__init__(
            'zpa:index/zPAApplicationServer:ZPAApplicationServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            app_server_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            config_space: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ZPAApplicationServer':
        """
        Get an existing ZPAApplicationServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: This field defines the domain or IP address of the server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_server_group_ids: This field defines the list of server groups IDs.
        :param pulumi.Input[str] description: This field defines the description of the server.
        :param pulumi.Input[bool] enabled: This field defines the status of the server.
        :param pulumi.Input[str] name: This field defines the name of the server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZPAApplicationServerState.__new__(_ZPAApplicationServerState)

        __props__.__dict__["address"] = address
        __props__.__dict__["app_server_group_ids"] = app_server_group_ids
        __props__.__dict__["config_space"] = config_space
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        return ZPAApplicationServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        This field defines the domain or IP address of the server.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="appServerGroupIds")
    def app_server_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        This field defines the list of server groups IDs.
        """
        return pulumi.get(self, "app_server_group_ids")

    @property
    @pulumi.getter(name="configSpace")
    def config_space(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "config_space")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        This field defines the description of the server.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        This field defines the status of the server.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        This field defines the name of the server.
        """
        return pulumi.get(self, "name")

