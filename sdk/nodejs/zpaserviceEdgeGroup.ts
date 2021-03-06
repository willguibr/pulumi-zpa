// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export class ZPAServiceEdgeGroup extends pulumi.CustomResource {
    /**
     * Get an existing ZPAServiceEdgeGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZPAServiceEdgeGroupState, opts?: pulumi.CustomResourceOptions): ZPAServiceEdgeGroup {
        return new ZPAServiceEdgeGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'zpa:index/zPAServiceEdgeGroup:ZPAServiceEdgeGroup';

    /**
     * Returns true if the given object is an instance of ZPAServiceEdgeGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ZPAServiceEdgeGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ZPAServiceEdgeGroup.__pulumiType;
    }

    public readonly cityCountry!: pulumi.Output<string>;
    public readonly countryCode!: pulumi.Output<string>;
    /**
     * Description of the Service Edge Group.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether this Service Edge Group is enabled or not.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Enable or disable public access for the Service Edge Group.
     */
    public readonly isPublic!: pulumi.Output<string | undefined>;
    /**
     * Latitude for the Service Edge Group.
     */
    public readonly latitude!: pulumi.Output<string>;
    /**
     * Location for the Service Edge Group.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * Longitude for the Service Edge Group.
     */
    public readonly longitude!: pulumi.Output<string>;
    /**
     * Name of the Service Edge Group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Whether the default version profile of the App Connector Group is applied or overridden.
     */
    public readonly overrideVersionProfile!: pulumi.Output<boolean | undefined>;
    public readonly serviceEdges!: pulumi.Output<outputs.ZPAServiceEdgeGroupServiceEdge[] | undefined>;
    public readonly trustedNetworks!: pulumi.Output<outputs.ZPAServiceEdgeGroupTrustedNetwork[] | undefined>;
    /**
     * Service Edges in this group will attempt to update to a newer version of the software during this specified day.
     */
    public readonly upgradeDay!: pulumi.Output<string | undefined>;
    /**
     * Service Edges in this group will attempt to update to a newer version of the software during this specified time.
     */
    public readonly upgradeTimeInSecs!: pulumi.Output<string | undefined>;
    /**
     * ID of the version profile. To learn more
     */
    public readonly versionProfileId!: pulumi.Output<string>;
    /**
     * ID of the version profile. To learn more
     */
    public /*out*/ readonly versionProfileName!: pulumi.Output<string>;
    /**
     * ID of the version profile. To learn more
     */
    public /*out*/ readonly versionProfileVisibilityScope!: pulumi.Output<string>;

    /**
     * Create a ZPAServiceEdgeGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ZPAServiceEdgeGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ZPAServiceEdgeGroupArgs | ZPAServiceEdgeGroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ZPAServiceEdgeGroupState | undefined;
            resourceInputs["cityCountry"] = state ? state.cityCountry : undefined;
            resourceInputs["countryCode"] = state ? state.countryCode : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["enabled"] = state ? state.enabled : undefined;
            resourceInputs["isPublic"] = state ? state.isPublic : undefined;
            resourceInputs["latitude"] = state ? state.latitude : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["longitude"] = state ? state.longitude : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["overrideVersionProfile"] = state ? state.overrideVersionProfile : undefined;
            resourceInputs["serviceEdges"] = state ? state.serviceEdges : undefined;
            resourceInputs["trustedNetworks"] = state ? state.trustedNetworks : undefined;
            resourceInputs["upgradeDay"] = state ? state.upgradeDay : undefined;
            resourceInputs["upgradeTimeInSecs"] = state ? state.upgradeTimeInSecs : undefined;
            resourceInputs["versionProfileId"] = state ? state.versionProfileId : undefined;
            resourceInputs["versionProfileName"] = state ? state.versionProfileName : undefined;
            resourceInputs["versionProfileVisibilityScope"] = state ? state.versionProfileVisibilityScope : undefined;
        } else {
            const args = argsOrState as ZPAServiceEdgeGroupArgs | undefined;
            if ((!args || args.latitude === undefined) && !opts.urn) {
                throw new Error("Missing required property 'latitude'");
            }
            if ((!args || args.location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'location'");
            }
            if ((!args || args.longitude === undefined) && !opts.urn) {
                throw new Error("Missing required property 'longitude'");
            }
            if ((!args || args.versionProfileId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'versionProfileId'");
            }
            resourceInputs["cityCountry"] = args ? args.cityCountry : undefined;
            resourceInputs["countryCode"] = args ? args.countryCode : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["isPublic"] = args ? args.isPublic : undefined;
            resourceInputs["latitude"] = args ? args.latitude : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["longitude"] = args ? args.longitude : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["overrideVersionProfile"] = args ? args.overrideVersionProfile : undefined;
            resourceInputs["serviceEdges"] = args ? args.serviceEdges : undefined;
            resourceInputs["trustedNetworks"] = args ? args.trustedNetworks : undefined;
            resourceInputs["upgradeDay"] = args ? args.upgradeDay : undefined;
            resourceInputs["upgradeTimeInSecs"] = args ? args.upgradeTimeInSecs : undefined;
            resourceInputs["versionProfileId"] = args ? args.versionProfileId : undefined;
            resourceInputs["versionProfileName"] = undefined /*out*/;
            resourceInputs["versionProfileVisibilityScope"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ZPAServiceEdgeGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ZPAServiceEdgeGroup resources.
 */
export interface ZPAServiceEdgeGroupState {
    cityCountry?: pulumi.Input<string>;
    countryCode?: pulumi.Input<string>;
    /**
     * Description of the Service Edge Group.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether this Service Edge Group is enabled or not.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * Enable or disable public access for the Service Edge Group.
     */
    isPublic?: pulumi.Input<string>;
    /**
     * Latitude for the Service Edge Group.
     */
    latitude?: pulumi.Input<string>;
    /**
     * Location for the Service Edge Group.
     */
    location?: pulumi.Input<string>;
    /**
     * Longitude for the Service Edge Group.
     */
    longitude?: pulumi.Input<string>;
    /**
     * Name of the Service Edge Group.
     */
    name?: pulumi.Input<string>;
    /**
     * Whether the default version profile of the App Connector Group is applied or overridden.
     */
    overrideVersionProfile?: pulumi.Input<boolean>;
    serviceEdges?: pulumi.Input<pulumi.Input<inputs.ZPAServiceEdgeGroupServiceEdge>[]>;
    trustedNetworks?: pulumi.Input<pulumi.Input<inputs.ZPAServiceEdgeGroupTrustedNetwork>[]>;
    /**
     * Service Edges in this group will attempt to update to a newer version of the software during this specified day.
     */
    upgradeDay?: pulumi.Input<string>;
    /**
     * Service Edges in this group will attempt to update to a newer version of the software during this specified time.
     */
    upgradeTimeInSecs?: pulumi.Input<string>;
    /**
     * ID of the version profile. To learn more
     */
    versionProfileId?: pulumi.Input<string>;
    /**
     * ID of the version profile. To learn more
     */
    versionProfileName?: pulumi.Input<string>;
    /**
     * ID of the version profile. To learn more
     */
    versionProfileVisibilityScope?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ZPAServiceEdgeGroup resource.
 */
export interface ZPAServiceEdgeGroupArgs {
    cityCountry?: pulumi.Input<string>;
    countryCode?: pulumi.Input<string>;
    /**
     * Description of the Service Edge Group.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether this Service Edge Group is enabled or not.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * Enable or disable public access for the Service Edge Group.
     */
    isPublic?: pulumi.Input<string>;
    /**
     * Latitude for the Service Edge Group.
     */
    latitude: pulumi.Input<string>;
    /**
     * Location for the Service Edge Group.
     */
    location: pulumi.Input<string>;
    /**
     * Longitude for the Service Edge Group.
     */
    longitude: pulumi.Input<string>;
    /**
     * Name of the Service Edge Group.
     */
    name?: pulumi.Input<string>;
    /**
     * Whether the default version profile of the App Connector Group is applied or overridden.
     */
    overrideVersionProfile?: pulumi.Input<boolean>;
    serviceEdges?: pulumi.Input<pulumi.Input<inputs.ZPAServiceEdgeGroupServiceEdge>[]>;
    trustedNetworks?: pulumi.Input<pulumi.Input<inputs.ZPAServiceEdgeGroupTrustedNetwork>[]>;
    /**
     * Service Edges in this group will attempt to update to a newer version of the software during this specified day.
     */
    upgradeDay?: pulumi.Input<string>;
    /**
     * Service Edges in this group will attempt to update to a newer version of the software during this specified time.
     */
    upgradeTimeInSecs?: pulumi.Input<string>;
    /**
     * ID of the version profile. To learn more
     */
    versionProfileId: pulumi.Input<string>;
}
