// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export class ZPASegmentGroup extends pulumi.CustomResource {
    /**
     * Get an existing ZPASegmentGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZPASegmentGroupState, opts?: pulumi.CustomResourceOptions): ZPASegmentGroup {
        return new ZPASegmentGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'zpa:index/zPASegmentGroup:ZPASegmentGroup';

    /**
     * Returns true if the given object is an instance of ZPASegmentGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ZPASegmentGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ZPASegmentGroup.__pulumiType;
    }

    public readonly applications!: pulumi.Output<outputs.ZPASegmentGroupApplication[]>;
    public readonly configSpace!: pulumi.Output<string | undefined>;
    /**
     * Description of the app group.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether this app group is enabled or not.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Name of the app group.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly policyMigrated!: pulumi.Output<boolean>;
    public readonly tcpKeepAliveEnabled!: pulumi.Output<string | undefined>;

    /**
     * Create a ZPASegmentGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ZPASegmentGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ZPASegmentGroupArgs | ZPASegmentGroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ZPASegmentGroupState | undefined;
            resourceInputs["applications"] = state ? state.applications : undefined;
            resourceInputs["configSpace"] = state ? state.configSpace : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["enabled"] = state ? state.enabled : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["policyMigrated"] = state ? state.policyMigrated : undefined;
            resourceInputs["tcpKeepAliveEnabled"] = state ? state.tcpKeepAliveEnabled : undefined;
        } else {
            const args = argsOrState as ZPASegmentGroupArgs | undefined;
            resourceInputs["applications"] = args ? args.applications : undefined;
            resourceInputs["configSpace"] = args ? args.configSpace : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["policyMigrated"] = args ? args.policyMigrated : undefined;
            resourceInputs["tcpKeepAliveEnabled"] = args ? args.tcpKeepAliveEnabled : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ZPASegmentGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ZPASegmentGroup resources.
 */
export interface ZPASegmentGroupState {
    applications?: pulumi.Input<pulumi.Input<inputs.ZPASegmentGroupApplication>[]>;
    configSpace?: pulumi.Input<string>;
    /**
     * Description of the app group.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether this app group is enabled or not.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * Name of the app group.
     */
    name?: pulumi.Input<string>;
    policyMigrated?: pulumi.Input<boolean>;
    tcpKeepAliveEnabled?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ZPASegmentGroup resource.
 */
export interface ZPASegmentGroupArgs {
    applications?: pulumi.Input<pulumi.Input<inputs.ZPASegmentGroupApplication>[]>;
    configSpace?: pulumi.Input<string>;
    /**
     * Description of the app group.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether this app group is enabled or not.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * Name of the app group.
     */
    name?: pulumi.Input<string>;
    policyMigrated?: pulumi.Input<boolean>;
    tcpKeepAliveEnabled?: pulumi.Input<string>;
}
