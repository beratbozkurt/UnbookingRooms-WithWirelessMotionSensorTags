import wirelesstagpy
import wirelesstagpy.constants as CONST

api = wirelesstagpy.WirelessTags(
    username="berat.bozkurt@cloudica.io", password="*****"
)

tags = api.load_tags()

# get temperature sensor value for tag
for (uuid, tag) in tags.items():
    sensor = tag.sensor[CONST.SENSOR_TEMPERATURE]
    if sensor is not None:
        print("{} temperature: {}".format(tag.name, sensor.value))

for (uuid, tag) in tags.items():
    if CONST.EVENT_MOTION in tag.supported_binary_events_types:
        event = tag.event[CONST.EVENT_MOTION]
        print(event)
        print("tag {} event state: {}".format(tag.name, event.is_state_on))
