from word_collection import WordCollection
from story_template import TEMPLATES
 


def main():
    print("===========================================")
    print("Welcome to the StoryTeller")
    print("===========================================")


    file_path = input("Enter the path to your word collection file: ")
    words = WordCollection.from_file(file_path)

    

    if len(words) == 0:
        print("No valid words found in the file. Exiting.")
        return
    
    # Display available templates
    print(f"Loaded {len(words)} words:")
    for pos in sorted(list(set(word.part_of_speech for word in words))):
        count = len(words.filter_by_pos(pos))
        print(f"- {pos}: {count}")


    while True:
        print("\nAvailable story templates:")
        for i, template in enumerate(TEMPLATES):
            print(f"{i + 1}. {template.name}")
        
        choice =  int (input("Choose a style : ")) - 1
        num_sentences = int(input("How many sentences to generate? "))

        selected_template = TEMPLATES[choice]
        print(f"---{selected_template.name} Story--- ")
        for _ in range(num_sentences):
            print(selected_template.generate(words))

        if input("Generate another story? (y/n) ").lower() != 'y':
            break

    print("Thank you for using StoryTeller. Goodbye!")


if __name__ == "__main__":
    main()
       
      