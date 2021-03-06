// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    [willguibrResourceType("zpa:index/zPAApplicationSegment:ZPAApplicationSegment")]
    public partial class ZPAApplicationSegment : Pulumi.CustomResource
    {
        /// <summary>
        /// Indicates whether users can bypass ZPA to access applications.
        /// </summary>
        [Output("bypassType")]
        public Output<string> BypassType { get; private set; } = null!;

        [Output("configSpace")]
        public Output<string?> ConfigSpace { get; private set; } = null!;

        [Output("defaultIdleTimeout")]
        public Output<string> DefaultIdleTimeout { get; private set; } = null!;

        /// <summary>
        /// Description of the application.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// List of domains and IPs.
        /// </summary>
        [Output("domainNames")]
        public Output<ImmutableArray<string>> DomainNames { get; private set; } = null!;

        /// <summary>
        /// Whether Double Encryption is enabled or disabled for the app.
        /// </summary>
        [Output("doubleEncrypt")]
        public Output<bool?> DoubleEncrypt { get; private set; } = null!;

        /// <summary>
        /// Whether this application is enabled or not.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        [Output("healthCheckType")]
        public Output<string?> HealthCheckType { get; private set; } = null!;

        /// <summary>
        /// Whether health reporting for the app is Continuous or On Access. Supported values: NONE, ON_ACCESS, CONTINUOUS.
        /// </summary>
        [Output("healthReporting")]
        public Output<string?> HealthReporting { get; private set; } = null!;

        [Output("icmpAccessType")]
        public Output<string?> IcmpAccessType { get; private set; } = null!;

        [Output("ipAnchored")]
        public Output<bool?> IpAnchored { get; private set; } = null!;

        /// <summary>
        /// Indicates if the Zscaler Client Connector (formerly Zscaler App or Z App) receives CNAME DNS records from the
        /// connectors.
        /// </summary>
        [Output("isCnameEnabled")]
        public Output<bool> IsCnameEnabled { get; private set; } = null!;

        /// <summary>
        /// Name of the application.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("passiveHealthEnabled")]
        public Output<bool> PassiveHealthEnabled { get; private set; } = null!;

        [Output("segmentGroupId")]
        public Output<string> SegmentGroupId { get; private set; } = null!;

        [Output("segmentGroupName")]
        public Output<string> SegmentGroupName { get; private set; } = null!;

        /// <summary>
        /// List of the server group IDs.
        /// </summary>
        [Output("serverGroups")]
        public Output<ImmutableArray<Outputs.ZPAApplicationSegmentServerGroup>> ServerGroups { get; private set; } = null!;

        /// <summary>
        /// TCP port ranges used to access the app.
        /// </summary>
        [Output("tcpPortRanges")]
        public Output<ImmutableArray<string>> TcpPortRanges { get; private set; } = null!;

        /// <summary>
        /// UDP port ranges used to access the app.
        /// </summary>
        [Output("udpPortRanges")]
        public Output<ImmutableArray<string>> UdpPortRanges { get; private set; } = null!;


        /// <summary>
        /// Create a ZPAApplicationSegment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ZPAApplicationSegment(string name, ZPAApplicationSegmentArgs args, CustomResourceOptions? options = null)
            : base("zpa:index/zPAApplicationSegment:ZPAApplicationSegment", name, args ?? new ZPAApplicationSegmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ZPAApplicationSegment(string name, Input<string> id, ZPAApplicationSegmentState? state = null, CustomResourceOptions? options = null)
            : base("zpa:index/zPAApplicationSegment:ZPAApplicationSegment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/willguibr/pulumi-zpa/releases/download/v${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ZPAApplicationSegment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ZPAApplicationSegment Get(string name, Input<string> id, ZPAApplicationSegmentState? state = null, CustomResourceOptions? options = null)
        {
            return new ZPAApplicationSegment(name, id, state, options);
        }
    }

    public sealed class ZPAApplicationSegmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether users can bypass ZPA to access applications.
        /// </summary>
        [Input("bypassType")]
        public Input<string>? BypassType { get; set; }

        [Input("configSpace")]
        public Input<string>? ConfigSpace { get; set; }

        [Input("defaultIdleTimeout")]
        public Input<string>? DefaultIdleTimeout { get; set; }

        /// <summary>
        /// Description of the application.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("domainNames", required: true)]
        private InputList<string>? _domainNames;

        /// <summary>
        /// List of domains and IPs.
        /// </summary>
        public InputList<string> DomainNames
        {
            get => _domainNames ?? (_domainNames = new InputList<string>());
            set => _domainNames = value;
        }

        /// <summary>
        /// Whether Double Encryption is enabled or disabled for the app.
        /// </summary>
        [Input("doubleEncrypt")]
        public Input<bool>? DoubleEncrypt { get; set; }

        /// <summary>
        /// Whether this application is enabled or not.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("healthCheckType")]
        public Input<string>? HealthCheckType { get; set; }

        /// <summary>
        /// Whether health reporting for the app is Continuous or On Access. Supported values: NONE, ON_ACCESS, CONTINUOUS.
        /// </summary>
        [Input("healthReporting")]
        public Input<string>? HealthReporting { get; set; }

        [Input("icmpAccessType")]
        public Input<string>? IcmpAccessType { get; set; }

        [Input("ipAnchored")]
        public Input<bool>? IpAnchored { get; set; }

        /// <summary>
        /// Indicates if the Zscaler Client Connector (formerly Zscaler App or Z App) receives CNAME DNS records from the
        /// connectors.
        /// </summary>
        [Input("isCnameEnabled")]
        public Input<bool>? IsCnameEnabled { get; set; }

        /// <summary>
        /// Name of the application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("passiveHealthEnabled")]
        public Input<bool>? PassiveHealthEnabled { get; set; }

        [Input("segmentGroupId")]
        public Input<string>? SegmentGroupId { get; set; }

        [Input("serverGroups", required: true)]
        private InputList<Inputs.ZPAApplicationSegmentServerGroupArgs>? _serverGroups;

        /// <summary>
        /// List of the server group IDs.
        /// </summary>
        public InputList<Inputs.ZPAApplicationSegmentServerGroupArgs> ServerGroups
        {
            get => _serverGroups ?? (_serverGroups = new InputList<Inputs.ZPAApplicationSegmentServerGroupArgs>());
            set => _serverGroups = value;
        }

        [Input("tcpPortRanges")]
        private InputList<string>? _tcpPortRanges;

        /// <summary>
        /// TCP port ranges used to access the app.
        /// </summary>
        public InputList<string> TcpPortRanges
        {
            get => _tcpPortRanges ?? (_tcpPortRanges = new InputList<string>());
            set => _tcpPortRanges = value;
        }

        [Input("udpPortRanges")]
        private InputList<string>? _udpPortRanges;

        /// <summary>
        /// UDP port ranges used to access the app.
        /// </summary>
        public InputList<string> UdpPortRanges
        {
            get => _udpPortRanges ?? (_udpPortRanges = new InputList<string>());
            set => _udpPortRanges = value;
        }

        public ZPAApplicationSegmentArgs()
        {
        }
    }

    public sealed class ZPAApplicationSegmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether users can bypass ZPA to access applications.
        /// </summary>
        [Input("bypassType")]
        public Input<string>? BypassType { get; set; }

        [Input("configSpace")]
        public Input<string>? ConfigSpace { get; set; }

        [Input("defaultIdleTimeout")]
        public Input<string>? DefaultIdleTimeout { get; set; }

        /// <summary>
        /// Description of the application.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("domainNames")]
        private InputList<string>? _domainNames;

        /// <summary>
        /// List of domains and IPs.
        /// </summary>
        public InputList<string> DomainNames
        {
            get => _domainNames ?? (_domainNames = new InputList<string>());
            set => _domainNames = value;
        }

        /// <summary>
        /// Whether Double Encryption is enabled or disabled for the app.
        /// </summary>
        [Input("doubleEncrypt")]
        public Input<bool>? DoubleEncrypt { get; set; }

        /// <summary>
        /// Whether this application is enabled or not.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("healthCheckType")]
        public Input<string>? HealthCheckType { get; set; }

        /// <summary>
        /// Whether health reporting for the app is Continuous or On Access. Supported values: NONE, ON_ACCESS, CONTINUOUS.
        /// </summary>
        [Input("healthReporting")]
        public Input<string>? HealthReporting { get; set; }

        [Input("icmpAccessType")]
        public Input<string>? IcmpAccessType { get; set; }

        [Input("ipAnchored")]
        public Input<bool>? IpAnchored { get; set; }

        /// <summary>
        /// Indicates if the Zscaler Client Connector (formerly Zscaler App or Z App) receives CNAME DNS records from the
        /// connectors.
        /// </summary>
        [Input("isCnameEnabled")]
        public Input<bool>? IsCnameEnabled { get; set; }

        /// <summary>
        /// Name of the application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("passiveHealthEnabled")]
        public Input<bool>? PassiveHealthEnabled { get; set; }

        [Input("segmentGroupId")]
        public Input<string>? SegmentGroupId { get; set; }

        [Input("segmentGroupName")]
        public Input<string>? SegmentGroupName { get; set; }

        [Input("serverGroups")]
        private InputList<Inputs.ZPAApplicationSegmentServerGroupGetArgs>? _serverGroups;

        /// <summary>
        /// List of the server group IDs.
        /// </summary>
        public InputList<Inputs.ZPAApplicationSegmentServerGroupGetArgs> ServerGroups
        {
            get => _serverGroups ?? (_serverGroups = new InputList<Inputs.ZPAApplicationSegmentServerGroupGetArgs>());
            set => _serverGroups = value;
        }

        [Input("tcpPortRanges")]
        private InputList<string>? _tcpPortRanges;

        /// <summary>
        /// TCP port ranges used to access the app.
        /// </summary>
        public InputList<string> TcpPortRanges
        {
            get => _tcpPortRanges ?? (_tcpPortRanges = new InputList<string>());
            set => _tcpPortRanges = value;
        }

        [Input("udpPortRanges")]
        private InputList<string>? _udpPortRanges;

        /// <summary>
        /// UDP port ranges used to access the app.
        /// </summary>
        public InputList<string> UdpPortRanges
        {
            get => _udpPortRanges ?? (_udpPortRanges = new InputList<string>());
            set => _udpPortRanges = value;
        }

        public ZPAApplicationSegmentState()
        {
        }
    }
}
