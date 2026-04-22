from cat import Cat
from dog import Dog
from fish import Fish


def main():
    pets = []

    while True:
        print("\n---Pet Simulator---")
        print("1. Add a new pet")
        print("2. Feed a pet")
        print("3. Play with a pet")
        print("4. Put a pet to sleep")
        print("5. View all pets")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pet_type = input("Enter pet type (cat/dog/fish): ").lower()
            name = input("Enter pet name: ")

            if pet_type == 'cat':
                pets.append(Cat(name))
            elif pet_type == 'dog':
                breed = input("Enter breed: ")
                pets.append(Dog(name, breed))
            elif pet_type == 'fish':
                species = input("Enter fish species: ")
                pets.append(Fish(name, species))
            else:
                print("Invalid pet type. Please try again.")

        elif choice in ["2", "3", "4", "5"]:
            if not pets:
                print("No pets to interact with. Please add a pet first.")
                continue

            if choice == "5":
                for i, pet in enumerate(pets, start=1):
                    print(f"{i}. {pet._name} ({pet.__class__.__name__})")
                continue

            for i, pet in enumerate(pets):
                print(f"{i}. {pet._name} ({pet.__class__.__name__})")

            index = int(input("Select a pet by index:"))
        
            target = pets[index]

            if choice == '2':
                target.feed()
            elif choice == '3':
                target.play()
            elif choice == '4':
                target.sleep()

        elif choice == '6':
            print("Exiting the simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()
