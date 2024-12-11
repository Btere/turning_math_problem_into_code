from typing import Dict

def unique_character(the_string) -> Dict[str, int]:
    tracker: Dict[str, int] = {}
    for str in the_string:
        if str in tracker:
            tracker[str] += 1
        else:
            tracker[str] = 1

    return tracker
the_string = "abcdf"
tracker = unique_character(the_string)
print(tracker)


Time and space complexity
Time Complexity: 
𝑂
(
𝑛
)
O(n), where 
𝑛
n is the length of the input string.
Space Complexity: 
𝑂
(
𝑘
)
O(k), where 
𝑘
k is the number of unique characters in the string.
