import requests
import json

def emotion_detector(text_to_analyze:str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url,json= input_json, headers= headers)
    data = response.json()
    result = data['emotionPredictions'][0]['emotion']

    max_value = 0
    max_emotion = ''

    for key,value in result.items():
        if value >  max_value:
            max_value = value
            max_emotion = key     

    result['dominant_emotion'] = max_emotion
    return result