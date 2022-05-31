// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package zpa

import (
	"fmt"
	"path/filepath"
	"strings"
	"unicode"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/willguibr/pulumi-zpa/provider/pkg/version"
	"github.com/zscaler/terraform-provider-zpa/zpa"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "zpa"
	// modules:
	mainMod = "Index"
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

var namespaceMap = map[string]string{
	mainPkg: "willguibr",
}

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(moduleTitle string, mem string) tokens.ModuleMember {
	moduleName := strings.ToLower(moduleTitle)
	namespaceMap[moduleName] = moduleTitle
	fn := string(unicode.ToLower(rune(mem[0]))) + mem[1:]
	token := moduleName + "/" + fn
	return tokens.ModuleMember(mainPkg + ":" + token + ":" + mem)
}

// func makeMember(mod string, mem string) tokens.ModuleMember {
// 	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
// }

func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

func makeDataSource(mod string, res string) tokens.ModuleMember {
	return makeMember(mod, res)
}

func makeResource(mod string, res string) tokens.Type {
	return makeType(mod, res)
}

func refProviderLicense(license tfbridge.TFProviderLicense) *tfbridge.TFProviderLicense {
	return &license
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(zpa.Provider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "zpa",
		Description: "A Pulumi package for creating and managing zpa cloud resources.",
		Keywords:    []string{"pulumi", "zpa"},
		License:     "Apache-2.0",
		Homepage:    "https://www.pulumi.com",
		GitHubOrg:   "willguibr",
		Repository:  "https://github.com/willguibr/pulumi-zpa",
		// PluginDownloadURL:    "https://github.com/willguibr/pulumi-zpa/releases/download/v${VERSION}",
		TFProviderLicense:    refProviderLicense(tfbridge.MITLicenseType),
		Config:               map[string]*tfbridge.SchemaInfo{},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"zpa_app_connector_group": {Tok: makeResource(mainMod, "ZPAAppConnectorGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_app_connector_group.md"},
			},
			"zpa_service_edge_group": {Tok: makeResource(mainMod, "ZPAServiceEdgeGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_service_edge_group.md"},
			},
			"zpa_segment_group": {Tok: makeResource(mainMod, "ZPASegmentGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_segment_group.md"},
			},
			"zpa_server_group": {Tok: makeResource(mainMod, "ZPAServerGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_server_group.md"},
			},
			"zpa_application_segment": {Tok: makeResource(mainMod, "ZPAApplicationSegment"),
				Docs: &tfbridge.DocInfo{Source: "zpa_application_segment.md"},
			},
			"zpa_application_server": {Tok: makeResource(mainMod, "ZPAApplicationServer"),
				Docs: &tfbridge.DocInfo{Source: "zpa_application_server.md"},
			},
			"zpa_browser_access": {Tok: makeResource(mainMod, "ZPAAppSegmentBrowserAccess"),
				Docs: &tfbridge.DocInfo{Source: "zpa_browser_access.md"},
			},
			"zpa_lss_config_controller": {Tok: makeResource(mainMod, "ZPALogStreamingService"),
				Docs: &tfbridge.DocInfo{Source: "zpa_lss_config_controller.md"},
			},
			"zpa_policy_access_rule": {Tok: makeResource(mainMod, "ZPAPolicyAccessRule"),
				Docs: &tfbridge.DocInfo{Source: "zpa_policy_access_rule.md"},
			},
			"zpa_policy_forwarding_rule": {Tok: makeResource(mainMod, "ZPAPolicyAccessForwardingRule"),
				Docs: &tfbridge.DocInfo{Source: "zpa_policy_forwarding_rule.md"},
			},
			"zpa_policy_timeout_rule": {Tok: makeResource(mainMod, "ZPAPolicyAccessTimeoutRule"),
				Docs: &tfbridge.DocInfo{Source: "zpa_policy_timeout_rule.md"},
			},
			"zpa_provisioning_key": {Tok: makeResource(mainMod, "ZPAProvisioningKey"),
				Docs: &tfbridge.DocInfo{Source: "zpa_provisioning_key.md"},
			},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"zpa_app_connector_controller": {Tok: makeDataSource(mainMod, "getZPAAppConnectorController"),
				Docs: &tfbridge.DocInfo{Source: "zpa_app_connector_controller.md"},
			},
			"zpa_service_edge_controller": {Tok: makeDataSource(mainMod, "getZPAServiceEdgeController"),
				Docs: &tfbridge.DocInfo{Source: "zpa_service_edge_controller.md"},
			},
			"zpa_app_connector_group": {Tok: makeDataSource(mainMod, "getZPAAppConnectorGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_app_connector_group.md"},
			},
			"zpa_service_edge_group": {Tok: makeDataSource(mainMod, "getZPAServiceEdgeGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_service_edge_group.md"},
			},
			"zpa_segment_group": {Tok: makeDataSource(mainMod, "getZPASegmentGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_segment_group.md"},
			},
			"zpa_server_group": {Tok: makeDataSource(mainMod, "getZPAServerGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_server_group.md"},
			},
			"zpa_application_segment": {Tok: makeDataSource(mainMod, "getZPAApplicationSegment"),
				Docs: &tfbridge.DocInfo{Source: "zpa_application_segment.md"},
			},
			"zpa_application_server": {Tok: makeDataSource(mainMod, "getZPAApplicationServer"),
				Docs: &tfbridge.DocInfo{Source: "zpa_application_segment.md"},
			},
			"zpa_browser_access": {Tok: makeDataSource(mainMod, "getZPAAppSegmentBrowserAccess"),
				Docs: &tfbridge.DocInfo{Source: "zpa_browser_access.md"},
			},
			"zpa_lss_config_controller": {Tok: makeDataSource(mainMod, "getZPALogStreamingService"),
				Docs: &tfbridge.DocInfo{Source: "zpa_lss_config_controller.md"},
			},
			"zpa_provisioning_key": {Tok: makeDataSource(mainMod, "getZPAProvisioningKey"),
				Docs: &tfbridge.DocInfo{Source: "zpa_provisioning_key.md"},
			},
			"zpa_ba_certificate": {Tok: makeDataSource(mainMod, "getZPABaCertificate"),
				Docs: &tfbridge.DocInfo{Source: "zpa_ba_certificate.md"},
			},
			"zpa_cloud_connector_group": {Tok: makeDataSource(mainMod, "getZPACloudConnectorGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_cloud_connector_group.md"},
			},
			"zpa_customer_version_profile": {Tok: makeDataSource(mainMod, "getZPACustomerVersionProfile"),
				Docs: &tfbridge.DocInfo{Source: "zpa_customer_version_profile.md"},
			},
			"zpa_enrollment_cert": {Tok: makeDataSource(mainMod, "getZPAEnrollmentCert"),
				Docs: &tfbridge.DocInfo{Source: "zpa_enrollment_cert.md"},
			},
			"zpa_idp_controller": {Tok: makeDataSource(mainMod, "getZPAIdPController"),
				Docs: &tfbridge.DocInfo{Source: "zpa_idp_controller.md"},
			},
			"zpa_lss_config_client_types": {Tok: makeDataSource(mainMod, "getZPALSSConfigClientTypes"),
				Docs: &tfbridge.DocInfo{Source: "zpa_lss_config_client_types.md"},
			},
			"zpa_lss_config_log_type_formats": {Tok: makeDataSource(mainMod, "getZPALSSConfigLogTypeFormats"),
				Docs: &tfbridge.DocInfo{Source: "zpa_lss_config_log_type_formats.md"},
			},
			"zpa_lss_config_status_codes": {Tok: makeDataSource(mainMod, "getZPALSSConfigStatusCodes"),
				Docs: &tfbridge.DocInfo{Source: "zpa_lss_config_status_codes.md"},
			},
			"zpa_machine_group": {Tok: makeDataSource(mainMod, "getZPALSSConfigMachineGroup"),
				Docs: &tfbridge.DocInfo{Source: "zpa_machine_group.md"},
			},
			"zpa_policy_type": {Tok: makeDataSource(mainMod, "getZPAPolicyType"),
				Docs: &tfbridge.DocInfo{Source: "zpa_policy_type.md"},
			},
			"zpa_posture_profile": {Tok: makeDataSource(mainMod, "getZPAPostureProfile"),
				Docs: &tfbridge.DocInfo{Source: "zpa_posture_profile.md"},
			},
			"zpa_saml_attribute": {Tok: makeDataSource(mainMod, "getZPASAMLAttribute"),
				Docs: &tfbridge.DocInfo{Source: "zpa_saml_attribute.md"},
			},
			"zpa_scim_attribute_header": {Tok: makeDataSource(mainMod, "getZPASCIMAttributeHeader"),
				Docs: &tfbridge.DocInfo{Source: "zpa_scim_attribute_header.md"},
			},
			"zpa_scim_groups": {Tok: makeDataSource(mainMod, "getZPASCIMGroups"),
				Docs: &tfbridge.DocInfo{Source: "zpa_scim_groups.md"},
			},
			"zpa_trusted_network": {Tok: makeDataSource(mainMod, "getZPATrustedNetwork"),
				Docs: &tfbridge.DocInfo{Source: "zpa_trusted_network.md"},
			},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@willguibr/zpa",
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "willguibr_zpa",
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/willguibr/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			Namespaces: namespaceMap,
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}

// func noUpstreamDocs() *tfbridge.DocInfo {
// 	return &tfbridge.DocInfo{
// 		Markdown: []byte(" "),
// 	}
// }
