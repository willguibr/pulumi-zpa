// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr.Inputs
{

    public sealed class ZPAPolicyAccessRuleConditionArgs : Pulumi.ResourceArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("negated")]
        public Input<bool>? Negated { get; set; }

        [Input("operands")]
        private InputList<Inputs.ZPAPolicyAccessRuleConditionOperandArgs>? _operands;
        public InputList<Inputs.ZPAPolicyAccessRuleConditionOperandArgs> Operands
        {
            get => _operands ?? (_operands = new InputList<Inputs.ZPAPolicyAccessRuleConditionOperandArgs>());
            set => _operands = value;
        }

        [Input("operator", required: true)]
        public Input<string> Operator { get; set; } = null!;

        public ZPAPolicyAccessRuleConditionArgs()
        {
        }
    }
}
