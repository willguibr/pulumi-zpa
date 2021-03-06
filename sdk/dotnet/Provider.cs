// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    /// <summary>
    /// The provider type for the zpa package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [willguibrResourceType("pulumi:providers:zpa")]
    public partial class Provider : Pulumi.ProviderResource
    {
        /// <summary>
        /// zpa client id
        /// </summary>
        [Output("zpaClientId")]
        public Output<string> ZpaClientId { get; private set; } = null!;

        /// <summary>
        /// zpa client secret
        /// </summary>
        [Output("zpaClientSecret")]
        public Output<string> ZpaClientSecret { get; private set; } = null!;

        /// <summary>
        /// zpa customer id
        /// </summary>
        [Output("zpaCustomerId")]
        public Output<string> ZpaCustomerId { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, CustomResourceOptions? options = null)
            : base("zpa", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
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
    }

    public sealed class ProviderArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// zpa client id
        /// </summary>
        [Input("zpaClientId", required: true)]
        public Input<string> ZpaClientId { get; set; } = null!;

        /// <summary>
        /// zpa client secret
        /// </summary>
        [Input("zpaClientSecret", required: true)]
        public Input<string> ZpaClientSecret { get; set; } = null!;

        /// <summary>
        /// zpa customer id
        /// </summary>
        [Input("zpaCustomerId", required: true)]
        public Input<string> ZpaCustomerId { get; set; } = null!;

        public ProviderArgs()
        {
        }
    }
}
