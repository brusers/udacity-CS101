########################################################################
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(L):
    st,fee=0,0
    for i in range(len(L)):
        st = st + L[i][1]
        fee = fee + (L[i][2]*L[i][1])
    return st, fee



print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

print total_enrollment(usa_univs)
#>>> (77285,3058581079L)


########################################################################
# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(p):
    n=len(p)
    digit = 1
    while digit <=n:
        i=0
        while i<n:
            row_count=0
            col_count=0
            j=0
            while j<n:
                if p[i][j]==digit:
                    row_count = row_count+1
                if p[j][i]==digit:
                    col_count = col_count+1
                j+=1
            if row_count != 1 or col_count !=1:
                print("false")
                return False
            i +=1
        digit+=1
    print("true")
    return True


    
    
#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False


########################################################################
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(L):
	for n in range(len(L)):
		newL = []
		for i in range(len(L)):
			newL.append(L[i][n])
		if newL != L[n]:
			return False
	return True

print symmetric([[1, 2, 3],[2, 3, 4],[3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],["dog", "dog", "fish"],["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False


########################################################################
# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit=False
            else:output[-1] = output[-1]+char
    return output



out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']


########################################################################
# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth and returns the time taken to download the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) whereas file size is given in
# megabytes (MB).

def convert_seconds(seconds):#   2321.428571
    hour=0
    min=0
    sec=0
    if seconds >= 3600:
        hour = int(seconds)/3600
        seconds -= hour*3600
    if seconds >= 60:
        print seconds
        min = int(seconds/60)
        seconds -= (min*60)
    sec = seconds

    if hour!=1:
        hhS = ' hours'
    else:
        hhS = ' hour'
    if min!=1:
        mmS = ' minutes'
    else:
        mmS = ' minute'
    if sec!=1:
        ssS = ' seconds'
    else:
        ssS = ' second'
    returnS = str(hour)+str(hhS)+', '+str(min)+str(mmS)+', '+str(sec)+str(ssS)
    return returnS

def download_time(size, unitS, band, unitB):
    if unitS == 'kB':
        size *= 2**10*8
    elif unitS == 'MB':
        size *= 2**20*8
    elif unitS == 'GB':
        size *= 2**30*8
    elif unitS == 'TB':
        size *= 2**40*8
    elif unitS == 'Tb':
        size *= 2**40
        
    if unitB == 'kB':
        band *= 2**10*8
    elif unitB == 'MB':
        band *= 2**20*8
    elif unitB == 'kb':
        band *= 2**10
    elif unitB == 'Mb':
        band *= 2**20
    elif unitB == 'GB':
        band *= 2**30*8
        
    
    time=float(size)/float(band)
    output=convert_seconds(time)
    return output



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


########################################################################
# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(word, n):
    nWord = []
    for l in word:
        num = ord(l)
        if num == 32:
            nWord.append(chr(num))
        else:
            num += n
            if num >= 123:
                num -= 26
            if num < 97:
                num += 26
            nWord.append(chr(num))
    return "".join(nWord)

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)


########################################################################
# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

def ancestors(genealogy, person):
	if person in genealogy:
		parents = genealogy[person]
		result = parents
		for parent in parents:
			result = result + ancestors(genealogy, parent)
		return result
	return []





# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print ancestors(ada_family, 'Dave')
#>>> []


########################################################################
def triangle(n):
    lastList = []
    tempList = []
    numList = []
    if n == 0: 
        return numList
    elif n == 1: 
        numList.append([1])
        return numList
    else:
        numList.append([1])
        for i in range(n-1):
            tempList = [1]
            for j in range(len(lastList)-1):
                myNum = lastList[j]+lastList[j+1]
                tempList.append(myNum)                
            tempList.append(1)
            lastList = tempList
            numList.append(tempList)
        return numList

#print triangle(0)
#>>> []
#print triangle(1)
#>>> [[1]]
#print triangle(2)
#>> [[1], [1, 1]]
print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]


########################################################################
# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(myString):
	myList = []
	temp = []
	while myString.find('>') is not -1:
		first = myString.find('<')
		second = myString.find('>')
		myString = myString[:first] + " " + myString[second+1:]
	for i in range(len(myString)):
		if myString[i] == " " or myString[i] == "\n":
			if "".join(temp) != "":
				myList.append("".join(temp))
			temp=[]
			pass
		else:
			temp.append(myString[i])
	if "".join(temp) != "":
		myList.append("".join(temp))
	
	return myList


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']


########################################################################
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. Itcan 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
	change = {'match':match, 'replacement':replacement, 'length':len(match)}
	return change

def apply_converter(converter, string):
	temp = []
	for i in range(len(string),-1,-1):

		if string[i-converter['length']:i] == converter['match']:
			string = string[:i-converter['length']] + converter['replacement'] + string[i:]

	return string


# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).


########################################################################
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(theList):
	count = 1
	most = 0
	if theList == []:
		return None
	else:
		name = theList[0]
		for i in range(len(theList)-1):
			if theList[i] == theList[i+1]:
				count += 1
				if count > most:
					print most
					print count
					name = theList[i]
			else:
				if count > most:
					most = count
				count = 1
	return name


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

#print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

#print longest_repetition([1,2,3,4,5])
# 1

#print longest_repetition([])
# None


########################################################################
# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(theList):
    newList = list(theList)
    for i in range(len(newList)):
		if is_list(newList[i]):
			newList[i] = deep_reverse(newList[i])
    newList.reverse()
    return newList


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]


