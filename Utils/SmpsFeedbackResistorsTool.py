
"""


"""


import resistor
import smps
import itertools

def get_error(voltage, target_voltage):
    return 100.0*abs((voltage-target_voltage)/target_voltage)



SMPS_NAME = "LT1372"
ROW_NAME = "E3"
DECADE_MIN = 1000
DECADE_MAX = 10000
RESULT_COUNT = 20

R1_R2_ENABLE = True
R1_R21_R22_ENABLE = False
R11_R12_R2_ENABLE = False


ref_voltage = smps.get_ref_voltage(SMPS_NAME)
target_voltage = 5.0


print("smps:", SMPS_NAME)
print("ref_voltage:", ref_voltage)
print("target_voltage:", target_voltage)
print()

chains = {}

r1_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
r2_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
for r1 in r1_gen:
    for r2 in r2_gen:
        voltage = ref_voltage / resistor.gain_r1_r2(r1, r2)
        r1, r2 = resistor.normalize(r1), resistor.normalize(r2)
        power = resistor.power_r1_r2(voltage, r1, r2)
        chain_id = ((r1,), (r2,))
        if R1_R2_ENABLE:
            chains[chain_id] = (voltage, get_error(voltage, target_voltage), power)

r1_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
r21_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
r22_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
for r1 in r1_gen:
    for r21 in r21_gen:
        for r22 in r22_gen:
            voltage = ref_voltage / resistor.gain_r1_r21_r22(r1, r21, r22)
            r1, r21, r22 = resistor.normalize(r1), resistor.normalize(r21), resistor.normalize(r22),
            power = resistor.power_r1_r21_r22(voltage, r1, r21, r22)
            if r21 >= r22:
                chain_r2_id = (r21, r22)
            else:
                chain_r2_id = (r22, r21)
            chain_id = ((r1,), chain_r2_id)
            if R1_R21_R22_ENABLE:
                chains[chain_id] = (voltage, get_error(voltage, target_voltage), power)


r11_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
r12_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
r2_gen = list(resistor.value_gen(ROW_NAME, DECADE_MIN, DECADE_MAX))
for r11 in r11_gen:
    for r12 in r12_gen:
        for r2 in r2_gen:
            voltage = ref_voltage / resistor.gain_r11_r12_r2(r1, r21, r22)
            r11, r12, r2 = resistor.normalize(r11), resistor.normalize(r12), resistor.normalize(r2),
            power = resistor.power_r1_r21_r22(voltage, r1, r21, r22)
            if r11 >= r12:
                chain_r1_id = (r11, r12)
            else:
                chain_r1_id = (r12, r11)
            chain_id = (chain_r1_id, (r2,))
            if R11_R12_R2_ENABLE:
                chains[chain_id] = (voltage, get_error(voltage, target_voltage), power)

chains_list = []
for chain_id in chains.keys():
    chain = (chain_id,) + chains[chain_id]
    chains_list.append(chain)

chains_sorted = sorted(chains_list, key=lambda item: item[2])


for i in range(RESULT_COUNT):
    chain = chains_sorted[i]
    print("\t", chain[0], "Ohm     ", "{0:0.2f}V {1:0.2f}% {2:0.0f}mW".format(chain[1], chain[2], 1000*chain[3]))
print()

