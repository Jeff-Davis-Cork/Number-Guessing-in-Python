def FindNumber():
    # Issue instructions, and then interactively determine,
    # using the least number of questions, the value of any
    # positive integer chosen in advance by the user.
    # For each question, the function presents a number to
    # the user, and the user gives one of the three responses
    # '<', '>', or '=', dependent on whether the chosen number
    # is less than, greater than or equal to the number presented,
    # respectively.
    # After it has determined the number, the function outputs
    # both the number itself and the number of questions which
    # were asked. If the user gives a response other than '<', '>',
    # or '=', the function issues an error message and repeats
    # the same question.
    guessCount=0
    notGuessed=True
    rangeIsNotSet=True
    lo=1
    hi=10
    print('''
Hello, and welcome to my number guessing game !

You will choose a number and I will try to guess it

and then I will attempt to guess the number as quickly as possible.

After each guess of mine, please enter in '<', '>', or '=',
to show if the number I guessed is less than,
greater than or equal to the number you choose, respectively.

First, I will check how big your number is.''')

    while rangeIsNotSet:
        numRange =input('''
Is your number between %i and %i?

Please please enter in '>', or '='.''' % (lo,hi))
        if numRange=='=':
            rangeIsNotSet=False
        elif numRange=='>':
            hi=hi*2
        else:
            print("Oops, you need to enter in '>', or '='")

    print('''
Thanks - Now it is my turn to guess.
''')
    
    mid = ( lo + hi ) // 2
    guessCount+=1
    print('Is your number %i?'% mid)
    sign=(input('''
Let me know how close I am. Enter in '<', '>', or '='
'''))
    while lo<=hi:
        if sign=='=':
            print()
            print('''Oh, I am good.

Your number was %i.

That was a quick game...''' % mid)
            print()
            if guessCount==1:
                print("I guessed it in only 1 try")
                print()
                break
            else:
                print("I guessed it in only %i tries" % guessCount)
                print()
                break
        elif sign=='<':
            hi=mid
            guessCount+=1
            mid = ( lo + hi ) // 2
            print("Ok, I'm a bit high. I'll guess lower next time")
            print('Is your number %i?'% mid)
            sign=(input('''
Let me know how close I am. Enter in '<', '>', or '='
'''))     
        elif sign=='>':
            lo=mid
            guessCount+=1
            mid = ( lo + hi ) // 2
            print("Ok, I'm a bit low. I'll guess higher next time")
            print('Is your number %i?'% mid)
            sign=(input('''
Let me know how close I am. Enter in '<', '>', or '='
'''))
        else:
            print("Oops, you need to enter in '<', '>', or '='")

def MinPos( lst ):
    # The position of the smallest item in the special list
    #‘lst’. Try to find it as efficiently as possible.
    # Here, a special list is a non-empty list of distinct
    # items, such that those at positions/indexes
    # k, k+1, k+2, …, n-1, 0, 1, …, k-1 are sorted in ascending
    # order, where ‘n’ denotes the length of the  list and ‘k’
    # is some integer in the range 0 ≤ k ≤ n-1.
    lo = 0
    hi = len(lst) - 1
    while lst[hi] < lst[lo]:
        hi = (hi + 1) % len(lst)
        lo = (lo + 1) % len(lst)
    return lo
        
sl1=[ 31, 38, 44, 53, 67, 75, 84, 16, 20, 27 ]
sl2=[ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
sl3=[ 12, 13, 14, 15, 16, 17, 18, 19, 20, 11 ]
sl4=[ 57 ]




            
