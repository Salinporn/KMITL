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

class ConvertMoneyWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def drawWidget(self):
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "300px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "USD to THB"
        self.button.style.width = "300px"
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

if __name__ == "__main__":
    output = ConvertMoneyWidget("container")
    output.drawWidget()