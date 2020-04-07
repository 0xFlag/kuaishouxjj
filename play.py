from  flask import Flask, render_template
import random
import linecache

app = Flask(__name__)

@app.route('/')
def index():
	txt = open(r'./templates/ks.txt','rb')
	data = txt.read().decode('utf-8')
	txt.close()
	n = data.count('\n')
	i = random.randint(1, (n+1))
	line = linecache.getline(r'./templates/ks.txt',i)
	video_src = line
	return render_template('player.html',video_path=video_src)

if __name__ == '__main__':
	app.run()