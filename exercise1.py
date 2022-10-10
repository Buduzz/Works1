##A program that does##
#num1=int(input('Enter a number: '))
#num2=int(input('Enter another number: '))
#num3=int(input('Enter another number: '))
#answer=num1+num2+num3
#print('The sum of the three numbers you entered is: ',answer)

#name = input('Enter your name: ')
#age = 78
#address = input('Enter your address: ')
#print('Hello',name,age,address)
#print('i am here')

#temp=eval(input('Enther temperature in Celsius: '))
#print('In Fahrenheit, that is', 9/5*temp+32)


#A program to show the percentage of numbers 2,3,4,...12# when a dice is rolled twice 
# from random import randint
# prob=[2,3,4,5,6,7,8,9,10,11,12]
# freq=[0]*11
# for k in range(10000):
#     a=randint(1,6)+randint(1,6)
#     freq[prob.index(a)]=freq[prob.index(a)]+1

# print(freq)
    
# for j in range(len(freq)):
#     p=freq[j]/10000
#     print(f'the percentage is {p}')


# from random import randint, sample

# lottary =[k for k in range(1,11)]    
# users = [randint(1,10) for k in range(6)]
# print(f'users: {users}')
# correct=False
# countCorrect=0
# for k in range(1000):
#     drawings=sample(lottary,6)
#     print(f'drawings: {drawings}')
#     for m in range(len(drawings)):
#         if drawings.count(drawings[m])==users.count(drawings[m]):
#             correct=True
#         else:
#             correct=False
#             break
#     if correct ==True:
#         countCorrect=k
#         break

# print(f'average: {countCorrect}')

#Physics'
# print(list(range(3)))
# print(list('physics'))
# print(list(str(124)))


#enters months and displays days
# month = int(input('Enter a month: '))
# days =[31,28,31,30,31,30,31,31,30,31,30,31]
# print(days[month-1])

#using a dictionary
# month = int(input('Enter a month: '))
# days ={'January':31,'February':28,'March':31,'April'30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'Decemebr':31}
# print(days[month-1])

#Creating a dictionary for a bunch of words in a sentence and display the largest

# s= 'I am a great man of the great father in this world'
# words =s.split( )
# frequency= { }
# for w in words:
#     if w in frequency:
#         frequency[w] = frequency[w]+1
#     else:
#         frequency[w] =1
# print(frequency)
# value = list(frequency.values())
# maxValue = max(value)
# for key in frequency:
#     if frequency[key]==maxValue:
#         print(key)


# from random import shuffle
# word =['Letter', 'amen', 'zero','physics']
# shuffle(word)
# for w in word:
#     word = set(w)
#     if len(w) != len(word):
#         pass
#     else:
#         print(w)
#         break


# from random import shuffle
# word =['Letter', 'amen', 'zero','physics']
# shuffle(word)
# for w in word:
#     word = set(w)
#     if len(w) == len(word):
#         print(w)
#         break

# from random import shuffle, sample
# word=['letter', 'amen', 'zero', 'physics', 'bring','question', 'high']
# shuffle(word)


# for each word
# count the letters 
# if a letter -count >1
# the word has a repeated character
# else:
#    the word has a unique character
#    return word
# end 


# for w in word:
#     for c in w:
#         if w.count(c) > 1:
#             break
#     else:
#         print(w)
#         break



# data =[[0]*5 for i in range (5)]
# from random import sample, shuffle
# # data2[0]=20
# i =0
# while i < 2:
#     for j in range (len(data[i])):
#         data[i][j] = 1
#     i+= 1
# shuffle(data)
# print(data)

# def fullName(firstName, lastName):
#     name=f'{firstName} {lastName}'
#     return name
# firstName= input('Enter your first name ')
# lastName= input('Enter your last name ')
# personName =fullName(firstName, lastName)
# print(personName)


# def printItems(data):
#     for items in data:
#         print(items)
# words =['word', 'road', 'man', 'woman', 'boy', 'girl']
# printItems(words)

def average(*args):
    value =sum(args)/len(args)
    return value


if __name__=='__main__':
    menNumber = average(1,2,4,5,7,9,11,23,24)
    print(menNumber)