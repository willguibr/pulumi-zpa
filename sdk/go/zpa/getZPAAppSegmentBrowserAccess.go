// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package zpa

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupZPAAppSegmentBrowserAccess(ctx *pulumi.Context, args *LookupZPAAppSegmentBrowserAccessArgs, opts ...pulumi.InvokeOption) (*LookupZPAAppSegmentBrowserAccessResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupZPAAppSegmentBrowserAccessResult
	err := ctx.Invoke("zpa:index/getZPAAppSegmentBrowserAccess:getZPAAppSegmentBrowserAccess", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getZPAAppSegmentBrowserAccess.
type LookupZPAAppSegmentBrowserAccessArgs struct {
	Id            *string                                     `pulumi:"id"`
	Name          *string                                     `pulumi:"name"`
	TcpPortRanges []GetZPAAppSegmentBrowserAccessTcpPortRange `pulumi:"tcpPortRanges"`
	UdpPortRanges []GetZPAAppSegmentBrowserAccessUdpPortRange `pulumi:"udpPortRanges"`
}

// A collection of values returned by getZPAAppSegmentBrowserAccess.
type LookupZPAAppSegmentBrowserAccessResult struct {
	BypassType           string                                       `pulumi:"bypassType"`
	ClientlessApps       []GetZPAAppSegmentBrowserAccessClientlessApp `pulumi:"clientlessApps"`
	ConfigSpace          string                                       `pulumi:"configSpace"`
	Description          string                                       `pulumi:"description"`
	DomainNames          []string                                     `pulumi:"domainNames"`
	DoubleEncrypt        bool                                         `pulumi:"doubleEncrypt"`
	Enabled              bool                                         `pulumi:"enabled"`
	HealthCheckType      string                                       `pulumi:"healthCheckType"`
	HealthReporting      string                                       `pulumi:"healthReporting"`
	Id                   *string                                      `pulumi:"id"`
	IpAnchored           bool                                         `pulumi:"ipAnchored"`
	IsCnameEnabled       bool                                         `pulumi:"isCnameEnabled"`
	Name                 *string                                      `pulumi:"name"`
	PassiveHealthEnabled bool                                         `pulumi:"passiveHealthEnabled"`
	SegmentGroupId       string                                       `pulumi:"segmentGroupId"`
	SegmentGroupName     string                                       `pulumi:"segmentGroupName"`
	ServerGroups         []GetZPAAppSegmentBrowserAccessServerGroup   `pulumi:"serverGroups"`
	TcpPortRanges        []string                                     `pulumi:"tcpPortRanges"`
	UdpPortRanges        []string                                     `pulumi:"udpPortRanges"`
}

func LookupZPAAppSegmentBrowserAccessOutput(ctx *pulumi.Context, args LookupZPAAppSegmentBrowserAccessOutputArgs, opts ...pulumi.InvokeOption) LookupZPAAppSegmentBrowserAccessResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupZPAAppSegmentBrowserAccessResult, error) {
			args := v.(LookupZPAAppSegmentBrowserAccessArgs)
			r, err := LookupZPAAppSegmentBrowserAccess(ctx, &args, opts...)
			var s LookupZPAAppSegmentBrowserAccessResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupZPAAppSegmentBrowserAccessResultOutput)
}

// A collection of arguments for invoking getZPAAppSegmentBrowserAccess.
type LookupZPAAppSegmentBrowserAccessOutputArgs struct {
	Id            pulumi.StringPtrInput                               `pulumi:"id"`
	Name          pulumi.StringPtrInput                               `pulumi:"name"`
	TcpPortRanges GetZPAAppSegmentBrowserAccessTcpPortRangeArrayInput `pulumi:"tcpPortRanges"`
	UdpPortRanges GetZPAAppSegmentBrowserAccessUdpPortRangeArrayInput `pulumi:"udpPortRanges"`
}

func (LookupZPAAppSegmentBrowserAccessOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupZPAAppSegmentBrowserAccessArgs)(nil)).Elem()
}

// A collection of values returned by getZPAAppSegmentBrowserAccess.
type LookupZPAAppSegmentBrowserAccessResultOutput struct{ *pulumi.OutputState }

func (LookupZPAAppSegmentBrowserAccessResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupZPAAppSegmentBrowserAccessResult)(nil)).Elem()
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) ToLookupZPAAppSegmentBrowserAccessResultOutput() LookupZPAAppSegmentBrowserAccessResultOutput {
	return o
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) ToLookupZPAAppSegmentBrowserAccessResultOutputWithContext(ctx context.Context) LookupZPAAppSegmentBrowserAccessResultOutput {
	return o
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) BypassType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.BypassType }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) ClientlessApps() GetZPAAppSegmentBrowserAccessClientlessAppArrayOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) []GetZPAAppSegmentBrowserAccessClientlessApp {
		return v.ClientlessApps
	}).(GetZPAAppSegmentBrowserAccessClientlessAppArrayOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) ConfigSpace() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.ConfigSpace }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) DomainNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) []string { return v.DomainNames }).(pulumi.StringArrayOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) DoubleEncrypt() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) bool { return v.DoubleEncrypt }).(pulumi.BoolOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) bool { return v.Enabled }).(pulumi.BoolOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) HealthCheckType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.HealthCheckType }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) HealthReporting() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.HealthReporting }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) IpAnchored() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) bool { return v.IpAnchored }).(pulumi.BoolOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) IsCnameEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) bool { return v.IsCnameEnabled }).(pulumi.BoolOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) PassiveHealthEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) bool { return v.PassiveHealthEnabled }).(pulumi.BoolOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) SegmentGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.SegmentGroupId }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) SegmentGroupName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) string { return v.SegmentGroupName }).(pulumi.StringOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) ServerGroups() GetZPAAppSegmentBrowserAccessServerGroupArrayOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) []GetZPAAppSegmentBrowserAccessServerGroup {
		return v.ServerGroups
	}).(GetZPAAppSegmentBrowserAccessServerGroupArrayOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) TcpPortRanges() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) []string { return v.TcpPortRanges }).(pulumi.StringArrayOutput)
}

func (o LookupZPAAppSegmentBrowserAccessResultOutput) UdpPortRanges() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupZPAAppSegmentBrowserAccessResult) []string { return v.UdpPortRanges }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupZPAAppSegmentBrowserAccessResultOutput{})
}