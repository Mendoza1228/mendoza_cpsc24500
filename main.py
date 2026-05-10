from word_collection import WordCollection
from story_template import TEMPLATES

def main():
    print("=" * 40)
    print("Welcome to StoryTeller")
    print("=" * 40)

    wc = WordCollection()
    wc = WordCollection.from_file("words.txt")
    


    
    if len(wc) == 0:
        print("No words loaded. Exiting.")
        return

    print(f"Loaded {len(wc)} words:")
    pos_counts = {}
    for w in wc:
        pos_counts[w.part_of_speech] = pos_counts.get(w.part_of_speech, 0) + 1
    
    for pos in sorted(pos_counts):
        print(f"{pos} : {pos_counts[pos]}")

    while True:
        print("\nAvailable story styles:")
        for i, temp in enumerate(TEMPLATES, 1):
            print(f"{i}. {temp.name}")

        try:
            choice = int(input("Choose a style: ")) - 1
            num_sentences = int(input("How many sentences? "))
            
            selected_template = TEMPLATES[choice]
            print(f"\n--- {selected_template.name} Story ---")
            
            for _ in range(num_sentences):
                print(selected_template.generate(wc))
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
            continue

        again = input("\nGenerate another story? (yes/no): ").lower()
        if again != 'yes':
            break

    print("Thank you for using StoryTeller!")

if __name__ == "__main__":
    main()