fire_stations = ["Alpha", "Beta", "Theta",
                 "Center", "Railway", "Harbor", "Suburb"]
personnel = [12,13,23,44,23,11,42]
fire_duty = []
station_on_duty = ""
m = 0
min = personnel[0]
understaffed = ""
input_device = ""

for i in range(7):
    fire_duty.append(fire_stations[i])

for m in range(7):
    if min >= personnel[m]:
        min = personnel[m]
        understaffed = fire_stations[m]
i = 0
while i < 52:
    input_device = input("Input true or false: ")
    if input_device == "true":
        if fire_duty:
            station_on_duty = fire_duty[m]
            if station_on_duty == understaffed:
                print("This station is understaffed")
            print(station_on_duty)
        else:
            fire_duty
            station_on_duty = fire_duty[m]
            if station_on_duty == understaffed:
                print("This station is understaffed")
            print(station_on_duty)
    elif input_device == "false":
        i = 53
        print("Emergency stop of procedure")
    i += 1

