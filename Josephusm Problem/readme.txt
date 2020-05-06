In this question, I separated the solution into two files,
"josephusproblem.py" used to display the function that can perform the Josephus Problem;
"josephusm.py" used to do the operation to find that the eliminate order of the game.

In "josephusproblem.py",
it simply prints out the outline and let users input the number counts,
and call out the function jose from "josephusm.py".

In "josephusm.py",
there is only one function called jose that called in "josephusproblem.py",
I created a list used to store the create circle,
since I can delete the specific number in the future and that's queue and stack did not have.

Also, I created a queue used to store the order of the eliminated people.

In function jose,
since we did not know how many people in the start and the number counts for elimination,
I used for-loop for both list and queue with the inputted data "n" for people in the start and
"m" for number counts for elimination from users.

Especially, there have an inner loop in the loop that counts from 1 to n,
it can act like count the elimination for n time(s) since there are n people.

In the inner loop,
there is the count for the number counts to find out the position that can eliminate people.

In the end,
display the queue "deadc" is the answer to this question.