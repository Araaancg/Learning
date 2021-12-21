import datetime as dt

# Formato iso fecha YYYY-MM-DD 


today = dt.datetime.now()
# print(today)


idate = "2021/12/10"
idate = idate.replace("/","-")
dt_idate = dt.datetime.fromisoformat(idate)

difference = today - dt_idate
print(difference)