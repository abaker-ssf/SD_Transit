"""
Script is responsible for monitoring and fetching data from the GTFS-realtime feed of MTS San Diego. 
It's importing a protocol buffer language API. I had to compile this api using a special protobuf
compiler google invited. Finally, when this script receives a the feed it begins to parse it and store the
results of the parse into the database.

Author: Alexander Baker
Date: 05/03/2017
"""
from protobuf_to_dict import protobuf_to_dict
import gtfs_rt_pb2 as gtfs_rt
import pandas as pd
from pandas.io.json import json_normalize
import requests

# First script written only works with files.
# f = open('MTS (1).pb', 'rb')
# raw_str = f.read()
#
# msg = gtfs_rt.FeedMessage()
# msg.ParseFromString(raw_str)
#
# # currently working on processing the gtfs rt feed into the correct format.
# print(msg)

feed = gtfs_rt.FeedMessage()
response = requests.get('https://realtime.sdmts.com/api/api/gtfs_realtime/vehicle-positions-for-agency/MTS.pb?key=d6d8bc59-5bd6-4160-acea-2965f2cb48b0')
feed.ParseFromString(response.content)

feed_dict = protobuf_to_dict(feed)
"""
    This is a test run for vehicle position only 
    
    {'id': '1', 
    'vehicle': {
        'trip': {'trip_id': '11975233', 'route_id': '41'}, 
        'timestamp': 1493839585, 
        'vehicle': {'id': '911'}, 
        'position': {'latitude': 32.86729049682617, 'longitude': -117.21359252929688}
        }
    }
    
    {
     'id': '1', 
     'vehicle': {
        'trip': {'trip_id': '11975234', 'route_id': '41'}, 
        'timestamp': 1493840910, 
        'position': {'longitude': -117.23302459716797, 'latitude': 32.87479782104492}, 
        'vehicle': {'id': '911'}
        }
    }

    
"""
print(sorted(feed_dict['entity'].iteritems(), key=lambda (k,v): (v,k)))


# proc_dict = json_normalize(feed_dict['entity'], 'id', 'vehicle')
# print(proc_dict)

# for entity in feed_dict['entity']:
#     print("Raw Entity Object from the RTFS-RT feed: ")
#     print(entity)
#
#     for key in entity[vehicle]:
#
#     proc_dict[entity['id']] = {
#         'trip_id': entity['vehicle']['trip']['trip_id'],
#         'route_id': entity['vehicle']['trip']['route_id'],
#         'timestap': entity['vehicle']['timestamp'],
#         'vehicle_id': entity['vehicle']['vehicle']['id'],
#         'latitude': entity['vehicle']['position']['latitude'],
#         'longitude': entity['vehicle']['position']['longitude']
#     }
#     # if entity.HasField('trip_update'):
#     #     print(entity.trip_update)


# print("\nNewly Processed Object for pandas manipulation: ")
# print(proc_dict)