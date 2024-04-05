import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random

class FallingObject:
    def __init__(self, object_type):
        self.object_type = object_type
        self.image = QPixmap(f"images/{object_type}.png")
        self.x = 0
        self.y = 0
        self.w = 80
        self.h = 80

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)
    
    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(-self.h, 0)

    def is_hit(self, mouse_x, mouse_y):
        if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else:
            return False
    
class FallingObjectsGame(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(800, 600)
        self.arena_w = 600
        self.arena_h = 600
        self.background_image = QPixmap("images/background.jpg") 

        self.fall_speed = 40
        self.falling_objects = []
        self.score = 0

        self.character_image = QPixmap("images/dinosaur.png") 
        self.character_x = 600
        self.character_y = 300

        self.quote = QPixmap("images/quote.png")
        self.quote_x = 600
        self.quote_y = 270

        self.score_label = QLabel(self)
        self.score_label.setGeometry(550, 20, 150, 50)
        font = QFont("Arial", 16, QFont.Bold)
        self.score_label.setFont(font)
        self.score_label.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.update_score_label()

        timer = QTimer(self)
        timer.timeout.connect(self.update_value)
        timer.start(700)

        self.QSH_good = QSoundEffect()
        self.QSH_good.setSource(QUrl.fromLocalFile("sounds/good_item_caught.wav"))
        self.QSH_bad = QSoundEffect()
        self.QSH_bad.setSource(QUrl.fromLocalFile("sounds/bad_item_caught.wav"))

    def update_score_label(self):
        self.score_label.setText(f"Score: {self.score}")

    def mousePressEvent(self, e):
        for obj in self.falling_objects:
            if obj.is_hit(e.pos().x(), e.pos().y()):
                if obj.object_type == 'egg1' or obj.object_type == 'egg2' or obj.object_type == 'egg3':
                    self.QSH_good.play()
                    print("Egg Caught! Score +1")
                    self.score += 1
                    self.update_score_label()
                else:
                    self.QSH_bad.play()
                    print("Bug Caught! Score -1")
                    self.score -= 1
                    self.update_score_label()
                self.falling_objects.remove(obj)
                break

        if self.score == 20:
            self.show_win_popup()

        if self.score == -10:
            self.show_lose_popup()

    def show_win_popup(self):
        popup = QMessageBox()
        popup.setWindowTitle("Congratulations!")
        popup.setText("You Win!")
        popup.exec_()
        self.restart_game()

    def show_lose_popup(self):
        popup = QMessageBox()
        popup.setWindowTitle("Sorry!")
        popup.setText("You Lose!")
        popup.exec_()
        self.restart_game()

    def restart_game(self):
        self.score = 0
        self.update_score_label()
        self.falling_objects = []

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(self.rect(), self.background_image)
        for obj in self.falling_objects:
            obj.draw(p)
        p.drawPixmap(QRect(self.quote_x, self.quote_y, 100, 100), self.quote)
        p.drawPixmap(QRect(self.character_x, self.character_y, 300, 300), self.character_image)
        p.end()

    # fuction to update the falling objects
    def update_value(self):
        for obj in self.falling_objects:
            obj.y += self.fall_speed

            if obj.y > self.arena_h:
                self.falling_objects.remove(obj)

        object_types = ['egg1', 'egg2', 'bug']
        new_object = FallingObject(random.choice(object_types))
        new_object.random_pos(self.arena_w, self.arena_h)
        self.falling_objects.append(new_object)

        self.update()

class CatchTheFallingEggsGame(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.falling_objects_game = FallingObjectsGame()
        layout = QVBoxLayout()
        layout.addWidget(self.falling_objects_game)
        self.setLayout(layout)
        self.setMinimumSize(430, 500)

def main():
    app = QApplication(sys.argv)
    game = CatchTheFallingEggsGame()
    game.setWindowTitle("Catch the Falling Eggs Game")
    game.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
