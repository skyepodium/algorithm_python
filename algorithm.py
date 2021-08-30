import re

def solution(skill, skill_trees):
    # 1. init
    pattern = f"[^{skill}]"
    res = 0

    # 2. loop
    for s in skill_trees:
        r = re.sub(pattern, "", s)
        if skill.startswith(r):
            res += 1

    return res