
import random



print()
print("*" * 80)
print(f"{'WELCOME TO THE FORTUNE TELLER APP!':^80}")
print(f"{'This app will predict your future based on your name and birth month.':^80}")
print("*" * 80)

#Function to get validated age input from the user
def get_validated_age():
    while True:
        try:
            age_input = int(input("Enter your age: "))
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
        

#Function to determine fortune category based on lucky number
def generate_fortune_category(lucky_number, favorite_color):
    if 1 <= lucky_number <= 3:
        category = "Patience and Perseverance"
    elif 4 <= lucky_number <= 6:
        category = "Adventure and New Experiences"
    else:
        category = "Prosperity and Success"
    return f"{favorite_color} {category}"

    
#Function to save results to a file
    
def save_fortune_to_file(name, age, color, lucky_number, category, fortune):
    try:
        with open("fortune_output.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Favorite Color: {color}\n")
            file.write(f"Lucky Number: {lucky_number}\n")
            file.write(f"Fortune Category: {category}\n")
            file.write(f"Fortune: {fortune}\n")
            
        #print("\nYour fortune has been saved to fortune_output.txt")
    except IOError as e:
        print(f"Error saving fortune to file: {e}")

#Main function to run the fortune teller app
def main():

    #collect user input
    full_name = input("Enter your full name: ")
    age = get_validated_age()
    favorite_color = input("Enter your favorite color: ")

    #Generate a lucky number 
    lucky_number = random.randint(1, 10)

    #Determine fortune category based on lucky number
    fortune_category = generate_fortune_category(lucky_number, favorite_color)

    #Select a fortune based on the category
    fortunes = [
        "Your aura will attract positive energy and new opportunities.",
        "A surprise encounter will lead to a valuable friendship.",
        "Your hard work will soon pay off with a significant reward.",
        "Embrace the vibes and let them guide you to exciting adventures.",
        "A new opportunity will arise that will challenge you in a positive way.",
        "Your perseverance will lead to a breakthrough in your personal or professional life.",
        "The energy will bring you clarity and insight in a difficult situation.",
        "A financial opportunity will present itself, but be cautious and do your research.",
        "Your creativity will flourish, leading to a new project or hobby that brings you joy.",
        "A positive change is on the horizon, and it will bring you happiness and fulfillment."

    ]

    #Simple fortune selection 
    selected_fortune = random.choice(fortunes)
    

    #Display the fortune to the user
    print("\n" + "*" * 80)
    print("YOUR FORTUNE".center(80))
    print("*" * 80)
    print(f"Name: {full_name.upper()}")
    print(f"Name character count: {len(full_name.strip())}")
    print(f"Age: {age}")
    print(f"Favorite Color: {favorite_color.lower()}")
    print(f"Lucky Number: {lucky_number}")
    print(f"Fortune Category: {fortune_category}")

    #Calculate and format lucky porcentage
    lucky_percentage = (lucky_number / age) * 100
    print(f"Your Lucky Percentage: ${lucky_percentage:.3f}$%")
    print(f"Your Fortune: {selected_fortune}")
    print("*" * 80)
   

    #Save results to a file
    save_fortune_to_file(full_name, age, favorite_color, lucky_number, fortune_category, selected_fortune)
    print("Fortune saved to 'fortune_output.txt'.")

    #Farewell message
    print(f"\nGoodbye {full_name.split()[0]}! May the fortune smile upon you.")
    print("*" * 80)
if __name__ == "__main__":
    main()