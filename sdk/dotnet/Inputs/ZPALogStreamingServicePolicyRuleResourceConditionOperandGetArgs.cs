// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr.Inputs
{

    public sealed class ZPALogStreamingServicePolicyRuleResourceConditionOperandGetArgs : Pulumi.ResourceArgs
    {
        [Input("objectType", required: true)]
        public Input<string> ObjectType { get; set; } = null!;

        [Input("values")]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public ZPALogStreamingServicePolicyRuleResourceConditionOperandGetArgs()
        {
        }
    }
}
