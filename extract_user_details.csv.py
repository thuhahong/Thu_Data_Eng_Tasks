import csv


def extract(user_details):
    try:
        with open(user_details) as csvfile:
            readcsv = csv.reader(csvfile, delimiter=',')

            for x in readcsv:
                print(x)

    except:
        pass


extract("user_details.csv")
