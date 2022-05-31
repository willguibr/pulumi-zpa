// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPATrustedNetwork
    {
        public static Task<GetZPATrustedNetworkResult> InvokeAsync(GetZPATrustedNetworkArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPATrustedNetworkResult>("zpa:index/getZPATrustedNetwork:getZPATrustedNetwork", args ?? new GetZPATrustedNetworkArgs(), options.WithDefaults());

        public static Output<GetZPATrustedNetworkResult> Invoke(GetZPATrustedNetworkInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPATrustedNetworkResult>("zpa:index/getZPATrustedNetwork:getZPATrustedNetwork", args ?? new GetZPATrustedNetworkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPATrustedNetworkArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetZPATrustedNetworkArgs()
        {
        }
    }

    public sealed class GetZPATrustedNetworkInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetZPATrustedNetworkInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPATrustedNetworkResult
    {
        public readonly string CreationTime;
        public readonly string Domain;
        public readonly string? Id;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string? Name;
        public readonly string NetworkId;
        public readonly string ZscalerCloud;

        [OutputConstructor]
        private GetZPATrustedNetworkResult(
            string creationTime,

            string domain,

            string? id,

            string modifiedTime,

            string modifiedby,

            string? name,

            string networkId,

            string zscalerCloud)
        {
            CreationTime = creationTime;
            Domain = domain;
            Id = id;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
            NetworkId = networkId;
            ZscalerCloud = zscalerCloud;
        }
    }
}
