
CODE_TO_NAME = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
                "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                "azure1": "	#f0ffff"}
QUIT = ""

hex_colour_code = input("Please enter colour code name\n").lower()

while hex_colour_code != QUIT:
    if hex_colour_code in CODE_TO_NAME:
        print("{:13} is {}".format(hex_colour_code, CODE_TO_NAME[hex_colour_code]))
    else:
        print("Invalid code name, try again")
    hex_colour_code = input("Please enter colour code name\n").lower()

print("You elected to quit, goodbye.")
