from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/facebook')
def render_static():
	return render_template('personality.html')
	
if __name__ == '__main__':
	app.run()