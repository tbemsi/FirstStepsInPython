__author__ = 'bemsibom'

anumber = None

while anumber != -1:
    try:
        anumber = int(input("enter an integer, -1 to stop:"))
    except (TypeError, ValueError) as err:
        print(err.args[0])
    else:
        print("success", anumber)5
