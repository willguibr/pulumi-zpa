// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPAServerGroup
    {
        public static Task<GetZPAServerGroupResult> InvokeAsync(GetZPAServerGroupArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPAServerGroupResult>("zpa:index/getZPAServerGroup:getZPAServerGroup", args ?? new GetZPAServerGroupArgs(), options.WithDefaults());

        public static Output<GetZPAServerGroupResult> Invoke(GetZPAServerGroupInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPAServerGroupResult>("zpa:index/getZPAServerGroup:getZPAServerGroup", args ?? new GetZPAServerGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPAServerGroupArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetZPAServerGroupArgs()
        {
        }
    }

    public sealed class GetZPAServerGroupInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetZPAServerGroupInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPAServerGroupResult
    {
        public readonly ImmutableArray<Outputs.GetZPAServerGroupAppConnectorGroupResult> AppConnectorGroups;
        public readonly ImmutableArray<Outputs.GetZPAServerGroupApplicationResult> Applications;
        public readonly string ConfigSpace;
        public readonly string CreationTime;
        public readonly string Description;
        public readonly bool DynamicDiscovery;
        public readonly bool Enabled;
        public readonly string? Id;
        public readonly bool IpAnchored;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.GetZPAServerGroupServerResult> Servers;

        [OutputConstructor]
        private GetZPAServerGroupResult(
            ImmutableArray<Outputs.GetZPAServerGroupAppConnectorGroupResult> appConnectorGroups,

            ImmutableArray<Outputs.GetZPAServerGroupApplicationResult> applications,

            string configSpace,

            string creationTime,

            string description,

            bool dynamicDiscovery,

            bool enabled,

            string? id,

            bool ipAnchored,

            string modifiedTime,

            string modifiedby,

            string? name,

            ImmutableArray<Outputs.GetZPAServerGroupServerResult> servers)
        {
            AppConnectorGroups = appConnectorGroups;
            Applications = applications;
            ConfigSpace = configSpace;
            CreationTime = creationTime;
            Description = description;
            DynamicDiscovery = dynamicDiscovery;
            Enabled = enabled;
            Id = id;
            IpAnchored = ipAnchored;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
            Servers = servers;
        }
    }
}
