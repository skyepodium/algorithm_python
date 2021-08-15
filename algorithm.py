import re
import collections

def solution(s):

    s = collections.Counter(re.findall("\d+", s))
    return [int(key) for key, cnt in sorted(s.items(), key=lambda x: x[1], reverse=True)]
