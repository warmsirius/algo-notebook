import datetime

def get_before_year(year):
    if year == 0:
        # 高考后
        # if datetime.datetime.now().month > 6 and datetime.datetime.now().day > 8:

        result = datetime.datetime.now().year - 5
        # 高考前
        # else:
        #     result = datetime.datetime.now().year - 5 - 1
    else:
        result = None
    return result


print(get_before_year(0))