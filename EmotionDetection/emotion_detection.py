# import the requests library to handle HTTP requests
import requests
import json

# define a function that analyzes the emotion of the input text
def emotion_detector(text_to_analyze):
    """
    this function takes string input 
    analyzes the emotion of the input text
    output emotion
    """

    # url of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # set the header required for the API request response
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # dictionary with the text to be analyzed
    myobj = {"raw_document" : {"text": text_to_analyze}}

    # send a post request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    # if the response status code 200, then extract the dominant emotion
    if response.status_code == 200:
        # Parsing the json response from the API
        formatted_response = json.loads(response.text)

        # extracting emotions (label and scores)
        emotions = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
    
        # extracting detail for emotion with highest score
        max_emotion_label = max(emotions, key=emotions.get)    
        max_emotion_score = emotions[max_emotion_label]
    
        # updating emotion collection dominal emotion label
        emotions['dominant_emotion'] = max_emotion_label
    # if the response status code is 500, set label and score to None
    elif response.status_code == 400:
        # set value for all keys to 'None'
        emotions = {
            
        }


    return emotions