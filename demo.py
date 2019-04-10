import kivy.app

# has to be imported after kivy.app so SDL2 is already dlopen-ed
import kivyjoy.controller

kc = kivyjoy.controller.KivyController()
kc.install()

app = kivy.app.App()
app.run()
