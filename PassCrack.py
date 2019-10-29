'''
Project 9 CSE 231

-Prompts use to make a selection of given choices
-if users chooses first selection, passwords are cracked from given text files
by forming a hash and crossreferencing it with hashes create from common
passwords
-if the user chooses the second, common words within passwords are found by
inputting common name, phrases, and words text files and cross referencing 
them with passwords from a given text file
-if the third option is chosen, the user can input a password and get its
entropy returned
-the user can select to exit the program
'''

from math import log2
from operator import itemgetter
from hashlib import md5
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def open_file(message):
    try: #try unless it gets error
        file = input(message) #get input name of file
        if file == "": #default if user hits enter
            f = open('pass.txt')
        else:
            f = open(file) #open file based on input
        #print()
        return f #return file pointer
    except IOError: #if an error happens (ioerror)
        print("File not found. Try again.")
        return open_file(message) #run function again with same message
    '''
        takes message as input for prompt
        returns file pointer of inputted file name
    '''
    
    pass

            
def check_characters(password, characters):
    for ch in password: #for each character in password string
        if ch in characters: #if char is in other string
            return True
    return False
    '''
    takes a password and strings of characters 
    checks if the password has characters that match the ones given
    returns true or false
    '''

    pass


def password_entropy_calculator(password):
    #check if pass has uppercase letters
    uppercase = check_characters(password, ascii_uppercase)
    #check if pass has lowercase letters
    lowercase = check_characters(password, ascii_lowercase)
    #check if pass has numbers(digits)
    nums = check_characters(password, digits)
    #check if pass has special chars (punctuation)
    specials = check_characters(password, punctuation)
    n = 0 #declare n to 0
    l = len(password) #get length of password
    
    if password == '': #return entropy of 0 if password is empty string
        return 0
    #check different possibilities of password and get respective N value
    elif nums and not uppercase and not lowercase and not specials:
        n = 10
    elif punctuation and not uppercase and not lowercase and not nums:
        n = 32
    elif punctuation and not uppercase and not lowercase and nums:
        n = 42
    elif lowercase and not uppercase and not specials and not nums:
        n = 26
    elif uppercase and not lowercase and not specials and not nums:
        n = 26
    elif uppercase and lowercase and not specials and not nums:
        n = 52
    elif lowercase and not uppercase and not specials and nums:
        n = 36
    elif uppercase and not lowercase and not specials and nums:
        n = 36
    elif lowercase and not uppercase and specials and not nums:
        n = 58
    elif uppercase and not lowercase and specials and not nums:
        n = 58
    elif lowercase and not uppercase and specials and nums:
        n = 68
    elif uppercase and not lowercase and specials and nums:
        n = 68
    elif lowercase and uppercase and nums and not specials:
        n = 62
    elif lowercase and uppercase and specials and not nums:
        n = 84
    elif lowercase and uppercase and specials and nums:
        n = 94
    #calculate entropy, round to 2nd decimal, and return as float
    return float(round(l*log2(n), 2)) 
    
    '''
    takes a password as input
    calculates entropy of password by checking characters within it and length
    return the calculated entropy rounded to the 2nd decimal as a float
    '''

    pass

def build_password_dictionary(fp):
    pass_dict = dict() #declare dictionary
    rank = 0 #declare rank to 0
    for line in fp: #iterate for each line in text file
        password = line.strip() #strip extra
        md5_hash = md5(password.encode()).hexdigest() #get hash value
        entropy = password_entropy_calculator(password) #get entropy
        rank+=1 #increment rank
        #add tuple to dict with hash as key
        pass_dict[md5_hash] = (password, rank, entropy) 
    return pass_dict #return dict
        
    
    '''
    takes a file pointer as input
    iterates through each line in file and creates a hash from each word
    increments rank each time to rank hashes
    gets entropy from calling other function
    returns a dictionary with hash as the key, and a tuple of
    (password, rank, entropy)
    '''

    pass

def cracking(fp,hash_D):
    list_of_tups = [] #initalize list
    cracked_count = 0 #declare variables to 0
    uncracked_count = 0
    for line in fp: #iterate for each line in file
        line = line.split(':') #split the line at colons
        if line[0] in hash_D: #if the hash (line[0]) is in hash dictionary
            p_hash = str(line[0]) #set has as a string
            password = hash_D[p_hash] #get password from hash dict
            password = password[0] #specify password from tuple
            entropy = password_entropy_calculator(password) #get entropy
            list_of_tups.append((p_hash, password, entropy)) #append tuple
            cracked_count +=1 #iterate count of cracked hashes
        else: #if hash isnt cracked
            uncracked_count+=1 #iterate uncracked counts
    list_of_tups = sorted(list_of_tups, key=itemgetter(1)) #sort list by pass
    return (list_of_tups, cracked_count, uncracked_count) #return tuple
            
    
    
    '''
    takes file pointer and hash dictionary as input
    creates a list of tuples of cracked hashes with their password and entropy
    returns sorted list by password name alphabetically, along with the 
    amount of hashes cracked and uncracked, all within a tuple
    '''

    pass

