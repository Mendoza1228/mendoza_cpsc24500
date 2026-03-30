from datetime import datetime

name = input("Enter your name:")
major = input("Enter your major")
today = datetime.now() .strftime ("%B %d, %Y")


print()
print("=" * 40)
print(f" Welcome , {name}!")
print(f" Major: {major}")
print(f" Date:  {today}")
print("=" * 40)
