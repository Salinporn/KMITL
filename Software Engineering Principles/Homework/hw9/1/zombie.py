import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod

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

class TheZombieAnimation(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.paused = False

    def on_click(self, event):
        if self.button.innerText == "Resume" or self.button.innerText == "Start Walking":
            self.button.innerText = "Pause"
            self.button.style.backgroundColor = "firebrick"
            self.paused = False
            self.zombie_growl_2.play()
        elif self.button.innerText == "Pause":
            self.button.innerText = "Resume"
            self.button.style.backgroundColor = "forestgreen"
            self.paused = True
            self.zombie_growl_2.pause()

    def on_click2(self, event):
        self.button.innerText = "Start Walking"
        self.button.style.backgroundColor = "DimGray"
        self.paused = False
        self.counter = 1
        self.image.src = "./images/Idle (1).png"
        self.zombie_growl_1.pause()
        self.zombie_growl_2.pause()

    def motion(self):
        if self.button.innerText == "Start Walking":
            self.standing()
        elif self.button.innerText == "Pause":
            self.zombie_growl_1.pause()
            self.walking()

    def walking(self):
        if self.paused:
            return
        self.counter += 1
        self.zombie_growl_2.play()
        if self.counter > 10:
            self.counter = 1
        self.image.src = "./images/Walk (" + str(self.counter) + ").png"

    def standing(self):
        if self.paused:
            return
        self.counter += 1
        self.zombie_growl_1.play()
        if self.counter > 15:
            self.counter = 1
        self.image.src = "./images/Idle (" + str(self.counter) + ").png"

    def drawWidget(self):
        container = document.createElement("div")
        container.style.display = "flex"
        container.style.flexDirection = "column"
        container.style.alignItems = "center"

        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.style.margin = "auto"
        self.image.src = "./images/Idle (1).png"

        on_setInterval = create_proxy(self.motion)
        js.setInterval(on_setInterval, 100)
        container.appendChild(self.image)

        self.zombie_growl_1 = js.Audio.new("./sounds/zombie_growl_1.mp3")
        self.zombie_growl_2 = js.Audio.new("./sounds/zombie_growl_2.mp3")

        self.button = document.createElement("button")
        self.button.innerText = "Start Walking"
        self.button.style.backgroundColor = "DimGray"
        self.button.style.color = "White"
        self.button.style.width = "300px"
        self.button.style.height = "50px"
        self.button.style.margin = "auto"
        self.button.onclick = self.on_click
        self.button.style.marginTop = "20px"
        self.button.style.marginBottom = "20px"
        container.appendChild(self.button)

        self.restart = document.createElement("button")
        self.restart.innerText = "Restart"
        self.restart.style.backgroundColor = "DimGray"
        self.restart.style.color = "White"
        self.restart.style.width = "300px"
        self.restart.style.height = "50px"
        self.restart.style.margin = "auto"
        self.restart.onclick = self.on_click2
        container.appendChild(self.restart)

        self.element.appendChild(container)

if __name__ == "__main__":
    output = TheZombieAnimation("container")
    output.drawWidget()