import * as pulumi from "@pulumi/pulumi";
import * as zpa from "@willguibr/zpa"

const lssClientTypes = zpa.getZPABaCertificate(args?: zpa.GetZPABaCertificateArgs{
    name:

});

export const clientTypes = lssClientTypes.then(x => x.id)