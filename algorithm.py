from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. init
        d = defaultdict()
        check = defaultdict()
        res = []

        # 2. make graph
        for s, e in tickets:
            if s in d: d[s].append(e)
            else: d[s] = [e]

            key = f"{s}{e}"
            if key in check: check[key] += 1
            else: check[key] = 1
        check["NneJFK"] = 1

        # 3. sort
        for k in d.keys():
            d[k].sort()

        # 4. dfs
        def dfs(s, e):
            key = f"{s}{e}"
            check[key] -= 1
            if e in d:
                for n_node in d[e]:
                    next_key = f"{e}{n_node}"
                    if check[next_key] > 0:
                        dfs(e, n_node)

            res.append(e)

        dfs("Nne", "JFK")

        return res[::-1]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
sl = Solution()

res = sl.findItinerary(tickets)

print('res', res)


