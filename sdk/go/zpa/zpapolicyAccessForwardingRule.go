// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ZPAPolicyAccessForwardingRule struct {
	pulumi.CustomResourceState

	// This is for providing the rule action.
	Action pulumi.StringPtrOutput `pulumi:"action"`
	// This field defines the description of the server.
	ActionId          pulumi.StringPtrOutput `pulumi:"actionId"`
	BypassDefaultRule pulumi.BoolPtrOutput   `pulumi:"bypassDefaultRule"`
	// This is for proviidng the set of conditions for the policy.
	Conditions ZPAPolicyAccessForwardingRuleConditionArrayOutput `pulumi:"conditions"`
	// This is for providing a customer message for the user.
	CustomMsg pulumi.StringPtrOutput `pulumi:"customMsg"`
	// This is for providing a customer message for the user.
	DefaultRule pulumi.BoolPtrOutput `pulumi:"defaultRule"`
	// This is the description of the access policy.
	Description    pulumi.StringPtrOutput `pulumi:"description"`
	LssDefaultRule pulumi.BoolPtrOutput   `pulumi:"lssDefaultRule"`
	// This is the name of the policy.
	Name              pulumi.StringOutput    `pulumi:"name"`
	Operator          pulumi.StringOutput    `pulumi:"operator"`
	PolicySetId       pulumi.StringOutput    `pulumi:"policySetId"`
	PolicyType        pulumi.StringOutput    `pulumi:"policyType"`
	Priority          pulumi.StringOutput    `pulumi:"priority"`
	ReauthDefaultRule pulumi.BoolPtrOutput   `pulumi:"reauthDefaultRule"`
	ReauthIdleTimeout pulumi.StringPtrOutput `pulumi:"reauthIdleTimeout"`
	ReauthTimeout     pulumi.StringPtrOutput `pulumi:"reauthTimeout"`
	RuleOrder         pulumi.StringOutput    `pulumi:"ruleOrder"`
}

