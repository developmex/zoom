import json
import urllib2

api_key="g7MZBr7GT3CdFn07F1F2Bw"
api_secret="jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y"
data_type="JSON"
host_id="7pCPQl2tSC-S9QoSbZ3RHA"
page_size=30
page_number=1

data = json.load(urllib2.urlopen('https://api.zoom.us/developer/v1/meeting/list'+ api_key + api_secret))

