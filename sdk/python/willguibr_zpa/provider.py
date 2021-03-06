# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 zpa_client_id: pulumi.Input[str],
                 zpa_client_secret: pulumi.Input[str],
                 zpa_customer_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] zpa_client_id: zpa client id
        :param pulumi.Input[str] zpa_client_secret: zpa client secret
        :param pulumi.Input[str] zpa_customer_id: zpa customer id
        """
        pulumi.set(__self__, "zpa_client_id", zpa_client_id)
        pulumi.set(__self__, "zpa_client_secret", zpa_client_secret)
        pulumi.set(__self__, "zpa_customer_id", zpa_customer_id)

    @property
    @pulumi.getter(name="zpaClientId")
    def zpa_client_id(self) -> pulumi.Input[str]:
        """
        zpa client id
        """
        return pulumi.get(self, "zpa_client_id")

    @zpa_client_id.setter
    def zpa_client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zpa_client_id", value)

    @property
    @pulumi.getter(name="zpaClientSecret")
    def zpa_client_secret(self) -> pulumi.Input[str]:
        """
        zpa client secret
        """
        return pulumi.get(self, "zpa_client_secret")

    @zpa_client_secret.setter
    def zpa_client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "zpa_client_secret", value)

    @property
    @pulumi.getter(name="zpaCustomerId")
    def zpa_customer_id(self) -> pulumi.Input[str]:
        """
        zpa customer id
        """
        return pulumi.get(self, "zpa_customer_id")

    @zpa_customer_id.setter
    def zpa_customer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zpa_customer_id", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 zpa_client_id: Optional[pulumi.Input[str]] = None,
                 zpa_client_secret: Optional[pulumi.Input[str]] = None,
                 zpa_customer_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the zpa package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] zpa_client_id: zpa client id
        :param pulumi.Input[str] zpa_client_secret: zpa client secret
        :param pulumi.Input[str] zpa_customer_id: zpa customer id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the zpa package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 zpa_client_id: Optional[pulumi.Input[str]] = None,
                 zpa_client_secret: Optional[pulumi.Input[str]] = None,
                 zpa_customer_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if zpa_client_id is None and not opts.urn:
                raise TypeError("Missing required property 'zpa_client_id'")
            __props__.__dict__["zpa_client_id"] = zpa_client_id
            if zpa_client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'zpa_client_secret'")
            __props__.__dict__["zpa_client_secret"] = zpa_client_secret
            if zpa_customer_id is None and not opts.urn:
                raise TypeError("Missing required property 'zpa_customer_id'")
            __props__.__dict__["zpa_customer_id"] = zpa_customer_id
        super(Provider, __self__).__init__(
            'zpa',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="zpaClientId")
    def zpa_client_id(self) -> pulumi.Output[str]:
        """
        zpa client id
        """
        return pulumi.get(self, "zpa_client_id")

    @property
    @pulumi.getter(name="zpaClientSecret")
    def zpa_client_secret(self) -> pulumi.Output[str]:
        """
        zpa client secret
        """
        return pulumi.get(self, "zpa_client_secret")

    @property
    @pulumi.getter(name="zpaCustomerId")
    def zpa_customer_id(self) -> pulumi.Output[str]:
        """
        zpa customer id
        """
        return pulumi.get(self, "zpa_customer_id")

