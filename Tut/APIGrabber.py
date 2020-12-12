#This tutorial was built by me, Farzain! You can ask me questions or troll me on Twitter (@farzatv)

#First we need to import requests. Installing this is a bit tricky. I included a step by step process on how to get requests in readme.txt which is included in the file along with this program.
import requests, threading, time, queue

def makeRequest(requestURL):
    statusCode = 0
    while statusCode < 200 or statusCode >= 300:
        try:
            response = requests.get(requestURL);
            statusCode = response.status_code
            if statusCode >= 500 and statusCode < 600:
                time.sleep(2)
            elif statusCode == 429:
                if "Retry-After" in response.headers:
                    time.sleep(int(response.headers["Retry-After"]))
                else:
                    time.sleep(.5)
            elif statusCode >= 400 and statusCode <500:
                print("ERROR CODE RETURNED:  " + str(statusCode))
                print("URL THAT RETURNED ERROR:  " + requestURL)
                return statusCode
        except:
            print("Socket Error!")

    return response.json();

def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    return makeRequest(URL)

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + ID + "?api_key=" + APIKey
    return makeRequest(URL)

def requestChallengerLeague(region, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5" "?api_key=" + APIKey
    return makeRequest(URL)

def requestGrandMasterLeague(region, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5" "?api_key=" + APIKey
    return makeRequest(URL)

def requestMasterLeague(region, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5" "?api_key=" + APIKey
    return makeRequest(URL)

def requestEncryptedID(region,summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    return makeRequest(URL)

def requestMatchID(region,encryptedID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedID + "?api_key=" + APIKey
    return makeRequest(URL)

def requestMatchDetails(region,matchId,APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + matchId + "?api_key=" + APIKey
    return makeRequest(URL)


def analyzeMatch(region, APIKey, matchId, outputQueue):
    #print(region + ": " + str(matchId))
    matchDetails = requestMatchDetails(region, str(matchId), APIKey)

    if type(matchDetails) == dict:
        win = ""
        blueTeamChampIds = []
        redTeamChampIds = []

        # print(matchDetails)

        if matchDetails["teams"][0]["win"] == 'Win':
            win = "blue"
        else:
            win = "red"

        for p in matchDetails["participants"]:
            if p["teamId"] == 100:
                blueTeamChampIds.append(p["championId"])
            else:
                redTeamChampIds.append(p["championId"])

        result = [region, str(matchId), win]
        for c in blueTeamChampIds:
            result.append(str(c))
        for c in redTeamChampIds:
            result.append(str(c))
        outputQueue.put(result)
        # see updating as it progresses
        #print("\n Team W/L: " + str(win))
        #print("\n Team Champion Ids: " + str(champIdArray))


def analyzePlayer(region, APIKey, player, analyzedMatches, outputQueue):
    summonerName = player["summonerName"]
    #print(summonerName)

    # print("\n Encrypted ID")
    result = requestEncryptedID(region, summonerName, APIKey)
    # print("\n Encrypted ID: " + encryptedID)
    if type(result) == dict:
        encryptedID = result['accountId']
        if(type(encryptedID) == str):
            # print("\n Matches for ID")
            response = requestMatchID(region, encryptedID, APIKey)
            if type(response) == dict:
                matchList = response["matches"][:1000]

                for m in matchList:
                    matchId = m["gameId"]
                    if matchId not in analyzedMatches:
                        analyzedMatches.add(matchId)
                        analyzeMatch(region, APIKey, matchId, outputQueue)


def analyzeLeague(region, APIKey, league, analyzedMatches, outputQueue):
    players = league["entries"]
    for p in players:
        if(type(p) == dict):
            analyzePlayer(region, APIKey, p, analyzedMatches, outputQueue)


def analyzeRegion(region, APIKey, analyzedMatches, outputQueue):
    challengerLeague = requestChallengerLeague(region, APIKey)
    if(type(challengerLeague) == dict):
        analyzeLeague(region, APIKey, challengerLeague, analyzedMatches, outputQueue)
    grandMasterLeague = requestGrandMasterLeague(region, APIKey)
    if (type(grandMasterLeague) == dict):
        analyzeLeague(region, APIKey, grandMasterLeague, analyzedMatches, outputQueue)
    masterLeague = requestMasterLeague(region, APIKey)
    if (type(masterLeague) == dict):
        analyzeLeague(region, APIKey, masterLeague, analyzedMatches, outputQueue)
    print("Done with Challenger league from " + region)


def threadsStillRunning(threads):
    running = False
    for t in threads:
        if t.is_alive():
            running = True
    return running


def printToFile(game, file):
    with open(file, 'a') as gameDataFile:
        gameDataFile.write(", ".join(game))
        gameDataFile.write("\n")

def parseLine(line, regionMatches):
    parsedLine = line.split(", ")
    regionMatches[parsedLine[0]].add(int(parsedLine[1]))
    #print("Adding existing match with region: " + parsedLine[0] + " And ID: " + parsedLine[1])

def parseExistingMatches(regionMatches, filename):
    file = open(filename, "r")
    line = file.readline()
    while line != "":
        parseLine(line, regionMatches)
        line = file.readline()


def main():
    regionMatches = {
        "na1": set(),
        "br1": set(),
        "eun1": set(),
        "euw1": set(),
        "jp1": set(),
        "kr": set(),
        "la1": set(),
        "la2": set(),
        "oc1": set(),
        "tr1": set(),
        "ru": set()
    }
    regionThreads = []
    APIKey = "RGAPI-3eabc4f5-bf79-4161-b7e3-1b14ef7e27b0"
    # Change to own machine
    filename = r'D:\Classes\COMP 490\LeagueChampionRecommender\Tut\leagueChampData.txt'
    outputQueue = queue.Queue()

    parseExistingMatches(regionMatches, filename)

    for r in regionMatches.keys():
        t = threading.Thread(target=analyzeRegion, args=(r,APIKey,regionMatches[r],outputQueue))
        t.start()
        regionThreads.insert(-1, t)

    while(threadsStillRunning(regionThreads) or not outputQueue.empty()):
        game = outputQueue.get()
        if type(game) == list:
            printToFile(game, filename)


if __name__ == "__main__":
    main()