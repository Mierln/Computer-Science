
# Parallels Arrays
fire_station = ["ALPHA", "BETA", "THETA","CENTER", "RAILWAY", "HARBOR", "SUBURB"]
personnel = [12, 13, 23, 44, 23, 11, 43]

# Cloning the fire stations
fire_duty = fire_station

# Finding the understaffed station
min = personnel[0]
for m in range(7):
    if min >= personnel[m]:
        min = personnel[m]
        understaffed = fire_station[m]

# Main Loop
i = 0
loop = 0

# 1 year = 52 weeks
while i < 52:

    # Mayor's input
    input_device = input("true / false: ")

    # Input is true
    if input_device == "true":

        # Pick the station
        station_on_duty = fire_duty[loop]

        if station_on_duty == understaffed:             # Check if it is understaffed
            print("this station is understaffed")       # If understaffed print "Station is Understaffed"
        print(station_on_duty)                          # Printing the station on duty
        loop += 1                                       # Prepare for next week

        if loop >= 7: loop = 0                          # Resets if there are no more stations left

    elif input_device == "false":                       # If mayors input is false
        i = 53                                          # Make i = 53 to end the loop
        print("Emergency stop of procedure")

    i += 1
