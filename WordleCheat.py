def inputGuess(yellow, green, black):
    guess = (input("Enter guess: ")).lower()
    result = (input("Enter result (B/Y/G): ")).lower()
    for index in range(len(result)):
        if result[index] == 'y':
            yellow[index] = guess[index]
        elif result[index] == 'g':
            green[index] = guess[index]
        elif result[index] == 'b':
            black.add(guess[index])

def appendPossibleWords(possibleWords, word, yellow, black, green):
    if len(word.strip()) != 5:
        return
    for pos, letter in yellow.items():
        if letter not in word:
            return
        if word[pos] == letter:
            return
    for pos, letter in green.items():
        if word[pos] != letter:
            return
    for letter in black:
        if letter in word:
            return
    possibleWords.append(word)
    return

def play():
    win = False
    yellow = {}
    black = set()
    green = {}
    while win == False:
        inputGuess(yellow, green, black)
        possibleWords = []
        with open("words.txt") as words:
            for word in words:
                appendPossibleWords(possibleWords, word, yellow, black, green)
        print(f"There are {len(possibleWords)} possible answers! ")
        for possibleWord in possibleWords:
            print(possibleWord.strip())
        winCheck = (input("Game done? (Y/N) ")).lower()
        if winCheck == 'y':
            win = True
    return

playing = True
while playing:
    play()
    playAgain = (input("Want to play again? (Y/N) ")).lower()
    if playAgain == 'n':
        playing = False