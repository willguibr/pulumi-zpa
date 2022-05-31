# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetZPAAppConnectorGroupResult',
    'AwaitableGetZPAAppConnectorGroupResult',
    'get_zpa_app_connector_group',
    'get_zpa_app_connector_group_output',
]

@pulumi.output_type
class GetZPAAppConnectorGroupResult:
    """
    A collection of values returned by getZPAAppConnectorGroup.
    """
    def __init__(__self__, city_country=None, connectors=None, country_code=None, creation_time=None, description=None, dns_query_type=None, enabled=None, geo_location_id=None, id=None, latitude=None, location=None, longitude=None, lss_app_connector_group=None, modified_time=None, modifiedby=None, name=None, override_version_profile=None, server_groups=None, upgrade_day=None, upgrade_time_in_secs=None, version_profile_id=None, version_profile_name=None, version_profile_visibility_scope=None):
        if city_country and not isinstance(city_country, str):
            raise TypeError("Expected argument 'city_country' to be a str")
        pulumi.set(__self__, "city_country", city_country)
        if connectors and not isinstance(connectors, list):
            raise TypeError("Expected argument 'connectors' to be a list")
        pulumi.set(__self__, "connectors", connectors)
        if country_code and not isinstance(country_code, str):
            raise TypeError("Expected argument 'country_code' to be a str")
        pulumi.set(__self__, "country_code", country_code)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dns_query_type and not isinstance(dns_query_type, str):
            raise TypeError("Expected argument 'dns_query_type' to be a str")
        pulumi.set(__self__, "dns_query_type", dns_query_type)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if geo_location_id and not isinstance(geo_location_id, str):
            raise TypeError("Expected argument 'geo_location_id' to be a str")
        pulumi.set(__self__, "geo_location_id", geo_location_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if latitude and not isinstance(latitude, str):
            raise TypeError("Expected argument 'latitude' to be a str")
        pulumi.set(__self__, "latitude", latitude)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if longitude and not isinstance(longitude, str):
            raise TypeError("Expected argument 'longitude' to be a str")
        pulumi.set(__self__, "longitude", longitude)
        if lss_app_connector_group and not isinstance(lss_app_connector_group, bool):
            raise TypeError("Expected argument 'lss_app_connector_group' to be a bool")
        pulumi.set(__self__, "lss_app_connector_group", lss_app_connector_group)
        if modified_time and not isinstance(modified_time, str):
            raise TypeError("Expected argument 'modified_time' to be a str")
        pulumi.set(__self__, "modified_time", modified_time)
        if modifiedby and not isinstance(modifiedby, str):
            raise TypeError("Expected argument 'modifiedby' to be a str")
        pulumi.set(__self__, "modifiedby", modifiedby)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if override_version_profile and not isinstance(override_version_profile, bool):
            raise TypeError("Expected argument 'override_version_profile' to be a bool")
        pulumi.set(__self__, "override_version_profile", override_version_profile)
        if server_groups and not isinstance(server_groups, list):
            raise TypeError("Expected argument 'server_groups' to be a list")
        pulumi.set(__self__, "server_groups", server_groups)
        if upgrade_day and not isinstance(upgrade_day, str):
            raise TypeError("Expected argument 'upgrade_day' to be a str")
        pulumi.set(__self__, "upgrade_day", upgrade_day)
        if upgrade_time_in_secs and not isinstance(upgrade_time_in_secs, str):
            raise TypeError("Expected argument 'upgrade_time_in_secs' to be a str")
        pulumi.set(__self__, "upgrade_time_in_secs", upgrade_time_in_secs)
        if version_profile_id and not isinstance(version_profile_id, str):
            raise TypeError("Expected argument 'version_profile_id' to be a str")
        pulumi.set(__self__, "version_profile_id", version_profile_id)
        if version_profile_name and not isinstance(version_profile_name, str):
            raise TypeError("Expected argument 'version_profile_name' to be a str")
        pulumi.set(__self__, "version_profile_name", version_profile_name)
        if version_profile_visibility_scope and not isinstance(version_profile_visibility_scope, str):
            raise TypeError("Expected argument 'version_profile_visibility_scope' to be a str")
        pulumi.set(__self__, "version_profile_visibility_scope", version_profile_visibility_scope)

    @property
    @pulumi.getter(name="cityCountry")
    def city_country(self) -> str:
        return pulumi.get(self, "city_country")

    @property
    @pulumi.getter
    def connectors(self) -> Sequence['outputs.GetZPAAppConnectorGroupConnectorResult']:
        return pulumi.get(self, "connectors")

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> str:
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsQueryType")
    def dns_query_type(self) -> str:
        return pulumi.get(self, "dns_query_type")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="geoLocationId")
    def geo_location_id(self) -> str:
        return pulumi.get(self, "geo_location_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def latitude(self) -> str:
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def longitude(self) -> str:
        return pulumi.get(self, "longitude")

    @property
    @pulumi.getter(name="lssAppConnectorGroup")
    def lss_app_connector_group(self) -> bool:
        return pulumi.get(self, "lss_app_connector_group")

    @property
    @pulumi.getter(name="modifiedTime")
    def modified_time(self) -> str:
        return pulumi.get(self, "modified_time")

    @property
    @pulumi.getter
    def modifiedby(self) -> str:
        return pulumi.get(self, "modifiedby")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overrideVersionProfile")
    def override_version_profile(self) -> Optional[bool]:
        return pulumi.get(self, "override_version_profile")

    @property
    @pulumi.getter(name="serverGroups")
    def server_groups(self) -> Sequence['outputs.GetZPAAppConnectorGroupServerGroupResult']:
        return pulumi.get(self, "server_groups")

    @property
    @pulumi.getter(name="upgradeDay")
    def upgrade_day(self) -> str:
        return pulumi.get(self, "upgrade_day")

    @property
    @pulumi.getter(name="upgradeTimeInSecs")
    def upgrade_time_in_secs(self) -> str:
        return pulumi.get(self, "upgrade_time_in_secs")

    @property
    @pulumi.getter(name="versionProfileId")
    def version_profile_id(self) -> str:
        return pulumi.get(self, "version_profile_id")

    @property
    @pulumi.getter(name="versionProfileName")
    def version_profile_name(self) -> str:
        return pulumi.get(self, "version_profile_name")

    @property
    @pulumi.getter(name="versionProfileVisibilityScope")
    def version_profile_visibility_scope(self) -> str:
        return pulumi.get(self, "version_profile_visibility_scope")


class AwaitableGetZPAAppConnectorGroupResult(GetZPAAppConnectorGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPAAppConnectorGroupResult(
            city_country=self.city_country,
            connectors=self.connectors,
            country_code=self.country_code,
            creation_time=self.creation_time,
            description=self.description,
            dns_query_type=self.dns_query_type,
            enabled=self.enabled,
            geo_location_id=self.geo_location_id,
            id=self.id,
            latitude=self.latitude,
            location=self.location,
            longitude=self.longitude,
            lss_app_connector_group=self.lss_app_connector_group,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            override_version_profile=self.override_version_profile,
            server_groups=self.server_groups,
            upgrade_day=self.upgrade_day,
            upgrade_time_in_secs=self.upgrade_time_in_secs,
            version_profile_id=self.version_profile_id,
            version_profile_name=self.version_profile_name,
            version_profile_visibility_scope=self.version_profile_visibility_scope)


def get_zpa_app_connector_group(id: Optional[str] = None,
                                name: Optional[str] = None,
                                override_version_profile: Optional[bool] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPAAppConnectorGroupResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['overrideVersionProfile'] = override_version_profile
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPAAppConnectorGroup:getZPAAppConnectorGroup', __args__, opts=opts, typ=GetZPAAppConnectorGroupResult).value

    return AwaitableGetZPAAppConnectorGroupResult(
        city_country=__ret__.city_country,
        connectors=__ret__.connectors,
        country_code=__ret__.country_code,
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        dns_query_type=__ret__.dns_query_type,
        enabled=__ret__.enabled,
        geo_location_id=__ret__.geo_location_id,
        id=__ret__.id,
        latitude=__ret__.latitude,
        location=__ret__.location,
        longitude=__ret__.longitude,
        lss_app_connector_group=__ret__.lss_app_connector_group,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        override_version_profile=__ret__.override_version_profile,
        server_groups=__ret__.server_groups,
        upgrade_day=__ret__.upgrade_day,
        upgrade_time_in_secs=__ret__.upgrade_time_in_secs,
        version_profile_id=__ret__.version_profile_id,
        version_profile_name=__ret__.version_profile_name,
        version_profile_visibility_scope=__ret__.version_profile_visibility_scope)


@_utilities.lift_output_func(get_zpa_app_connector_group)
def get_zpa_app_connector_group_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       override_version_profile: Optional[pulumi.Input[Optional[bool]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPAAppConnectorGroupResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
