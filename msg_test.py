# Very Simple script to test that specific messages are available in the pymavlink install
from pymavlink.dialects.v20 import ardupilotmega as d

NAME = "MAV_CMD_NAV_WAYPOINT_ARC"
# NAME = "MAV_CMD_NAV_WAYPOINT"

print(NAME, "exists?:", hasattr(d, NAME), "; value:", getattr(d, NAME, None))


cmd_id = d.MAV_CMD_NAV_WAYPOINT_ARC
e = d.enums['MAV_CMD']          # enum table generated from the XML
entry = e[cmd_id]               # lookup by numeric id

print(entry.name)               # e.g. 'MAV_CMD_NAV_WAYPOINT_ARC'
print(getattr(entry, 'description', ''))


