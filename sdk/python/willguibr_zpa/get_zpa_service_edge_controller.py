# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetZPAServiceEdgeControllerResult',
    'AwaitableGetZPAServiceEdgeControllerResult',
    'get_zpa_service_edge_controller',
    'get_zpa_service_edge_controller_output',
]

@pulumi.output_type
class GetZPAServiceEdgeControllerResult:
    """
    A collection of values returned by getZPAServiceEdgeController.
    """
    def __init__(__self__, application_start_time=None, control_channel_status=None, creation_time=None, ctrl_broker_name=None, current_version=None, description=None, enabled=None, enrollment_cert=None, expected_upgrade_time=None, expected_version=None, fingerprint=None, id=None, ip_acl=None, issued_cert_id=None, last_broker_connect_time=None, last_broker_connect_time_duration=None, last_broker_disconnect_time=None, last_broker_disconnect_time_duration=None, last_upgrade_time=None, latitude=None, listen_ips=None, location=None, longitude=None, modified_time=None, modifiedby=None, name=None, platform=None, previous_version=None, private_ip=None, provisioning_key_id=None, provisioning_key_name=None, public_ip=None, publish_ips=None, sarge_version=None, service_edge_group_id=None, service_edge_group_name=None, upgrade_attempt=None, upgrade_status=None):
        if application_start_time and not isinstance(application_start_time, str):
            raise TypeError("Expected argument 'application_start_time' to be a str")
        pulumi.set(__self__, "application_start_time", application_start_time)
        if control_channel_status and not isinstance(control_channel_status, str):
            raise TypeError("Expected argument 'control_channel_status' to be a str")
        pulumi.set(__self__, "control_channel_status", control_channel_status)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if ctrl_broker_name and not isinstance(ctrl_broker_name, str):
            raise TypeError("Expected argument 'ctrl_broker_name' to be a str")
        pulumi.set(__self__, "ctrl_broker_name", ctrl_broker_name)
        if current_version and not isinstance(current_version, str):
            raise TypeError("Expected argument 'current_version' to be a str")
        pulumi.set(__self__, "current_version", current_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if enrollment_cert and not isinstance(enrollment_cert, dict):
            raise TypeError("Expected argument 'enrollment_cert' to be a dict")
        pulumi.set(__self__, "enrollment_cert", enrollment_cert)
        if expected_upgrade_time and not isinstance(expected_upgrade_time, str):
            raise TypeError("Expected argument 'expected_upgrade_time' to be a str")
        pulumi.set(__self__, "expected_upgrade_time", expected_upgrade_time)
        if expected_version and not isinstance(expected_version, str):
            raise TypeError("Expected argument 'expected_version' to be a str")
        pulumi.set(__self__, "expected_version", expected_version)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_acl and not isinstance(ip_acl, str):
            raise TypeError("Expected argument 'ip_acl' to be a str")
        pulumi.set(__self__, "ip_acl", ip_acl)
        if issued_cert_id and not isinstance(issued_cert_id, str):
            raise TypeError("Expected argument 'issued_cert_id' to be a str")
        pulumi.set(__self__, "issued_cert_id", issued_cert_id)
        if last_broker_connect_time and not isinstance(last_broker_connect_time, str):
            raise TypeError("Expected argument 'last_broker_connect_time' to be a str")
        pulumi.set(__self__, "last_broker_connect_time", last_broker_connect_time)
        if last_broker_connect_time_duration and not isinstance(last_broker_connect_time_duration, str):
            raise TypeError("Expected argument 'last_broker_connect_time_duration' to be a str")
        pulumi.set(__self__, "last_broker_connect_time_duration", last_broker_connect_time_duration)
        if last_broker_disconnect_time and not isinstance(last_broker_disconnect_time, str):
            raise TypeError("Expected argument 'last_broker_disconnect_time' to be a str")
        pulumi.set(__self__, "last_broker_disconnect_time", last_broker_disconnect_time)
        if last_broker_disconnect_time_duration and not isinstance(last_broker_disconnect_time_duration, str):
            raise TypeError("Expected argument 'last_broker_disconnect_time_duration' to be a str")
        pulumi.set(__self__, "last_broker_disconnect_time_duration", last_broker_disconnect_time_duration)
        if last_upgrade_time and not isinstance(last_upgrade_time, str):
            raise TypeError("Expected argument 'last_upgrade_time' to be a str")
        pulumi.set(__self__, "last_upgrade_time", last_upgrade_time)
        if latitude and not isinstance(latitude, str):
            raise TypeError("Expected argument 'latitude' to be a str")
        pulumi.set(__self__, "latitude", latitude)
        if listen_ips and not isinstance(listen_ips, str):
            raise TypeError("Expected argument 'listen_ips' to be a str")
        pulumi.set(__self__, "listen_ips", listen_ips)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if longitude and not isinstance(longitude, str):
            raise TypeError("Expected argument 'longitude' to be a str")
        pulumi.set(__self__, "longitude", longitude)
        if modified_time and not isinstance(modified_time, str):
            raise TypeError("Expected argument 'modified_time' to be a str")
        pulumi.set(__self__, "modified_time", modified_time)
        if modifiedby and not isinstance(modifiedby, str):
            raise TypeError("Expected argument 'modifiedby' to be a str")
        pulumi.set(__self__, "modifiedby", modifiedby)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        pulumi.set(__self__, "platform", platform)
        if previous_version and not isinstance(previous_version, str):
            raise TypeError("Expected argument 'previous_version' to be a str")
        pulumi.set(__self__, "previous_version", previous_version)
        if private_ip and not isinstance(private_ip, str):
            raise TypeError("Expected argument 'private_ip' to be a str")
        pulumi.set(__self__, "private_ip", private_ip)
        if provisioning_key_id and not isinstance(provisioning_key_id, str):
            raise TypeError("Expected argument 'provisioning_key_id' to be a str")
        pulumi.set(__self__, "provisioning_key_id", provisioning_key_id)
        if provisioning_key_name and not isinstance(provisioning_key_name, str):
            raise TypeError("Expected argument 'provisioning_key_name' to be a str")
        pulumi.set(__self__, "provisioning_key_name", provisioning_key_name)
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        pulumi.set(__self__, "public_ip", public_ip)
        if publish_ips and not isinstance(publish_ips, str):
            raise TypeError("Expected argument 'publish_ips' to be a str")
        pulumi.set(__self__, "publish_ips", publish_ips)
        if sarge_version and not isinstance(sarge_version, str):
            raise TypeError("Expected argument 'sarge_version' to be a str")
        pulumi.set(__self__, "sarge_version", sarge_version)
        if service_edge_group_id and not isinstance(service_edge_group_id, str):
            raise TypeError("Expected argument 'service_edge_group_id' to be a str")
        pulumi.set(__self__, "service_edge_group_id", service_edge_group_id)
        if service_edge_group_name and not isinstance(service_edge_group_name, str):
            raise TypeError("Expected argument 'service_edge_group_name' to be a str")
        pulumi.set(__self__, "service_edge_group_name", service_edge_group_name)
        if upgrade_attempt and not isinstance(upgrade_attempt, str):
            raise TypeError("Expected argument 'upgrade_attempt' to be a str")
        pulumi.set(__self__, "upgrade_attempt", upgrade_attempt)
        if upgrade_status and not isinstance(upgrade_status, str):
            raise TypeError("Expected argument 'upgrade_status' to be a str")
        pulumi.set(__self__, "upgrade_status", upgrade_status)

    @property
    @pulumi.getter(name="applicationStartTime")
    def application_start_time(self) -> str:
        return pulumi.get(self, "application_start_time")

    @property
    @pulumi.getter(name="controlChannelStatus")
    def control_channel_status(self) -> str:
        return pulumi.get(self, "control_channel_status")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="ctrlBrokerName")
    def ctrl_broker_name(self) -> str:
        return pulumi.get(self, "ctrl_broker_name")

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> str:
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="enrollmentCert")
    def enrollment_cert(self) -> Mapping[str, Any]:
        return pulumi.get(self, "enrollment_cert")

    @property
    @pulumi.getter(name="expectedUpgradeTime")
    def expected_upgrade_time(self) -> str:
        return pulumi.get(self, "expected_upgrade_time")

    @property
    @pulumi.getter(name="expectedVersion")
    def expected_version(self) -> str:
        return pulumi.get(self, "expected_version")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAcl")
    def ip_acl(self) -> str:
        return pulumi.get(self, "ip_acl")

    @property
    @pulumi.getter(name="issuedCertId")
    def issued_cert_id(self) -> str:
        return pulumi.get(self, "issued_cert_id")

    @property
    @pulumi.getter(name="lastBrokerConnectTime")
    def last_broker_connect_time(self) -> str:
        return pulumi.get(self, "last_broker_connect_time")

    @property
    @pulumi.getter(name="lastBrokerConnectTimeDuration")
    def last_broker_connect_time_duration(self) -> str:
        return pulumi.get(self, "last_broker_connect_time_duration")

    @property
    @pulumi.getter(name="lastBrokerDisconnectTime")
    def last_broker_disconnect_time(self) -> str:
        return pulumi.get(self, "last_broker_disconnect_time")

    @property
    @pulumi.getter(name="lastBrokerDisconnectTimeDuration")
    def last_broker_disconnect_time_duration(self) -> str:
        return pulumi.get(self, "last_broker_disconnect_time_duration")

    @property
    @pulumi.getter(name="lastUpgradeTime")
    def last_upgrade_time(self) -> str:
        return pulumi.get(self, "last_upgrade_time")

    @property
    @pulumi.getter
    def latitude(self) -> str:
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter(name="listenIps")
    def listen_ips(self) -> str:
        return pulumi.get(self, "listen_ips")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def longitude(self) -> str:
        return pulumi.get(self, "longitude")

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
    @pulumi.getter
    def platform(self) -> str:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="previousVersion")
    def previous_version(self) -> str:
        return pulumi.get(self, "previous_version")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="provisioningKeyId")
    def provisioning_key_id(self) -> str:
        return pulumi.get(self, "provisioning_key_id")

    @property
    @pulumi.getter(name="provisioningKeyName")
    def provisioning_key_name(self) -> str:
        return pulumi.get(self, "provisioning_key_name")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="publishIps")
    def publish_ips(self) -> str:
        return pulumi.get(self, "publish_ips")

    @property
    @pulumi.getter(name="sargeVersion")
    def sarge_version(self) -> str:
        return pulumi.get(self, "sarge_version")

    @property
    @pulumi.getter(name="serviceEdgeGroupId")
    def service_edge_group_id(self) -> str:
        return pulumi.get(self, "service_edge_group_id")

    @property
    @pulumi.getter(name="serviceEdgeGroupName")
    def service_edge_group_name(self) -> str:
        return pulumi.get(self, "service_edge_group_name")

    @property
    @pulumi.getter(name="upgradeAttempt")
    def upgrade_attempt(self) -> str:
        return pulumi.get(self, "upgrade_attempt")

    @property
    @pulumi.getter(name="upgradeStatus")
    def upgrade_status(self) -> str:
        return pulumi.get(self, "upgrade_status")


