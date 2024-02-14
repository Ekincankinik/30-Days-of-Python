
# Exercises

1. 

word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = "Python"
space = " "
print(word1 + space + word2 + space + word3 + space + word4)

# or
print('Thirty' + ' Days' + ' Of' + ' Python')

2. 

a = 'Coding'
b = "For"
c = 'All'

sentence = a + space + b + space + c
print(sentence)

3. 
company = "Coding For All"

4.
print(company)

5. 
print(len(company))

6. 
upper_case_company = company.upper()
print(upper_case_company)

7. 
lower_case_company = company.lower()
print(lower_case_company)

8. 

print(company.capitalize()) 
print(company.title())
print(company.swapcase())

9. 

sentenceCut = company.split()[0]
print(sentenceCut) 

10. 

print("Coding" in company)

# or 

word = "Coding"

if word in company:
    print(f"{word} is found in the {company}")

11. 

sentence = "Coding For All"
firstWord = sentence.split()[0]
sentenceReplaced = sentence.replace(firstWord, "Python")
print(sentenceReplaced)

12. 

sent = "Python For Everyone"
lastWord = sent.split()[2]
newSent = sent.replace(lastWord, "All")
print(newSent)

# or
newSent2 = sent.replace("Everyone", "All")
print(newSent2)

13. 

strSen = "Coding For All"
strSenSplt = strSen.split()
print(strSenSplt)

14. 
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companiesSplt = companies.split(",")
print(companiesSplt)

15. 
strCompany = "Coding For All"
firstIndex = strCompany[0]
print(firstIndex)
16. 

lastIndex = strCompany[-1]
print(lastIndex)

17. 

tenthChr = strCompany[10]
print(tenthChr)

18. 
sent1 = 'Python For Everyone'
abr = sent1.split()[0][0] + sent1.split()[1][0] + sent1.split()[2][0]
print(abr)

19.
acr = strCompany.split()[0][0] + strCompany.split()[1][0]+strCompany.split()[2][0]
print(acr)


20. 

words = "Coding For All"
letter = "C"
print( words.index(letter)) 

# or 

print(words.find('C'))

21. 

firstIndexOfF = words.index('F')
print(firstIndexOfF)

22. 

a = 'Coding For All People'
last_index = a.rfind('l')
print(last_index)

23. 

sentenceRepet = "You cannot end a sentence with because because because is a conjunction"
wordRepet = "because"
firsOcc = sentenceRepet.index(wordRepet)
print(firsOcc)

24. 
lastOcc = sentenceRepet.rfind(wordRepet)
print(lastOcc)

25. 
sentenceX = 'You cannot end a sentence with because because because is a conjunction'

phrase = sentenceX[30:54]

print(phrase)

# or 

newSentence = sentenceX.replace("because","").split()
newSentence_up = " ".join(newSentence)
print(newSentence_up)

26. 

phraseS = 'You cannot end a sentence with because because because is a conjunction'
word = "because"
firstOccurence = phraseS.index(word)
print(firstOccurence)

27. 
newSentence = sentenceX.replace("because","").split()
newSentence_up = " ".join(newSentence)
print(newSentence_up)

28. 
strA = 'Coding For All'
substr = "Coding"

print(strA.startswith(substr))

29. 

sbstr = "coding"
result = strA.endswith(sbstr)
print(result)

# or

print(strA.endswith(sbstr))

30. 

sentenceWithBlank = '   Coding For All      ' 
trimmedstrA = sentenceWithBlank.strip()

31. 

word1 = '30DaysOfPython'
word2 = 'thirty_days_of_python'

result1 = word1.isidentifier()
result2 = word2.isidentifier()

print(result1)
print(result2)

32. 

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
updated_lib = " #".join(libraries)
print(updated_lib)

33. 

sentences1 = "I am enjoying this challenge. I just wonder what is next."
updated_sentences1 = "I am enjoying this challenge.  \nI just wonder what is next."
print(updated_sentences1)

34.

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

35. 
radius = 10
area = 3.14* radius * radius
print(f"The area of a circle with radius {radius} is {area} meter square.")

36. 

a = 8
b = 6

addition =f" {a} + {b} = {a+b} "
subs = f"{a} - {b} = {a - b} "
multi = f"{a} * {b} = {a*b}"
division = f"{a} / {b} = {a / b}"
mod = f"{a} % {b} = {a % b} "
floor_division = f"{a} // {b} = {a // b}"
exp = f"{a} ** {b} = {a ** b}"

