# WEIGHT CONVERTER EXERCISE

weight = float(input("Weight: "))
inptu = input("Your Unit: (K)g or (L)bs: ")
cvtu = input("Convert to (K)g or (L)bs: ")

if inptu == "L" and cvtu == "L":
    converted = weight
    print("Weight in Lbs: " + str(converted))
elif inptu == "L" and cvtu == "K":
    converted = weight / 2.205
    print("Weight in Kg: " + str(converted))
elif inptu == "K" and cvtu == "K":
    converted = weight
    print("Weight in Kg:" + str(converted))
elif inptu == "K" and cvtu == "L":
    converted = weight * 2.205
    print("Weight in Lbs:" + str(converted))
print("Done")
