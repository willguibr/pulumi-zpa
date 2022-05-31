// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetZPAEnrollmentCert(ctx *pulumi.Context, args *GetZPAEnrollmentCertArgs, opts ...pulumi.InvokeOption) (*GetZPAEnrollmentCertResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetZPAEnrollmentCertResult
	err := ctx.Invoke("zpa:index/getZPAEnrollmentCert:getZPAEnrollmentCert", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZPAEnrollmentCert.
type GetZPAEnrollmentCertArgs struct {
	Id   *string `pulumi:"id"`
	Name *string `pulumi:"name"`
}

// A collection of values returned by getZPAEnrollmentCert.
type GetZPAEnrollmentCertResult struct {
	AllowSigning            bool    `pulumi:"allowSigning"`
	Certificate             string  `pulumi:"certificate"`
	ClientCertType          string  `pulumi:"clientCertType"`
	Cname                   string  `pulumi:"cname"`
	CreationTime            string  `pulumi:"creationTime"`
	Csr                     string  `pulumi:"csr"`
	Description             string  `pulumi:"description"`
	Id                      *string `pulumi:"id"`
	IssuedBy                string  `pulumi:"issuedBy"`
	IssuedTo                string  `pulumi:"issuedTo"`
	ModifiedTime            string  `pulumi:"modifiedTime"`
	Modifiedby              string  `pulumi:"modifiedby"`
	Name                    *string `pulumi:"name"`
	ParentCertId            string  `pulumi:"parentCertId"`
	ParentCertName          string  `pulumi:"parentCertName"`
	PrivateKey              string  `pulumi:"privateKey"`
	PrivateKeyPresent       bool    `pulumi:"privateKeyPresent"`
	SerialNo                string  `pulumi:"serialNo"`
	ValidFromInEpochSec     string  `pulumi:"validFromInEpochSec"`
	ValidToInEpochSec       string  `pulumi:"validToInEpochSec"`
	ZrsaEncryptedPrivateKey string  `pulumi:"zrsaEncryptedPrivateKey"`
	ZrsaEncryptedSessionKey string  `pulumi:"zrsaEncryptedSessionKey"`
}

func GetZPAEnrollmentCertOutput(ctx *pulumi.Context, args GetZPAEnrollmentCertOutputArgs, opts ...pulumi.InvokeOption) GetZPAEnrollmentCertResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetZPAEnrollmentCertResult, error) {
			args := v.(GetZPAEnrollmentCertArgs)
			r, err := GetZPAEnrollmentCert(ctx, &args, opts...)
			var s GetZPAEnrollmentCertResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetZPAEnrollmentCertResultOutput)
}

// A collection of arguments for invoking getZPAEnrollmentCert.
type GetZPAEnrollmentCertOutputArgs struct {
	Id   pulumi.StringPtrInput `pulumi:"id"`
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetZPAEnrollmentCertOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPAEnrollmentCertArgs)(nil)).Elem()
}

// A collection of values returned by getZPAEnrollmentCert.
type GetZPAEnrollmentCertResultOutput struct{ *pulumi.OutputState }

func (GetZPAEnrollmentCertResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetZPAEnrollmentCertResult)(nil)).Elem()
}

func (o GetZPAEnrollmentCertResultOutput) ToGetZPAEnrollmentCertResultOutput() GetZPAEnrollmentCertResultOutput {
	return o
}

func (o GetZPAEnrollmentCertResultOutput) ToGetZPAEnrollmentCertResultOutputWithContext(ctx context.Context) GetZPAEnrollmentCertResultOutput {
	return o
}

func (o GetZPAEnrollmentCertResultOutput) AllowSigning() pulumi.BoolOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) bool { return v.AllowSigning }).(pulumi.BoolOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Certificate() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.Certificate }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ClientCertType() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ClientCertType }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Cname() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.Cname }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.CreationTime }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Csr() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.Csr }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GetZPAEnrollmentCertResultOutput) IssuedBy() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.IssuedBy }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) IssuedTo() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.IssuedTo }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ModifiedTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ModifiedTime }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Modifiedby() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.Modifiedby }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ParentCertId() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ParentCertId }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ParentCertName() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ParentCertName }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) PrivateKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.PrivateKey }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) PrivateKeyPresent() pulumi.BoolOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) bool { return v.PrivateKeyPresent }).(pulumi.BoolOutput)
}

func (o GetZPAEnrollmentCertResultOutput) SerialNo() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.SerialNo }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ValidFromInEpochSec() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ValidFromInEpochSec }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ValidToInEpochSec() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ValidToInEpochSec }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ZrsaEncryptedPrivateKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ZrsaEncryptedPrivateKey }).(pulumi.StringOutput)
}

func (o GetZPAEnrollmentCertResultOutput) ZrsaEncryptedSessionKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetZPAEnrollmentCertResult) string { return v.ZrsaEncryptedSessionKey }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetZPAEnrollmentCertResultOutput{})
}
