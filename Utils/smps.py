"""

TODO:
"""

def get_ref_voltage(name):

	smps_ref_voltages = {}
	smps_ref_voltages["LM43603"] = 1.011
	smps_ref_voltages["LTC3124"] = 1.2
	smps_ref_voltages["LTC3127"] = 1.195 #1.165 1.195 1.225
	smps_ref_voltages["LT1372"] = 1.245


	return smps_ref_voltages[name]



if __name__ == "__main__":
    print("main start")
    print(get_ref_voltage("LM43603"))
    print("main done")

