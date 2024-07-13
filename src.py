import random
from collections import Counter

words = ['apple', 'pineapple', 'watermelon', 'lemon', 'grapes', 'orange']

word = random.choice(words)

if __name__ == "__main__":
    print("___ HANGMAN ___")
    print("Guess the word....")
    print("Hint! The word is name of the fruit")
    
    for i in word:
        print("_", end = " ")
    print()    
    
    letterguessed = " "
    chances = len(word)+2
    flag = 0
    try:
        while chances!=0 and flag ==0:
            
            print("Available Chances: ", chances)
            
            try:
                guess = str(input("Enter a letter to guess the word: "))
            except:
                print("Enter only one letter.")
                continue
            
            if not guess.isalpha():
                print("Enter only a letter")
                continue
            elif len(guess)>1:
                print("Enter only a single letter")
                continue
            elif guess in letterguessed:
                print("You already guessed this letter")
                continue
            
            if guess in word:
                k = word.count(guess)
                
                for _ in range(k):
                    letterguessed += guess
            else:
                chances -= 1
                    
            for char in word:
                if char in letterguessed and Counter(letterguessed) != Counter(word):
                    print(char, end=" ")
                    # correct += 1
                    
                elif Counter(letterguessed) == Counter(word):
                    print("The word is:", end =" ")
                    print(word)
                    flag = 1
                    print("Congratulation you guessed the word correctly.")
                else:
                    print("_", end=" ")
            
            if chances<=0 and Counter(letterguessed) != Counter(word): 
                print()
                print("You are out of the chances and loss the game")
                print("The word if {}".format(word))
            
    except KeyboardInterrupt:
        print()
        print("Bye! and try again")
        exit()