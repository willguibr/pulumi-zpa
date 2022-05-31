// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetZPASCIMGroups(ctx *pulumi.Context, args *GetZPASCIMGroupsArgs, opts ...pulumi.InvokeOption) (*GetZPASCIMGroupsResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetZPASCIMGroupsResult
	err := ctx.Invoke("zpa:index/getZPASCIMGroups:getZPASCIMGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZPASCIMGroups.
type GetZPASCIMGroupsArgs struct {
	Id      *string `pulumi:"id"`
	IdpId   *int    `pulumi:"idpId"`
	IdpName *string `pulumi:"idpName"`
	Name    *string `pulumi:"name"`
}

// A collection of values returned by getZPASCIMGroups.
type GetZPASCIMGroupsResult struct {
	CreationTime int     `pulumi:"creationTime"`
	Id           *string `pulumi:"id"`
	IdpGroupId   string  `pulumi:"idpGroupId"`
	IdpId        *int    `pulumi:"idpId"`
	IdpName      *string `pulumi:"idpName"`
	ModifiedTime int     `pulumi:"modifiedTime"`
	Name         *string `pulumi:"name"`
}

func GetZPASCIMGroupsOutput(ctx *pulumi.Context, args GetZPASCIMGroupsOutputArgs, opts ...pulumi.InvokeOption) GetZPASCIMGroupsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetZPASCIMGroupsResult, error) {
			args := v.(GetZPASCIMGroupsArgs)
			r, err := GetZPASCIMGroups(ctx, &args, opts...)
			var s GetZPASCIMGroupsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetZPASCIMGroupsResultOutput)
}

// A collection of arguments for invoking getZPASCIMGroups.
type GetZPASCIMGroupsOutputArgs struct {
	Id      pulumi.StringPtrInput `pulumi:"id"`
	IdpId   pulumi.IntPtrInput    `pulumi:"idpId"`
	IdpName pulumi.StringPtrInput `pulumi:"idpName"`
	Name    pulumi.StringPtrInput `pulumi:"name"`
}

func (GetZPASCIMGroupsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPASCIMGroupsArgs)(nil)).Elem()
}

// A collection of values returned by getZPASCIMGroups.
type GetZPASCIMGroupsResultOutput struct{ *pulumi.OutputState }

func (GetZPASCIMGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPASCIMGroupsResult)(nil)).Elem()
}

func (o GetZPASCIMGroupsResultOutput) ToGetZPASCIMGroupsResultOutput() GetZPASCIMGroupsResultOutput {
	return o
}

func (o GetZPASCIMGroupsResultOutput) ToGetZPASCIMGroupsResultOutputWithContext(ctx context.Context) GetZPASCIMGroupsResultOutput {
	return o
}

func (o GetZPASCIMGroupsResultOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) int { return v.CreationTime }).(pulumi.IntOutput)
}

func (o GetZPASCIMGroupsResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GetZPASCIMGroupsResultOutput) IdpGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) string { return v.IdpGroupId }).(pulumi.StringOutput)
}

func (o GetZPASCIMGroupsResultOutput) IdpId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) *int { return v.IdpId }).(pulumi.IntPtrOutput)
}

func (o GetZPASCIMGroupsResultOutput) IdpName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) *string { return v.IdpName }).(pulumi.StringPtrOutput)
}

func (o GetZPASCIMGroupsResultOutput) ModifiedTime() pulumi.IntOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) int { return v.ModifiedTime }).(pulumi.IntOutput)
}

func (o GetZPASCIMGroupsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPASCIMGroupsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetZPASCIMGroupsResultOutput{})
}
