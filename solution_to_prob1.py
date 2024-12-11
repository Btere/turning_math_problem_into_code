from typing import List

Solution 1: 
score = [95,87,85,93,94]
m = len(score)
counter = 0
average_score_wanted = 90
unknown_score = None
for i in range(0, m):
    counter = (counter + score[i])
new_len = m +1

unknown_score =  average_score_wanted * new_len - counter
#unknown_score = average_score_wanted - result
print(unknown_score)



Solution 2: improved version, by writing it as a function

def new_average_scoring(scores: List)-> int:
    """We want to calculate the average score for a new math test"""

    m = len(scores)
    counter = 0
    average_score_wanted = 90
    unknown_score = None
    for score in range(0, m):
        counter = (counter + scores[score])
    new_len = m +1
    unknown_score =  average_score_wanted * new_len - counter
    print(unknown_score)

SCORE: List = [95,87,85,93,94]
new_average_scoring(SCORE)
