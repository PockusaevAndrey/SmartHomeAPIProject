from SmartHomeAPI import commands, microManage

microManage.find_micros()

recognizer = commands.CommandRecognition()
home = microManage.HomeAudio()

recognizer.addcommand('Привет', 'Здравствуйте')

home.start_listen(recognizer)
