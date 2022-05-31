import * as pulumi from "@pulumi/pulumi";
import * as zpa from "@willguibr/zpa";



const segmentGroup = new zpa.ZPASegmentGroup("my-demo-segment-group", {
    name: "pulumi-test",
    description: "pulumi-test",
    enabled: true,
    policyMigrated: true,
    tcpKeepAliveEnabled: "1",
});

export const segmentGroupId = segmentGroup.id;

