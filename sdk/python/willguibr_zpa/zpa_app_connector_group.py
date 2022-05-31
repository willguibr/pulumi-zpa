# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ZPAAppConnectorGroupArgs', 'ZPAAppConnectorGroup']

@pulumi.input_type
class ZPAAppConnectorGroupArgs:
    def __init__(__self__, *,
                 latitude: pulumi.Input[str],
                 location: pulumi.Input[str],
                 longitude: pulumi.Input[str],
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_query_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 lss_app_connector_group: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 override_version_profile: Optional[pulumi.Input[bool]] = None,
                 upgrade_day: Optional[pulumi.Input[str]] = None,
                 upgrade_time_in_secs: Optional[pulumi.Input[str]] = None,
                 version_profile_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZPAAppConnectorGroup resource.
        :param pulumi.Input[str] latitude: Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        :param pulumi.Input[str] location: Location of the App Connector Group
        :param pulumi.Input[str] longitude: Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        :param pulumi.Input[str] description: Description of the App Connector Group
        :param pulumi.Input[str] dns_query_type: Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        :param pulumi.Input[bool] enabled: Whether this App Connector Group is enabled or not
        :param pulumi.Input[str] name: Name of the App Connector Group
        :param pulumi.Input[bool] override_version_profile: Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        :param pulumi.Input[str] upgrade_day: App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
               of valid days (i.e., Sunday, Monday)
        :param pulumi.Input[str] upgrade_time_in_secs: App Connectors in this group will attempt to update to a newer version of the software during this specified time.
               Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
               intervals
        :param pulumi.Input[str] version_profile_id: ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
               overrideVersionProfile is set to true
        """
        pulumi.set(__self__, "latitude", latitude)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "longitude", longitude)
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_query_type is not None:
            pulumi.set(__self__, "dns_query_type", dns_query_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if lss_app_connector_group is not None:
            pulumi.set(__self__, "lss_app_connector_group", lss_app_connector_group)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if override_version_profile is not None:
            pulumi.set(__self__, "override_version_profile", override_version_profile)
        if upgrade_day is not None:
            pulumi.set(__self__, "upgrade_day", upgrade_day)
        if upgrade_time_in_secs is not None:
            pulumi.set(__self__, "upgrade_time_in_secs", upgrade_time_in_secs)
        if version_profile_id is not None:
            pulumi.set(__self__, "version_profile_id", version_profile_id)

    @property
    @pulumi.getter
    def latitude(self) -> pulumi.Input[str]:
        """
        Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        """
        return pulumi.get(self, "latitude")

    @latitude.setter
    def latitude(self, value: pulumi.Input[str]):
        pulumi.set(self, "latitude", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        Location of the App Connector Group
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def longitude(self) -> pulumi.Input[str]:
        """
        Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        """
        return pulumi.get(self, "longitude")

    @longitude.setter
    def longitude(self, value: pulumi.Input[str]):
        pulumi.set(self, "longitude", value)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the App Connector Group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsQueryType")
    def dns_query_type(self) -> Optional[pulumi.Input[str]]:
        """
        Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        """
        return pulumi.get(self, "dns_query_type")

    @dns_query_type.setter
    def dns_query_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_query_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this App Connector Group is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="lssAppConnectorGroup")
    def lss_app_connector_group(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "lss_app_connector_group")

    @lss_app_connector_group.setter
    def lss_app_connector_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lss_app_connector_group", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the App Connector Group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="overrideVersionProfile")
    def override_version_profile(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        """
        return pulumi.get(self, "override_version_profile")

    @override_version_profile.setter
    def override_version_profile(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "override_version_profile", value)

    @property
    @pulumi.getter(name="upgradeDay")
    def upgrade_day(self) -> Optional[pulumi.Input[str]]:
        """
        App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
        of valid days (i.e., Sunday, Monday)
        """
        return pulumi.get(self, "upgrade_day")

    @upgrade_day.setter
    def upgrade_day(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upgrade_day", value)

    @property
    @pulumi.getter(name="upgradeTimeInSecs")
    def upgrade_time_in_secs(self) -> Optional[pulumi.Input[str]]:
        """
        App Connectors in this group will attempt to update to a newer version of the software during this specified time.
        Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
        intervals
        """
        return pulumi.get(self, "upgrade_time_in_secs")

    @upgrade_time_in_secs.setter
    def upgrade_time_in_secs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upgrade_time_in_secs", value)

    @property
    @pulumi.getter(name="versionProfileId")
    def version_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
        overrideVersionProfile is set to true
        """
        return pulumi.get(self, "version_profile_id")

    @version_profile_id.setter
    def version_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_profile_id", value)


@pulumi.input_type
class _ZPAAppConnectorGroupState:
    def __init__(__self__, *,
                 city_country: Optional[pulumi.Input[str]] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_query_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 latitude: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 longitude: Optional[pulumi.Input[str]] = None,
                 lss_app_connector_group: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 override_version_profile: Optional[pulumi.Input[bool]] = None,
                 upgrade_day: Optional[pulumi.Input[str]] = None,
                 upgrade_time_in_secs: Optional[pulumi.Input[str]] = None,
                 version_profile_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZPAAppConnectorGroup resources.
        :param pulumi.Input[str] description: Description of the App Connector Group
        :param pulumi.Input[str] dns_query_type: Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        :param pulumi.Input[bool] enabled: Whether this App Connector Group is enabled or not
        :param pulumi.Input[str] latitude: Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        :param pulumi.Input[str] location: Location of the App Connector Group
        :param pulumi.Input[str] longitude: Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        :param pulumi.Input[str] name: Name of the App Connector Group
        :param pulumi.Input[bool] override_version_profile: Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        :param pulumi.Input[str] upgrade_day: App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
               of valid days (i.e., Sunday, Monday)
        :param pulumi.Input[str] upgrade_time_in_secs: App Connectors in this group will attempt to update to a newer version of the software during this specified time.
               Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
               intervals
        :param pulumi.Input[str] version_profile_id: ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
               overrideVersionProfile is set to true
        """
        if city_country is not None:
            pulumi.set(__self__, "city_country", city_country)
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_query_type is not None:
            pulumi.set(__self__, "dns_query_type", dns_query_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if latitude is not None:
            pulumi.set(__self__, "latitude", latitude)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if longitude is not None:
            pulumi.set(__self__, "longitude", longitude)
        if lss_app_connector_group is not None:
            pulumi.set(__self__, "lss_app_connector_group", lss_app_connector_group)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if override_version_profile is not None:
            pulumi.set(__self__, "override_version_profile", override_version_profile)
        if upgrade_day is not None:
            pulumi.set(__self__, "upgrade_day", upgrade_day)
        if upgrade_time_in_secs is not None:
            pulumi.set(__self__, "upgrade_time_in_secs", upgrade_time_in_secs)
        if version_profile_id is not None:
            pulumi.set(__self__, "version_profile_id", version_profile_id)

    @property
    @pulumi.getter(name="cityCountry")
    def city_country(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "city_country")

    @city_country.setter
    def city_country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city_country", value)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the App Connector Group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsQueryType")
    def dns_query_type(self) -> Optional[pulumi.Input[str]]:
        """
        Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        """
        return pulumi.get(self, "dns_query_type")

    @dns_query_type.setter
    def dns_query_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_query_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this App Connector Group is enabled or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def latitude(self) -> Optional[pulumi.Input[str]]:
        """
        Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        """
        return pulumi.get(self, "latitude")

    @latitude.setter
    def latitude(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "latitude", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the App Connector Group
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def longitude(self) -> Optional[pulumi.Input[str]]:
        """
        Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        """
        return pulumi.get(self, "longitude")

    @longitude.setter
    def longitude(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "longitude", value)

    @property
    @pulumi.getter(name="lssAppConnectorGroup")
    def lss_app_connector_group(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "lss_app_connector_group")

    @lss_app_connector_group.setter
    def lss_app_connector_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lss_app_connector_group", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the App Connector Group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="overrideVersionProfile")
    def override_version_profile(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        """
        return pulumi.get(self, "override_version_profile")

    @override_version_profile.setter
    def override_version_profile(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "override_version_profile", value)

    @property
    @pulumi.getter(name="upgradeDay")
    def upgrade_day(self) -> Optional[pulumi.Input[str]]:
        """
        App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
        of valid days (i.e., Sunday, Monday)
        """
        return pulumi.get(self, "upgrade_day")

    @upgrade_day.setter
    def upgrade_day(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upgrade_day", value)

    @property
    @pulumi.getter(name="upgradeTimeInSecs")
    def upgrade_time_in_secs(self) -> Optional[pulumi.Input[str]]:
        """
        App Connectors in this group will attempt to update to a newer version of the software during this specified time.
        Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
        intervals
        """
        return pulumi.get(self, "upgrade_time_in_secs")

    @upgrade_time_in_secs.setter
    def upgrade_time_in_secs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upgrade_time_in_secs", value)

    @property
    @pulumi.getter(name="versionProfileId")
    def version_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
        overrideVersionProfile is set to true
        """
        return pulumi.get(self, "version_profile_id")

    @version_profile_id.setter
    def version_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_profile_id", value)


class ZPAAppConnectorGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_query_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 latitude: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 longitude: Optional[pulumi.Input[str]] = None,
                 lss_app_connector_group: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 override_version_profile: Optional[pulumi.Input[bool]] = None,
                 upgrade_day: Optional[pulumi.Input[str]] = None,
                 upgrade_time_in_secs: Optional[pulumi.Input[str]] = None,
                 version_profile_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZPAAppConnectorGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the App Connector Group
        :param pulumi.Input[str] dns_query_type: Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        :param pulumi.Input[bool] enabled: Whether this App Connector Group is enabled or not
        :param pulumi.Input[str] latitude: Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        :param pulumi.Input[str] location: Location of the App Connector Group
        :param pulumi.Input[str] longitude: Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        :param pulumi.Input[str] name: Name of the App Connector Group
        :param pulumi.Input[bool] override_version_profile: Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        :param pulumi.Input[str] upgrade_day: App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
               of valid days (i.e., Sunday, Monday)
        :param pulumi.Input[str] upgrade_time_in_secs: App Connectors in this group will attempt to update to a newer version of the software during this specified time.
               Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
               intervals
        :param pulumi.Input[str] version_profile_id: ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
               overrideVersionProfile is set to true
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZPAAppConnectorGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZPAAppConnectorGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZPAAppConnectorGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZPAAppConnectorGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_query_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 latitude: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 longitude: Optional[pulumi.Input[str]] = None,
                 lss_app_connector_group: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 override_version_profile: Optional[pulumi.Input[bool]] = None,
                 upgrade_day: Optional[pulumi.Input[str]] = None,
                 upgrade_time_in_secs: Optional[pulumi.Input[str]] = None,
                 version_profile_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZPAAppConnectorGroupArgs.__new__(ZPAAppConnectorGroupArgs)

            __props__.__dict__["country_code"] = country_code
            __props__.__dict__["description"] = description
            __props__.__dict__["dns_query_type"] = dns_query_type
            __props__.__dict__["enabled"] = enabled
            if latitude is None and not opts.urn:
                raise TypeError("Missing required property 'latitude'")
            __props__.__dict__["latitude"] = latitude
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if longitude is None and not opts.urn:
                raise TypeError("Missing required property 'longitude'")
            __props__.__dict__["longitude"] = longitude
            __props__.__dict__["lss_app_connector_group"] = lss_app_connector_group
            __props__.__dict__["name"] = name
            __props__.__dict__["override_version_profile"] = override_version_profile
            __props__.__dict__["upgrade_day"] = upgrade_day
            __props__.__dict__["upgrade_time_in_secs"] = upgrade_time_in_secs
            __props__.__dict__["version_profile_id"] = version_profile_id
            __props__.__dict__["city_country"] = None
        super(ZPAAppConnectorGroup, __self__).__init__(
            'zpa:index/zPAAppConnectorGroup:ZPAAppConnectorGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            city_country: Optional[pulumi.Input[str]] = None,
            country_code: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dns_query_type: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            latitude: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            longitude: Optional[pulumi.Input[str]] = None,
            lss_app_connector_group: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            override_version_profile: Optional[pulumi.Input[bool]] = None,
            upgrade_day: Optional[pulumi.Input[str]] = None,
            upgrade_time_in_secs: Optional[pulumi.Input[str]] = None,
            version_profile_id: Optional[pulumi.Input[str]] = None) -> 'ZPAAppConnectorGroup':
        """
        Get an existing ZPAAppConnectorGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the App Connector Group
        :param pulumi.Input[str] dns_query_type: Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        :param pulumi.Input[bool] enabled: Whether this App Connector Group is enabled or not
        :param pulumi.Input[str] latitude: Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        :param pulumi.Input[str] location: Location of the App Connector Group
        :param pulumi.Input[str] longitude: Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        :param pulumi.Input[str] name: Name of the App Connector Group
        :param pulumi.Input[bool] override_version_profile: Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        :param pulumi.Input[str] upgrade_day: App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
               of valid days (i.e., Sunday, Monday)
        :param pulumi.Input[str] upgrade_time_in_secs: App Connectors in this group will attempt to update to a newer version of the software during this specified time.
               Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
               intervals
        :param pulumi.Input[str] version_profile_id: ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
               overrideVersionProfile is set to true
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZPAAppConnectorGroupState.__new__(_ZPAAppConnectorGroupState)

        __props__.__dict__["city_country"] = city_country
        __props__.__dict__["country_code"] = country_code
        __props__.__dict__["description"] = description
        __props__.__dict__["dns_query_type"] = dns_query_type
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["latitude"] = latitude
        __props__.__dict__["location"] = location
        __props__.__dict__["longitude"] = longitude
        __props__.__dict__["lss_app_connector_group"] = lss_app_connector_group
        __props__.__dict__["name"] = name
        __props__.__dict__["override_version_profile"] = override_version_profile
        __props__.__dict__["upgrade_day"] = upgrade_day
        __props__.__dict__["upgrade_time_in_secs"] = upgrade_time_in_secs
        __props__.__dict__["version_profile_id"] = version_profile_id
        return ZPAAppConnectorGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cityCountry")
    def city_country(self) -> pulumi.Output[str]:
        return pulumi.get(self, "city_country")

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Output[str]:
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the App Connector Group
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsQueryType")
    def dns_query_type(self) -> pulumi.Output[Optional[str]]:
        """
        Whether to enable IPv4 or IPv6, or both, for DNS resolution of all applications in the App Connector Group
        """
        return pulumi.get(self, "dns_query_type")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this App Connector Group is enabled or not
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def latitude(self) -> pulumi.Output[str]:
        """
        Latitude of the App Connector Group. Integer or decimal. With values in the range of -90 to 90
        """
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the App Connector Group
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def longitude(self) -> pulumi.Output[str]:
        """
        Longitude of the App Connector Group. Integer or decimal. With values in the range of -180 to 180
        """
        return pulumi.get(self, "longitude")

    @property
    @pulumi.getter(name="lssAppConnectorGroup")
    def lss_app_connector_group(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "lss_app_connector_group")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the App Connector Group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overrideVersionProfile")
    def override_version_profile(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the default version profile of the App Connector Group is applied or overridden. Supported values: true, false
        """
        return pulumi.get(self, "override_version_profile")

    @property
    @pulumi.getter(name="upgradeDay")
    def upgrade_day(self) -> pulumi.Output[Optional[str]]:
        """
        App Connectors in this group will attempt to update to a newer version of the software during this specified day. List
        of valid days (i.e., Sunday, Monday)
        """
        return pulumi.get(self, "upgrade_day")

    @property
    @pulumi.getter(name="upgradeTimeInSecs")
    def upgrade_time_in_secs(self) -> pulumi.Output[Optional[str]]:
        """
        App Connectors in this group will attempt to update to a newer version of the software during this specified time.
        Integer in seconds (i.e., -66600). The integer should be greater than or equal to 0 and less than 86400, in 15 minute
        intervals
        """
        return pulumi.get(self, "upgrade_time_in_secs")

    @property
    @pulumi.getter(name="versionProfileId")
    def version_profile_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the version profile. To learn more, see Version Profile Use Cases. This value is required, if the value for
        overrideVersionProfile is set to true
        """
        return pulumi.get(self, "version_profile_id")

