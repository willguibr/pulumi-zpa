// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ZPAServerGroup struct {
	pulumi.CustomResourceState

	// List of app-connector IDs.
	AppConnectorGroups ZPAServerGroupAppConnectorGroupArrayOutput `pulumi:"appConnectorGroups"`
	// This field is a json array of app-connector-id only.
	Applications ZPAServerGroupApplicationArrayOutput `pulumi:"applications"`
	ConfigSpace  pulumi.StringPtrOutput               `pulumi:"configSpace"`
	// This field is the description of the server group.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// This field controls dynamic discovery of the servers.
	DynamicDiscovery pulumi.BoolPtrOutput `pulumi:"dynamicDiscovery"`
	// This field defines if the server group is enabled or disabled.
	Enabled    pulumi.BoolPtrOutput `pulumi:"enabled"`
	IpAnchored pulumi.BoolPtrOutput `pulumi:"ipAnchored"`
	// This field defines the name of the server group.
	Name pulumi.StringOutput `pulumi:"name"`
	// This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
	// only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
	Servers ZPAServerGroupServerArrayOutput `pulumi:"servers"`
}

// NewZPAServerGroup registers a new resource with the given unique name, arguments, and options.
func NewZPAServerGroup(ctx *pulumi.Context,
	name string, args *ZPAServerGroupArgs, opts ...pulumi.ResourceOption) (*ZPAServerGroup, error) {
	if args == nil {
		args = &ZPAServerGroupArgs{}
	}

	opts = pkgResourceDefaultOpts(opts)
	var resource ZPAServerGroup
	err := ctx.RegisterResource("zpa:index/zPAServerGroup:ZPAServerGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetZPAServerGroup gets an existing ZPAServerGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetZPAServerGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ZPAServerGroupState, opts ...pulumi.ResourceOption) (*ZPAServerGroup, error) {
	var resource ZPAServerGroup
	err := ctx.ReadResource("zpa:index/zPAServerGroup:ZPAServerGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ZPAServerGroup resources.
type zpaserverGroupState struct {
	// List of app-connector IDs.
	AppConnectorGroups []ZPAServerGroupAppConnectorGroup `pulumi:"appConnectorGroups"`
	// This field is a json array of app-connector-id only.
	Applications []ZPAServerGroupApplication `pulumi:"applications"`
	ConfigSpace  *string                     `pulumi:"configSpace"`
	// This field is the description of the server group.
	Description *string `pulumi:"description"`
	// This field controls dynamic discovery of the servers.
	DynamicDiscovery *bool `pulumi:"dynamicDiscovery"`
	// This field defines if the server group is enabled or disabled.
	Enabled    *bool `pulumi:"enabled"`
	IpAnchored *bool `pulumi:"ipAnchored"`
	// This field defines the name of the server group.
	Name *string `pulumi:"name"`
	// This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
	// only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
	Servers []ZPAServerGroupServer `pulumi:"servers"`
}

type ZPAServerGroupState struct {
	// List of app-connector IDs.
	AppConnectorGroups ZPAServerGroupAppConnectorGroupArrayInput
	// This field is a json array of app-connector-id only.
	Applications ZPAServerGroupApplicationArrayInput
	ConfigSpace  pulumi.StringPtrInput
	// This field is the description of the server group.
	Description pulumi.StringPtrInput
	// This field controls dynamic discovery of the servers.
	DynamicDiscovery pulumi.BoolPtrInput
	// This field defines if the server group is enabled or disabled.
	Enabled    pulumi.BoolPtrInput
	IpAnchored pulumi.BoolPtrInput
	// This field defines the name of the server group.
	Name pulumi.StringPtrInput
	// This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
	// only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
	Servers ZPAServerGroupServerArrayInput
}

func (ZPAServerGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*zpaserverGroupState)(nil)).Elem()
}

type zpaserverGroupArgs struct {
	// List of app-connector IDs.
	AppConnectorGroups []ZPAServerGroupAppConnectorGroup `pulumi:"appConnectorGroups"`
	// This field is a json array of app-connector-id only.
	Applications []ZPAServerGroupApplication `pulumi:"applications"`
	ConfigSpace  *string                     `pulumi:"configSpace"`
	// This field is the description of the server group.
	Description *string `pulumi:"description"`
	// This field controls dynamic discovery of the servers.
	DynamicDiscovery *bool `pulumi:"dynamicDiscovery"`
	// This field defines if the server group is enabled or disabled.
	Enabled    *bool `pulumi:"enabled"`
	IpAnchored *bool `pulumi:"ipAnchored"`
	// This field defines the name of the server group.
	Name *string `pulumi:"name"`
	// This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
	// only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
	Servers []ZPAServerGroupServer `pulumi:"servers"`
}

// The set of arguments for constructing a ZPAServerGroup resource.
type ZPAServerGroupArgs struct {
	// List of app-connector IDs.
	AppConnectorGroups ZPAServerGroupAppConnectorGroupArrayInput
	// This field is a json array of app-connector-id only.
	Applications ZPAServerGroupApplicationArrayInput
	ConfigSpace  pulumi.StringPtrInput
	// This field is the description of the server group.
	Description pulumi.StringPtrInput
	// This field controls dynamic discovery of the servers.
	DynamicDiscovery pulumi.BoolPtrInput
	// This field defines if the server group is enabled or disabled.
	Enabled    pulumi.BoolPtrInput
	IpAnchored pulumi.BoolPtrInput
	// This field defines the name of the server group.
	Name pulumi.StringPtrInput
	// This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
	// only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
	Servers ZPAServerGroupServerArrayInput
}

func (ZPAServerGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*zpaserverGroupArgs)(nil)).Elem()
}

