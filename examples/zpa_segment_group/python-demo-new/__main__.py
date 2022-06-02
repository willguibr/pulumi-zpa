"""A Python Pulumi program"""

import pulumi
import willguibr_zpa as zpa

segmentgroup = zpa.ZPASegmentGroup("segmentgroup",
  name="pulumi-test",
  description="pulumi-test",
  enabled=True,
  policy_migrated=True,
  tcp_keep_alive_enabled=True
)

applicationServer01 = zpa.ZPAApplicationServer("appServer01",
  name="pulumi-test01",
  description="pulumi-test01",
  enabled=True,
  address="pulumi01.acme.com"
)

applicationServer02 = zpa.ZPAApplicationServer("appServer02",
  name="pulumi-test02",
  description="pulumi-test02",
  enabled=True,
  address="pulumi02.acme.com"
)

applicationServer03 = zpa.ZPAApplicationServer("appServer03",
  name="pulumi-test03",
  description="pulumi-test03",
  enabled=True,
  address="pulumi03.acme.com"
)

applicationServer04 = zpa.ZPAApplicationServer("appServer04",
  name="pulumi-test04",
  description="pulumi-test04",
  enabled=True,
  address="pulumi04.acme.com"
)