# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    words = line.split()
    join = ""
    for word in words:
        join += word + "-"
    return join[0:len(join) - 1]