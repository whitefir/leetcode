class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        months=[0,31,28,31,30,31,30,31,31,30,31,30,31]#no 0th month,no leap year
        #standard 1/1/1971 firday, 1971 not leap year
        
        days=(year-1971)*365+(year-1968)//4+sum(months[0:month])+day
        if year%4==0 and month<3:
            days-=1
        return weekdays[(4+days)%7]