// NewZPAPolicyAccessForwardingRule registers a new resource with the given unique name, arguments, and options.
func NewZPAPolicyAccessForwardingRule(ctx *pulumi.Context,
	name string, args *ZPAPolicyAccessForwardingRuleArgs, opts ...pulumi.ResourceOption) (*ZPAPolicyAccessForwardingRule, error) {
	if args == nil {
		args = &ZPAPolicyAccessForwardingRuleArgs{}
	}

	opts = pkgResourceDefaultOpts(opts)
	var resource ZPAPolicyAccessForwardingRule
	err := ctx.RegisterResource("zpa:index/zPAPolicyAccessForwardingRule:ZPAPolicyAccessForwardingRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetZPAPolicyAccessForwardingRule gets an existing ZPAPolicyAccessForwardingRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetZPAPolicyAccessForwardingRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ZPAPolicyAccessForwardingRuleState, opts ...pulumi.ResourceOption) (*ZPAPolicyAccessForwardingRule, error) {
	var resource ZPAPolicyAccessForwardingRule
	err := ctx.ReadResource("zpa:index/zPAPolicyAccessForwardingRule:ZPAPolicyAccessForwardingRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ZPAPolicyAccessForwardingRule resources.
type zpapolicyAccessForwardingRuleState struct {
	// This is for providing the rule action.
	Action *string `pulumi:"action"`
	// This field defines the description of the server.
	ActionId          *string `pulumi:"actionId"`
	BypassDefaultRule *bool   `pulumi:"bypassDefaultRule"`
	// This is for proviidng the set of conditions for the policy.
	Conditions []ZPAPolicyAccessForwardingRuleCondition `pulumi:"conditions"`
	// This is for providing a customer message for the user.
	CustomMsg *string `pulumi:"customMsg"`
	// This is for providing a customer message for the user.
	DefaultRule *bool `pulumi:"defaultRule"`
	// This is the description of the access policy.
	Description    *string `pulumi:"description"`
	LssDefaultRule *bool   `pulumi:"lssDefaultRule"`
	// This is the name of the policy.
	Name              *string `pulumi:"name"`
	Operator          *string `pulumi:"operator"`
	PolicySetId       *string `pulumi:"policySetId"`
	PolicyType        *string `pulumi:"policyType"`
	Priority          *string `pulumi:"priority"`
	ReauthDefaultRule *bool   `pulumi:"reauthDefaultRule"`
	ReauthIdleTimeout *string `pulumi:"reauthIdleTimeout"`
	ReauthTimeout     *string `pulumi:"reauthTimeout"`
	RuleOrder         *string `pulumi:"ruleOrder"`
}

type ZPAPolicyAccessForwardingRuleState struct {
	// This is for providing the rule action.
	Action pulumi.StringPtrInput
	// This field defines the description of the server.
	ActionId          pulumi.StringPtrInput
	BypassDefaultRule pulumi.BoolPtrInput
	// This is for proviidng the set of conditions for the policy.
	Conditions ZPAPolicyAccessForwardingRuleConditionArrayInput
	// This is for providing a customer message for the user.
	CustomMsg pulumi.StringPtrInput
	// This is for providing a customer message for the user.
	DefaultRule pulumi.BoolPtrInput
	// This is the description of the access policy.
	Description    pulumi.StringPtrInput
	LssDefaultRule pulumi.BoolPtrInput
	// This is the name of the policy.
	Name              pulumi.StringPtrInput
	Operator          pulumi.StringPtrInput
	PolicySetId       pulumi.StringPtrInput
	PolicyType        pulumi.StringPtrInput
	Priority          pulumi.StringPtrInput
	ReauthDefaultRule pulumi.BoolPtrInput
	ReauthIdleTimeout pulumi.StringPtrInput
	ReauthTimeout     pulumi.StringPtrInput
	RuleOrder         pulumi.StringPtrInput
}

func (ZPAPolicyAccessForwardingRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*zpapolicyAccessForwardingRuleState)(nil)).Elem()
}

type zpapolicyAccessForwardingRuleArgs struct {
	// This is for providing the rule action.
	Action *string `pulumi:"action"`
	// This field defines the description of the server.
	ActionId          *string `pulumi:"actionId"`
	BypassDefaultRule *bool   `pulumi:"bypassDefaultRule"`
	// This is for proviidng the set of conditions for the policy.
	Conditions []ZPAPolicyAccessForwardingRuleCondition `pulumi:"conditions"`
	// This is for providing a customer message for the user.
	CustomMsg *string `pulumi:"customMsg"`
	// This is for providing a customer message for the user.
	DefaultRule *bool `pulumi:"defaultRule"`
	// This is the description of the access policy.
	Description    *string `pulumi:"description"`
	LssDefaultRule *bool   `pulumi:"lssDefaultRule"`
	// This is the name of the policy.
	Name              *string `pulumi:"name"`
	Operator          *string `pulumi:"operator"`
	PolicySetId       *string `pulumi:"policySetId"`
	PolicyType        *string `pulumi:"policyType"`
	Priority          *string `pulumi:"priority"`
	ReauthDefaultRule *bool   `pulumi:"reauthDefaultRule"`
	ReauthIdleTimeout *string `pulumi:"reauthIdleTimeout"`
	ReauthTimeout     *string `pulumi:"reauthTimeout"`
	RuleOrder         *string `pulumi:"ruleOrder"`
}

// The set of arguments for constructing a ZPAPolicyAccessForwardingRule resource.
type ZPAPolicyAccessForwardingRuleArgs struct {
	// This is for providing the rule action.
	Action pulumi.StringPtrInput
	// This field defines the description of the server.
	ActionId          pulumi.StringPtrInput
	BypassDefaultRule pulumi.BoolPtrInput
	// This is for proviidng the set of conditions for the policy.
	Conditions ZPAPolicyAccessForwardingRuleConditionArrayInput
	// This is for providing a customer message for the user.
	CustomMsg pulumi.StringPtrInput
	// This is for providing a customer message for the user.
	DefaultRule pulumi.BoolPtrInput
	// This is the description of the access policy.
	Description    pulumi.StringPtrInput
	LssDefaultRule pulumi.BoolPtrInput
	// This is the name of the policy.
	Name              pulumi.StringPtrInput
	Operator          pulumi.StringPtrInput
	PolicySetId       pulumi.StringPtrInput
	PolicyType        pulumi.StringPtrInput
	Priority          pulumi.StringPtrInput
	ReauthDefaultRule pulumi.BoolPtrInput
	ReauthIdleTimeout pulumi.StringPtrInput
	ReauthTimeout     pulumi.StringPtrInput
	RuleOrder         pulumi.StringPtrInput
}

func (ZPAPolicyAccessForwardingRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*zpapolicyAccessForwardingRuleArgs)(nil)).Elem()
}

type ZPAPolicyAccessForwardingRuleInput interface {
	pulumi.Input

	ToZPAPolicyAccessForwardingRuleOutput() ZPAPolicyAccessForwardingRuleOutput
	ToZPAPolicyAccessForwardingRuleOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleOutput
}

func (*ZPAPolicyAccessForwardingRule) ElementType() reflect.Type {
	return reflect.TypeOf((**ZPAPolicyAccessForwardingRule)(nil)).Elem()
}

