// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPASCIMAttributeHeader
    {
        public static Task<GetZPASCIMAttributeHeaderResult> InvokeAsync(GetZPASCIMAttributeHeaderArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPASCIMAttributeHeaderResult>("zpa:index/getZPASCIMAttributeHeader:getZPASCIMAttributeHeader", args ?? new GetZPASCIMAttributeHeaderArgs(), options.WithDefaults());

        public static Output<GetZPASCIMAttributeHeaderResult> Invoke(GetZPASCIMAttributeHeaderInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPASCIMAttributeHeaderResult>("zpa:index/getZPASCIMAttributeHeader:getZPASCIMAttributeHeader", args ?? new GetZPASCIMAttributeHeaderInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPASCIMAttributeHeaderArgs : Pulumi.InvokeArgs
    {
        [Input("idpName")]
        public string? IdpName { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetZPASCIMAttributeHeaderArgs()
        {
        }
    }

    public sealed class GetZPASCIMAttributeHeaderInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("idpName")]
        public Input<string>? IdpName { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetZPASCIMAttributeHeaderInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPASCIMAttributeHeaderResult
    {
        public readonly ImmutableArray<string> CanonicalValues;
        public readonly bool CaseSensitive;
        public readonly string CreationTime;
        public readonly string DataType;
        public readonly string Description;
        public readonly string Id;
        public readonly string IdpId;
        public readonly string? IdpName;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly bool Multivalued;
        public readonly string Mutability;
        public readonly string? Name;
        public readonly bool Required;
        public readonly string Returned;
        public readonly string SchemaUri;
        public readonly bool Uniqueness;

        [OutputConstructor]
        private GetZPASCIMAttributeHeaderResult(
            ImmutableArray<string> canonicalValues,

            bool caseSensitive,

            string creationTime,

            string dataType,

            string description,

            string id,

            string idpId,

            string? idpName,

            string modifiedTime,

            string modifiedby,

            bool multivalued,

            string mutability,

            string? name,

            bool required,

            string returned,

            string schemaUri,

            bool uniqueness)
        {
            CanonicalValues = canonicalValues;
            CaseSensitive = caseSensitive;
            CreationTime = creationTime;
            DataType = dataType;
            Description = description;
            Id = id;
            IdpId = idpId;
            IdpName = idpName;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Multivalued = multivalued;
            Mutability = mutability;
            Name = name;
            Required = required;
            Returned = returned;
            SchemaUri = schemaUri;
            Uniqueness = uniqueness;
        }
    }
}
