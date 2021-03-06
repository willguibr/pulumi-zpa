// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("zpa");

/**
 * zpa client id
 */
export declare const zpaClientId: string | undefined;
Object.defineProperty(exports, "zpaClientId", {
    get() {
        return __config.get("zpaClientId");
    },
    enumerable: true,
});

/**
 * zpa client secret
 */
export declare const zpaClientSecret: string | undefined;
Object.defineProperty(exports, "zpaClientSecret", {
    get() {
        return __config.get("zpaClientSecret");
    },
    enumerable: true,
});

/**
 * zpa customer id
 */
export declare const zpaCustomerId: string | undefined;
Object.defineProperty(exports, "zpaCustomerId", {
    get() {
        return __config.get("zpaCustomerId");
    },
    enumerable: true,
});

