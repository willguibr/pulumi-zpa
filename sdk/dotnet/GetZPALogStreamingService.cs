// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPALogStreamingService
    {
        public static Task<GetZPALogStreamingServiceResult> InvokeAsync(GetZPALogStreamingServiceArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPALogStreamingServiceResult>("zpa:index/getZPALogStreamingService:getZPALogStreamingService", args ?? new GetZPALogStreamingServiceArgs(), options.WithDefaults());

        public static Output<GetZPALogStreamingServiceResult> Invoke(GetZPALogStreamingServiceInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPALogStreamingServiceResult>("zpa:index/getZPALogStreamingService:getZPALogStreamingService", args ?? new GetZPALogStreamingServiceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPALogStreamingServiceArgs : Pulumi.InvokeArgs
    {
        [Input("configs")]
        private List<Inputs.GetZPALogStreamingServiceConfigArgs>? _configs;
        public List<Inputs.GetZPALogStreamingServiceConfigArgs> Configs
        {
            get => _configs ?? (_configs = new List<Inputs.GetZPALogStreamingServiceConfigArgs>());
            set => _configs = value;
        }

        [Input("id")]
        public string? Id { get; set; }

        public GetZPALogStreamingServiceArgs()
        {
        }
    }

    public sealed class GetZPALogStreamingServiceInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("configs")]
        private InputList<Inputs.GetZPALogStreamingServiceConfigInputArgs>? _configs;
        public InputList<Inputs.GetZPALogStreamingServiceConfigInputArgs> Configs
        {
            get => _configs ?? (_configs = new InputList<Inputs.GetZPALogStreamingServiceConfigInputArgs>());
            set => _configs = value;
        }

        [Input("id")]
        public Input<string>? Id { get; set; }

        public GetZPALogStreamingServiceInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPALogStreamingServiceResult
    {
        public readonly ImmutableArray<Outputs.GetZPALogStreamingServiceConfigResult> Configs;
        public readonly ImmutableArray<Outputs.GetZPALogStreamingServiceConnectorGroupResult> ConnectorGroups;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.GetZPALogStreamingServicePolicyRuleResult> PolicyRules;

        [OutputConstructor]
        private GetZPALogStreamingServiceResult(
            ImmutableArray<Outputs.GetZPALogStreamingServiceConfigResult> configs,

            ImmutableArray<Outputs.GetZPALogStreamingServiceConnectorGroupResult> connectorGroups,

            string? id,

            ImmutableArray<Outputs.GetZPALogStreamingServicePolicyRuleResult> policyRules)
        {
            Configs = configs;
            ConnectorGroups = connectorGroups;
            Id = id;
            PolicyRules = policyRules;
        }
    }
}
