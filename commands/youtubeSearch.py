from googleapiclient.discovery import build
from dotenv import load_dotenv

import os

def config(nome):
    load_dotenv()

    DEVELOPER_KEY = os.getenv("GOOGLE_DEVELOPER_KEY")
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    CONFIG = {
        "DEVELOPER_KEY": DEVELOPER_KEY, 
        "YOUTUBE_API_SERVICE_NAME":YOUTUBE_API_SERVICE_NAME, 
        "YOUTUBE_API_VERSION":YOUTUBE_API_VERSION}

    #print(CONFIG[nome])
    return CONFIG[nome]



def youtube_search(frase):
    youtube = build(config("YOUTUBE_API_SERVICE_NAME"), config("YOUTUBE_API_VERSION"),
                    developerKey=config("DEVELOPER_KEY"))

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=frase,
        part="id,snippet",
        maxResults=25
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
          videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 "https://youtube.com/watch?v={}".format(search_result["id"]["videoId"])))

    print("Videos:\n", "\n".join(videos), "\n")

    return videos

youtube_search("save me")
