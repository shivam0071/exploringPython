#Just Type all these in interactive Shell

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=YcKACsvp6Ck")
yt.title
yt.streams.all() #Choose a stream 
stream = yt.streams.first() #lets take 1st for example
stream.download() #You can give a path here


