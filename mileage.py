# function that prompts user in the command line
print("How many kilometers did you run today?")
kms = input()
# kms is a string when it comes directly from the input
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"{kms} kilometers is equal to {miles} miles.")
