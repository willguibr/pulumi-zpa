# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('zpa')


class _ExportableConfig(types.ModuleType):
    @property
    def zpa_client_id(self) -> Optional[str]:
        """
        zpa client id
        """
        return __config__.get('zpaClientId')

    @property
    def zpa_client_secret(self) -> Optional[str]:
        """
        zpa client secret
        """
        return __config__.get('zpaClientSecret')

    @property
    def zpa_customer_id(self) -> Optional[str]:
        """
        zpa customer id
        """
        return __config__.get('zpaCustomerId')
