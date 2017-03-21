

"""


"""


def value_gen(row_name="E6", power_min=0.1, power_max=1000000):
    """

    """
    rows = {}
    rows["E3"] = (1.0,2.2,4.7)
    rows["E6"] = (1.0,1.5,2.2,3.3,4.7,6.8)
    mants = tuple(rows[row_name])

    powers = ()
    power = power_min
    while True:
        powers = powers + (power,)
        power *= 10.0
        if power > power_max:
            break

    for mant in mants:
        for power in powers:
            yield float(mant)*float(power)


def gain_r1_r2(r1, r2):
    return r2 / (r1+r2)

def gain_r1_r21_r22(r1, r21, r22):
    r2 = 1/(1/r21+1/r22)
    return r2 / (r1+r2)

def gain_r11_r12_r2(r11, r12, r2):
    r1 = 1/(1/r11+1/r12)
    return r2 / (r1+r2)

def normalize(r):
    if r == round(r):
        return int(round(r))
    else:
        return r

def power_r1_r2(voltage, r1, r2):
    return voltage**2 / (r1+r2)

def power_r1_r21_r22(voltage, r1, r21, r22):
    r2 = 1/(1/r21+1/r22)
    return voltage**2 / (r1+r2)

def power_r11_r12_r2(voltage, r11, r12, r2):
    r1 = 1/(1/r11+1/r12)
    return voltage**2 / (r1+r2)




if __name__ == "__main__":
    print("main start")
    r_gen = value_gen("E6", 100, 100000)
    print(list(r_gen))
    assert gain_r1_r2(1000, 3000) == 0.75
    assert gain_r1_r2(3000, 1000) == 0.25
    assert gain_r1_r21_r22(1500,1000,1000) == 0.25
    assert gain_r11_r12_r2(3000,3000,500) == 0.25
    assert normalize(1000.0) == 1000
    assert normalize(0.1) == 0.1
    assert power_r1_r2(10,0.1,0.1) == 500
    print("main done")
