import os


board = [
'''
 +------+
 |      |
 |
 |
 |
 |
 |
''',
'''
 +------+
 |      |
 |      O
 |
 |
 |
 |
''',
'''
 +------+
 |      |
 |      O
 |      |
 |
 |
 |
''',
'''
 +------+
 |      |
 |      O
 |     /|
 |
 |
 |
''',
'''
 +------+
 |      |
 |      O
 |     /|\\
 |
 |
 |
''',
'''
 +------+
 |      |
 |      O
 |     /|\\
 |     /
 |
 |
''',
'''
 +------+
 |      |
 |      O
 |     /|\\
 |     / \\
 |
 |
'''
]


class Hangman:
    def __init__(self, word: str) -> None:
        self.word = word.upper()
        self.correct_letters = []
        self.wrong_letters = []
    

    def hidden_word(self) -> str:
        hidden_word = ''

        for letter in self.word:
            if letter not in self.correct_letters:
                hidden_word += '_ '
            else:
                hidden_word += (letter + ' ')

        return ' | ' + hidden_word

    
    def guess_letter(self, letter: str) -> bool:
        self.leter = letter

        if letter in self.word and letter not in self.correct_letters:
            self.correct_letters.append(letter)
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        else:
            return False
        
        return True
    

    def update_board(self):
        os.system('cls')
        print(board[len(self.wrong_letters)], end='')
        print(self.hidden_word())

        print('\nLetras erradas: ', end='')

        for i in self.wrong_letters:
            print(i, end=' ')


    def hangman_over(self):
        return self.hangman_won() or len(self.wrong_letters) == 6


    def hangman_won(self) -> bool:
        if '_' not in self.hidden_word():
            return True
        else:
            return False

    
def main(word):
    game = Hangman(word=word)

    while not game.hangman_over():
        game.update_board()
        guessing_letter = input('\n\nDigite uma letra: ')
        game.guess_letter(guessing_letter.upper())

    
    game.update_board()

    if game.hangman_won():
        print('\n\nGANHOU\n')
    else:
        print('\n\nGAME OVER\n')


if __name__ == '__main__':
    word = input('Digite a palavra que será adivinhada: ')

    main(word.upper())