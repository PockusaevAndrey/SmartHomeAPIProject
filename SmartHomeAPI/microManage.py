import speech_recognition


def find_micros():
    return speech_recognition.Microphone.list_microphone_names()


class HomeAudio:
    def __init__(self):
        self._mic = speech_recognition.Microphone()
        self._recognizer = speech_recognition.Recognizer()

    def start_listen(self, recognition):
        with self._mic as audio_file:
            print("Speak Please")

            self._recognizer.adjust_for_ambient_noise(audio_file)
            audio = self._recognizer.listen(audio_file)

            print("Converting Speech to Text...")
            try:
                title: str = self._recognizer.recognize_google(audio, language='ru-RU')
                self._searchOfMatches(title, recognition)

            except Exception as e:
                print("Error: " + str(e))

    @staticmethod
    def _searchOfMatches(title, recognizer):
        for i in range(len(recognizer.commandlist)):
            if recognizer.commandlist[i].upper() in title.upper():
                print(recognizer.answerlist[i])
