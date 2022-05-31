// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class ZPAProvisioningKey extends pulumi.CustomResource {
    /**
     * Get an existing ZPAProvisioningKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZPAProvisioningKeyState, opts?: pulumi.CustomResourceOptions): ZPAProvisioningKey {
        return new ZPAProvisioningKey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'zpa:index/zPAProvisioningKey:ZPAProvisioningKey';

    /**
     * Returns true if the given object is an instance of ZPAProvisioningKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ZPAProvisioningKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ZPAProvisioningKey.__pulumiType;
    }

    public readonly appConnectorGroupId!: pulumi.Output<string | undefined>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    public /*out*/ readonly appConnectorGroupName!: pulumi.Output<string>;
    /**
     * Specifies the provisioning key type for App Connectors or ZPA Private Service Edges. The supported values are
     * CONNECTOR_GRP and SERVICE_EDGE_GRP.
     */
    public readonly associationType!: pulumi.Output<string>;
    /**
     * Whether the provisioning key is enabled or not. Supported values: true, false
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * ID of the enrollment certificate that can be used for this provisioning key.
     */
    public readonly enrollmentCertId!: pulumi.Output<string>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    public /*out*/ readonly enrollmentCertName!: pulumi.Output<string>;
    public readonly ipAcls!: pulumi.Output<string[] | undefined>;
    /**
     * The maximum number of instances where this provisioning key can be used for enrolling an App Connector or Service Edge.
     */
    public readonly maxUsage!: pulumi.Output<string>;
    /**
     * Name of the provisioning key.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * read only field. Ignored in PUT/POST calls.
     */
    public /*out*/ readonly provisioningKey!: pulumi.Output<string>;
    public readonly uiConfig!: pulumi.Output<string | undefined>;
    /**
     * The provisioning key utilization count.
     */
    public readonly usageCount!: pulumi.Output<string>;
    /**
     * ID of the existing App Connector or Service Edge Group.
     */
    public readonly zcomponentId!: pulumi.Output<string>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    public readonly zcomponentName!: pulumi.Output<string>;

    /**
     * Create a ZPAProvisioningKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ZPAProvisioningKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ZPAProvisioningKeyArgs | ZPAProvisioningKeyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ZPAProvisioningKeyState | undefined;
            resourceInputs["appConnectorGroupId"] = state ? state.appConnectorGroupId : undefined;
            resourceInputs["appConnectorGroupName"] = state ? state.appConnectorGroupName : undefined;
            resourceInputs["associationType"] = state ? state.associationType : undefined;
            resourceInputs["enabled"] = state ? state.enabled : undefined;
            resourceInputs["enrollmentCertId"] = state ? state.enrollmentCertId : undefined;
            resourceInputs["enrollmentCertName"] = state ? state.enrollmentCertName : undefined;
            resourceInputs["ipAcls"] = state ? state.ipAcls : undefined;
            resourceInputs["maxUsage"] = state ? state.maxUsage : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["provisioningKey"] = state ? state.provisioningKey : undefined;
            resourceInputs["uiConfig"] = state ? state.uiConfig : undefined;
            resourceInputs["usageCount"] = state ? state.usageCount : undefined;
            resourceInputs["zcomponentId"] = state ? state.zcomponentId : undefined;
            resourceInputs["zcomponentName"] = state ? state.zcomponentName : undefined;
        } else {
            const args = argsOrState as ZPAProvisioningKeyArgs | undefined;
            if ((!args || args.associationType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'associationType'");
            }
            if ((!args || args.enrollmentCertId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'enrollmentCertId'");
            }
            if ((!args || args.maxUsage === undefined) && !opts.urn) {
                throw new Error("Missing required property 'maxUsage'");
            }
            if ((!args || args.zcomponentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'zcomponentId'");
            }
            resourceInputs["appConnectorGroupId"] = args ? args.appConnectorGroupId : undefined;
            resourceInputs["associationType"] = args ? args.associationType : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["enrollmentCertId"] = args ? args.enrollmentCertId : undefined;
            resourceInputs["ipAcls"] = args ? args.ipAcls : undefined;
            resourceInputs["maxUsage"] = args ? args.maxUsage : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["uiConfig"] = args ? args.uiConfig : undefined;
            resourceInputs["usageCount"] = args ? args.usageCount : undefined;
            resourceInputs["zcomponentId"] = args ? args.zcomponentId : undefined;
            resourceInputs["zcomponentName"] = args ? args.zcomponentName : undefined;
            resourceInputs["appConnectorGroupName"] = undefined /*out*/;
            resourceInputs["enrollmentCertName"] = undefined /*out*/;
            resourceInputs["provisioningKey"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ZPAProvisioningKey.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ZPAProvisioningKey resources.
 */
export interface ZPAProvisioningKeyState {
    appConnectorGroupId?: pulumi.Input<string>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    appConnectorGroupName?: pulumi.Input<string>;
    /**
     * Specifies the provisioning key type for App Connectors or ZPA Private Service Edges. The supported values are
     * CONNECTOR_GRP and SERVICE_EDGE_GRP.
     */
    associationType?: pulumi.Input<string>;
    /**
     * Whether the provisioning key is enabled or not. Supported values: true, false
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * ID of the enrollment certificate that can be used for this provisioning key.
     */
    enrollmentCertId?: pulumi.Input<string>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    enrollmentCertName?: pulumi.Input<string>;
    ipAcls?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The maximum number of instances where this provisioning key can be used for enrolling an App Connector or Service Edge.
     */
    maxUsage?: pulumi.Input<string>;
    /**
     * Name of the provisioning key.
     */
    name?: pulumi.Input<string>;
    /**
     * read only field. Ignored in PUT/POST calls.
     */
    provisioningKey?: pulumi.Input<string>;
    uiConfig?: pulumi.Input<string>;
    /**
     * The provisioning key utilization count.
     */
    usageCount?: pulumi.Input<string>;
    /**
     * ID of the existing App Connector or Service Edge Group.
     */
    zcomponentId?: pulumi.Input<string>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    zcomponentName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ZPAProvisioningKey resource.
 */
export interface ZPAProvisioningKeyArgs {
    appConnectorGroupId?: pulumi.Input<string>;
    /**
     * Specifies the provisioning key type for App Connectors or ZPA Private Service Edges. The supported values are
     * CONNECTOR_GRP and SERVICE_EDGE_GRP.
     */
    associationType: pulumi.Input<string>;
    /**
     * Whether the provisioning key is enabled or not. Supported values: true, false
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * ID of the enrollment certificate that can be used for this provisioning key.
     */
    enrollmentCertId: pulumi.Input<string>;
    ipAcls?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The maximum number of instances where this provisioning key can be used for enrolling an App Connector or Service Edge.
     */
    maxUsage: pulumi.Input<string>;
    /**
     * Name of the provisioning key.
     */
    name?: pulumi.Input<string>;
    uiConfig?: pulumi.Input<string>;
    /**
     * The provisioning key utilization count.
     */
    usageCount?: pulumi.Input<string>;
    /**
     * ID of the existing App Connector or Service Edge Group.
     */
    zcomponentId: pulumi.Input<string>;
    /**
     * Read only property. Applicable only for GET calls, ignored in PUT/POST calls.
     */
    zcomponentName?: pulumi.Input<string>;
}
