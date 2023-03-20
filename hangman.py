import random
import copy
import getpass
import os

def get_words(txt, minmaxlen):
    f = open(txt, 'r')
    AllWords = f.readlines()[0].split()
    f.close()
    
    while True:
        n = random.randint(0, len(AllWords)-1)
        word = [*AllWords[n]]
        if len(word) >= minmaxlen[0] and len(word) <= minmaxlen[1]: break
    
    asterisks = ['*']
    for i in range(len(word)-1):
        asterisks.append('*')
    return AllWords, word, asterisks

level_length = {1: (3,5), 2: (6, 8), 3: (9, 11), 4:(12, 30)}

hangman = {0: """
            ————————
            |   ╵
            |
            |
          """,
           1: """
            ————————
            |   ╵
            |
            |
            |
          """,
           2: """
            ————————
            |   ╵
            |
            |
            |
            |
          """,
           3: """
            ————————
            |   ╵
            |
            |
            |
            |
            |
          """,
           4: """
            ————————
            |   ╵
            |   O
            |
            |
            |
            |
         """,
           5: """
            ————————
            |   ╵
            |   O
            |   ║
            |   
            |
            |
         """,
           6: """
            ————————
            |   ╵
            |   O
            |   ║
            |   ║  
            |
            |
         """,
          7: """
            ————————
            |   ╵
            |   O
            |  ╱║
            |   ║
            |
            |
         """,
         8: """
            ————————
            |   ╵
            |   O
            |  ╱║╲
            |   ║
            |  
            |
         """,
          9: """
            ————————
            |   ╵
            |   O
            |  ╱║╲
            |   ║
            |  ╱ 
            |
         """,
         10: """
            ————————
            |   ╵
            |   O
            |  ╱║╲
            |   ║
            |  ╱ ╲
            |
         """}
      

class GAMES:
    def __init__(self):
        pass
    
    def hangman_instructions(self):
        print('This is a classic Hangman game whose rules I assume everyone is familiar with.')
        print('The words are loaded from a text file, and all letters are lowercase.')
        print('In the next page, you will be prompted to select one of 4 levels')
        print('the harder the level, the longer the word, and the more attempts you will have, though.')
        print('The word to be guessed wll be randomly selected and shown in asterisks *.')
        print('Your goal is to guess what that word is one letter at a time by typing into the terminal the letter you think')
        print('the word has; the letters you type will not be shown on the screen.')
        print('You can keep guessing until all body parts of HangMan is hown on the screen ^^')
        print('Press any key to continue...')
        k = input()
        os.system('clear')

    def encryption_instructions(self):
        print("""
            A 9-digit social security number is generated randomly with the function random.choice().
            Each digit is then replaced by its index in the corresponding permutation of [0,1,2,3,4,5,6,7,8,9].
            For instance, if the original social security number is 131452047, then\n
            the 1st digit 1 corresponds to index 1 in [0,1,2,3,4,5,6,7,8,9]\n
            the 2nd digit 3 corresponds to index 2 in [1,2,3,4,5,6,7,8,9,0]\n
            the 3rd digit 1 corresponds to index 8 in [2,3,4,5,6,7,8,9,1,0]\n
            ...\n
            Each new digit in the replaced security number is mapped to a unicode according to a key dictionary that
            will be printed out. Each uniquecode is then fed to the native Python function ord() and divided by 9 to obtain
            the remainder (i.e., modulo 9). This is the encrypted message that you are to decrypt.
            """)
        print('Press any key to continue...')
        k = input()
        os.system('clear')
    
    def select_level(self, rep):
        if rep == 0: self.hangman_instructions()
        lvls = ['1','2','3','4']
        print('Level 1: Easy\nLevel 2: Medium\nLevel 3: Hard\nLevel 4: Master')
        level = input()
        if level in lvls:
            os.system('clear')
            return level
        else:
            os.system('clear')
            while level not in lvls:
                print('Please enter a number between 1 and 4')
                print('Level 1: Easy\nLevel 2: Medium\nLevel 3: Hard\nLevel 4: Master')
                level = input()
                os.system('clear')
            return level     
    
    def continue_game(self):
        print('Continue to the next round? [yes]/[no]')
        respond = input()
        if respond == 'yes':
            os.system('clear')
            return True
        elif respond == 'no':
            os.system('clear')
            return False
        else:
            os.system('clear')
            while respond != 'yes' and respond != 'no':
                print('Continue to the next round? [yes]/[no]')
                print('Please enter either [yes] or [no]')
                respond = input()
                os.system('clear')
            if respond == 'yes': return True
            elif respond == 'no': return False
            

class WORD(GAMES):
    def __init__(self, txt, rep):
        self.txt = txt
        self.rep = rep
        self.level = int(self.select_level(self.rep))
        self.AllWords, self.word, self.asterisks = get_words(self.txt, level_length[self.level])
        
        
    def check(self, letter, asterisks):
        guess = True
        word = copy.deepcopy(self.word)
        
        if letter in word:
            idx = [i for i, x in enumerate(word) if x==letter]
            for i, x in enumerate(idx):
                asterisks[x] = letter
            
        else: guess = False
        return asterisks, guess
    
    
    def user_guess(self):
        word = copy.deepcopy(self.word)
        asterisks = copy.deepcopy(self.asterisks)
        i = 5-self.level
        print(''.join(asterisks), '   ', hangman[i-1], end='\r')
        while True:
            letter = getpass.getpass()
            asterisks, guess = self.check(letter, asterisks)
            os.system('clear')
            if guess == True: print(''.join(asterisks), '   ', hangman[i], end='\r')
            elif guess == False and i <= len(hangman)-1:
                print(''.join(asterisks), '   ', hangman[i])
                i += 1
            if '*' not in asterisks:
                print('YOU WIN ヽ(*・ω・)ﾉ')
                break
            elif i > len(hangman)-1: 
                print('YOU LOSE ಥ _ʖಥ')
                break

class ENCRYPT(GAMES):
    def __init__(self, message, keydict):
        self.message = message
        self.keydict = keydict
    
    def encryption(self):
        digits = [0,1,2,3,4,5,6,7,8,9]
        msg_list = [*self.message]
        for i, x in enumerate(msg_list):
            msg_list[i] = digits.index(int(msg_list[i]))
            digits=digits[1:]+[digits[0]]
        for i, x in enumerate(msg_list):
            msg_list[i] = str(ord(self.keydict[msg_list[i]])%9)
        return ''.join(msg_list)
    
    def user_guess(self):
        print('The encrypted message is')
        print(self.encryption())
        print('The encryption key dictionary is')
        print(self.keydict)
        print('Guess what the originial social security number is:')
        guess = input()
        if guess == self.message:
            print('YUUUUP!!!')
        else:
            print('NOOOPE!!!')

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', dest='txt', type=str, required=True,
                     help='Provide a text file or the path to it')
args = parser.parse_args()

if __name__ == "__main__":
    rep = 0
    W = WORD(args.txt, rep)
    W.user_guess()
    while W.continue_game() == True: 
        rep += 1
        W = WORD(args.txt, rep)
        W.user_guess()
    print('You have exited the Hangman :/ Press any key to continue...')
    k = input()
    os.system('clear')


garbage = {0:'!', 1:'&', 2:'*', 3:'%', 4:'#', 5:'@', 6:'~', 7:'(', 8:')', 9:'^'}
E = ENCRYPT(''.join([random.choice('0123456789') for _ in range(9)]), garbage)
E.encryption_instructions()
E.user_guess()
while W.continue_game() == True: 
    E.user_guess()
print('You have exited the the whole game >TAT<')
