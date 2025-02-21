# Logan H's Kilometer to Miles Program (2/21/25)

# 1st, We use a def function to multiply Kilometers by .6214 to get miles
def km_to_miles(kilometers):
    return kilometers * .6214

# 2nd, We ask for the number of Kilometers
km = float(input("How many Kilometers?: "))

# 3rd, We mash everything up, the number that was inputted goes into the km_to_miles(__),
#      which then goes to the def function to be multiplied by .6214
miles = km_to_miles(km)

# 4th, print the answer.
print(km, "kilometers is:",miles, "miles")
