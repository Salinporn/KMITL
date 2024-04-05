import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
    @abstractmethod
    def drawWidget(self):
        pass

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.paused = False

    def on_click(self, event):
        if self.button.innerText == "Pause":
            self.button.innerText = "Play"
            
        else:
            self.button.innerText = "Pause"

        self.paused = not self.paused

    def on_setInterval(self):
        if self.paused:
            return
        self.counter += 1
        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")

        self.button = document.createElement("button")
        self.button.innerText = "Pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)

    def drawWidget(self):
        super().drawWidget()
        self.random_button = document.createElement("button")
        self.random_button.innerText = "Random"
        self.random_button.style.width = "600px"
        self.random_button.onclick = self.on_random_click
        self.element.appendChild(self.random_button)

    def on_random_click(self, event):
        self.image.style.backgroundColor = f"rgb({js.Math.random() * 255},{js.Math.random() * 255},{js.Math.random() * 255})"

if __name__ == "__main__":
    output = ColorfulAnimationWidget("container")
    output.drawWidget()