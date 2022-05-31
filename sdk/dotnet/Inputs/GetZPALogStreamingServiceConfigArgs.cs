// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr.Inputs
{

    public sealed class GetZPALogStreamingServiceConfigInputArgs : Pulumi.ResourceArgs
    {
        [Input("auditMessage", required: true)]
        public Input<string> AuditMessage { get; set; } = null!;

        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        [Input("filters", required: true)]
        private InputList<string>? _filters;
        public InputList<string> Filters
        {
            get => _filters ?? (_filters = new InputList<string>());
            set => _filters = value;
        }

        [Input("format", required: true)]
        public Input<string> Format { get; set; } = null!;

        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("lssHost", required: true)]
        public Input<string> LssHost { get; set; } = null!;

        [Input("lssPort", required: true)]
        public Input<string> LssPort { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("sourceLogType", required: true)]
        public Input<string> SourceLogType { get; set; } = null!;

        [Input("useTls", required: true)]
        public Input<bool> UseTls { get; set; } = null!;

        public GetZPALogStreamingServiceConfigInputArgs()
        {
        }
    }
}
