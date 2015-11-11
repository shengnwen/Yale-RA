__author__ = 'shengwen'

import csv
# 1. extract all authors
def extractAuthor(csvFile="./allDutch.csv"):
    authorSet = set()
    with open(csvFile) as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        for row in data[1:]:
            author = row[2].strip().decode("latin-1").encode('utf-8')
            if author == None or author == '' or author == 'undefined':
                continue
            author = author.replace(',', ' ')
            authorSet.add(author)
    author_list = sorted(list(authorSet))
    for author in author_list:
        print author
    author_filename = csvFile[:-4] + "-author.csv"
    print("create author file:" + author_filename)
    with open(author_filename, 'w') as f:
        result = 'author\n'
        for author in author_list:
            result += (str(author) + "\n")
        f.writelines(result)
# 2. extract all subjects
def extractSubjects(csvFile="./allDutch.csv"):
    dict = {}
    with open(csvFile) as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        for row in data[1:]:
            ele = row[6].strip().rstrip(',')
            if ele == None or ele == '' or ele == 'undefined':
                continue
            ele = ele.replace(',', '|')
            if ele in dict:
                dict[ele] += 1
            else:
                dict[ele] = 1
    for ele in sorted(dict):
        print ele, dict[ele]
    ele_filename = csvFile[:-4] + "-subject.csv"
    print("create subject file:" + ele_filename)
    with open(ele_filename, 'w') as f:
        result = 'Subject, Count\n'
        for ele in sorted(dict):
            result += (str(ele) + "," + str(dict[ele]) + "\n")
        f.writelines(result)
# 3. parse subjects
# def classifySubjects(csvFile="./allDutch-subject.csv"):
#     dict = {}
#     with open(csvFile) as f:
#         data = [row for row in csv.reader(f.read().splitlines())]
#         for row in data[1:]:
#             ele = row[0].strip()
#             count = row[1].strip()
#             if ele == None or ele == '' or ele == 'undefined':
#                 continue
#             words = ele.split('|')
#             for word in words:
#                 word = word.strip()
#                 if word in dict:
#                     dict[word] += count
#                 else:
#                     dict[word] = count
#     for ele in sorted(dict):
#         print ele, dict[ele]
#     ele_filename = csvFile[:-4] + "-classified.csv"
#     print("create classified subject file:" + ele_filename)
#     with open(ele_filename, 'w') as f:
#         result = 'Keyword, Count\n'
#         for ele in sorted(dict):
#             result += (str(ele) + "," + str(dict[ele]) + "\n")
#         f.writelines(result)

def classifySubjects(csvFile="./allDutch.csv"):
    dict = {}
    with open(csvFile) as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        for row in data[1:]:
            ele = row[6].strip().rstrip(',')
            if ele == None or ele == '' or ele == 'undefined':
                continue
            # ele = ele.replace(',', '|')
            eles = ele.split(',')
            for element in eles:
                if element in dict:
                    dict[element] += 1
                else:
                    dict[element] = 1
    for element in sorted(dict):
        print element, dict[element]
    ele_filename = csvFile[:-4] + "-subject-classified.csv"
    print("create subject file:" + ele_filename)
    with open(ele_filename, 'w') as f:
        result = 'Subject, Count\n'
        for ele in sorted(dict):
            result += (str(ele) + "," + str(dict[ele]) + "\n")
        f.writelines(result)

# extractAuthor("allDutch.csv")
# extractAuthor("English_MMW_1580 1720.csv")
# extractSubjects("allDutch.csv")
# extractSubjects("English_MMW_1580 1720.csv")
# classifySubjects("allDutch-subject.csv")
# classifySubjects("English_MMW_1580 1720-subject.csv")

def extractKeyWord(csvFile = "./allDutch.csv",keywords=["Company", "Companies", "Compagnie", "Corporation","Corporations"]):
    dict = {}
    with open(csvFile) as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        for row in data[1:]:
            ele = row[6].strip().rstrip(',')
            if ele == None or ele == '' or ele == 'undefined':
                continue
            ele = ele.replace(',', ' ')
            # eles = ele.split(",")
            # for element in eles:
            for key in keywords:
                if key in ele:
                    if ele in dict:
                        dict[ele] += 1
                    else:
                        dict[ele] = 1
    for ele in sorted(dict):
        print ele, dict[ele]
    ele_filename = csvFile[:-4] + "-subject-keywords-"+keywords[0]+".csv"
    print("create subject file:" + ele_filename)
    with open(ele_filename, 'w') as f:
        result = 'Key:' + keywords[0] + ', Count\n'
        for ele in sorted(dict):
            result += (str(ele) + "," + str(dict[ele]) + "\n")
        f.writelines(result)

# special for deuth
def extractKeyWordClassiefied(csvFile = "./allDutch.csv",keywords=["Company", "Companies", "Compagnie", "Corporation","Corporations"]):
    dict = {}
    with open(csvFile) as f:
        data = [row for row in csv.reader(f.read().splitlines())]
        for row in data[1:]:
            ele = row[6].strip().rstrip(',')
            if ele == None or ele == '' or ele == 'undefined':
                continue
            #ele = ele.replace(',', ' ')
            eles = ele.split(",")
            for element in eles:
                for key in keywords:
                    if key in element:
                        if element in dict:
                            dict[element] += 1
                        else:
                            dict[element] = 1
    for ele in sorted(dict):
        print ele, dict[ele]
    ele_filename = csvFile[:-4] + "-subject-keywords-"+keywords[0]+".csv"
    print("create subject file:" + ele_filename)
    with open(ele_filename, 'w') as f:
        result = 'Key:' + keywords[0] + ', Count\n'
        for ele in sorted(dict):
            result += (str(ele) + "," + str(dict[ele]) + "\n")
        f.writelines(result)

extractKeyWord("./English_MMW_1580 1720.csv")
extractKeyWordClassiefied()
classifySubjects("./English_MMW_1580 1720.csv")