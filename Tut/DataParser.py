import requests

def main():
    championCompScalings = [
        [0.40, 0.14, 0.40, 0.29, 0.50],
        [0.44, 0.53, 0.15, 0.34, 0.25],
        [0.35, 0.55, 0.14, 0.24, 0.45],
        [0.58, 0.20, 0.48, 0.20, 0.20],
        [0.70, 0.50, 0.24, 0.14, 0.14],
        [0.29, 0.25, 0.38, 0.29, 0.42],
        [0.39, 0.67, 0.20, 0.20, 0.20],
        [0.39, 0.20, 0.62, 0.25, 0.29],
        [0.34, 0.58, 0.20, 0.39, 0.25],
        [0.42, 0.42, 0.29, 0.34, 0.16],
        [0.44, 0.20, 0.53, 0.29, 0.20],
        [0.38, 0.47, 0.29, 0.34, 0.25],
        [0.24, 0.75, 0.14, 0.29, 0.09],
        [0.70, 0.29, 0.09, 0.45, 0.14],
        [0.29, 0.34, 0.51, 0.29, 0.25],
        [0.34, 0.11, 0.44, 0.53, 0.29],
        [0.48, 0.44, 0.20, 0.11, 0.48],
        [0.40, 0.14, 0.70, 0.19, 0.24],
        [0.44, 0.20, 0.53, 0.34, 0.15],
        [0.29, 0.11, 0.48, 0.53, 0.29],
        [0.48, 0.15, 0.44, 0.15, 0.48],
        [0.48, 0.53, 0.15, 0.20, 0.34],
        [0.34, 0.29, 0.42, 0.42, 0.21],
        [0.40, 0.07, 0.84, 0.07, 0.07],
        [0.39, 0.48, 0.20, 0.25, 0.39],
        [0.29, 0.53, 0.15, 0.39, 0.34],
        [0.34, 0.53, 0.20, 0.15, 0.48],
        [0.29, 0.19, 0.19, 0.75, 0.24],
        [0.53, 0.39, 0.39, 0.25, 0.15],
        [0.06, 0.06, 0.06, 0.06, 1.00],
        [0.29, 0.62, 0.15, 0.15, 0.44],
        [0.47, 0.25, 0.34, 0.38, 0.25],
        [0.48, 0.11, 0.39, 0.39, 0.39],
        [0.34, 0.20, 0.44, 0.25, 0.48],
        [0.47, 0.25, 0.21, 0.34, 0.38],
        [0.38, 0.51, 0.34, 0.34, 0.16],
        [0.53, 0.25, 0.20, 0.25, 0.44],
        [0.44, 0.62, 0.25, 0.15, 0.25],
        [0.25, 0.25, 0.42, 0.42, 0.34],
        [0.25, 0.21, 0.38, 0.34, 0.51],
        [0.48, 0.39, 0.11, 0.11, 0.58],
        [0.34, 0.44, 0.53, 0.25, 0.15],
        [0.15, 0.11, 0.53, 0.48, 0.44],
        [0.60, 0.60, 0.14, 0.09, 0.24],
        [0.35, 0.40, 0.09, 0.09, 0.70],
        [0.19, 0.09, 0.09, 0.70, 0.60],
        [0.25, 0.58, 0.15, 0.44, 0.25],
        [0.45, 0.09, 0.70, 0.24, 0.24],
        [0.48, 0.29, 0.58, 0.11, 0.20],
        [0.44, 0.25, 0.58, 0.11, 0.29],
        [0.15, 0.15, 0.44, 0.53, 0.44],
        [0.34, 0.25, 0.34, 0.51, 0.25],
        [0.29, 0.53, 0.11, 0.25, 0.53],
        [0.53, 0.53, 0.11, 0.29, 0.25],
        [0.39, 0.11, 0.58, 0.11, 0.53],
        [0.44, 0.53, 0.25, 0.15, 0.34],
        [0.67, 0.25, 0.25, 0.15, 0.34],
        [0.25, 0.67, 0.15, 0.20, 0.44],
        [0.39, 0.25, 0.53, 0.25, 0.25],
        [0.44, 0.53, 0.11, 0.11, 0.53],
        [0.18, 0.06, 0.94, 0.06, 0.06],
        [0.25, 0.58, 0.11, 0.20, 0.53],
        [0.40, 0.70, 0.19, 0.19, 0.14],
        [0.53, 0.53, 0.25, 0.29, 0.11],
        [0.29, 0.46, 0.07, 0.35, 0.07],
        [0.75, 0.40, 0.09, 0.09, 0.29],
        [0.44, 0.20, 0.44, 0.20, 0.39],
        [0.15, 0.11, 0.53, 0.53, 0.39],
        [0.39, 0.48, 0.20, 0.53, 0.11],
        [0.62, 0.53, 0.20, 0.25, 0.11],
        [0.29, 0.67, 0.25, 0.25, 0.20],
        [0.42, 0.38, 0.34, 0.29, 0.25],
        [0.34, 0.29, 0.53, 0.11, 0.44],
        [0.75, 0.14, 0.09, 0.35, 0.19],
        [0.29, 0.15, 0.44, 0.29, 0.48],
        [0.25, 0.53, 0.48, 0.34, 0.11],
        [0.21, 0.34, 0.38, 0.42, 0.34],
        [0.29, 0.20, 0.39, 0.29, 0.53],
        [0.47, 0.42, 0.34, 0.21, 0.25],
        [0.58, 0.39, 0.25, 0.39, 0.11],
        [0.15, 0.48, 0.25, 0.53, 0.29],
        [0.24, 0.75, 0.09, 0.09, 0.35],
        [0.29, 0.39, 0.48, 0.44, 0.11],
        [0.29, 0.58, 0.29, 0.25, 0.25],
        [0.62, 0.20, 0.29, 0.39, 0.15],
        [0.67, 0.39, 0.25, 0.25, 0.20],
        [0.35, 0.70, 0.09, 0.19, 0.29],
        [0.39, 0.15, 0.48, 0.48, 0.20],
        [0.40, 0.84, 0.07, 0.07, 0.07],
        [0.40, 0.75, 0.09, 0.14, 0.24],
        [0.25, 0.44, 0.39, 0.15, 0.53],
        [0.70, 0.45, 0.35, 0.09, 0.09],
        [0.44, 0.53, 0.34, 0.25, 0.15],
        [0.39, 0.67, 0.15, 0.20, 0.25],
        [0.44, 0.44, 0.25, 0.11, 0.48],
        [0.35, 0.75, 0.14, 0.09, 0.29],
        [0.29, 0.45, 0.09, 0.09, 0.70],
        [0.75, 0.14, 0.35, 0.24, 0.14],
        [0.24, 0.09, 0.40, 0.19, 0.70],
        [0.53, 0.53, 0.11, 0.44, 0.25],
        [0.53, 0.53, 0.29, 0.15, 0.20],
        [0.29, 0.39, 0.39, 0.53, 0.11],
        [0.38, 0.25, 0.38, 0.47, 0.21],
        [0.25, 0.21, 0.47, 0.29, 0.42],
        [0.25, 0.51, 0.29, 0.29, 0.38],
        [0.34, 0.39, 0.48, 0.11, 0.39],
        [0.47, 0.21, 0.42, 0.25, 0.34],
        [0.29, 0.29, 0.24, 0.09, 0.70],
        [0.53, 0.11, 0.48, 0.44, 0.11],
        [0.34, 0.39, 0.39, 0.11, 0.48],
        [0.24, 0.84, 0.24, 0.07, 0.07],
        [0.38, 0.25, 0.38, 0.47, 0.21],
        [0.29, 0.11, 0.53, 0.53, 0.25],
        [0.62, 0.29, 0.29, 0.20, 0.29],
        [0.62, 0.39, 0.15, 0.15, 0.39],
        [0.40, 0.75, 0.24, 0.14, 0.14],
        [0.39, 0.15, 0.48, 0.34, 0.29],
        [0.44, 0.53, 0.29, 0.29, 0.15],
        [0.29, 0.58, 0.11, 0.25, 0.44],
        [0.29, 0.25, 0.58, 0.39, 0.20],
        [0.15, 0.44, 0.29, 0.29, 0.53],
        [0.25, 0.67, 0.39, 0.25, 0.11],
        [0.39, 0.11, 0.53, 0.44, 0.20],
        [0.25, 0.34, 0.42, 0.38, 0.29],
        [0.06, 0.06, 0.06, 0.06, 1.00],
        [0.34, 0.58, 0.11, 0.29, 0.34],
        [0.53, 0.39, 0.53, 0.11, 0.15],
        [0.21, 0.34, 0.38, 0.38, 0.34],
        [0.34, 0.11, 0.44, 0.34, 0.48],
        [0.34, 0.34, 0.34, 0.47, 0.16],
        [0.40, 0.09, 0.75, 0.09, 0.24],
        [0.34, 0.42, 0.38, 0.38, 0.16],
        [0.53, 0.29, 0.15, 0.58, 0.15],
        [0.35, 0.75, 0.24, 0.09, 0.14],
        [0.48, 0.15, 0.39, 0.44, 0.20],
        [0.53, 0.20, 0.25, 0.25, 0.44],
        [0.29, 0.44, 0.53, 0.20, 0.25],
        [0.44, 0.58, 0.25, 0.15, 0.25],
        [0.75, 0.45, 0.14, 0.14, 0.14],
        [0.48, 0.20, 0.58, 0.15, 0.29],
        [0.24, 0.24, 0.07, 0.84, 0.07],
        [0.39, 0.58, 0.29, 0.11, 0.29],
        [0.70, 0.14, 0.14, 0.14, 0.55],
        [0.70, 0.14, 0.14, 0.14, 0.55],
        [0.18, 0.07, 0.13, 0.18, 0.90],
        [0.29, 0.25, 0.53, 0.44, 0.20],
        [0.75, 0.50, 0.09, 0.09, 0.09],
        [0.07, 0.79, 0.07, 0.07, 0.46],
        [0.40, 0.07, 0.07, 0.84, 0.07],
        [0.14, 0.29, 0.70, 0.50, 0.09],
        [0.19, 0.60, 0.09, 0.70, 0.09],
        [0.51, 0.38, 0.25, 0.34, 0.21]
    ]

    sourceFileName = r'C:\Users\cobio\Desktop\LeagueChampionRecommender\Tut\leagueChampData.txt'
    targetFileName = r'C:\Users\cobio\Desktop\LeagueChampionRecommender\Tut\ParsedGameData.txt'
    response = requests.get("https://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json").json()
    data = response["data"]
    mappingTable = {}
    dataKeys = list(data.keys())
    for i in range(len(dataKeys)):  #For each champion
        champion = data[dataKeys[i]]
        mappingTable[champion["key"]] = i  #Map each champion "key" to a specific index

    sourceFile = open(sourceFileName, "r")
    targetFile = open(targetFileName, "w")

    uncountableLines = 0

    line = sourceFile.readline().rstrip()
    while(line != ""):
        parsedLine = line.split(", ")
        if(len(parsedLine) == 13):
            resultData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for i in range(len(dataKeys)*2):
                resultData.append(0)

            if parsedLine[2] == "blue":
                resultData[len(resultData) - 1] = 1
            elif parsedLine[2] == "red":
                resultData[len(resultData) - 1] = 0
            else:
                print("ERROR")

            blueCompScores = [0,0,0,0,0]
            redCompScores = [0,0,0,0,0]

            for i in range(3, 8):
                key = parsedLine[i]
                resultData[mappingTable[key]] = 1
                champCompScalings = championCompScalings[mappingTable[key]]
                for i in range(0,5):
                    blueCompScores[i] += champCompScalings[i]

            for i in range(8, 13):
                key = parsedLine[i]
                resultData[mappingTable[key] + len(dataKeys) + 5] = 1
                champCompScalings = championCompScalings[mappingTable[key]]
                for i in range(0, 5):
                    redCompScores[i] += champCompScalings[i]

            for i in range(0, 5):
                resultData[len(dataKeys) + i] = blueCompScores[i]
                resultData[len(dataKeys) * 2 + 5 + i] = redCompScores[i]

            for i in range(len(resultData)):
                resultData[i] = str(resultData[i])

            targetFile.write(", ".join(resultData))
            targetFile.write("\n")

        else:
            uncountableLines += 1

        line = sourceFile.readline().rstrip()

    print(uncountableLines)


if __name__ == "__main__":
    main()