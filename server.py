'''
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on 
localhost:5000
'''
# Import Flask, render_template, request from the Flask framework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotiondetector():
    '''
    This code receives the text from the HTML interface
    and runs emotion detection over it using emotion_detector()
    function. The output returned shows various emotions and their
    score along with dominant emotion     
    '''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the value is None for all key, indicating an error or invalid input
    if all(v == 'None' for v in response.values()):
        return "Invalid input! Try again." 
    
    # format the response
    formatted_response =", ".join([f"'{k}': {v}" for i, (k,v) in enumerate(response.items()) if i < len(response.items()) - 1])

    return f"For the given statement, the system response is {formatted_response}. \
    The dominat emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main 
    application page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)