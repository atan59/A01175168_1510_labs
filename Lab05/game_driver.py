"""Short program demonstrating functions from function.py."""
import Lab05.lab05


def main():
    # Welcome message
    print("*~~~~~~~~~~Welcome to the Demo!~~~~~~~~~~*")
    # Demo roll_dice
    die_roll = str(Lab05.lab05.roll_die(3, 6))
    print("\nHere's the \'roll_die\' function:" + "\n" +
          "For example, you want to roll a six-sided die three times." + "\n" +
          "Call the function: roll_die(3, 6)" + "\n" +
          "Output: " + die_roll + "\n" +
          "This means that the total number after rolling a six-sided die three times is equal to " +
          die_roll + ".")
    # Demo choose_inventory
    inventory_choices = str(Lab05.lab05.choose_inventory(['Sword', 'Shield', 'Bow'], 2))
    print("\nHere's the \'choose_inventory\' function:" + "\n" +
          "For example, you want to select two items from a list with a sword, a shield, and a bow." + "\n" +
          "Call the function: choose_inventory([\'Sword\', \'Shield\', \'Bow\'], 2)" + "\n" +
          "Output: " + inventory_choices + "\n" +
          "This means you have chosen the two items listed above from the inventory.")
    # Demo generate_vowel
    vowel = Lab05.lab05.generate_vowel()
    print("\nHere's the \'generate_vowel\' function:" + "\n" +
          "For example, you want to generate a vowel." + "\n" +
          "Call the function: generate_vowel()" + "\n" +
          "Output: " + vowel + "\n" +
          "This means you have generated " + vowel + ".")
    # Demo generate_consonant
    consonant = Lab05.lab05.generate_consonant()
    print("\nHere's the \'generate_consonant\' function:" + "\n" +
          "For example, you want to generate a vowel." + "\n" +
          "Call the function: generate_consonant()" + "\n" +
          "Output: " + consonant + "\n" +
          "This means you have generated " + consonant + ".")
    # Demo generate_name
    name = Lab05.lab05.generate_name(3)
    print("\nHere's the \'generate_name\' function:" + "\n" +
          "For example, you want to generate a name with three syllables." + "\n" +
          "Call the function: generate_name(3)" + "\n" +
          "Output: " + name + "\n" +
          "This means you have generated " + name + ".")
    # Demo create_character
    character = Lab05.lab05.create_character(3)
    print("\nHere's the \'create_character\' function:" + "\n" +
          "For example, you want to create a character with a name with three syllables." + "\n" +
          "Call the function: create_character(3)" + "\n" +
          "Output: " + str(character) + "\n" +
          "This means you have created a character with the name and attributes listed above.")
    # Demo print_character
    print("\nHere's the \'print_character\' function:" + "\n" +
          "For example, you want to print out the information about the character we created above." + "\n" +
          "Call the function: print_character(character)" + "\n" +
          "Output: ")
    Lab05.lab05.print_character(character)
    print("\nThis prints out the character information.")
    # Bonus
    

if __name__ == "__main__":
    main()
