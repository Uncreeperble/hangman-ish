

class Game:
    """
    Hangman Game Paramaters:

    word : The word that the player has to guess

    guessCount : The amount of wrong guesses the player gets

    """
    def __init__(self, word, guessCount):
        self.secret_word = str(word.lower())
        self.guesses = int(guessCount)
        self.guessedLetters = []
        self.guessedWord = ["_" for l in self.secret_word]

        # Allows for spaces in words
        letter = " "
        for x in [int(pos) for pos, char in enumerate(self.secret_word) if char == letter]:
            self.guessedWord[x] = list(self.secret_word)[x]
        
    def check(self):
        # runs checks for gameover
        if self.guesses == 0:
            print("Game Over")
            return True
        if self.guessedWord.count("_") == 0:
            print("You guessed it! ", self.secret_word)
            return True

        
    def update(self):
        # ran each guess to update scores & guess etc.
        if self.check():
            return True
        
        inp = str(input("What Letter? ")).lower()
        if len(inp) > 1:
            print("Doing multiple letters at once ....")
        for letter in list(inp):
            if self.check():
                return True
            if letter not in self.guessedLetters:
                self.guessedLetters.append(letter)
                if letter in self.secret_word:
                    print("Yes its in there!")
                    for x in [int(pos) for pos, char in enumerate(self.secret_word) if char == letter]:
                        self.guessedWord[x] = list(self.secret_word)[x]
                else:
                    self.guesses -= 1
                    
                    print("not in word guesses left:", self.guesses)
            else:
                print("Already Guessed That")
                
    def start(self):
        # Used to start the game 
        while not self.update():
            print("".join(self.guessedWord))

            
Game("guess this", 10).start()

