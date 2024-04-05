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

class MainWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.running_id = 0

    def drawWidget(self):
        self.add_convert_money_button = document.createElement("button")
        self.add_convert_money_button.innerText = "Convert Money"
        self.add_convert_money_button.style.width = "300px"
        self.add_convert_money_button.style.margin = "5px"
        self.add_convert_money_button.style.height = "30px"
        self.add_convert_money_button.onclick = self.add_convert_money
        self.element.appendChild(self.add_convert_money_button)

        self.add_animation_button = document.createElement("button")
        self.add_animation_button.innerText = "Animation"
        self.add_animation_button.style.width = "300px"
        self.add_animation_button.style.margin = "5px"
        self.add_animation_button.style.height = "30px"
        self.add_animation_button.onclick = self.add_animation
        self.element.appendChild(self.add_animation_button)

        self.add_colorful_animation_button = document.createElement("button")
        self.add_colorful_animation_button.innerText = "Colorful Animation"
        self.add_colorful_animation_button.style.width = "300px"
        self.add_colorful_animation_button.style.margin = "5px"
        self.add_colorful_animation_button.style.height = "30px"
        self.add_colorful_animation_button.onclick = self.add_colorful_animation
        self.element.appendChild(self.add_colorful_animation_button)

    def add_convert_money(self, event):
        id = f"container{self.running_id}"
        container = document.createElement("div")
        container.id = id
        self.element.appendChild(container)
        self.running_id += 1

        self.convert_money = ConvertMoneyWidget(id)
        self.convert_money.drawWidget()

    def add_animation(self, event):
        
        id = f"container{self.running_id}"
        container = document.createElement("div")
        container.id = id
        self.element.appendChild(container)
        self.running_id += 1
        self.animation = AnimationWidget("container")
        self.animation.drawWidget()

    def add_colorful_animation(self, event):
        self.colorful_animation = ColorfulAnimationWidget("container")
        self.colorful_animation.drawWidget()

class ConvertMoneyWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def drawWidget(self):
        self.element.appendChild(document.createElement("br"))
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "300px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "USD to THB"
        self.button.style.width = "300px"
        self.button.style.margin = "10px"
        self.button.onclick = self.convert_to_thb
        self.element.appendChild(self.button)

        self.button = document.createElement("button")
        self.button.innerText = "THB to USD"
        self.button.style.width = "300px"
        self.button.onclick = self.convert_to_usd
        self.element.appendChild(self.button)

    def convert_to_usd(self, event):
        text = self.input_text.value
        js.alert("USD: " + str(float(text) / 30))

    def convert_to_thb(self, event):
        text = self.input_text.value
        js.alert("THB: " + str(float(text) * 30))
        
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
        self.element.appendChild(document.createElement("br"))
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")

        self.element.appendChild(document.createElement("br"))
        self.button = document.createElement("button")
        self.button.innerText = "Pause"
        self.button.style.width = "600px"
        self.button.style.margin = "5px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)

    def drawWidget(self):
        super().drawWidget()
        self.element.appendChild(document.createElement("br"))
        self.random_button = document.createElement("button")
        self.random_button.innerText = "Random"
        self.random_button.style.width = "600px"
        self.random_button.style.margin = "5px"
        self.random_button.onclick = self.on_random_click
        self.element.appendChild(self.random_button)

    def on_random_click(self, event):
        self.image.style.backgroundColor = f"rgb({js.Math.random() * 255},{js.Math.random() * 255},{js.Math.random() * 255})"

if __name__ == "__main__":
    output = MainWidget("container")
    output.drawWidget()