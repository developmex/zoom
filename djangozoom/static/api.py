from __future__ import absolute_import
import json

from zoomus import ZoomClient


api_key="g7MZBr7GT3CdFn07F1F2Bw"
api_secret="jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y"
data_type="JSON"
host_id="7pCPQl2tSC-S9QoSbZ3RHA"
page_size=30
page_number=1

client = ZoomClient('g7MZBr7GT3CdFn07F1F2Bw','jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y')

for user in json.loads(client.user.list().content)['users']:
    user_id = user['id']

    print client.meeting.list(host_id=user_id)


