body_weight = float(input("Please enter weight in lbs: "))
body_height = float(input("Please enter hieght in inches: "))

body_weight_metric = body_weight * 0.453592
body_height_metric = body_height /12 * 0.3048

def bmi(weight, height):
    return weight / height ** 2


num = (bmi(body_weight_metric, body_height_metric))
print(round(num, 2))