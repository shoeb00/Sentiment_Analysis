import csv
import string


def csvhandler(csvfile):

    with open(csvfile, 'r') as file:
        csv_reader = csv.reader(file)
        ans = ''
        index = 0
        temp = []
        for line in csv_reader:
            temp.append(line)
            break
        index = temp[0].index('reviews')
        print(index)
        for line in csv_reader:
            ans += line[index] + ' '
        print(ans)
        return ans


def handler(inputFile, file):
    ans = ''
    if inputFile == 'txt':
        with open(file, 'r') as text:
            for word in text:
                ans += word + ' '
        return ans
    else:
        return csvhandler(file)
