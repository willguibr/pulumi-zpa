// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetZPALSSConfigMachineGroup(ctx *pulumi.Context, args *GetZPALSSConfigMachineGroupArgs, opts ...pulumi.InvokeOption) (*GetZPALSSConfigMachineGroupResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetZPALSSConfigMachineGroupResult
	err := ctx.Invoke("zpa:index/getZPALSSConfigMachineGroup:getZPALSSConfigMachineGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZPALSSConfigMachineGroup.
type GetZPALSSConfigMachineGroupArgs struct {
	Id   *string `pulumi:"id"`
	Name *string `pulumi:"name"`
}

// A collection of values returned by getZPALSSConfigMachineGroup.
type GetZPALSSConfigMachineGroupResult struct {
	CreationTime string                               `pulumi:"creationTime"`
	Description  string                               `pulumi:"description"`
	Enabled      bool                                 `pulumi:"enabled"`
	Id           *string                              `pulumi:"id"`
	Machines     []GetZPALSSConfigMachineGroupMachine `pulumi:"machines"`
	ModifiedTime string                               `pulumi:"modifiedTime"`
	Modifiedby   string                               `pulumi:"modifiedby"`
	Name         *string                              `pulumi:"name"`
}

func GetZPALSSConfigMachineGroupOutput(ctx *pulumi.Context, args GetZPALSSConfigMachineGroupOutputArgs, opts ...pulumi.InvokeOption) GetZPALSSConfigMachineGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetZPALSSConfigMachineGroupResult, error) {
			args := v.(GetZPALSSConfigMachineGroupArgs)
			r, err := GetZPALSSConfigMachineGroup(ctx, &args, opts...)
			var s GetZPALSSConfigMachineGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetZPALSSConfigMachineGroupResultOutput)
}

// A collection of arguments for invoking getZPALSSConfigMachineGroup.
type GetZPALSSConfigMachineGroupOutputArgs struct {
	Id   pulumi.StringPtrInput `pulumi:"id"`
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetZPALSSConfigMachineGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPALSSConfigMachineGroupArgs)(nil)).Elem()
}

// A collection of values returned by getZPALSSConfigMachineGroup.
type GetZPALSSConfigMachineGroupResultOutput struct{ *pulumi.OutputState }

func (GetZPALSSConfigMachineGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPALSSConfigMachineGroupResult)(nil)).Elem()
}

func (o GetZPALSSConfigMachineGroupResultOutput) ToGetZPALSSConfigMachineGroupResultOutput() GetZPALSSConfigMachineGroupResultOutput {
	return o
}

func (o GetZPALSSConfigMachineGroupResultOutput) ToGetZPALSSConfigMachineGroupResultOutputWithContext(ctx context.Context) GetZPALSSConfigMachineGroupResultOutput {
	return o
}

func (o GetZPALSSConfigMachineGroupResultOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) string { return v.CreationTime }).(pulumi.StringOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) bool { return v.Enabled }).(pulumi.BoolOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) Machines() GetZPALSSConfigMachineGroupMachineArrayOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) []GetZPALSSConfigMachineGroupMachine { return v.Machines }).(GetZPALSSConfigMachineGroupMachineArrayOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) ModifiedTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) string { return v.ModifiedTime }).(pulumi.StringOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) Modifiedby() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) string { return v.Modifiedby }).(pulumi.StringOutput)
}

func (o GetZPALSSConfigMachineGroupResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPALSSConfigMachineGroupResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetZPALSSConfigMachineGroupResultOutput{})
}
