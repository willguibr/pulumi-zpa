// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetZPATrustedNetwork(ctx *pulumi.Context, args *GetZPATrustedNetworkArgs, opts ...pulumi.InvokeOption) (*GetZPATrustedNetworkResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetZPATrustedNetworkResult
	err := ctx.Invoke("zpa:index/getZPATrustedNetwork:getZPATrustedNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZPATrustedNetwork.
type GetZPATrustedNetworkArgs struct {
	Id   *string `pulumi:"id"`
	Name *string `pulumi:"name"`
}

// A collection of values returned by getZPATrustedNetwork.
type GetZPATrustedNetworkResult struct {
	CreationTime string  `pulumi:"creationTime"`
	Domain       string  `pulumi:"domain"`
	Id           *string `pulumi:"id"`
	ModifiedTime string  `pulumi:"modifiedTime"`
	Modifiedby   string  `pulumi:"modifiedby"`
	Name         *string `pulumi:"name"`
	NetworkId    string  `pulumi:"networkId"`
	ZscalerCloud string  `pulumi:"zscalerCloud"`
}

func GetZPATrustedNetworkOutput(ctx *pulumi.Context, args GetZPATrustedNetworkOutputArgs, opts ...pulumi.InvokeOption) GetZPATrustedNetworkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetZPATrustedNetworkResult, error) {
			args := v.(GetZPATrustedNetworkArgs)
			r, err := GetZPATrustedNetwork(ctx, &args, opts...)
			var s GetZPATrustedNetworkResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetZPATrustedNetworkResultOutput)
}

// A collection of arguments for invoking getZPATrustedNetwork.
type GetZPATrustedNetworkOutputArgs struct {
	Id   pulumi.StringPtrInput `pulumi:"id"`
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetZPATrustedNetworkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPATrustedNetworkArgs)(nil)).Elem()
}

// A collection of values returned by getZPATrustedNetwork.
type GetZPATrustedNetworkResultOutput struct{ *pulumi.OutputState }

func (GetZPATrustedNetworkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPATrustedNetworkResult)(nil)).Elem()
}

func (o GetZPATrustedNetworkResultOutput) ToGetZPATrustedNetworkResultOutput() GetZPATrustedNetworkResultOutput {
	return o
}

func (o GetZPATrustedNetworkResultOutput) ToGetZPATrustedNetworkResultOutputWithContext(ctx context.Context) GetZPATrustedNetworkResultOutput {
	return o
}

func (o GetZPATrustedNetworkResultOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) string { return v.CreationTime }).(pulumi.StringOutput)
}

func (o GetZPATrustedNetworkResultOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) string { return v.Domain }).(pulumi.StringOutput)
}

func (o GetZPATrustedNetworkResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GetZPATrustedNetworkResultOutput) ModifiedTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) string { return v.ModifiedTime }).(pulumi.StringOutput)
}

func (o GetZPATrustedNetworkResultOutput) Modifiedby() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) string { return v.Modifiedby }).(pulumi.StringOutput)
}

func (o GetZPATrustedNetworkResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetZPATrustedNetworkResultOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) string { return v.NetworkId }).(pulumi.StringOutput)
}

func (o GetZPATrustedNetworkResultOutput) ZscalerCloud() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPATrustedNetworkResult) string { return v.ZscalerCloud }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetZPATrustedNetworkResultOutput{})
}
