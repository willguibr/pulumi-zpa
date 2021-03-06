// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export function getZPASegmentGroup(args?: GetZPASegmentGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetZPASegmentGroupResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("zpa:index/getZPASegmentGroup:getZPASegmentGroup", {
        "id": args.id,
        "name": args.name,
        "policyMigrated": args.policyMigrated,
    }, opts);
}

/**
 * A collection of arguments for invoking getZPASegmentGroup.
 */
export interface GetZPASegmentGroupArgs {
    id?: string;
    name?: string;
    policyMigrated?: boolean;
}

/**
 * A collection of values returned by getZPASegmentGroup.
 */
export interface GetZPASegmentGroupResult {
    readonly applications: outputs.GetZPASegmentGroupApplication[];
    readonly configSpace: string;
    readonly creationTime: string;
    readonly description: string;
    readonly enabled: boolean;
    readonly id?: string;
    readonly modifiedTime: string;
    readonly modifiedby: string;
    readonly name?: string;
    readonly policyMigrated: boolean;
    readonly tcpKeepAliveEnabled: string;
}

export function getZPASegmentGroupOutput(args?: GetZPASegmentGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetZPASegmentGroupResult> {
    return pulumi.output(args).apply(a => getZPASegmentGroup(a, opts))
}

/**
 * A collection of arguments for invoking getZPASegmentGroup.
 */
export interface GetZPASegmentGroupOutputArgs {
    id?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    policyMigrated?: pulumi.Input<boolean>;
}
