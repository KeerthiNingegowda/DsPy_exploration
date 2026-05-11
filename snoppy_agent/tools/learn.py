import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

logger = logging.getLogger(__name__)

from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

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
            mac_results - Maximum results to fetch from youtube

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
    ytt_api = YouTubeTranscriptApi()
    try:
        transcript = ytt_api.fetch(video_id)
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






if __name__ == "__main__":
    #print(get_transcript("svCnShDvgQg"))
    print(get_transcript_summary("Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam","[music] >> How's everyone doing? It's a full room. Look at this thing. >> [laughter] >> Um okay, let's get started. Um okay. So, here is our, you know, agent. You know, it's got the turn loop, it's got the LM loop. You know, this little example sort of works well enough running on your own machine, but what if we want to sort of deploy these two production backends and, you know, run them on our servers? So, what do we want them to do, right? When they run on our servers, we want them to do, you know, long-running meaningful work. Uh should be durable across turns and and versions of our code, and it should be able to, you know, recover from errors. So, I'm Eric, I'm one of the founders of trigger.dev, and we've been sort of trying to make it easy to deploy these types of agents to production for the last few years. Um what I like about this uh little meme here is, which one is the agent and which one is the human? I think I think. >> [laughter] >> Yeah. Uh yeah. So, uh this talk is sort of about like the fundamental shift that agents are like posing to backend infrastructure and some of the ideas for sort of how to achieve these durable agents. So, before we go into that, I want to do a little history lesson here. Um take a step back and see sort of how we got here. So, the very first dynamic web backend was CGI back in 1993. Anyone here ever done CGI stuff? >> [laughter] >> Cool. Nice. Uh so, the model was really simple. Uh HTTP HTTP request comes in, the server forks a whole new process. Request data goes in, the process does some stuff, and then it writes the response to standard out, and then the process goes away. Go So, it's completely stateless. Um shortly after that, uh PHP came out, which sort of turned into the LAMP stack. Um and oops. Um so, sort of uh the LAMP stack sort of reused the PHP process, right? Um but, it kept sort of the principle that like all you needed to do to create a response was the request, some state from the database, um and then it would do the request. So, the second request would come in, and it would do all the same work again, and it would produce the response. So, this is sort of request plus DB equals the responses sort of became known as the shared nothing architecture, right? So, looking at another way, shared nothing sort of means that the compute layer is stateless, right? There's nothing There's no meaningful state like in the compute. The state is in the in the database, right? So, this became the dominant backend infrastructure for the last 30 years, right? Everything that followed from this, like uh Ruby on Rails, Node.js, serverless, it all follows the same paradigm, right? Um as web applications became more uh you know, complicated and sophisticated, they started performing these like sort of side effects outside of the request and DB life cycle. Um these side effects are async tasks. So, they you know, started out simple, let's send an email, charge a credit card, you know, resize an image. But soon they became sort of these like multi-step side effects, right? That like this process order example here. Um where you sort of do things in sequence, right? Uh you'd quickly run into a problem how to handle failures in something like this, right? So, if send receipt fails, uh you can't just retry the whole process order thing again um without charging the credit card again twice, which is bad. So, about 10 to 15 years ago, workflow and durable execution engines were sort of adopted to solve this problem, right? So, you'd write your code like this now, where you sort of uh wrap every single side effect in like a step that becomes cached as it's uh executed. So, now that, you know, solves the problem nicely. When you call process order for the second time, uh you skip the things you've already done, and then you do the thing that you want to do originally, right? And you don't charge the credit card twice. So, this is uh I call this model sort of the replay model. Um so, it builds durable execution on top of existing like stateless compute architecture, which is I covered was the you know, that's how everything works, right? So, you know, you get this nice side effect of you get this execution history, this audit trail of everything that happened. Um and also by being able to sort of resume to a specific point in time, you can Yeah, you can re- recover from a failure for that, but you can also like wait for something else to happen, right? Um so, you can wait for like a human to do something, and then you can resume execution. Um some of the downsides of this replay system is like because now you sort of have to wrap everything in in these steps, and then everything outside of steps is has to be deterministic, you kind of get this like uh rigid structure. You have to write your code in a certain way, or things break. Um and also like replay journaling uh re- the replay journal versioning is is kind of tricky if you deploy a new version. So, this is sort of the very simple and truncated history of like sort of the state of the world in 2023 when LLMs came out. Um At first, they really fit neatly into this paradigm, right? They would just become another step in a workflow, right? Um they would uh they would classify some text or something, but it was still in this old workflow era, right? Uh not long after that, we sort of got tool calling, and tool calling got good, and we were sort of introduced to the agent loop, right? The big difference there is code is sort of no longer orchestrating the LLM. LLM sort of orchestrates the code, right? So, we're back at our agent loop, right? And like what happens if we uh Yeah, you can see that. Um if you can If basically we want to, you know, make this agent loop durable, and can we do it with this replay model, right? What does that look like? Um so, what does that look like? Every LLM call, right, becomes a a step in in the replay uh journal. Uh every tool call becomes a step. Uh on resume, you know, the function re-executes on top and sort of replays all that stuff, right? Um so, after a single turn of uh the LLM not doing too much, you know, this is sort of what the uh the replay log looks like, right? And as you sort of keep interacting with the agent, the log grows and grows and grows. At a certain point, you might hit into some sort of like fundamental limit of your replay system. Um that could be either like too many actual entries, or it could be like the entries get grow too large. Um but yeah, this sort of kind of falls over once you hit that limit. And sort of uh there's a this measure of like how long agents uh can actually do meaningful work, and apparently it's doubling every 4 to 7 months. So, right now we're on about like a few hours, but like not too long from now we'll be on like multiple days of length as these agents build to actually do meaningful work. So, you know, replay gave us these like sort of durable transactions, but you know, an agent isn't like a transaction, it's like a session, right? And it lasts like as long as the user wants it to last. Uh multi-step workflows are sort of start and end, and sessions keep going for as long as possible. So, if we sort of take a step back and think about what an agent needs to be durable for like from first principles, um I think of it as like an agent sort of has these two halves, right? Um the first half is the context. So, this is all all your your system messages, user messages, tool calls, tool results, assistant responses, right? So, this is all like the actual context, everything that went in and out of the LLM. Um so, this is extremely valuable, obviously. You want to make that durable, right? Um but, you also have this sort of execution layer. And as agents are like more complicated, doing more things, they kind of want a machine, right? They want to be able to do stuff like they could do on your laptop, right? They want to be able to write files, use memory, like create subprocesses. And so, I I we I think of both of these um as super valuable pieces of state, but they can be treated separately. So, the context is first and the most important, and it's just an append-only log of sort of everything that happened, right? Like I said. Um and you can make this log durable using any sort of like primitive that already exists, like a database, object storage, like distributed file system. You know, there's a a ton of like technologies that are coming out that that are specialized in making this sort of thing durable, right? And when that is durable, you When that context log is saved somewhere, now you can have durability across versions of your code, right? So, you upgrade your harness, and you can still use that same context, right? Um maybe the machine crashes, and you can still that saved somewhere, so you can pick up where you left off, right? Um and append-only logs scale really well. Uh but, what about making this sort of execution side durable, right? Uh for these, you know, as I was saying, the types of agents right now that are doing meaningful work, we there's a lot of state that happens in the compute layer that we might want to save. Maybe you've cloned a GitHub repo, you know, you've installed some packages, you've got some data sets in memory, you're running a dev server, right? You sandbox in a subprocess, whatever it is, right? You can't really make that uh durable using a log. And how do we get this to work, right? So, you you have to wait for some amount of time for the next user message, right? And we can't just keep the machine running. It'd be nice, but we can't. It'd be too expensive. So, instead of recreating the execution state from a log, we should use snapshot and restore. So, this allows us to snapshot the machine, shut it down, save it to disk, and then when the user message comes in, we restore it, right? So, this gives us durability across turns. So, when the user goes to lunch, right? We don't have to run the machine the whole time. Uh it allows us to preserve everything that the agent was doing. Uh, and you know, effectively compared to running the machine um, live, it's pretty cheap. So, I think if you combine these two things, then you sort of get a durable agent, right? Um, you've got the context, so you're sort of uh, yeah, you're context durability and execution durability, right? Um, and this also allows you to cover recover from errors. So, one of the whole whole points of having these like durability guarantees is to recover, right? And so, it depends on what happened, what went wrong, you can come recover in different ways. So, say the LLM isn't working for some reason. That never happens, but you never know, it could happen. Um, and it takes a long time to like retry. Maybe it says like wait wait, you know, 15 minutes, so you retry your next message. Well, you don't want to wait in memory, so you snapshot, and then you restore when you can retry. But, if there's something wrong with the machine, uh, maybe you've like shipped a bug, or maybe there's just a an issue with the machine, right? It crashes. You have the context log, and you can recover that. So, I think, you know, for 30 years we sort of had this, uh, stateless compute as the sort of core of back-end infrastructure. And I think agents are sort of forcing this, uh, move to become stateful compute. So, and sort of at the heart of that, I think, is is going to have to be this snapshot and restore, uh, capability. Um, but sort of, you know, this isn't actually new. Um, this is an IBM mainframe from 1966, and it actually has checkpoint and and restore. Um, cuz they would run these super expensive jobs for hours, and, you know, something went wrong, and they could couldn't afford to run it all again, so they would add these like checkpoints into their code, right? Fast forward to 2011, a thing called CRIU was um, developed. It was a way to like suspend and restore a uh, a process like from user space. So, it would basically like inject a process with this like a parasite, basically. And then they would force the process to like dump everything to memory, and then it would remove all the traces of the parasite, and it actually worked. Um, in 2024, we actually shipped this, um, and we've done millions of snapshot restores since. You know, it's transparent to the process, so the process doesn't have to like participate in it, and it's compatible with container runtimes, which is good. So, the downsides are you sort of can only checkpoint like a process. So, if you're doing stuff with like FFmpeg, or like you've got a Chrome instance running, or anything else, right? It sort of doesn't work. Uh, it only captures open files, so if you're working with the file system, it has to be open at the time of snapshot, or you won't get snapshot. And then it also, if you it yeah, it's nice that it's compatible with containers, but once you are compatible with containers, you have to work with registries and push and pull, and then it gets very slow. Uh, so last year we moved to, um, Firecracker micro VMs. And this allows us to sort of snapshot like the entire machine, right? So, everything that's is on a machine on a VM, we can snapshot it, and then we can restore it, and it pick up right where it left off, no matter what was happening in the machine, right? But, if you do that it's sort of, uh, in a naive way, uh, it can be quite expensive. So, say you have a default machine size of 512 megabytes, you know, uh, if you do a snapshot, it's 512 megabytes on disk. So, that's that's not great. Um, so obviously you've got like network network transfer costs, you've got storage costs, and there's a lot of memory there that's not actually being used. Uh, so we actually solved this with, uh, compressing it. Uh, we actually use a a seekable compression. Um, so when we restore, we actually don't restore all the memory pages at once. We actually like capture when it needs to be restored, and just like decompress like that little bit that needs to be um, restored at time. We also have a couple other techniques for layering the snapshot, and we can get the the, um, snapshot down to like 14 megabytes compressed. And that's sort of like a knob you can tweak, and um, depending on how perform what kind of performance you want. Um, you can compress more or less. Um, so that's pretty much all we had to do other than all of that. Um, and once we did that, uh, we we got super fast snapshot and restore times. So, this is a sort of a stupid graph, uh, comparing CRIU and Firecracker, but it's basically the the moral of the story is that snapshots are like slightly under a second, and restores are a couple hundred milliseconds. Um, we've actually bundled all of this into, uh, tool that's going to be open source here soon. Uh, it's called FC Run, or F Crun, depending on who you ask. Um, so this allows you it's like a Docker-like CLI, so you can drop in replacement for like the Docker command, uh, for running containers in in Firecracker VMs, and snapshotting and restoring them. So, for example, um, you can run Alpine, and it's super fast, and you can snapshot running VM, and it's super fast. You can like fork a VM, also very fast. Um, this is a little benchmark for TTI, so basically how long it takes for the VM to become, uh, interactable with the internet. So, this is, uh, but we're doing like 15,000 VM starts per minute. Um, you can almost render, uh, like a video. The the FPS would be about 30 FPS. Um, so it's it's extremely extremely fast. Um, so this is going to be powering sort of our future like compute layer, but it's open source. Um, not yet, but very soon. Um, so kind of back to where we started with our little agent loop here, and, um, we've sort of made it durable now by doing two different things, context log and execution snapshot. So, we got durability across versions, durability across turns, across failures, and I think this will lead to a future of, you know, stateful compute. That's it. Yeah. >> [applause] [music]"
))


# [{'video_id': 'svCnShDvgQg', 'title': 'Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam,
#    Trigger.dev', 'published_at': '2026-05-10T20:00:06Z', 'description': 'Replay-based durability — wrapping every step in a journal, 
#    replaying on recovery, requiring deterministic code — is how ...'}, {'video_id': 'esY99nYXxR4', 'title': 'Hierarchical Memory: Context Management 
#    in Agents — Sally-Ann Delucia', 'published_at': '2026-05-10T19:00:06Z', 'description': 'The naive solution is truncation.
#      The obvious solution is summarization. Neither worked — and the Arize team found out the hard ...'}, 
#      {'video_id': 'ON5LIT0M4do', 'title': 'You can&#39;t just one shot it — Mehedi Hassan, Granola', 'published_at': '2026-05-10T18:00:06Z', 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#'description': "One-shotting is seductive. One line of code for web search. One prompt to serve every user. One deploy and you're done. Granola ..."}]