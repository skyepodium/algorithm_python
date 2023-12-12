class Solution:
    def interpret(self, command: str) -> str:
        # 1. init
        s = []

        # 2. loop
        for c in command:
            if c == "(":
                s.append(c)
            elif c == ")":
                if s[-1] == "(":
                    s.pop()
                    s.append("o")
            else:
                if len(s) < 1:
                    s.append(c)
                elif s[-1] == "(":
                    s.pop()
                    s.append(c)
                else:
                    s.append(c)

        # 3. return
        return "".join(s)


command = "G()(al)"
command = "G()()()()(al)"
command = "(al)G(al)()()G"
sl = Solution()
print(sl.interpret(command))
