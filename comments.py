import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')


class GEMINI:

    def __init__(self, _api_key, _model_name):
        
        self.api_key = _api_key
        self.response = None
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(_model_name)




    def set_text(self,_req_text):
        self.response = self.model.generate_content(_req_text)

    def get_text(self):
        return self.response.text

