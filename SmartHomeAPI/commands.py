class CommandRecognition:
    def __init__(self):
        self.commandlist: list = []
        self.answerlist: list = []

    def addcommand(self, title: str, answer: str):
        self.commandlist.append(title)
        self.answerlist.append(answer)

    def addcommandlist(self, titles: list, answer: list):
        for i in range(len(titles)):
            self.commandlist.append(titles[i])
            self.answerlist.append(answer[i])

    def showcommands(self):
        for i in range(len(self.commandlist)):
            print(self.commandlist[i])
            print(self.answerlist[i])

    def removecommand(self, title: str, answer: list):
        self.commandlist.remove(title)
        self.answerlist.remove(answer)
