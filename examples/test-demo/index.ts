import * as pulumi from "@pulumi/pulumi";
import * as zpa from "@willguibr/zpa"

const baCertificate = zpa.getZPABaCertificateOutput()

// export const clientTypes = lssClientTypes.then(x => x.id)