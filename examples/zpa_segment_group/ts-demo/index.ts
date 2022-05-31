import * as pulumi from "@pulumi/pulumi";
import * as zpa from "@willguibr/zpa";

const segmentGroup = new zpa.ZPASegmentGroup("segment-group", {
    name:          "pulumi-test",
    description:   "pulumi-test",
    enabled: true,
    policyMigrated: true,
    tcpKeepAliveEnabled: "1",
});

export const segGroupId = segmentGroup.id;

const appConnectorGroup = new zpa.ZPAAppConnectorGroup("app-connector-group", {
    name                     : "Pulumi Connector Group",
    description              : "Pulumi Connector Group",
    enabled                  : true,
    countryCode              :"US",
    dnsQueryType             : "IPV4",
    latitude                 : "37.3382082",
    longitude                : "-121.8863286",
    location                 : "San Jose, CA, USA",
    upgradeDay               : "SUNDAY",
    upgradeTimeInSecs        : "66600",
    overrideVersionProfile   : true,
    versionProfileId         : "2",

});

export const appConnectorGroupId = appConnectorGroup.id;

const applicationServer = new zpa.ZPAApplicationServer("application-server", {
    name                     : "pulumi.securitygeek.io",
    description              : "pulumi.securitygeek.io",
    enabled                  : true,
    address                  : "pulumi.securitygeek.io",
});

export const serverId = applicationServer.id;

