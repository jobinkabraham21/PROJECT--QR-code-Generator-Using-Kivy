# BASIC APP
from kivy.app import App
from kivy.uix.widget import Widget
import pyqrcode
from kivy.core.window import Window
class MyScreen(Widget):
    def genimg(self, text):
        self.qr_text = text
        img = pyqrcode.create(self.qr_text)
        img.png("qr.png", scale=8)
        self.ids.my_image.source = "qr.png"
        self.ids.my_image.reload()
        return "", 204


class MyKivyApp(App):
    def build(self):
        Window.size = (305, 600)  # SET WINDOW SIZE
        return MyScreen()


if __name__=="__main__":
    MyKivyApp().run()