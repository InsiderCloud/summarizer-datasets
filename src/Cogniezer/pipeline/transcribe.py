import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
from Cogniezer.logging import logger

# Load environment variables from .env file
load_dotenv()

# Access the Azure key from the environment
azure_key = os.getenv("AZURE_KEY")
azure_region = os.getenv("AZURE_REGION")

class TranscribePipeline:
    """
    Transcribe class
    """

    def __init__(self):
        pass

    def transcribe(self,audio_file):
        """
        Transcribe function
        """
        logger.info("Transcribing audio file")
        speech_config = speechsdk.SpeechConfig(subscription=azure_key, region=azure_region)
        audio_config = speechsdk.AudioConfig(filename=audio_file)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        result = speech_recognizer.recognize_once_async().get()
        logger.info("Transcription completed")
        return result.text