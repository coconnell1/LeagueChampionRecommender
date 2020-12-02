#This tutorial was built by me, Farzain! You can ask me questions or troll me on Twitter (@farzatv)

#First we need to import requests. Installing this is a bit tricky. I included a step by step process on how to get requests in readme.txt which is included in the file along with this program.
import requests, sys, threading, time, queue

def makeRequest(requestURL):
    statusCode = 0
    while statusCode < 200 or statusCode >= 300:
        response = requests.get(requestURL);
        statusCode = response.status_code
        if(statusCode >= 500 and statusCode < 600):
            time.sleep(2)
        elif(statusCode == 429):
            time.sleep(int(response.headers["Retry-After"]))
        elif(statusCode >= 400 and statusCode <500):
            print("ERROR CODE RETURNED:  " + str(statusCode))
            print("URL THAT RETURNED ERROR:  " + requestURL)
            return statusCode

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
    print(region + ": " + str(matchId))
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
        # see updating as it progresses
        #print("\n Team W/L: " + str(win))
        #print("\n Team Champion Ids: " + str(champIdArray))


def analyzePlayer(region, APIKey, player, analyzedMatches, outputQueue):
    summonerName = player["summonerName"]
    #print(summonerName)

    # print("\n Encrypted ID")
    encryptedID = requestEncryptedID(region, summonerName, APIKey)['accountId']
    # print("\n Encrypted ID: " + encryptedID)

    if(type(encryptedID) == str):
        # print("\n Matches for ID")
        response = requestMatchID(region, encryptedID, APIKey)
        if type(response) == dict:
            matchList = response["matches"]

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


def analyzeRegion(region, APIKey, outputQueue):
    analyzedMatches = set()

    challengerLeague = requestChallengerLeague(region, APIKey)
    if(type(challengerLeague) == dict):
        analyzeLeague(region, APIKey, challengerLeague, analyzedMatches, outputQueue)


def threadsStillRunning(threads):
    running = False
    for t in threads:
        if t.is_alive():
            running = True
    return running


def printToFile():
    # Change to own machine
    filename = r'D:\Classes\COMP 490\LeagueChampionRecommender\Tut\leagueChampData.txt'
    with open(filename, 'w') as file_object:
        file_object.write(str(win) + str(champIdArray))


def main():

    regions = ["na1", "br1", "eun1", "euw1", "jp1", "kr", "la1", "la2", "oc1", "tr1", "ru"]
    regionThreads = []
    APIKey = "RGAPI-f1b010ee-8c01-4dc5-9f2b-572e67d643f3"
    outputQueue = queue.Queue()

    for r in regions:
        t = threading.Thread(target=analyzeRegion, args=(r,APIKey,-1))
        t.start();
        regionThreads.insert(-1, t)

    while(threadsStillRunning(regionThreads) or not outputQueue.empty()):
        printToFile(outputQueue.get())


if __name__ == "__main__":
    main()