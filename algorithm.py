import re

class Solution:
    def reformatDate(self, date: str) -> str:
        # 1. init
        d = {"Jan": '1', "Feb": '2', "Mar": '3', "Apr": '4', "May": '5', "Jun": '6', "Jul": '7', "Aug": '8', "Sep": '9', "Oct": '10', "Nov": '11', "Dec": '12'}

        # 2. split
        day, month, year = date.split(" ")
        day = re.sub("[a-zA-Z]+", "", day)

        return f"{year}-{d[month].zfill(2)}-{day.zfill(2)}"