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

__all__ = ['ZPAPolicyAccessTimeoutRuleArgs', 'ZPAPolicyAccessTimeoutRule']

@pulumi.input_type
class ZPAPolicyAccessTimeoutRuleArgs:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 action_id: Optional[pulumi.Input[str]] = None,
                 bypass_default_rule: Optional[pulumi.Input[bool]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]]] = None,
                 custom_msg: Optional[pulumi.Input[str]] = None,
                 default_rule: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lss_default_rule: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator: Optional[pulumi.Input[str]] = None,
                 policy_set_id: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 reauth_default_rule: Optional[pulumi.Input[bool]] = None,
                 reauth_idle_timeout: Optional[pulumi.Input[str]] = None,
                 reauth_timeout: Optional[pulumi.Input[str]] = None,
                 rule_order: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZPAPolicyAccessTimeoutRule resource.
        :param pulumi.Input[str] action: This is for providing the rule action.
        :param pulumi.Input[str] action_id: This field defines the description of the server.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]] conditions: This is for proviidng the set of conditions for the policy.
        :param pulumi.Input[str] custom_msg: This is for providing a customer message for the user.
        :param pulumi.Input[bool] default_rule: This is for providing a customer message for the user.
        :param pulumi.Input[str] description: This is the description of the access policy.
        :param pulumi.Input[str] name: This is the name of the policy.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if action_id is not None:
            pulumi.set(__self__, "action_id", action_id)
        if bypass_default_rule is not None:
            pulumi.set(__self__, "bypass_default_rule", bypass_default_rule)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if custom_msg is not None:
            pulumi.set(__self__, "custom_msg", custom_msg)
        if default_rule is not None:
            pulumi.set(__self__, "default_rule", default_rule)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if lss_default_rule is not None:
            pulumi.set(__self__, "lss_default_rule", lss_default_rule)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operator is not None:
            pulumi.set(__self__, "operator", operator)
        if policy_set_id is not None:
            pulumi.set(__self__, "policy_set_id", policy_set_id)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if reauth_default_rule is not None:
            pulumi.set(__self__, "reauth_default_rule", reauth_default_rule)
        if reauth_idle_timeout is not None:
            pulumi.set(__self__, "reauth_idle_timeout", reauth_idle_timeout)
        if reauth_timeout is not None:
            pulumi.set(__self__, "reauth_timeout", reauth_timeout)
        if rule_order is not None:
            pulumi.set(__self__, "rule_order", rule_order)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        This is for providing the rule action.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the description of the server.
        """
        return pulumi.get(self, "action_id")

    @action_id.setter
    def action_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_id", value)

    @property
    @pulumi.getter(name="bypassDefaultRule")
    def bypass_default_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "bypass_default_rule")

    @bypass_default_rule.setter
    def bypass_default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bypass_default_rule", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]:
        """
        This is for proviidng the set of conditions for the policy.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="customMsg")
    def custom_msg(self) -> Optional[pulumi.Input[str]]:
        """
        This is for providing a customer message for the user.
        """
        return pulumi.get(self, "custom_msg")

    @custom_msg.setter
    def custom_msg(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_msg", value)

    @property
    @pulumi.getter(name="defaultRule")
    def default_rule(self) -> Optional[pulumi.Input[bool]]:
        """
        This is for providing a customer message for the user.
        """
        return pulumi.get(self, "default_rule")

    @default_rule.setter
    def default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_rule", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        This is the description of the access policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lssDefaultRule")
    def lss_default_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "lss_default_rule")

    @lss_default_rule.setter
    def lss_default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lss_default_rule", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        This is the name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter(name="policySetId")
    def policy_set_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_set_id")

    @policy_set_id.setter
    def policy_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_set_id", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="reauthDefaultRule")
    def reauth_default_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "reauth_default_rule")

    @reauth_default_rule.setter
    def reauth_default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reauth_default_rule", value)

    @property
    @pulumi.getter(name="reauthIdleTimeout")
    def reauth_idle_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "reauth_idle_timeout")

    @reauth_idle_timeout.setter
    def reauth_idle_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reauth_idle_timeout", value)

    @property
    @pulumi.getter(name="reauthTimeout")
    def reauth_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "reauth_timeout")

    @reauth_timeout.setter
    def reauth_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reauth_timeout", value)

    @property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rule_order")

    @rule_order.setter
    def rule_order(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_order", value)


@pulumi.input_type
class _ZPAPolicyAccessTimeoutRuleState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 action_id: Optional[pulumi.Input[str]] = None,
                 bypass_default_rule: Optional[pulumi.Input[bool]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]]] = None,
                 custom_msg: Optional[pulumi.Input[str]] = None,
                 default_rule: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lss_default_rule: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator: Optional[pulumi.Input[str]] = None,
                 policy_set_id: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 reauth_default_rule: Optional[pulumi.Input[bool]] = None,
                 reauth_idle_timeout: Optional[pulumi.Input[str]] = None,
                 reauth_timeout: Optional[pulumi.Input[str]] = None,
                 rule_order: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZPAPolicyAccessTimeoutRule resources.
        :param pulumi.Input[str] action: This is for providing the rule action.
        :param pulumi.Input[str] action_id: This field defines the description of the server.
        :param pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]] conditions: This is for proviidng the set of conditions for the policy.
        :param pulumi.Input[str] custom_msg: This is for providing a customer message for the user.
        :param pulumi.Input[bool] default_rule: This is for providing a customer message for the user.
        :param pulumi.Input[str] description: This is the description of the access policy.
        :param pulumi.Input[str] name: This is the name of the policy.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if action_id is not None:
            pulumi.set(__self__, "action_id", action_id)
        if bypass_default_rule is not None:
            pulumi.set(__self__, "bypass_default_rule", bypass_default_rule)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if custom_msg is not None:
            pulumi.set(__self__, "custom_msg", custom_msg)
        if default_rule is not None:
            pulumi.set(__self__, "default_rule", default_rule)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if lss_default_rule is not None:
            pulumi.set(__self__, "lss_default_rule", lss_default_rule)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if operator is not None:
            pulumi.set(__self__, "operator", operator)
        if policy_set_id is not None:
            pulumi.set(__self__, "policy_set_id", policy_set_id)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if reauth_default_rule is not None:
            pulumi.set(__self__, "reauth_default_rule", reauth_default_rule)
        if reauth_idle_timeout is not None:
            pulumi.set(__self__, "reauth_idle_timeout", reauth_idle_timeout)
        if reauth_timeout is not None:
            pulumi.set(__self__, "reauth_timeout", reauth_timeout)
        if rule_order is not None:
            pulumi.set(__self__, "rule_order", rule_order)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        This is for providing the rule action.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[pulumi.Input[str]]:
        """
        This field defines the description of the server.
        """
        return pulumi.get(self, "action_id")

    @action_id.setter
    def action_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_id", value)

    @property
    @pulumi.getter(name="bypassDefaultRule")
    def bypass_default_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "bypass_default_rule")

    @bypass_default_rule.setter
    def bypass_default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bypass_default_rule", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]:
        """
        This is for proviidng the set of conditions for the policy.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="customMsg")
    def custom_msg(self) -> Optional[pulumi.Input[str]]:
        """
        This is for providing a customer message for the user.
        """
        return pulumi.get(self, "custom_msg")

    @custom_msg.setter
    def custom_msg(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_msg", value)

    @property
    @pulumi.getter(name="defaultRule")
    def default_rule(self) -> Optional[pulumi.Input[bool]]:
        """
        This is for providing a customer message for the user.
        """
        return pulumi.get(self, "default_rule")

    @default_rule.setter
    def default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_rule", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        This is the description of the access policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lssDefaultRule")
    def lss_default_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "lss_default_rule")

    @lss_default_rule.setter
    def lss_default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lss_default_rule", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        This is the name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter(name="policySetId")
    def policy_set_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_set_id")

    @policy_set_id.setter
    def policy_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_set_id", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="reauthDefaultRule")
    def reauth_default_rule(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "reauth_default_rule")

    @reauth_default_rule.setter
    def reauth_default_rule(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reauth_default_rule", value)

    @property
    @pulumi.getter(name="reauthIdleTimeout")
    def reauth_idle_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "reauth_idle_timeout")

    @reauth_idle_timeout.setter
    def reauth_idle_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reauth_idle_timeout", value)

    @property
    @pulumi.getter(name="reauthTimeout")
    def reauth_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "reauth_timeout")

    @reauth_timeout.setter
    def reauth_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reauth_timeout", value)

    @property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rule_order")

    @rule_order.setter
    def rule_order(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_order", value)


class ZPAPolicyAccessTimeoutRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 action_id: Optional[pulumi.Input[str]] = None,
                 bypass_default_rule: Optional[pulumi.Input[bool]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]] = None,
                 custom_msg: Optional[pulumi.Input[str]] = None,
                 default_rule: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lss_default_rule: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator: Optional[pulumi.Input[str]] = None,
                 policy_set_id: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 reauth_default_rule: Optional[pulumi.Input[bool]] = None,
                 reauth_idle_timeout: Optional[pulumi.Input[str]] = None,
                 reauth_timeout: Optional[pulumi.Input[str]] = None,
                 rule_order: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZPAPolicyAccessTimeoutRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: This is for providing the rule action.
        :param pulumi.Input[str] action_id: This field defines the description of the server.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAPolicyAccessTimeoutRuleConditionArgs']]]] conditions: This is for proviidng the set of conditions for the policy.
        :param pulumi.Input[str] custom_msg: This is for providing a customer message for the user.
        :param pulumi.Input[bool] default_rule: This is for providing a customer message for the user.
        :param pulumi.Input[str] description: This is the description of the access policy.
        :param pulumi.Input[str] name: This is the name of the policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ZPAPolicyAccessTimeoutRuleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZPAPolicyAccessTimeoutRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZPAPolicyAccessTimeoutRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZPAPolicyAccessTimeoutRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 action_id: Optional[pulumi.Input[str]] = None,
                 bypass_default_rule: Optional[pulumi.Input[bool]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]] = None,
                 custom_msg: Optional[pulumi.Input[str]] = None,
                 default_rule: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lss_default_rule: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operator: Optional[pulumi.Input[str]] = None,
                 policy_set_id: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 reauth_default_rule: Optional[pulumi.Input[bool]] = None,
                 reauth_idle_timeout: Optional[pulumi.Input[str]] = None,
                 reauth_timeout: Optional[pulumi.Input[str]] = None,
                 rule_order: Optional[pulumi.Input[str]] = None,
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
            __props__ = ZPAPolicyAccessTimeoutRuleArgs.__new__(ZPAPolicyAccessTimeoutRuleArgs)

            __props__.__dict__["action"] = action
            __props__.__dict__["action_id"] = action_id
            __props__.__dict__["bypass_default_rule"] = bypass_default_rule
            __props__.__dict__["conditions"] = conditions
            __props__.__dict__["custom_msg"] = custom_msg
            __props__.__dict__["default_rule"] = default_rule
            __props__.__dict__["description"] = description
            __props__.__dict__["lss_default_rule"] = lss_default_rule
            __props__.__dict__["name"] = name
            __props__.__dict__["operator"] = operator
            __props__.__dict__["policy_set_id"] = policy_set_id
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["priority"] = priority
            __props__.__dict__["reauth_default_rule"] = reauth_default_rule
            __props__.__dict__["reauth_idle_timeout"] = reauth_idle_timeout
            __props__.__dict__["reauth_timeout"] = reauth_timeout
            __props__.__dict__["rule_order"] = rule_order
        super(ZPAPolicyAccessTimeoutRule, __self__).__init__(
            'zpa:index/zPAPolicyAccessTimeoutRule:ZPAPolicyAccessTimeoutRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            action_id: Optional[pulumi.Input[str]] = None,
            bypass_default_rule: Optional[pulumi.Input[bool]] = None,
            conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAPolicyAccessTimeoutRuleConditionArgs']]]]] = None,
            custom_msg: Optional[pulumi.Input[str]] = None,
            default_rule: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            lss_default_rule: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            operator: Optional[pulumi.Input[str]] = None,
            policy_set_id: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[str]] = None,
            reauth_default_rule: Optional[pulumi.Input[bool]] = None,
            reauth_idle_timeout: Optional[pulumi.Input[str]] = None,
            reauth_timeout: Optional[pulumi.Input[str]] = None,
            rule_order: Optional[pulumi.Input[str]] = None) -> 'ZPAPolicyAccessTimeoutRule':
        """
        Get an existing ZPAPolicyAccessTimeoutRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: This is for providing the rule action.
        :param pulumi.Input[str] action_id: This field defines the description of the server.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZPAPolicyAccessTimeoutRuleConditionArgs']]]] conditions: This is for proviidng the set of conditions for the policy.
        :param pulumi.Input[str] custom_msg: This is for providing a customer message for the user.
        :param pulumi.Input[bool] default_rule: This is for providing a customer message for the user.
        :param pulumi.Input[str] description: This is the description of the access policy.
        :param pulumi.Input[str] name: This is the name of the policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZPAPolicyAccessTimeoutRuleState.__new__(_ZPAPolicyAccessTimeoutRuleState)

        __props__.__dict__["action"] = action
        __props__.__dict__["action_id"] = action_id
        __props__.__dict__["bypass_default_rule"] = bypass_default_rule
        __props__.__dict__["conditions"] = conditions
        __props__.__dict__["custom_msg"] = custom_msg
        __props__.__dict__["default_rule"] = default_rule
        __props__.__dict__["description"] = description
        __props__.__dict__["lss_default_rule"] = lss_default_rule
        __props__.__dict__["name"] = name
        __props__.__dict__["operator"] = operator
        __props__.__dict__["policy_set_id"] = policy_set_id
        __props__.__dict__["policy_type"] = policy_type
        __props__.__dict__["priority"] = priority
        __props__.__dict__["reauth_default_rule"] = reauth_default_rule
        __props__.__dict__["reauth_idle_timeout"] = reauth_idle_timeout
        __props__.__dict__["reauth_timeout"] = reauth_timeout
        __props__.__dict__["rule_order"] = rule_order
        return ZPAPolicyAccessTimeoutRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[Optional[str]]:
        """
        This is for providing the rule action.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="actionId")
    def action_id(self) -> pulumi.Output[Optional[str]]:
        """
        This field defines the description of the server.
        """
        return pulumi.get(self, "action_id")

    @property
    @pulumi.getter(name="bypassDefaultRule")
    def bypass_default_rule(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "bypass_default_rule")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence['outputs.ZPAPolicyAccessTimeoutRuleCondition']]:
        """
        This is for proviidng the set of conditions for the policy.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="customMsg")
    def custom_msg(self) -> pulumi.Output[Optional[str]]:
        """
        This is for providing a customer message for the user.
        """
        return pulumi.get(self, "custom_msg")

    @property
    @pulumi.getter(name="defaultRule")
    def default_rule(self) -> pulumi.Output[Optional[bool]]:
        """
        This is for providing a customer message for the user.
        """
        return pulumi.get(self, "default_rule")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        This is the description of the access policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lssDefaultRule")
    def lss_default_rule(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "lss_default_rule")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        This is the name of the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Output[str]:
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter(name="policySetId")
    def policy_set_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_set_id")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[str]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="reauthDefaultRule")
    def reauth_default_rule(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "reauth_default_rule")

    @property
    @pulumi.getter(name="reauthIdleTimeout")
    def reauth_idle_timeout(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "reauth_idle_timeout")

    @property
    @pulumi.getter(name="reauthTimeout")
    def reauth_timeout(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "reauth_timeout")

    @property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> pulumi.Output[str]:
        return pulumi.get(self, "rule_order")

