# Solution to http://programmingpraxis.com/2013/08/30/bmi-calculator/


def bmi_metric(w_kg, h_m):
    return float(w_kg) / (h_m * h_m)


def bmi_imperial(w_pound, h_inch):
    return float(w_pound) / (h_inch * h_inch) * 703


if __name__ == '__main__':
    print(bmi_metric(95, 1.9))
    print(bmi_imperial(125, 64))