
guesses = 0;
correct_chars = [];
wrong_chars = [];

print("Choose a word to guess");
word = input();
word = word.lower();


def print_guessed(word,correct_chars,wrong_chars):
    for char in word:
        if (char in correct_chars):
            if(char == word[0]):
                print(char.upper(), end=" ");
            else:
                print(char, end=" ");
        else:
            print("_ ", end="");

while (guesses < 8):
    print("\nGuess a character from the word");
    guessed_char = input();
    guessed_char = guessed_char.lower();
    if (len(guessed_char) < 2):
        if (guessed_char in word):
            if (guessed_char not in correct_chars):
                correct_chars.append(guessed_char);
                print("Correct!");
        elif (guessed_char not in word):
            if (guessed_char not in wrong_chars):
                wrong_chars.append(guessed_char);
                guesses = guesses + 1;
                print(guessed_char, "isnt in the word, you have: ", 8 - guesses, "left");
    if (len(correct_chars) == len(word)):
        print("You WON!");

    print_guessed(word,correct_chars,wrong_chars);

if (guesses == 8):
    print("You lost, the word was: ", word);





