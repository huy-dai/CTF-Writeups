import uuid
import time_uuid
import datetime

my_uuid = uuid.UUID('{53f56307-b6bf-11d0-94f2-00a0c91efb8b}')
ts = time_uuid.TimeUUID(bytes=my_uuid.bytes)

print(type(ts))
print(datetime.datetime.fromtimestamp(((ts.time - 0x01b21dd213814000)*100/1e9)))