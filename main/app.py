from flask import Flask, render_template, request, redirect
import youtube_dl
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/error')
def error():
	return render_template('error.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/fb')
def fb():
	return render_template('facebook.html')


@app.route('/download', methods=["POST", "GET"])
def download():
	url = request.form["url"]
	print("Someone just tried to download", url)
	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		print(url)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")

@app.route('/yt')
def yt():
	return render_template('youtube.html')

@app.route('/downloadyt', methods=["POST", "GET"])
def downloadyt():		
    # Get the YouTube video URL from the form submission
    video_url = request.form['urll']

    # Create a YouTube object from the video URL
    yt = YouTube(video_url)

    # Get the highest quality video stream
    ys = yt.streams.get_highest_resolution()

    # Get the download link for the video
    download_link = ys.url

    # Redirect the user to the download link
    return redirect(download_link)


if __name__ == '__main__':
	app.run(port=80, debug=True)