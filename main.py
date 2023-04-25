# q1
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


def list3(list1, list2):
    return [element for element in list1 if element in list2]


list4 = list3(list1, list2)
print(list4)


# q2
def palidromes(list):
    palidromess = []
    for word in list:
        if word == word[::-1]:
            palidromess.append(word)
    return palidromess


list = ["sinem", "yesil", "software", "engineering", "sinnis", "yessey"]
print(palidromes(list))


# q3
def prime_function(int_list):
    max_number= max(int_list)
    sieve = [True] * (max_number + 1)
    sieve[0] = sieve[1] = False
    prime = []
    for number in int_list:
        if sieve[number]:
            prime.append(number)
            for mult in range(number * 2, max_number + 1, number):
                sieve[mult] = False
    return prime


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primes_list = prime_function(int_list)
print(primes_list)
#q4
def anagrams(word, word_list):
    sortWord=sorted(word.lower().replace("",""))
    output=[]
    for string in word_list:
        sortString=sorted(string.lower().replace("",""))
        if sortString ==sortWord:
            output.append(string)
    return output

word="cinema"
word_list= ["iceman","sinem","yesil", "iiceman"]
output=anagrams(word,word_list)
print(output)
