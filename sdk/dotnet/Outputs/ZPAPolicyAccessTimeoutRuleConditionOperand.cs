// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr.Outputs
{

    [OutputType]
    public sealed class ZPAPolicyAccessTimeoutRuleConditionOperand
    {
        public readonly string? Id;
        public readonly string? IdpId;
        public readonly string Lhs;
        public readonly string? Name;
        public readonly string ObjectType;
        public readonly string? Rhs;
        public readonly ImmutableArray<string> RhsLists;

        [OutputConstructor]
        private ZPAPolicyAccessTimeoutRuleConditionOperand(
            string? id,

            string? idpId,

            string lhs,

            string? name,

            string objectType,

            string? rhs,

            ImmutableArray<string> rhsLists)
        {
            Id = id;
            IdpId = idpId;
            Lhs = lhs;
            Name = name;
            ObjectType = objectType;
            Rhs = rhs;
            RhsLists = rhsLists;
        }
    }
}
