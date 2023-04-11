import speech_recognition
import pyttsx3

def to_speech(message):
	text_engine.say(message)
	text_enghine.runAndWait()


if __name__ == "__main__":
	text_engine = pyttsx3.init()
	speech_engine = speech_recognition.Recognizer()

	user_input = ""

	while user_input != "exit":

		try:
			with speech_recognition.Microphone() as input_source:
				speech_engine.adjust_for_ambient_noise(input_source, duration = 0.2)
				input_audio = speech_engine.listen(input_source)
				print("hello")
				to_text = speech_engine.recognize_google(input_audio)
				user_inpt = to_text.lower()
				print(user_input)

		except speech_recognition.RequestError:
			continue

		except speech_recognition.UnknownValueError:
			continue


