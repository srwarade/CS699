##
#@file 
#file description
#


from flask import Flask ,render_template, request
import os

app = Flask(__name__) 

@app.route('/') 
def render():
    """!render() function helps in rendering index.html file.
	@param None : No Argument
	
	@return render_template : index.html file
	"""
    return render_template('index.html')
    
@app.route('/speak2',methods=['POST'])
def speak2():
    """!speak2() function opens and write commands to the file input.txt .
	@param None : No Argument
	
	@return System call : festival system call with input.txt file as argument
	"""
    speech = request.form['speech']
    with open('input.txt', 'w') as f:

        f.write('(voice_hindi_NSK_diphone)\n')
        f.write('(SayText "')
        f.write(speech)
        f.write('")')
    return os.system("festival input.txt")

  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4443, debug = True)