def create_set(fp):  
    word_set = set() #declare set
    for line in fp: #iterate for line in file
        if line.strip() not in word_set: #remove excess and check if in set
            word_set.add(line.strip()) #add to set
        else:
            continue
    return word_set #return set
    
    
    '''
    takes file pointer as inpute
    creates a set from words in the file with no duplicates
    returns the set
    '''

    pass

def common_patterns(D,common,names,phrases):
    new_D = dict() #declare dictionary
    for key in D: #iterate for each key
        password = D[key] 
        password = password[0].lower() #get password and set to lower
        s = set() #declare set
        s.clear() #empty set
        for word in common: #iterate for each word in file (line)
            if word.lower() in password: #check if word is in current password
                s.add(word.lower()) #add lowercase version of word to set
        for word in names:
            if word.lower() in password:
                s.add(word.lower())
        for word in phrases:
            if word.lower() in password:
                s.add(word.lower())
        s = list(s) #change set to a list
        s = sorted(s) #sort the list alphabetically
        new_D[password] = s #add to dictionary with password as key
    return new_D #return dictionary
    
    
    
    '''
    takes dictionary with password data along with common words, names, and 
    phrases txt file pointers
    iterates through each password from password dictionary and finds common
    words names and phrases that are in that password by iterating through
    the text files
    adds common words phrases and names to sorted list and appends to new dict
    returns new dict with password being the key
    
    '''

    pass
                
def main():
    '''Put your docstring here'''
    
    BANNER = """
       -Password Analysis-

          ____
         , =, ( _________
         | ='  (VvvVvV--'
         |____(


    https://security.cse.msu.edu/
    """

    MENU = '''
    [ 1 ] Crack MD5 password hashes
    [ 2 ] Locate common patterns
    [ 3 ] Calculate entropy of a password
    [ 4 ] Exit

    [ ? ] Enter choice: '''

    print(BANNER) #display banner
    
    while True: #main loop
        i = int(input(MENU)) #take user input
        while i != 1 and i != 2 and i != 3 and i != 4: #misinput handle loop
            print('Error. Try again.')
            i = int(input(MENU))
        
        if i == 1: #if input is 1
            #get file pointers
            fp = open_file('Common passwords file [enter for default]: ')
            h = open_file('Hashes file: ')
            #get hash dictionary from fp
            hash_D = build_password_dictionary(fp)
            #get cracked data tuple
            cracked = cracking(h, hash_D)
            #get tuple list from cracked tuple
            tup_list = cracked[0]
            #display data
            print("\nCracked Passwords:")
            for tup in tup_list:
                print('[ + ] {:<12s} {:<34s} {:<14s} {:.2f}'
                      .format('crack3d!', tup[0], tup[1], tup[2]))
            print('[ i ] stats: cracked {:,d}; uncracked {:,d}'
                  .format(cracked[1], cracked[2]))
        
        if i == 2:
            #get file pointers
            fp = open_file('Common passwords file [enter for default]: ')
            ep = open_file('Common English Words file: ')
            np = open_file('First names file: ')
            pp = open_file('Phrases file: ')
            #get dictionary
            d = build_password_dictionary(fp)
            #get sets
            word_set = create_set(ep)
            name_set = create_set(np)
            phrase_set = create_set(pp)
            #create common word dict
            common_dict = common_patterns(d, word_set, name_set, phrase_set)
            #print phrases
            print("\n{:20s} {}".format('Password', 'Patterns'))
            #given code for printing
            for k,v in common_dict.items():
                print("{:20s} [".format(k),end='')# print password
                print(', '.join(v),end=']\n') # print comma separated list
                
        if i == 3:
            inp = input('Enter the password: ') #take string input
            entropy = password_entropy_calculator(inp) #get entropy
            #print entropy
            print('The entropy of {} is {}'.format(inp, entropy))
            
        if i == 4:
            break #exit
        
        
        '''
        uses functions to create user input loop to crack passwords, get password
        entropy, and find common phrases in passwords
        '''
        
    
    pass
    
if __name__ == '__main__':
    main()