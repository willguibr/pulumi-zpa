// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export function getZPACustomerVersionProfile(args: GetZPACustomerVersionProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetZPACustomerVersionProfileResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("zpa:index/getZPACustomerVersionProfile:getZPACustomerVersionProfile", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getZPACustomerVersionProfile.
 */
export interface GetZPACustomerVersionProfileArgs {
    name: string;
}

/**
 * A collection of values returned by getZPACustomerVersionProfile.
 */
export interface GetZPACustomerVersionProfileResult {
    readonly creationTime: string;
    readonly customScopeCustomerIds: outputs.GetZPACustomerVersionProfileCustomScopeCustomerId[];
    readonly customerId: string;
    readonly description: string;
    readonly id: string;
    readonly modifiedTime: string;
    readonly modifiedby: string;
    readonly name: string;
    readonly upgradePriority: string;
    readonly versions: outputs.GetZPACustomerVersionProfileVersion[];
    readonly visibilityScope: string;
}

export function getZPACustomerVersionProfileOutput(args: GetZPACustomerVersionProfileOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetZPACustomerVersionProfileResult> {
    return pulumi.output(args).apply(a => getZPACustomerVersionProfile(a, opts))
}

/**
 * A collection of arguments for invoking getZPACustomerVersionProfile.
 */
export interface GetZPACustomerVersionProfileOutputArgs {
    name: pulumi.Input<string>;
}
