
fire_station = ["ALPHA", "BETA", "THETA","CENTER", "RAILWAY", "HARBOR", "SUBURB"]
personnel = [2, 13, 23, 44, 23, 11, 43]
fire_duty = []
station_on_duty = ""
min = personnel[0]
understaffed = ""
input_device = ""
csgo = 0

for i in range(7):
    fire_duty.append(fire_station[i])

for m in range(7):
    if min >= personnel[m]:
        min = personnel[m]
        understaffed = fire_station[m]

i = 0
while i < 52:
    input_device = input("true / false: ")
    if input_device == "true":
        if csgo < 7:
            station_on_duty = fire_duty[csgo]
            if station_on_duty == understaffed:
                print("this station is understaffed")
            print(station_on_duty)
            csgo += 1
        else:
            csgo = 0
            station_on_duty = fire_duty[csgo]
            if station_on_duty == understaffed:
                print("this station is understaffed")
            print(station_on_duty)
            csgo += 1

    elif input_device == "false":
        i = 53
        print("Emergency stop of procedure")
    i += 1