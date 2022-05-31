// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.willguibr
{
    public static class GetZPAEnrollmentCert
    {
        public static Task<GetZPAEnrollmentCertResult> InvokeAsync(GetZPAEnrollmentCertArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetZPAEnrollmentCertResult>("zpa:index/getZPAEnrollmentCert:getZPAEnrollmentCert", args ?? new GetZPAEnrollmentCertArgs(), options.WithDefaults());

        public static Output<GetZPAEnrollmentCertResult> Invoke(GetZPAEnrollmentCertInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetZPAEnrollmentCertResult>("zpa:index/getZPAEnrollmentCert:getZPAEnrollmentCert", args ?? new GetZPAEnrollmentCertInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetZPAEnrollmentCertArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetZPAEnrollmentCertArgs()
        {
        }
    }

    public sealed class GetZPAEnrollmentCertInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetZPAEnrollmentCertInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetZPAEnrollmentCertResult
    {
        public readonly bool AllowSigning;
        public readonly string Certificate;
        public readonly string ClientCertType;
        public readonly string Cname;
        public readonly string CreationTime;
        public readonly string Csr;
        public readonly string Description;
        public readonly string? Id;
        public readonly string IssuedBy;
        public readonly string IssuedTo;
        public readonly string ModifiedTime;
        public readonly string Modifiedby;
        public readonly string? Name;
        public readonly string ParentCertId;
        public readonly string ParentCertName;
        public readonly string PrivateKey;
        public readonly bool PrivateKeyPresent;
        public readonly string SerialNo;
        public readonly string ValidFromInEpochSec;
        public readonly string ValidToInEpochSec;
        public readonly string ZrsaEncryptedPrivateKey;
        public readonly string ZrsaEncryptedSessionKey;

        [OutputConstructor]
        private GetZPAEnrollmentCertResult(
            bool allowSigning,

            string certificate,

            string clientCertType,

            string cname,

            string creationTime,

            string csr,

            string description,

            string? id,

            string issuedBy,

            string issuedTo,

            string modifiedTime,

            string modifiedby,

            string? name,

            string parentCertId,

            string parentCertName,

            string privateKey,

            bool privateKeyPresent,

            string serialNo,

            string validFromInEpochSec,

            string validToInEpochSec,

            string zrsaEncryptedPrivateKey,

            string zrsaEncryptedSessionKey)
        {
            AllowSigning = allowSigning;
            Certificate = certificate;
            ClientCertType = clientCertType;
            Cname = cname;
            CreationTime = creationTime;
            Csr = csr;
            Description = description;
            Id = id;
            IssuedBy = issuedBy;
            IssuedTo = issuedTo;
            ModifiedTime = modifiedTime;
            Modifiedby = modifiedby;
            Name = name;
            ParentCertId = parentCertId;
            ParentCertName = parentCertName;
            PrivateKey = privateKey;
            PrivateKeyPresent = privateKeyPresent;
            SerialNo = serialNo;
            ValidFromInEpochSec = validFromInEpochSec;
            ValidToInEpochSec = validToInEpochSec;
            ZrsaEncryptedPrivateKey = zrsaEncryptedPrivateKey;
            ZrsaEncryptedSessionKey = zrsaEncryptedSessionKey;
        }
    }
}
