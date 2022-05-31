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
    public sealed class GetZPAApplicationSegmentServerGroupResult
    {
        public readonly string ConfigSpace;
        public readonly string CreationTime;
        public readonly string Description;
        public readonly bool DynamicDiscovery;
        public readonly bool Enabled;
        public readonly string Id;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string Name;

        [OutputConstructor]
        private GetZPAApplicationSegmentServerGroupResult(
            string configSpace,

            string creationTime,

            string description,

            bool dynamicDiscovery,

            bool enabled,

            string id,

            string modifiedTime,

            string modifiedby,

            string name)
        {
            ConfigSpace = configSpace;
            CreationTime = creationTime;
            Description = description;
            DynamicDiscovery = dynamicDiscovery;
            Enabled = enabled;
            Id = id;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
        }
    }
}