func (i *ZPAPolicyAccessForwardingRule) ToZPAPolicyAccessForwardingRuleOutput() ZPAPolicyAccessForwardingRuleOutput {
	return i.ToZPAPolicyAccessForwardingRuleOutputWithContext(context.Background())
}

func (i *ZPAPolicyAccessForwardingRule) ToZPAPolicyAccessForwardingRuleOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZPAPolicyAccessForwardingRuleOutput)
}

// ZPAPolicyAccessForwardingRuleArrayInput is an input type that accepts ZPAPolicyAccessForwardingRuleArray and ZPAPolicyAccessForwardingRuleArrayOutput values.
// You can construct a concrete instance of `ZPAPolicyAccessForwardingRuleArrayInput` via:
//
//          ZPAPolicyAccessForwardingRuleArray{ ZPAPolicyAccessForwardingRuleArgs{...} }
type ZPAPolicyAccessForwardingRuleArrayInput interface {
	pulumi.Input

	ToZPAPolicyAccessForwardingRuleArrayOutput() ZPAPolicyAccessForwardingRuleArrayOutput
	ToZPAPolicyAccessForwardingRuleArrayOutputWithContext(context.Context) ZPAPolicyAccessForwardingRuleArrayOutput
}

type ZPAPolicyAccessForwardingRuleArray []ZPAPolicyAccessForwardingRuleInput

func (ZPAPolicyAccessForwardingRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZPAPolicyAccessForwardingRule)(nil)).Elem()
}

func (i ZPAPolicyAccessForwardingRuleArray) ToZPAPolicyAccessForwardingRuleArrayOutput() ZPAPolicyAccessForwardingRuleArrayOutput {
	return i.ToZPAPolicyAccessForwardingRuleArrayOutputWithContext(context.Background())
}

func (i ZPAPolicyAccessForwardingRuleArray) ToZPAPolicyAccessForwardingRuleArrayOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZPAPolicyAccessForwardingRuleArrayOutput)
}

// ZPAPolicyAccessForwardingRuleMapInput is an input type that accepts ZPAPolicyAccessForwardingRuleMap and ZPAPolicyAccessForwardingRuleMapOutput values.
// You can construct a concrete instance of `ZPAPolicyAccessForwardingRuleMapInput` via:
//
//          ZPAPolicyAccessForwardingRuleMap{ "key": ZPAPolicyAccessForwardingRuleArgs{...} }
type ZPAPolicyAccessForwardingRuleMapInput interface {
	pulumi.Input

	ToZPAPolicyAccessForwardingRuleMapOutput() ZPAPolicyAccessForwardingRuleMapOutput
	ToZPAPolicyAccessForwardingRuleMapOutputWithContext(context.Context) ZPAPolicyAccessForwardingRuleMapOutput
}

type ZPAPolicyAccessForwardingRuleMap map[string]ZPAPolicyAccessForwardingRuleInput

func (ZPAPolicyAccessForwardingRuleMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZPAPolicyAccessForwardingRule)(nil)).Elem()
}

func (i ZPAPolicyAccessForwardingRuleMap) ToZPAPolicyAccessForwardingRuleMapOutput() ZPAPolicyAccessForwardingRuleMapOutput {
	return i.ToZPAPolicyAccessForwardingRuleMapOutputWithContext(context.Background())
}

func (i ZPAPolicyAccessForwardingRuleMap) ToZPAPolicyAccessForwardingRuleMapOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZPAPolicyAccessForwardingRuleMapOutput)
}

type ZPAPolicyAccessForwardingRuleOutput struct{ *pulumi.OutputState }

func (ZPAPolicyAccessForwardingRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ZPAPolicyAccessForwardingRule)(nil)).Elem()
}

func (o ZPAPolicyAccessForwardingRuleOutput) ToZPAPolicyAccessForwardingRuleOutput() ZPAPolicyAccessForwardingRuleOutput {
	return o
}

func (o ZPAPolicyAccessForwardingRuleOutput) ToZPAPolicyAccessForwardingRuleOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleOutput {
	return o
}

// This is for providing the rule action.
func (o ZPAPolicyAccessForwardingRuleOutput) Action() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringPtrOutput { return v.Action }).(pulumi.StringPtrOutput)
}

// This field defines the description of the server.
func (o ZPAPolicyAccessForwardingRuleOutput) ActionId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringPtrOutput { return v.ActionId }).(pulumi.StringPtrOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) BypassDefaultRule() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.BoolPtrOutput { return v.BypassDefaultRule }).(pulumi.BoolPtrOutput)
}

