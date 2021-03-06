// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPASAMLAttribute
    {
        public static Task<GetZPASAMLAttributeResult> InvokeAsync(GetZPASAMLAttributeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPASAMLAttributeResult>("zpa:index/getZPASAMLAttribute:getZPASAMLAttribute", args ?? new GetZPASAMLAttributeArgs(), options.WithDefaults());

        public static Output<GetZPASAMLAttributeResult> Invoke(GetZPASAMLAttributeInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPASAMLAttributeResult>("zpa:index/getZPASAMLAttribute:getZPASAMLAttribute", args ?? new GetZPASAMLAttributeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPASAMLAttributeArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public string? Id { get; set; }

        [Input("idpName")]
        public string? IdpName { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetZPASAMLAttributeArgs()
        {
        }
    }

    public sealed class GetZPASAMLAttributeInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("idpName")]
        public Input<string>? IdpName { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetZPASAMLAttributeInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPASAMLAttributeResult
    {
        public readonly string CreationTime;
        public readonly string Id;
        public readonly string IdpId;
        public readonly string? IdpName;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string Name;
        public readonly string SamlName;
        public readonly bool UserAttribute;

        [OutputConstructor]
        private GetZPASAMLAttributeResult(
            string creationTime,

            string id,

            string idpId,

            string? idpName,

            string modifiedTime,

            string modifiedby,

            string name,

            string samlName,

            bool userAttribute)
        {
            CreationTime = creationTime;
            Id = id;
            IdpId = idpId;
            IdpName = idpName;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
            SamlName = samlName;
            UserAttribute = userAttribute;
        }
    }
}
