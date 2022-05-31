// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getZPALSSConfigLogTypeFormats(args: GetZPALSSConfigLogTypeFormatsArgs, opts?: pulumi.InvokeOptions): Promise<GetZPALSSConfigLogTypeFormatsResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("zpa:index/getZPALSSConfigLogTypeFormats:getZPALSSConfigLogTypeFormats", {
        "logType": args.logType,
    }, opts);
}

/**
 * A collection of arguments for invoking getZPALSSConfigLogTypeFormats.
 */
export interface GetZPALSSConfigLogTypeFormatsArgs {
    logType: string;
}

/**
 * A collection of values returned by getZPALSSConfigLogTypeFormats.
 */
export interface GetZPALSSConfigLogTypeFormatsResult {
    readonly csv: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly json: string;
    readonly logType: string;
    readonly tsv: string;
}

export function getZPALSSConfigLogTypeFormatsOutput(args: GetZPALSSConfigLogTypeFormatsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetZPALSSConfigLogTypeFormatsResult> {
    return pulumi.output(args).apply(a => getZPALSSConfigLogTypeFormats(a, opts))
}

/**
 * A collection of arguments for invoking getZPALSSConfigLogTypeFormats.
 */
export interface GetZPALSSConfigLogTypeFormatsOutputArgs {
    logType: pulumi.Input<string>;
}
