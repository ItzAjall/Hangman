import hangman,random

def showHangman(position:int) -> None:
    print(hangman.hangman[position],end="")

def isFinished(word:list[str]) -> None:
    if not "_" in word:
        print("You Won!! 🎉")
        exit()

def main() -> None:
    guess: list[str] = []
    pos: int = 0
    rndword: str = random.choice(hangman.words)
    word: list[str] = ["_" for _ in range(len(rndword))]
    while pos < 7:
        isFinished(word)
        showHangman(pos)
        print("     Guessed letters"," ".join(word[i] for i in range(len(word))))
        print("Letters that have already been entered")
        print(" | ".join(guess[i] for i in range(len(guess))).upper())
        choice: str = input("Enter your choice: ").lower()
        if not choice.isalpha() or choice == "":
            print("Please Enter a valid Character!")
            continue
        if choice in guess:
            print(f"You already entered '{choice}'!")
            continue
        if len(choice) != 1:
            print("Please enter only one character")
            continue
        guess.append(choice)
        if choice in rndword:
            for i in range(len(rndword)):
                if rndword[i] == choice:
                    word[i] = choice
        else:
            pos += 1
            print(f"'{choice}' is not in the word. Try again!")
    print(f"Game Over! The Word Was {rndword}")
if __name__ == '__main__':
    main()