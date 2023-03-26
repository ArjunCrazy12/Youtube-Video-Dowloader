from flask import Flask, render_template, request, redirect,url_for
from pytube import YouTube

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Users/Arjun/Downloads'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    choice = request.form['choice']
    message = ''
    if choice == 'video':
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4').first()
        video.download('C:/Users/Arjun/Downloads')
        message = 'Video download successful!'
    elif choice == 'audio':
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download('C:/Users/Arjun/Downloads')
        message = 'Audio download successful!'
    else:
        message = 'Invalid choice.'
    return redirect(url_for('status', message=message))

@app.route('/status')
def status():
    message = request.args.get('message')
    return render_template('status.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
