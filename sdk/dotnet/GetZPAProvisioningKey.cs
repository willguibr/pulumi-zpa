// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPAProvisioningKey
    {
        public static Task<GetZPAProvisioningKeyResult> InvokeAsync(GetZPAProvisioningKeyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPAProvisioningKeyResult>("zpa:index/getZPAProvisioningKey:getZPAProvisioningKey", args ?? new GetZPAProvisioningKeyArgs(), options.WithDefaults());

        public static Output<GetZPAProvisioningKeyResult> Invoke(GetZPAProvisioningKeyInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPAProvisioningKeyResult>("zpa:index/getZPAProvisioningKey:getZPAProvisioningKey", args ?? new GetZPAProvisioningKeyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPAProvisioningKeyArgs : Pulumi.InvokeArgs
    {
        [Input("associationType", required: true)]
        public string AssociationType { get; set; } = null!;

        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetZPAProvisioningKeyArgs()
        {
        }
    }

    public sealed class GetZPAProvisioningKeyInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("associationType", required: true)]
        public Input<string> AssociationType { get; set; } = null!;

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetZPAProvisioningKeyInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPAProvisioningKeyResult
    {
        public readonly string AppConnectorGroupId;
        public readonly string AppConnectorGroupName;
        public readonly string AssociationType;
        public readonly string CreationTime;
        public readonly bool Enabled;
        public readonly string EnrollmentCertId;
        public readonly string EnrollmentCertName;
        public readonly string ExpirationInEpochSec;
        public readonly string? Id;
        public readonly ImmutableArray<string> IpAcls;
        public readonly string MaxUsage;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string? Name;
        public readonly string ProvisioningKey;
        public readonly string UiConfig;
        public readonly string UsageCount;
        public readonly string ZcomponentId;
        public readonly string ZcomponentName;

        [OutputConstructor]
        private GetZPAProvisioningKeyResult(
            string appConnectorGroupId,

            string appConnectorGroupName,

            string associationType,

            string creationTime,

            bool enabled,

            string enrollmentCertId,

            string enrollmentCertName,

            string expirationInEpochSec,

            string? id,

            ImmutableArray<string> ipAcls,

            string maxUsage,

            string modifiedTime,

            string modifiedby,

            string? name,

            string provisioningKey,

            string uiConfig,

            string usageCount,

            string zcomponentId,

            string zcomponentName)
        {
            AppConnectorGroupId = appConnectorGroupId;
            AppConnectorGroupName = appConnectorGroupName;
            AssociationType = associationType;
            CreationTime = creationTime;
            Enabled = enabled;
            EnrollmentCertId = enrollmentCertId;
            EnrollmentCertName = enrollmentCertName;
            ExpirationInEpochSec = expirationInEpochSec;
            Id = id;
            IpAcls = ipAcls;
            MaxUsage = maxUsage;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
            ProvisioningKey = provisioningKey;
            UiConfig = uiConfig;
            UsageCount = usageCount;
            ZcomponentId = zcomponentId;
            ZcomponentName = zcomponentName;
        }
    }
}
