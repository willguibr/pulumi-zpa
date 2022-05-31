// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr.Inputs
{

    public sealed class ZPAPolicyAccessTimeoutRuleConditionOperandArgs : Pulumi.ResourceArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("idpId")]
        public Input<string>? IdpId { get; set; }

        [Input("lhs", required: true)]
        public Input<string> Lhs { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("objectType", required: true)]
        public Input<string> ObjectType { get; set; } = null!;

        [Input("rhs")]
        public Input<string>? Rhs { get; set; }

        [Input("rhsLists")]
        private InputList<string>? _rhsLists;
        public InputList<string> RhsLists
        {
            get => _rhsLists ?? (_rhsLists = new InputList<string>());
            set => _rhsLists = value;
        }

        public ZPAPolicyAccessTimeoutRuleConditionOperandArgs()
        {
        }
    }
}
