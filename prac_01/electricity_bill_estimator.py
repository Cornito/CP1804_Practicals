
print("Electricity bill estimator")

TARIFF_11 = 0.244619
TARIFF_31 = 0.136928


#cents_per_kwh = int(input("Enter cents per KWh: "))

def tariff_choice():
    tariff_choice = input("Which tariff? 11 or 31: ")
    if tariff_choice == 11:
        estimated_bill = TARIFF_11 * daily_use_kwh * numberOf_days_billing
    #    estimated_bill /= 100
    elif tariff_choice == 31:
        estimated_bill = TARIFF_31 * daily_use_kwh * numberOf_days_billing
    #    estimated_bill /= 100
    return (estimated_bill);


def main():
    # TODO finish function
    tariff_choice()
    daily_use_kwh = float(input("Enter daily use in KWh: "))
    numberOf_days_billing = int(input("Enter number of billing days: "))


tariff_choice = input("Which tariff? 11 or 31: ")
daily_use_kwh = float(input("Enter daily use in KWh: "))
numberOf_days_billing = int(input("Enter number of billing days: "))

if tariff_choice == 11:
    estimated_bill = TARIFF_11 * daily_use_kwh * numberOf_days_billing
#    estimated_bill /= 100
elif tariff_choice == 31:
    estimated_bill = TARIFF_31 * daily_use_kwh * numberOf_days_billing
#    estimated_bill /= 100
return (estimated_bill);
print("Estimated bill: ${}".format(estimated_bill))