type ZPAServerGroupInput interface {
	pulumi.Input

	ToZPAServerGroupOutput() ZPAServerGroupOutput
	ToZPAServerGroupOutputWithContext(ctx context.Context) ZPAServerGroupOutput
}

func (*ZPAServerGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**ZPAServerGroup)(nil)).Elem()
}

func (i *ZPAServerGroup) ToZPAServerGroupOutput() ZPAServerGroupOutput {
	return i.ToZPAServerGroupOutputWithContext(context.Background())
}

func (i *ZPAServerGroup) ToZPAServerGroupOutputWithContext(ctx context.Context) ZPAServerGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZPAServerGroupOutput)
}

// ZPAServerGroupArrayInput is an input type that accepts ZPAServerGroupArray and ZPAServerGroupArrayOutput values.
// You can construct a concrete instance of `ZPAServerGroupArrayInput` via:
//
//          ZPAServerGroupArray{ ZPAServerGroupArgs{...} }
type ZPAServerGroupArrayInput interface {
	pulumi.Input

	ToZPAServerGroupArrayOutput() ZPAServerGroupArrayOutput
	ToZPAServerGroupArrayOutputWithContext(context.Context) ZPAServerGroupArrayOutput
}

type ZPAServerGroupArray []ZPAServerGroupInput

func (ZPAServerGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZPAServerGroup)(nil)).Elem()
}

func (i ZPAServerGroupArray) ToZPAServerGroupArrayOutput() ZPAServerGroupArrayOutput {
	return i.ToZPAServerGroupArrayOutputWithContext(context.Background())
}

func (i ZPAServerGroupArray) ToZPAServerGroupArrayOutputWithContext(ctx context.Context) ZPAServerGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZPAServerGroupArrayOutput)
}

// ZPAServerGroupMapInput is an input type that accepts ZPAServerGroupMap and ZPAServerGroupMapOutput values.
// You can construct a concrete instance of `ZPAServerGroupMapInput` via:
//
//          ZPAServerGroupMap{ "key": ZPAServerGroupArgs{...} }
type ZPAServerGroupMapInput interface {
	pulumi.Input

	ToZPAServerGroupMapOutput() ZPAServerGroupMapOutput
	ToZPAServerGroupMapOutputWithContext(context.Context) ZPAServerGroupMapOutput
}

type ZPAServerGroupMap map[string]ZPAServerGroupInput

func (ZPAServerGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZPAServerGroup)(nil)).Elem()
}

func (i ZPAServerGroupMap) ToZPAServerGroupMapOutput() ZPAServerGroupMapOutput {
	return i.ToZPAServerGroupMapOutputWithContext(context.Background())
}

func (i ZPAServerGroupMap) ToZPAServerGroupMapOutputWithContext(ctx context.Context) ZPAServerGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZPAServerGroupMapOutput)
}

type ZPAServerGroupOutput struct{ *pulumi.OutputState }

func (ZPAServerGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ZPAServerGroup)(nil)).Elem()
}

func (o ZPAServerGroupOutput) ToZPAServerGroupOutput() ZPAServerGroupOutput {
	return o
}

