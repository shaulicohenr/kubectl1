# להדפיס את כל המחרוזת 3 אפשרויות
#print(word[:])
#print(word[0:23])
#print(word)
###############
sentence_1 = "Python makes string manipulation fun and"  
# 1) Split the sentence into a list of words and store it in a variable named words_1.
words_1=sentence_1.split()
#print(words_1)
# 2) Print the number of words.
#print(len(words_1))
# 3) Print the first word and the last word using indexing.
#print(words_1[0],words_1[-1])
# 4) Create a hyphen-separated version of the sentence (e.g., "Python-makes -... ") using .join().
#print("-".join(words_1))
# 5) Create a string of the last two words joined by a single space using slicing and .join().
#words_2=words_1[-2:] 
#str2=" ".join(words_2)
#print(str2)
#print(" ".join(words_1[5:]))
len_list=len(words_1)
#print(len_list)
#print(words_1[len_list-2:])
list1=["apple", "false", "2","salt", "pepper",'hello']
#print the second item in the list
#print(list1[1])
#create and print a new list containing "salt" and "pepper"
#list2=list1[1:]
#print(list2)
#access and print the first letter of the last item in the list
#print(list1[-1][0])
#create a new string by joining the 2nd and 3rd items from the list
#print("-".join(list1[1:3]))
str1 = "learning python is fun"
#Print the string in uppercase
#print(str1.upper())
#Check if the word "python" exists in the string
#print(str1.find('p'))
#Replace "fun" with "awesome"
#str1=str1.replace("fun","awesome")
#print(str1)
str2 = "programming"
#print(str2[-1:])
#print(str2[-1::-1])
#list1=str1.split()
str3='-'.join(list1)
#print(str3)
###############
#print("hello")
###############
word="helloworldiloveicedream"
#1.print the letter in index 5?
#print(word[5])
#2.print the index of the letter e? print the letter using the index
#print(word.index('e'))
#print(word.find('e'))
#3.print all the letters from index 10 to index 15 - not including
#print(word[10:15])
#4.print from the start of the string to index 5 - not including
#print(word[:5])
#7. print from index 1 to index 10 every 3 chars
#print(word[1:10:3])
#print(word[2],word[5],word[10])
#8. print all even indexes - start from begining till end jumps of 2
####################
#list1=["apple", "false", 2,"salt", "pepper","hello"] 
#print the second item in the list
#print(list1[1])
#print the second to last item in the list
#print(list1[-2])
######################
list1 = ['a', 'b', 'c', 'a']
list1.sort()
letters_list=list1
letters_list.sort()
print(letters_list)
letters_tuple = tuple(letters_list)
print(letters_tuple)
letters_set = set(letters_list)
set1=letters_set 
set1.add('d')
print(set1)
set1.discard('c')
print(set1)
################

str_numbers = ["100", "25.5", "8"] 
print(type(str_numbers[0]))

##########
#age = int(input("הכנס את גילך: "))

#if age < 13:
    #print("אתה ילד/ה")
#elif age <= 18:
    #print("אתה מתבגר/ת")
#else:
    #print("אתה בוגר/ת")

##############
country = input("באיזו מדינה אתה גר? (USA/ISRAEL/UK): ").strip().upper()
#age = int(input("הכנס את גילך: "))

if country == "USA":
    adult_age = 17
elif country == "ISRAEL":
    adult_age = 18
elif country == "UK":
    adult_age = 20
else:
    print("מדינה לא מוכרת")
    adult_age = 18  # ברירת מחדל

#if age < 13:
    print("אתה ילד/ה")
#elif age < adult_age:
    print("אתה מתבגר/ת")
#else:
    print("אתה בוגר/ת")
#############

stored_username = "shauli"
stored_password = "1234"

username = input("שם משתמש: ")
password = input("סיסמה: ")

# אימות
if username == stored_username and password == stored_password:
    print("התחברות הצליחה!")
else:
    print("שם משתמש או סיסמה שגויים.")
############
usernames=[]
user1=input('enter username  ')
if user1 in usernames:
    print("The username is already exist")
else:
    usernames.append(user1)
print(usernames)
















