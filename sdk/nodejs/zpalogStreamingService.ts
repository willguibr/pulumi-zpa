// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export class ZPALogStreamingService extends pulumi.CustomResource {
    /**
     * Get an existing ZPALogStreamingService resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZPALogStreamingServiceState, opts?: pulumi.CustomResourceOptions): ZPALogStreamingService {
        return new ZPALogStreamingService(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'zpa:index/zPALogStreamingService:ZPALogStreamingService';

    /**
     * Returns true if the given object is an instance of ZPALogStreamingService.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ZPALogStreamingService {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ZPALogStreamingService.__pulumiType;
    }

    public readonly config!: pulumi.Output<outputs.ZPALogStreamingServiceConfig | undefined>;
    /**
     * App Connector Group(s) to be added to the LSS configuration
     */
    public readonly connectorGroups!: pulumi.Output<outputs.ZPALogStreamingServiceConnectorGroup[] | undefined>;
    public /*out*/ readonly policyRuleId!: pulumi.Output<string>;
    public readonly policyRuleResource!: pulumi.Output<outputs.ZPALogStreamingServicePolicyRuleResource | undefined>;

    /**
     * Create a ZPALogStreamingService resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ZPALogStreamingServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ZPALogStreamingServiceArgs | ZPALogStreamingServiceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ZPALogStreamingServiceState | undefined;
            resourceInputs["config"] = state ? state.config : undefined;
            resourceInputs["connectorGroups"] = state ? state.connectorGroups : undefined;
            resourceInputs["policyRuleId"] = state ? state.policyRuleId : undefined;
            resourceInputs["policyRuleResource"] = state ? state.policyRuleResource : undefined;
        } else {
            const args = argsOrState as ZPALogStreamingServiceArgs | undefined;
            resourceInputs["config"] = args ? args.config : undefined;
            resourceInputs["connectorGroups"] = args ? args.connectorGroups : undefined;
            resourceInputs["policyRuleResource"] = args ? args.policyRuleResource : undefined;
            resourceInputs["policyRuleId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ZPALogStreamingService.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ZPALogStreamingService resources.
 */
export interface ZPALogStreamingServiceState {
    config?: pulumi.Input<inputs.ZPALogStreamingServiceConfig>;
    /**
     * App Connector Group(s) to be added to the LSS configuration
     */
    connectorGroups?: pulumi.Input<pulumi.Input<inputs.ZPALogStreamingServiceConnectorGroup>[]>;
    policyRuleId?: pulumi.Input<string>;
    policyRuleResource?: pulumi.Input<inputs.ZPALogStreamingServicePolicyRuleResource>;
}

/**
 * The set of arguments for constructing a ZPALogStreamingService resource.
 */
export interface ZPALogStreamingServiceArgs {
    config?: pulumi.Input<inputs.ZPALogStreamingServiceConfig>;
    /**
     * App Connector Group(s) to be added to the LSS configuration
     */
    connectorGroups?: pulumi.Input<pulumi.Input<inputs.ZPALogStreamingServiceConnectorGroup>[]>;
    policyRuleResource?: pulumi.Input<inputs.ZPALogStreamingServicePolicyRuleResource>;
}
