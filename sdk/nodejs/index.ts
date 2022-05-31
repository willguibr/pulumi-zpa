// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./getZPAAppConnectorController";
export * from "./getZPAAppConnectorGroup";
export * from "./getZPAAppSegmentBrowserAccess";
export * from "./getZPAApplicationSegment";
export * from "./getZPAApplicationServer";
export * from "./getZPABaCertificate";
export * from "./getZPACloudConnectorGroup";
export * from "./getZPACustomerVersionProfile";
export * from "./getZPAEnrollmentCert";
export * from "./getZPAIdPController";
export * from "./getZPALSSConfigClientTypes";
export * from "./getZPALSSConfigLogTypeFormats";
export * from "./getZPALSSConfigMachineGroup";
export * from "./getZPALSSConfigStatusCodes";
export * from "./getZPALogStreamingService";
export * from "./getZPAPolicyType";
export * from "./getZPAPostureProfile";
export * from "./getZPAProvisioningKey";
export * from "./getZPASAMLAttribute";
export * from "./getZPASCIMAttributeHeader";
export * from "./getZPASCIMGroups";
export * from "./getZPASegmentGroup";
export * from "./getZPAServerGroup";
export * from "./getZPAServiceEdgeController";
export * from "./getZPAServiceEdgeGroup";
export * from "./getZPATrustedNetwork";
export * from "./provider";
export * from "./zpaappConnectorGroup";
export * from "./zpaappSegmentBrowserAccess";
export * from "./zpaapplicationSegment";
export * from "./zpaapplicationServer";
export * from "./zpalogStreamingService";
export * from "./zpapolicyAccessForwardingRule";
export * from "./zpapolicyAccessRule";
export * from "./zpapolicyAccessTimeoutRule";
export * from "./zpaprovisioningKey";
export * from "./zpasegmentGroup";
export * from "./zpaserverGroup";
export * from "./zpaserviceEdgeGroup";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { ZPAAppConnectorGroup } from "./zpaappConnectorGroup";
import { ZPAAppSegmentBrowserAccess } from "./zpaappSegmentBrowserAccess";
import { ZPAApplicationSegment } from "./zpaapplicationSegment";
import { ZPAApplicationServer } from "./zpaapplicationServer";
import { ZPALogStreamingService } from "./zpalogStreamingService";
import { ZPAPolicyAccessForwardingRule } from "./zpapolicyAccessForwardingRule";
import { ZPAPolicyAccessRule } from "./zpapolicyAccessRule";
import { ZPAPolicyAccessTimeoutRule } from "./zpapolicyAccessTimeoutRule";
import { ZPAProvisioningKey } from "./zpaprovisioningKey";
import { ZPASegmentGroup } from "./zpasegmentGroup";
import { ZPAServerGroup } from "./zpaserverGroup";
import { ZPAServiceEdgeGroup } from "./zpaserviceEdgeGroup";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "zpa:index/zPAAppConnectorGroup:ZPAAppConnectorGroup":
                return new ZPAAppConnectorGroup(name, <any>undefined, { urn })
            case "zpa:index/zPAAppSegmentBrowserAccess:ZPAAppSegmentBrowserAccess":
                return new ZPAAppSegmentBrowserAccess(name, <any>undefined, { urn })
            case "zpa:index/zPAApplicationSegment:ZPAApplicationSegment":
                return new ZPAApplicationSegment(name, <any>undefined, { urn })
            case "zpa:index/zPAApplicationServer:ZPAApplicationServer":
                return new ZPAApplicationServer(name, <any>undefined, { urn })
            case "zpa:index/zPALogStreamingService:ZPALogStreamingService":
                return new ZPALogStreamingService(name, <any>undefined, { urn })
            case "zpa:index/zPAPolicyAccessForwardingRule:ZPAPolicyAccessForwardingRule":
                return new ZPAPolicyAccessForwardingRule(name, <any>undefined, { urn })
            case "zpa:index/zPAPolicyAccessRule:ZPAPolicyAccessRule":
                return new ZPAPolicyAccessRule(name, <any>undefined, { urn })
            case "zpa:index/zPAPolicyAccessTimeoutRule:ZPAPolicyAccessTimeoutRule":
                return new ZPAPolicyAccessTimeoutRule(name, <any>undefined, { urn })
            case "zpa:index/zPAProvisioningKey:ZPAProvisioningKey":
                return new ZPAProvisioningKey(name, <any>undefined, { urn })
            case "zpa:index/zPASegmentGroup:ZPASegmentGroup":
                return new ZPASegmentGroup(name, <any>undefined, { urn })
            case "zpa:index/zPAServerGroup:ZPAServerGroup":
                return new ZPAServerGroup(name, <any>undefined, { urn })
            case "zpa:index/zPAServiceEdgeGroup:ZPAServiceEdgeGroup":
                return new ZPAServiceEdgeGroup(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("zpa", "index/zPAAppConnectorGroup", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAAppSegmentBrowserAccess", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAApplicationSegment", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAApplicationServer", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPALogStreamingService", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAPolicyAccessForwardingRule", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAPolicyAccessRule", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAPolicyAccessTimeoutRule", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAProvisioningKey", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPASegmentGroup", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAServerGroup", _module)
pulumi.runtime.registerResourceModule("zpa", "index/zPAServiceEdgeGroup", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("zpa", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:zpa") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
