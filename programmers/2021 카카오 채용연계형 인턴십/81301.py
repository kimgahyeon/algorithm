# https://programmers.co.kr/learn/courses/30/lessons/81301

s = "23four5six7"
def solution(s):
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
               "eight": "8", "nine": "9"}
    for k,v in num_dict.items():
        s = s.replace(k,v)
    return int(s)