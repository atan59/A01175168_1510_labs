"""Short program demonstrating functions from function.py."""
import Lab05.lab05


def main():
    # Welcome message
    print("*~~~~~~~~~~Welcome to the Demo!~~~~~~~~~~*")

    # Demo roll_dice
    print("\n*~~~~~~~~~~~~~~Rolling a Die~~~~~~~~~~~~~~*")

    number_of_rolls = input("Input times you will roll: ")
    number_of_sides = input("Input number of sides on die: ")
    die_rolls = str(Lab05.lab05.roll_die(int(number_of_rolls), int(number_of_sides)))

    print("\nHere's the \'roll_die\' function:" + "\n" +
          "You want to roll a " + number_of_rolls + "-sided die " + number_of_sides + " times." + "\n" +
          "Call the function: roll_die(" + number_of_rolls + ", " + number_of_sides + ")" + "\n" +
          "Output: " + die_rolls + "\n" +
          "This means that the total number after rolling a " + number_of_sides + "-sided die " + number_of_rolls +
          " times is equal to " + die_rolls + ".")

    # Demo choose_inventory
    print("\n*~~~~~~~Choosing Items From an Inventory~~~~~~~*")

    number_of_items = input("Input number of items you want: ")
    inventory_choices = str(Lab05.lab05.choose_inventory(['Sword', 'Shield', 'Bow'], int(number_of_items)))

    print("\nHere's the \'choose_inventory\' function:" + "\n" +
          "You want to select " + number_of_items + " items from a list with a sword, a shield, and a bow." + "\n" +
          "Call the function: choose_inventory([\'Sword\', \'Shield\', \'Bow\'], " + number_of_items + ")" + "\n" +
          "Output: " + inventory_choices + "\n" +
          "This means you have chosen the " + number_of_items + " items listed above from the inventory.")

    # Demo generate_vowel
    print("\n*~~~~~~~~~~~Generating a Random Vowel~~~~~~~~~~~*")

    vowel = Lab05.lab05.generate_vowel()

    print("\nHere's the \'generate_vowel\' function:" + "\n" +
          "You want to generate a vowel." + "\n" +
          "Call the function: generate_vowel()" + "\n" +
          "Output: " + vowel + "\n" +
          "This means you have generated " + vowel + ".")

    # Demo generate_consonant
    print("\n*~~~~~~~~~Generating a Random Consonant~~~~~~~~~*")

    consonant = Lab05.lab05.generate_consonant()

    print("\nHere's the \'generate_consonant\' function:" + "\n" +
          "You want to generate a vowel." + "\n" +
          "Call the function: generate_consonant()" + "\n" +
          "Output: " + consonant + "\n" +
          "This means you have generated " + consonant + ".")

    # Demo generate_name
    print("\n*~~~~~~~~~~~Generating a Random Name~~~~~~~~~~~*")

    syllable = input("Input how many syllables do you want in your name: ")
    name = Lab05.lab05.generate_name(int(syllable))

    print("\nHere's the \'generate_name\' function:" + "\n" +
          "You want to generate a name with " + syllable + " syllables." + "\n" +
          "Call the function: generate_name(" + syllable + ")" + "\n" +
          "Output: " + name + "\n" +
          "This means you have generated " + name + ".")

    # Demo create_character
    print("\n*~~~~~~~~~~~Creating a Character~~~~~~~~~~~*")

    name_length = input("Input how long you want your name to be: ")
    character = Lab05.lab05.create_character(int(name_length))

    print("\nHere's the \'create_character\' function:" + "\n" +
          "For example, you want to create a character with a name with " + name_length + " syllables." + "\n" +
          "Call the function: create_character(" + name_length + ")" + "\n" +
          "Output: " + str(character) + "\n" +
          "This means you have created a character with the name and attributes listed above.")
    
    # Demo print_character
    print("\n*~~~~~~~~~~~Printing Character Information~~~~~~~~~~~*")
    print("\nHere's the \'print_character\' function:" + "\n" +
          "For example, you want to print out the information about the character we created above." + "\n" +
          "Call the function: print_character(character)" + "\n" +
          "Output: " + "\n")
    Lab05.lab05.print_character(character)
    print("\nThis prints out the character information.")
    # Bonus


if __name__ == "__main__":
    main()
