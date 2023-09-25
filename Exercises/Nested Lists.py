if __name__ == '__main__':
    records = []
    scoreList = []
    for _ in range(int(input())):  # number of students (first input)
        name = input()
        score = float(input())
        records.append([name, score])
        scoreList.append(score)
    sortedScores = sorted(set(scoreList))  # sorts scoreList from least to greatest, overrides duplicates
    namesList = sorted([x[0] for x in records if x[1] == sortedScores[1]])
    # for each index of records at position of 1, if that score == sorted scores at 1 add to namesList
    # sorted at beginning just organizes alphabetical order
    for name in namesList:
        print(name)

    # print(records)
    # print(scoreList)
    # print(sortedScores)
    # print(namesList)
