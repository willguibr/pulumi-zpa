// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPAAppConnectorGroup
    {
        public static Task<GetZPAAppConnectorGroupResult> InvokeAsync(GetZPAAppConnectorGroupArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPAAppConnectorGroupResult>("zpa:index/getZPAAppConnectorGroup:getZPAAppConnectorGroup", args ?? new GetZPAAppConnectorGroupArgs(), options.WithDefaults());

        public static Output<GetZPAAppConnectorGroupResult> Invoke(GetZPAAppConnectorGroupInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPAAppConnectorGroupResult>("zpa:index/getZPAAppConnectorGroup:getZPAAppConnectorGroup", args ?? new GetZPAAppConnectorGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPAAppConnectorGroupArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("overrideVersionProfile")]
        public bool? OverrideVersionProfile { get; set; }

        public GetZPAAppConnectorGroupArgs()
        {
        }
    }

    public sealed class GetZPAAppConnectorGroupInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("overrideVersionProfile")]
        public Input<bool>? OverrideVersionProfile { get; set; }

        public GetZPAAppConnectorGroupInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPAAppConnectorGroupResult
    {
        public readonly string CityCountry;
        public readonly ImmutableArray<Outputs.GetZPAAppConnectorGroupConnectorResult> Connectors;
        public readonly string CountryCode;
        public readonly string CreationTime;
        public readonly string Description;
        public readonly string DnsQueryType;
        public readonly bool Enabled;
        public readonly string GeoLocationId;
        public readonly string? Id;
        public readonly string Latitude;
        public readonly string Location;
        public readonly string Longitude;
        public readonly bool LssAppConnectorGroup;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string? Name;
        public readonly bool? OverrideVersionProfile;
        public readonly ImmutableArray<Outputs.GetZPAAppConnectorGroupServerGroupResult> ServerGroups;
        public readonly string UpgradeDay;
        public readonly string UpgradeTimeInSecs;
        public readonly string VersionProfileId;
        public readonly string VersionProfileName;
        public readonly string VersionProfileVisibilityScope;

        [OutputConstructor]
        private GetZPAAppConnectorGroupResult(
            string cityCountry,

            ImmutableArray<Outputs.GetZPAAppConnectorGroupConnectorResult> connectors,

            string countryCode,

            string creationTime,

            string description,

            string dnsQueryType,

            bool enabled,

            string geoLocationId,

            string? id,

            string latitude,

            string location,

            string longitude,

            bool lssAppConnectorGroup,

            string modifiedTime,

            string modifiedby,

            string? name,

            bool? overrideVersionProfile,

            ImmutableArray<Outputs.GetZPAAppConnectorGroupServerGroupResult> serverGroups,

            string upgradeDay,

            string upgradeTimeInSecs,

            string versionProfileId,

            string versionProfileName,

            string versionProfileVisibilityScope)
        {
            CityCountry = cityCountry;
            Connectors = connectors;
            CountryCode = countryCode;
            CreationTime = creationTime;
            Description = description;
            DnsQueryType = dnsQueryType;
            Enabled = enabled;
            GeoLocationId = geoLocationId;
            Id = id;
            Latitude = latitude;
            Location = location;
            Longitude = longitude;
            LssAppConnectorGroup = lssAppConnectorGroup;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
            OverrideVersionProfile = overrideVersionProfile;
            ServerGroups = serverGroups;
            UpgradeDay = upgradeDay;
            UpgradeTimeInSecs = upgradeTimeInSecs;
            VersionProfileId = versionProfileId;
            VersionProfileName = versionProfileName;
            VersionProfileVisibilityScope = versionProfileVisibilityScope;
        }
    }
}
