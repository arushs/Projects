word = raw_input("Word to count Vowels in? ")
vowels = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for c in word:
    if c == 'a':
        a+=1
        vowels+=1
    if c == 'e':
        e+=1
        vowels+=1
    if c == 'i':
        i+=1
        vowels+=1
    if c == 'o':
        o+=1
        vowels+=1
    if c == 'u':
        u+=1
        vowels+=1
print "Vowels ", vowels
print "a's ",a
print "e's ",e
print "i's ",i
print "o's ",o
print "u's ",u