// This is for proviidng the set of conditions for the policy.
func (o ZPAPolicyAccessForwardingRuleOutput) Conditions() ZPAPolicyAccessForwardingRuleConditionArrayOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) ZPAPolicyAccessForwardingRuleConditionArrayOutput {
		return v.Conditions
	}).(ZPAPolicyAccessForwardingRuleConditionArrayOutput)
}

// This is for providing a customer message for the user.
func (o ZPAPolicyAccessForwardingRuleOutput) CustomMsg() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringPtrOutput { return v.CustomMsg }).(pulumi.StringPtrOutput)
}

// This is for providing a customer message for the user.
func (o ZPAPolicyAccessForwardingRuleOutput) DefaultRule() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.BoolPtrOutput { return v.DefaultRule }).(pulumi.BoolPtrOutput)
}

// This is the description of the access policy.
func (o ZPAPolicyAccessForwardingRuleOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) LssDefaultRule() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.BoolPtrOutput { return v.LssDefaultRule }).(pulumi.BoolPtrOutput)
}

// This is the name of the policy.
func (o ZPAPolicyAccessForwardingRuleOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) Operator() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringOutput { return v.Operator }).(pulumi.StringOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) PolicySetId() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringOutput { return v.PolicySetId }).(pulumi.StringOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) PolicyType() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringOutput { return v.PolicyType }).(pulumi.StringOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) Priority() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringOutput { return v.Priority }).(pulumi.StringOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) ReauthDefaultRule() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.BoolPtrOutput { return v.ReauthDefaultRule }).(pulumi.BoolPtrOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) ReauthIdleTimeout() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringPtrOutput { return v.ReauthIdleTimeout }).(pulumi.StringPtrOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) ReauthTimeout() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringPtrOutput { return v.ReauthTimeout }).(pulumi.StringPtrOutput)
}

func (o ZPAPolicyAccessForwardingRuleOutput) RuleOrder() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAPolicyAccessForwardingRule) pulumi.StringOutput { return v.RuleOrder }).(pulumi.StringOutput)
}

type ZPAPolicyAccessForwardingRuleArrayOutput struct{ *pulumi.OutputState }

func (ZPAPolicyAccessForwardingRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZPAPolicyAccessForwardingRule)(nil)).Elem()
}

func (o ZPAPolicyAccessForwardingRuleArrayOutput) ToZPAPolicyAccessForwardingRuleArrayOutput() ZPAPolicyAccessForwardingRuleArrayOutput {
	return o
}

func (o ZPAPolicyAccessForwardingRuleArrayOutput) ToZPAPolicyAccessForwardingRuleArrayOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleArrayOutput {
	return o
}

func (o ZPAPolicyAccessForwardingRuleArrayOutput) Index(i pulumi.IntInput) ZPAPolicyAccessForwardingRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ZPAPolicyAccessForwardingRule {
		return vs[0].([]*ZPAPolicyAccessForwardingRule)[vs[1].(int)]
	}).(ZPAPolicyAccessForwardingRuleOutput)
}

type ZPAPolicyAccessForwardingRuleMapOutput struct{ *pulumi.OutputState }

func (ZPAPolicyAccessForwardingRuleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZPAPolicyAccessForwardingRule)(nil)).Elem()
}

func (o ZPAPolicyAccessForwardingRuleMapOutput) ToZPAPolicyAccessForwardingRuleMapOutput() ZPAPolicyAccessForwardingRuleMapOutput {
	return o
}

func (o ZPAPolicyAccessForwardingRuleMapOutput) ToZPAPolicyAccessForwardingRuleMapOutputWithContext(ctx context.Context) ZPAPolicyAccessForwardingRuleMapOutput {
	return o
}

func (o ZPAPolicyAccessForwardingRuleMapOutput) MapIndex(k pulumi.StringInput) ZPAPolicyAccessForwardingRuleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ZPAPolicyAccessForwardingRule {
		return vs[0].(map[string]*ZPAPolicyAccessForwardingRule)[vs[1].(string)]
	}).(ZPAPolicyAccessForwardingRuleOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ZPAPolicyAccessForwardingRuleInput)(nil)).Elem(), &ZPAPolicyAccessForwardingRule{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZPAPolicyAccessForwardingRuleArrayInput)(nil)).Elem(), ZPAPolicyAccessForwardingRuleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZPAPolicyAccessForwardingRuleMapInput)(nil)).Elem(), ZPAPolicyAccessForwardingRuleMap{})
	pulumi.RegisterOutputType(ZPAPolicyAccessForwardingRuleOutput{})
	pulumi.RegisterOutputType(ZPAPolicyAccessForwardingRuleArrayOutput{})
	pulumi.RegisterOutputType(ZPAPolicyAccessForwardingRuleMapOutput{})
}