func (o ZPAServerGroupOutput) ToZPAServerGroupOutputWithContext(ctx context.Context) ZPAServerGroupOutput {
	return o
}

// List of app-connector IDs.
func (o ZPAServerGroupOutput) AppConnectorGroups() ZPAServerGroupAppConnectorGroupArrayOutput {
	return o.ApplyT(func(v *ZPAServerGroup) ZPAServerGroupAppConnectorGroupArrayOutput { return v.AppConnectorGroups }).(ZPAServerGroupAppConnectorGroupArrayOutput)
}

// This field is a json array of app-connector-id only.
func (o ZPAServerGroupOutput) Applications() ZPAServerGroupApplicationArrayOutput {
	return o.ApplyT(func(v *ZPAServerGroup) ZPAServerGroupApplicationArrayOutput { return v.Applications }).(ZPAServerGroupApplicationArrayOutput)
}

func (o ZPAServerGroupOutput) ConfigSpace() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAServerGroup) pulumi.StringPtrOutput { return v.ConfigSpace }).(pulumi.StringPtrOutput)
}

// This field is the description of the server group.
func (o ZPAServerGroupOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZPAServerGroup) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// This field controls dynamic discovery of the servers.
func (o ZPAServerGroupOutput) DynamicDiscovery() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAServerGroup) pulumi.BoolPtrOutput { return v.DynamicDiscovery }).(pulumi.BoolPtrOutput)
}

// This field defines if the server group is enabled or disabled.
func (o ZPAServerGroupOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAServerGroup) pulumi.BoolPtrOutput { return v.Enabled }).(pulumi.BoolPtrOutput)
}

func (o ZPAServerGroupOutput) IpAnchored() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ZPAServerGroup) pulumi.BoolPtrOutput { return v.IpAnchored }).(pulumi.BoolPtrOutput)
}

// This field defines the name of the server group.
func (o ZPAServerGroupOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ZPAServerGroup) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// This field is a list of servers that are applicable only when dynamic discovery is disabled. Server name is required
// only in cases where the new servers need to be created in this API. For existing servers, pass only the serverId.
func (o ZPAServerGroupOutput) Servers() ZPAServerGroupServerArrayOutput {
	return o.ApplyT(func(v *ZPAServerGroup) ZPAServerGroupServerArrayOutput { return v.Servers }).(ZPAServerGroupServerArrayOutput)
}

type ZPAServerGroupArrayOutput struct{ *pulumi.OutputState }

func (ZPAServerGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZPAServerGroup)(nil)).Elem()
}

func (o ZPAServerGroupArrayOutput) ToZPAServerGroupArrayOutput() ZPAServerGroupArrayOutput {
	return o
}

func (o ZPAServerGroupArrayOutput) ToZPAServerGroupArrayOutputWithContext(ctx context.Context) ZPAServerGroupArrayOutput {
	return o
}

func (o ZPAServerGroupArrayOutput) Index(i pulumi.IntInput) ZPAServerGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ZPAServerGroup {
		return vs[0].([]*ZPAServerGroup)[vs[1].(int)]
	}).(ZPAServerGroupOutput)
}

type ZPAServerGroupMapOutput struct{ *pulumi.OutputState }

func (ZPAServerGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZPAServerGroup)(nil)).Elem()
}

func (o ZPAServerGroupMapOutput) ToZPAServerGroupMapOutput() ZPAServerGroupMapOutput {
	return o
}

func (o ZPAServerGroupMapOutput) ToZPAServerGroupMapOutputWithContext(ctx context.Context) ZPAServerGroupMapOutput {
	return o
}

func (o ZPAServerGroupMapOutput) MapIndex(k pulumi.StringInput) ZPAServerGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ZPAServerGroup {
		return vs[0].(map[string]*ZPAServerGroup)[vs[1].(string)]
	}).(ZPAServerGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ZPAServerGroupInput)(nil)).Elem(), &ZPAServerGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZPAServerGroupArrayInput)(nil)).Elem(), ZPAServerGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZPAServerGroupMapInput)(nil)).Elem(), ZPAServerGroupMap{})
	pulumi.RegisterOutputType(ZPAServerGroupOutput{})
	pulumi.RegisterOutputType(ZPAServerGroupArrayOutput{})
	pulumi.RegisterOutputType(ZPAServerGroupMapOutput{})
}
