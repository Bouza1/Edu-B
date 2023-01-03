from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
import csv
import re

Window.clearcolor = "#ffffff"
Window.size = (700, 700)

global user

class LoadScreen(Screen):
    userName = ObjectProperty(None)
    userAge = ObjectProperty(None)

    def playBtn(self):
        userName = self.userName.text
        userAge = self.userAge.text
        global user
        user = [userName, userAge]
        print(user)
        sm.current = "MainMenuScreen"


class MainMenuScreen(Screen):

    def highScoreButton(self):
        highScoreBoard().open()

    def spellingBBtn(self):
        sm.current = "SpellingBScreen"
        print(user)

    def mathsBBtn(self):
        sm.current = "MathsBScreen"
        print("test")



class SpellingBScreen(Screen):
    pass


class MathsBScreen(Screen):
    pass


class highScoreBoard(ModalView):
    def highScoreBoardOpenSeq(self):
        global highScores
        highScores = {}

        global scoreOrder
        scoreOrder = []

        global scoreLblList
        scoreLblList = []

        with open('scores.csv', 'r') as file:
            filecontent = csv.reader(file)
            for i in filecontent:
                highScores.update({(i[0]): (i[1])})
                scoreOrder.append(i[1])

        scoreOrder.sort()
        scoreOrder.reverse()

        def get_key(val):
            for key, value in highScores.items():
                if val == value:
                    x = (key, value)
                    return x

        for i in range(len(highScores)):
            result = get_key(scoreOrder[i])
            scoreLblList.append(result)

        global letterList

        nameList = [self.ids.highname1, self.ids.highname2, self.ids.highname3, self.ids.highname4, self.ids.highname5]
        scoreList = [self.ids.highscore1, self.ids.highscore2, self.ids.highscore3, self.ids.highscore4,
                     self.ids.highscore5]
        for i in range(5):
            highScorer1to5 = str(scoreLblList[i])
            highScorer1to5Formatted = re.sub("[(',)]", '', highScorer1to5)
            splitted = highScorer1to5Formatted.split()
            scoreList[i].text = splitted[1]
            nameList[i].text = splitted[0]


class CorrectGuess(ModalView):
    # CorrectGuess().open()
    def resetGameSeq(self):
        print("Reset Button")

class InCorrecrGuess(ModalView):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

sm = WindowManager()
sm.add_widget(LoadScreen(name='LoadScreen'))
sm.add_widget(MainMenuScreen(name='MainMenuScreen'))
sm.add_widget(SpellingBScreen(name='SpellingBScreen'))
sm.add_widget(MathsBScreen(name='MathsBScreen'))


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
