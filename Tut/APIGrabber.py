#This tutorial was built by me, Farzain! You can ask me questions or troll me on Twitter (@farzatv)

#First we need to import requests. Installing this is a bit tricky. I included a step by step process on how to get requests in readme.txt which is included in the file along with this program.
import requests, sys, time

def requestSummonerData(region, summonerName, APIKey):

    #Here is how I make my URL.  There are many ways to create these.
    
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    print(URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    #Here I return the JSON we just got.
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + ID + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()

def requestChallenegerLeague(region, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5" "?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()

def requestEncryptedID(region,summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()

def requestMatchID(region,encryptedID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedID + "?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()

def requestMatchDetails(region,matchId,APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + matchId + "?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()



    

def main():


    #I first ask the user for three things, their region, summoner name, and API Key.
    #These are the only three things I need from them in order to get create my URL and grab their ID.

    region = "na1"
    APIKey =  "RGAPI-32022707-b610-4b1a-aa40-a0d53b53e809"

    print("\n Challeneger League")
    responseJSON = requestChallenegerLeague(region, APIKey)

    win = []
    champIdArray = []
    matchesPlayed = []
    matchesCount = 0
    sleepCount = 0
    for e in range(len(responseJSON["entries"])):
        summonerName = responseJSON["entries"][e]["summonerName"]
        print(summonerName)

        #print("\n Encrypted ID")
        responseJSON2 = requestEncryptedID(region, summonerName, APIKey)

        if 'accountId' in responseJSON2:
            encryptedID = responseJSON2['accountId']
            #print("\n Encrypted ID: " + encryptedID)

            #print("\n Matches for ID")
            responseJSON3 = requestMatchID(region, encryptedID, APIKey)

            for m in range(len(responseJSON3["matches"])):
                matchesCount+=1
                print(matchesCount)
                sleepCount+=1
                if sleepCount > 90:
                    time.sleep(50)
                    sleepCount = 0

                matchId = responseJSON3["matches"][m]["gameId"]
                if matchId not in matchesPlayed:
                    matchesPlayed.insert(-1, matchId)
                    #print("\n Game ID: " + str(matchId))

                    #print("\n Match Details")

                    responseJSON4 = requestMatchDetails(region, str(matchId), APIKey)


                    championTeam1Ids = []
                    championTeam2Ids = []

                    if "teams" in responseJSON4:
                        for j in range(len(responseJSON4["teams"])):
                            win.insert(-1, responseJSON4["teams"][j]["win"])


                        for i in range(10):
                            if i < 5:
                                championTeam1Ids.insert(-1, responseJSON4["participants"][i]["championId"])
                            else:
                                championTeam2Ids.insert(-1, responseJSON4["participants"][i]["championId"])
                        champIdArray.insert(-1, championTeam1Ids)
                        champIdArray.insert(-1, championTeam2Ids)

                        # see updating as it progresses
                        #print("\n Team W/L: " + str(win))
                        #print("\n Team Champion Ids: " + str(champIdArray))


    #Change to own machine
    filename = r'C:\Users\cobio\Desktop\LeagueChampionRecommender\leagueChampData.txt'
    with open(filename, 'w') as file_object:
        file_object.write(str(win) + str(champIdArray))


    print("\n Team W/L: " + str(win))
    print("\n Team Champion Ids: " + str(champIdArray))











          #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    #responseJSON  = requestSummonerData(region, summonerName, APIKey)
    
    #ID = responseJSON['id']
    #ID = str(ID)
    #print(ID)
    #responseJSON2 = requestRankedData(region, ID, APIKey)
    #print(responseJSON2[ID][0]['tier'])
    #print(responseJSON2[ID][0]['entries'][0]['division'])
    #print(responseJSON2[ID][0]['entries'][0]['leaguePoints'])

#This starts my program!
if __name__ == "__main__":
    main()

