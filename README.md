# Number-Guessing-in-Python


FindNumber( )
Issue instructions, and then interactively determine, using the least number of questions, the value of any positive integer chosen in advance by the user.

For each question, the function presents a number to the user, and the user gives one of the three responses ‘<’, ‘>’, or ‘=’, dependent on whether the chosen number is less than, greater than or equal to the number presented, respectively.
After it has determined the number, the function outputs both the number itself and the number of questions which were asked. If the user gives a response other than ‘<’, ‘>’, or ‘=’, the function issues an error message and repeats the same question.

MinPos( lst )
The position of the smallest item in the special list ‘lst’. hopefully as efficiently as possible.

Here, a special list is a non-empty list of distinct items, such that those at positions/indexes

k, k+1, k+2, …, n-1, 0, 1, …, k-1

are sorted in ascending order, where ‘n’ denotes the length of the list and ‘k’ is some integer in the range 0 ≤ k ≤ n-1.
