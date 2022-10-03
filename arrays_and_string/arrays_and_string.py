from copy import deepcopy
from collections import defaultdict

#1.1 Is Unique, determine if a string has all unique characters:

def is_unique(word: str) -> bool:
    seen = {}
    for char in word:
        if char in seen:
            return False
        else:
            seen[char] = True
    return True

def teste():
    print('IS_UNIQUE_TESTE')
    print(is_unique('abcdef'), '= True')
    print(is_unique('abcabc'), '= False')
    print(is_unique('abcdea'), '= False')
    print(is_unique('fedcba'), '= True')

teste()

#1.1.2 Is Unique, but without additional data structure:
#Need to understand about bits first
def is_unique(word: str) ->bool:
    pass


#1.2 Check permutation, given two strings check if they are permutations:
def is_permutation(word1: str,word2: str) ->bool:
    if len(word1) != len(word2):
        return False
    
    count = defaultdict(int)
    for i in range(len(word1)):
        count[word1[i]] +=1
        count[word2[i]] -=1
    for key in count:
        if count[key] != 0:
            return False
    return True

def teste():
    print('IS_PERMUTATION_TESTE')
    print(is_permutation('abc','cba'), '=True')
    print(is_permutation('abc','cbadd'),'=False')
    print(is_permutation('abcabc','cbaabb'),'=False')
    print(is_permutation('abcabcabc','cbabbccaa'),'=True')

teste()

#1.3 URLfy: write a method to replace all spaces in a string with '%20'

def urlfy(word: str) ->str:
    letters = list(word)
    for i in range(len(letters)):
        if letters[i] == ' ':
            letters[i] = '%20'
    return "".join(letters)

def teste():
    print("TESTING URLFY")
    print(urlfy("Joao Pedro"))
    print(urlfy("teste"))
    print(urlfy("  minha nossa  "))
    print(urlfy("cabeça de pica"))
  
teste()

#1.4 Palindrome Permutation: write a function to check if a string is a permutation of a palindrome

def is_perm_palindrome(word: str)-> bool:
    count = defaultdict(int)
    for l in word:
        if count[l] ==0:
            count[l]+=1
        else:
            count[l]-=1
    one_count = 0
    for key in count:
        if one_count>1:
            return False
        if count[key] != 0:
            one_count+=1
    return True

def teste():
    print('TESTING IS PERM PALINDROME')
    print(is_perm_palindrome('tactcoa'),"= True")
    print(is_perm_palindrome('abcdef'),"= False")
    print(is_perm_palindrome('aaccbaaccbd'),"= True")
    print(is_perm_palindrome('tttttaaaccc'),"= False")

teste()

#1.5 One Away: There are three types of edits that can be performed on strings: insert, remove or replace a character
# Given two strings, write a functions to check if they are one or zero edits away

def one_edit_away(s1: str,s2: str) -> bool:
    if len(s1) == len(s2):
        return one_edit_replace(s1,s2)
    elif abs(len(s1)-len(s2)) ==1:
        return one_edit_insert(s1,s2)
    else:
        return False

def one_edit_replace(s1,s2):
    found_difference = False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit_insert(s1,s2):
    if len(s1)>len(s2):
        big = s1
        small= s2
    else:
        big = s1
        small = s2
    foun_difference = False
    small_i = 0
    big_i = 0
    while big_i < len(big) and small_i<len(small):

        if small[small_i] != big[big_i]:
            if foun_difference:
                return False
            foun_difference = True
            big_i+=1
            continue
        small_i +=1
        big_i+=1
    return True

def teste():
    print('TESTING ONE AWAY')
    print(one_edit_away('pale','ple'),'= True')
    print(one_edit_away('pales','pale'),'= True')
    print(one_edit_away('pale','bale'),'= True')
    print(one_edit_away('pale','bake'),'= False')
    print(one_edit_away('pale','bakess'),'= False')
    print(one_edit_away('pal','palp'),'= True')

teste()

#1.6 String Compression: perform a basic string compression using the counts of repetead characters
# aabbbbcccccc -> a2

def str_compress(s):
    if len(s)<=2:
        return s
    compressed_str = ""
    curr_char = s[0]
    curr_char_count = 1
    for i in range(1,len(s)):
        if curr_char == s[i]:
            curr_char_count+=1
        else:
            compressed_str+=curr_char+str(curr_char_count)
            curr_char = s[i]
            curr_char_count =1
    compressed_str+=curr_char+str(curr_char_count)
    return compressed_str if len(compressed_str)<len(s) else s

def teste():
    print('TESTING COMPRESSED STR')
    print(str_compress('aaabbbccc'),'-> a3b3c3')
    print(str_compress('abc'),'-> abc')
    print(str_compress('abbbc'),'-> abbbc')
    print(str_compress('aaaaaaaaaaaaaabbbbbbbccc'),'-> a14b7c3')

teste()

# 1.7 Rotate Matrix: Given a image represented by a NxN matrix write a method to rotate the image by 90 degrees:
#[1 , 2 , 3 ]          [7 , 4 , 1 ] 
#[4 , 0 , 6 ]   --->   [8 , 5 , 2 ] 
#[7 , 8 , 9 ]          [9 , 6 , 3 ] 

def rotate(matrix):
    new_matrix = deepcopy(matrix)
    end_matrix = len(matrix)-1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[j][end_matrix] = matrix[i][j]
        end_matrix-=1
    return new_matrix

def rotate_in_place(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i-first
            top = matrix[first][i]
            matrix[first][i] - matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix [i][last]
            matrix[i][last] = top
    return matrix

def teste():
    print('TESTE ROTATE MATRIX')
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    x = rotate([[1,2,3],[4,5,6],[7,8,9]])
    x = rotate(x)
    x = rotate(x)
    x = rotate(x)
    print(x)
    print(rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    x = rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    x = rotate(x)
    x = rotate(x)
    x = rotate(x)
    print(x)
    print(rotate_in_place([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    print(rotate_in_place([[1,2,3],[4,5,6],[7,8,9]]))
teste()

# 1.8 Zero Matrix: write an algorithm that if an element in the matrix is 0
#its column and row are set to 0

def zero_matrix(matrix):
    zero_pos = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_pos.append((i,j))
    for pos in zero_pos:
        set_to_zero(matrix,pos)
    return matrix

def set_to_zero(matrix,pos):
    x = len(matrix)
    y = (len(matrix[0]))
    for i in range(x):
        matrix[i][pos[1]] = 0
    for i in range(y):
        matrix[pos[0]][i] = 0

def teste():
    print("TESTE ZERO MATRIX")
    print(zero_matrix([[1,2,3],[4,0,6],[7,8,9]]))
    print(zero_matrix([[1,2,3,3,5,6],[4,0,6,1,2,3],[7,8,9,1,0,3],[1,2,3,4,5,6],[1,0,3,4,5,6]]))

teste()

#1.9 String Rotation: Given two string s1 and s2 write code to check if s2 is a rotation os d1 using only one call to isSubstring
def string_rotation(s1,s2):
    return is_substring(s1+s1,s2)

def is_substring(s1,s2):
    return s2 in s1

def teste():
    print('TESTE STRING ROTATION')
    print(string_rotation('waterbottle','erbottlewat'))
    print(string_rotation('abc','bca'))
    print(string_rotation('carlos','carinho'))

teste()

