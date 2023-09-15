import replicate
import argparse
import os
import numpy as np
np.bool = bool
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource
from flask_restful import Api
from flask import jsonify, make_response, send_file
cwd = os.getcwd()
import requests
from bs4 import BeautifulSoup, Comment
import base64
import os
PAT = os.environ.get("PAT")
import re
import random





from flask import Flask, request, jsonify
from flask_cors import CORS
import argparse
import os
cwd = os.getcwd()
import numpy as np
np.bool = bool
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource
from flask_restful import Api
from flask import jsonify, make_response, send_file
import requests
from bs4 import BeautifulSoup, Comment
import base64
import wave
import array
from io import BytesIO
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")
print("key:", openai.api_key)

PAT = os.environ.get("PAT")
print("PAT:", PAT)


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)
metadata = (('authorization', 'Key ' + PAT),)



port = os.environ.get("PORT")
print(port)
if port is None:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    

def get_openai_response(prompt):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
            ],
        temperature=0.1,
        max_tokens=2000,
        top_p=0.95,
    )
    text = response.choices[0].message.content

    print("returning ai text:", text)
    return text













model = None
tokenizer = None
def get_phi_response(prompt):
    global model
    global tokenizer
    if model is None:
        tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5")
        model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True).cuda()
        model = torch.load("phi-1.5-learning_objectives_generator.pt")

    with torch.no_grad():
        batch = tokenizer(prompt, return_tensors='pt', return_attention_mask=False, max_length=2048, truncation=True)
        batch = {k: v.cuda() for k, v in batch.items()}
        with torch.cuda.amp.autocast():
            eos_token_id = tokenizer.eos_token_id
            newline_ids = tokenizer.encode("\n\n", add_special_tokens=False)
            hash_ids = tokenizer.encode("#", add_special_tokens=False)
            hash_ids_2 = tokenizer.encode("##", add_special_tokens=False)
            hash_ids_3 = tokenizer.encode("###", add_special_tokens=False)
            output_tokens = model.generate(**batch, max_new_tokens=110, temperature=1.2, do_sample=True, top_p=0.97, num_return_sequences=1, bad_words_ids=
                                           [[eos_token_id], newline_ids, hash_ids, hash_ids_2, hash_ids_3]
                                           )
            text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

    print("text before split:", text)
    # text = text.split("###Learning Objectives:")[1].strip()
    text = text.split("###Learning Objectives:")[1].strip()
    text = re.sub(r' (?=\d+\.)', '\n', text)
    print("returning ai text:", text)
    return text


def create_app():
    app = Flask(__name__)  # static_url_path, static_folder, template_folder...
    CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*"}})
    api = Api(app)

    @app.route('/learningobjectives', methods=['POST'])
    def generate_learning_objectives():
        lecture = request.json.get('lecture')
        lecture = lecture.replace("\n", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")

        prompt = "###Lecture:\n\n" + lecture[:4500] + "\n\n###Learning Objectives:\n\nDescribe"
        response = get_phi_response(prompt)


        return jsonify({'response': response})


    return app






def start_server():
    print("Starting server...")
    parser = argparse.ArgumentParser()

    #python server.py --host 127.0.0.1 --port 8000 --debug

    # API flag
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="The host to run the server",
    )
    parser.add_argument(
        "--port",
        default=os.environ.get("PORT"),
        help="The port to run the server",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run Flask in debug mode",
    )

    args = parser.parse_args()

    server_app = create_app()

    server_app.run(debug=args.debug, host=args.host, port=args.port)


if __name__ == "__main__":
    start_server()