class AwaitableGetZPAServiceEdgeControllerResult(GetZPAServiceEdgeControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZPAServiceEdgeControllerResult(
            application_start_time=self.application_start_time,
            control_channel_status=self.control_channel_status,
            creation_time=self.creation_time,
            ctrl_broker_name=self.ctrl_broker_name,
            current_version=self.current_version,
            description=self.description,
            enabled=self.enabled,
            enrollment_cert=self.enrollment_cert,
            expected_upgrade_time=self.expected_upgrade_time,
            expected_version=self.expected_version,
            fingerprint=self.fingerprint,
            id=self.id,
            ip_acl=self.ip_acl,
            issued_cert_id=self.issued_cert_id,
            last_broker_connect_time=self.last_broker_connect_time,
            last_broker_connect_time_duration=self.last_broker_connect_time_duration,
            last_broker_disconnect_time=self.last_broker_disconnect_time,
            last_broker_disconnect_time_duration=self.last_broker_disconnect_time_duration,
            last_upgrade_time=self.last_upgrade_time,
            latitude=self.latitude,
            listen_ips=self.listen_ips,
            location=self.location,
            longitude=self.longitude,
            modified_time=self.modified_time,
            modifiedby=self.modifiedby,
            name=self.name,
            platform=self.platform,
            previous_version=self.previous_version,
            private_ip=self.private_ip,
            provisioning_key_id=self.provisioning_key_id,
            provisioning_key_name=self.provisioning_key_name,
            public_ip=self.public_ip,
            publish_ips=self.publish_ips,
            sarge_version=self.sarge_version,
            service_edge_group_id=self.service_edge_group_id,
            service_edge_group_name=self.service_edge_group_name,
            upgrade_attempt=self.upgrade_attempt,
            upgrade_status=self.upgrade_status)


def get_zpa_service_edge_controller(name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZPAServiceEdgeControllerResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('zpa:index/getZPAServiceEdgeController:getZPAServiceEdgeController', __args__, opts=opts, typ=GetZPAServiceEdgeControllerResult).value

    return AwaitableGetZPAServiceEdgeControllerResult(
        application_start_time=__ret__.application_start_time,
        control_channel_status=__ret__.control_channel_status,
        creation_time=__ret__.creation_time,
        ctrl_broker_name=__ret__.ctrl_broker_name,
        current_version=__ret__.current_version,
        description=__ret__.description,
        enabled=__ret__.enabled,
        enrollment_cert=__ret__.enrollment_cert,
        expected_upgrade_time=__ret__.expected_upgrade_time,
        expected_version=__ret__.expected_version,
        fingerprint=__ret__.fingerprint,
        id=__ret__.id,
        ip_acl=__ret__.ip_acl,
        issued_cert_id=__ret__.issued_cert_id,
        last_broker_connect_time=__ret__.last_broker_connect_time,
        last_broker_connect_time_duration=__ret__.last_broker_connect_time_duration,
        last_broker_disconnect_time=__ret__.last_broker_disconnect_time,
        last_broker_disconnect_time_duration=__ret__.last_broker_disconnect_time_duration,
        last_upgrade_time=__ret__.last_upgrade_time,
        latitude=__ret__.latitude,
        listen_ips=__ret__.listen_ips,
        location=__ret__.location,
        longitude=__ret__.longitude,
        modified_time=__ret__.modified_time,
        modifiedby=__ret__.modifiedby,
        name=__ret__.name,
        platform=__ret__.platform,
        previous_version=__ret__.previous_version,
        private_ip=__ret__.private_ip,
        provisioning_key_id=__ret__.provisioning_key_id,
        provisioning_key_name=__ret__.provisioning_key_name,
        public_ip=__ret__.public_ip,
        publish_ips=__ret__.publish_ips,
        sarge_version=__ret__.sarge_version,
        service_edge_group_id=__ret__.service_edge_group_id,
        service_edge_group_name=__ret__.service_edge_group_name,
        upgrade_attempt=__ret__.upgrade_attempt,
        upgrade_status=__ret__.upgrade_status)


@_utilities.lift_output_func(get_zpa_service_edge_controller)
def get_zpa_service_edge_controller_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZPAServiceEdgeControllerResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
