import wirelesstagpy
import json

api = wirelesstagpy.WirelessTags(
    username="berat.bozkurt@cloudica.io", password="*****"
)
tags = api.load_tags()

for (uuid, tag) in tags.items():
    print("Motion Number: ", tag.motion_state)
    print("uuid: ", uuid)
    print(
        "Loaded tag: {}, temp: {}, humidity: {} probe taken: {}".format(
            tag.name, tag.temperature, tag.humidity, tag.time_since_last_update
        )
    )
