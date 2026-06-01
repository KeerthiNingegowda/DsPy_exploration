import os
from dotenv import load_dotenv
from openai import OpenAI
import logging
import http.cookiejar
import requests

logger = logging.getLogger(__name__)

from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

COOKIE_PATH = os.path.join(os.getcwd(), "youtube_cookies.txt")

#DAILY QUOTA LIMIT - 10K

def get_channel_id(channel_name:str) -> str:
    """ Resolve channel name to channel id
        Args:-
            channel_name - Channel of interest
        Returns:-
            channel_id
        Be cautious - This costs around 100 units per call
    """
    response = youtube.search().list(q=channel_name,
                                     type="channel",
                                     part="id",
                                     maxResults=1).execute()
    items = response.get("items", [])
    if not items:
        return None
    return items[0]["id"]["channelId"]

def get_recent_videos(channel_id:str, max_results:int=3) -> list:
    """ Given a channel id return most recent results.
        Args:-
            channel_id - Channel id
            max_results - Maximum results to fetch from youtube

        Returns:- 
            A list consisting of metadata related to videos - like video id, title, published time, description

            Be cautious - This costs around 100 units per call

    """

    response = youtube.search().list(channelId=channel_id, type="video", part="id,snippet", order="date", maxResults=max_results).execute()
    videos = []
    for item in response.get("items", []):
        videos.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "published_at": item["snippet"]["publishedAt"],
            "description":item["snippet"]["description"]
        })
    return videos

def get_transcript(video_id:str) -> str:
    """ Get transcript for a video
        Args:-
            video_id - video id
        Returns video transcipt
    """
    try:
        session = requests.Session()
        cookie_jar = http.cookiejar.MozillaCookieJar(COOKIE_PATH)
        cookie_jar.load(ignore_discard=True, ignore_expires=True)
        session.cookies = cookie_jar

        ytt_api = YouTubeTranscriptApi(http_client=session)
        transcript = ytt_api.fetch(video_id)
        #print(ytt_api.fetch("dQw4w9WgXcQ"))
        return " ".join([entry.text for entry in transcript])
    except Exception as e:
        logger.warning(str(e))
        return "Cant get transcription for this video"
    
def get_transcript_summary(title:str, transcript:str) -> str:
    """ Summarize a given youtube transcript based on use preferences
        Args:- 
            title - Video title
            transcript - Video transcript
        Returns 
            A summary of the said transcript
    """
    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
    response = client.responses.create(
    model="gpt-4o-mini",
    max_output_tokens=500,
    input=f""" You will be given a youtube video transcript and its title. Your role is to organize and summarize the content in the following format:-
    1) Title 2) The problem that is being discussed in the video and any historical context associated with it
    3) Key topics covered and key takeaways from the discussions 4) Any limitations discussed.
    The heart of the content are sections 2 and 3. So dedicate most of the tokens there. Do not abruptly end the summary.
    The title and the transcript are as follows {title} {transcript}""")

    return response.output_text

def get_youtube_summaries(channel_metadata:list) -> dict:

    results = dict()

    for channel in channel_metadata:
        try:
            if len(channel["channel_id"]) != 0:
                channel_id = channel["channel_id"]
            else:
                channel_id = get_channel_id(channel["name"])
                if not channel_id:
                    results[channel["name"]] = "Results not Found"
                    continue

            videos = get_recent_videos(channel_id)
            channel_summaries = []

            for video in videos:
                transcript = get_transcript(video["video_id"])
                if transcript:
                    summary = get_transcript_summary(video["title"], transcript)
                else:
                    summary = "Transcript not available for this video"

                channel_summaries.append({
                        "title":video["title"],
                        "published_at":video["published_at"],
                        "summary":summary,
                        "url": f"https://youtube.com/watch?v={video['video_id']}"
                    })

                results[channel["name"]] = channel_summaries

        except Exception as e:
            logger.error(f"Failed to process channel {channel['name']}")
            results[channel["name"]] = f"Error:{str(e)}"

    return results

