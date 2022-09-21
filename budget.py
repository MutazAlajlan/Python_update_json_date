import json

with open('filePath', "r") as file:
    budget = json.load(file)
for i in range(len(budget['transactions'])):
    currentDate = budget['transactions'][i]['date']
    if (currentDate > "2022-02-26"):
        date = currentDate.split("-", 2)
        month = date[1]
        day = date[2]
        if (day >= "27" and day <= "31"):
            newMonth = int(month) + 1
            newDate = "2022-"+str(newMonth)+"-01"
            memo = ""
            if ('memo' in budget['transactions'][i]):
                memo = budget['transactions'][i]['memo']
            newMemo = month + "-" + day + " " + memo
            budget['transactions'][i]['memo'] = newMemo
            budget['transactions'][i]['date'] = newDate
            print("The old value is:", month, "-", day, " The value has been changed to:",
                  budget['transactions'][i]['date'], "The memo is:", budget['transactions'][i]['memo'])

with open('filePath', "w") as file:
    json.dump(budget, file)
