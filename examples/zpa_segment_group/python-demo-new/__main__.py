"""A Python Pulumi program"""

import pulumi

import willguibr_zpa as zpa

segmentgroup = zpa.ZPASegmentGroup("example-user",
    name="test-pulumi-python",
    description="test-pulumi-python",
    enabled=True,
    policy_migrated=True,
    tcp_keep_alive_enabled=True,
)