########################################################################
# One Gold Star
# Question 1-star: Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to 
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling 
# takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. The second procedure, bell, takes as input a 
# positive integer n and returns the Bell number B(n).

def stirling(items, sets):
    if items == sets or sets == 1:
		return 1
    elif sets > items:
		return 0
    else:
		ways = (sets*stirling(items-1, sets)) + stirling(items-1, sets-1)
    return ways

# B(n) is the sum of S(n,k) for k =1,2, ... , n.
def bell(num):
	bell = 0
	for i in range(num):
		bell += stirling(num, i+1)
	return bell
	
	
########################################################################
# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can 
# collude with each other to improve their page ranks.  We consider 
# A->B a reciprocal link if there is a link path from B to A of length 
# equal to or below the collusion level, k.  The length of a link path 
# is the number of links which are taken to travel from one page to the 
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A, 
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link 
# A->B, which includes one link and so is of length 1. (it requires 
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to 
#   - take an extra input k, which is a non-negative integer, and 
#   - exclude reciprocal links of length up to and including k from 
#     helping the page rank.


def collude(graph, page, k):
	depth = k
	checkList = []
	if depth > 0:
		checkList = graph[page][:]
	while depth > 1:
		temp_list = []
		for node in checkList:
			temp_list = temp_list + graph[node]
		for item in temp_list:
			if item not in checkList:
				checkList.append(item)
		depth -= 1
	return checkList
	
def compute_ranks(graph, k):
	collusion = {}
	d = 0.8 # damping factor
	numloops = 10
	ranks = {}
	npages = len(graph)
	for page in graph:
		ranks[page] = 1.0 / npages

		collusion[page] = collude(graph, page, k)

	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newrank = (1 - d) / npages
			for node in graph:
				if page in graph[node]and page != node:
					if node not in collusion[page]:
						newrank = newrank + d * (ranks[node]/len(graph[node]))
			newranks[page] = newrank
		ranks = newranks
	return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

#print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

#print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

#print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}


########################################################################
# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our 
# case, consists of the characters '.' and 'x', and changes it according 
# to some predetermined rules. The rules consider three characters, which 
# are a character at position k and its two neighbours, and determine 
# what the character at the corresponding position k will be in the new 
# string.

# For example, if the character at position k in the string  is '.' and 
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up 
# '..x' in the table below. In the table, '..x' corresponds to 'x' which 
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work 
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all 
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position 
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs: 
#     a non-empty string, 
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and 
#     a positive integer, n, which is the number of generations. 
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.

def set_cells(c, pattern):
	if pattern - 128 >= 0:
		c[7] = 'x'
		pattern -= 128
	if pattern - 64 >= 0:
		c[6] = 'x'
		pattern -= 64
	if pattern - 32 >= 0:
		c[5] = 'x'
		pattern -= 32
	if pattern - 16 >= 0:
		c[4] = 'x'
		pattern -= 16
	if pattern - 8 >= 0:
		c[3] = 'x'
		pattern -= 8
	if pattern - 4 >= 0:
		c[2] = 'x'
		pattern -= 4
	if pattern - 2 >= 0:
		c[1] = 'x'
		pattern -= 2
	if pattern - 1 >= 0:
		c[0] = 'x'
		pattern -= 1
	return c

def bin2num(ch1, ch2, ch3):
	number = 0
	if ch1 == 'x':
		number += 4
	if ch2 == 'x':
		number += 2
	if ch3 == 'x':
		number += 1
	return number
	
def cellular_automaton(x, pattern, gen):
	seeds = list(x)
	result = list(seeds)
	length = len(result)
	cells = ['.','.','.','.','.','.','.','.']
	cells = set_cells(cells, pattern)

	if length < 3 and gen == 2:
		return "."
	if length < 3 and gen == 1:
		return "x"
	for i in range(gen):
		bNum = bin2num(seeds[-1],seeds[0],seeds[1])
		result[0] = cells[bNum]
		for n in range(length-1):
			if n > 0:
				bNum = bin2num(seeds[n-1],seeds[n],seeds[n+1])
				result[n] = cells[bNum]
		bNum = bin2num(seeds[-2],seeds[-1],seeds[0])
		result[-1] = cells[bNum]
		seeds = list(result)
	return "".join(result)

print cellular_automaton('.', 21, 1)
#>>> .
print cellular_automaton('.', 21, 1)
#>>> x
print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
