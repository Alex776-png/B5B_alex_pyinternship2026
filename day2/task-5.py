height_cm = "175"
weight_kg = "68.5"

height_m=int(height_cm)/100
weight_kg=float(weight_kg)

BMI=weight_kg/(height_m*height_m)

print(BMI)