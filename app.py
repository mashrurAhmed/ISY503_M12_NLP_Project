from flask import Flask, make_response, jsonify, request
import tensorflow as tf
import tensorflow_hub as hub
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

loaded_model = tf.keras.models.load_model(r'saved_model.h5', custom_objects={'KerasLayer': hub.KerasLayer})


@app.route('/')
def index():
    return "Welcome to Golab REST API"



@app.route('/api/analyse', methods=['POST'])
def analyse():
    data = request.get_json()
    resp = {}
    

    resp.update({"length": len(data['content'])})
    resp.update({"content": data['content']})
    
    # add model here
    prediction = loaded_model.predict([data['content']])
    prediction = prediction[0][0].astype("float")
    prediction = round(prediction, 2)
    resp.update({"positive": prediction})
    resp.update({"negative": round(1 - prediction, 2)})
    resp.update({"prediction": prediction})
    if prediction < 0.4:
      tensor_flow = 'negative'
    elif prediction > 0.6:
      tensor_flow = 'positive'
    else:
      tensor_flow = 'neutral'
    
    #this value is the thresh hold value beyound this we can determine if the sentiment is positive or not
    resp.update({"threshold": 0.5})

    resp.update({"overall": tensor_flow})
    print(resp)
    return jsonify(resp)
    

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)