"""
Game controller input for Kivy.

Open game controllers as they become available, expose with full SDL2 API.
"""

# Kivy must open so we can find the symbols,
# or kivyjoy must explicitly link with the same
# kivyjoy2 shared library as kivy.
import kivy.app

from kivy.event import EventDispatcher
from kivy.properties import DictProperty

# Special version of (pysdl2-cffi) that doesn't explictly link
# to a particular version on OSX. It could link to the SDL2
# bundled wih kivy explicitly.
import kivyjoy

JOYSTICK_EVENTS = (
    kivyjoy.JoyDeviceEvent,
    kivyjoy.JoyAxisEvent,
    kivyjoy.JoyHatEvent,
    kivyjoy.JoyBallEvent,
    kivyjoy.JoyButtonEvent,
    kivyjoy.ControllerDeviceEvent,
    kivyjoy.ControllerAxisEvent,
    kivyjoy.ControllerButtonEvent,
)

class KivyController(EventDispatcher):
    """
    Manage game controllers.

    Game controllers are assigned to and removed from the controllers list at the
    index of their id (so controllers[n] could be None if one was removed)
    """
    controllers = DictProperty()

    def __init__(self):
        self._handle = kivyjoy.ffi.new_handle(self.event)

    def install(self):
        """
        Attach to kivyjoy2 event loop
        """
        # will generate controllerdeviceadded events for existing sticks when first init
        kivyjoy.init(kivyjoy.INIT_GAMECONTROLLER|kivyjoy.INIT_JOYSTICK)
        kivyjoy.addEventWatch(kivyjoy.lib.pysdl2_event_filter, self._handle)

    def event(self, event):
        """
        Handle wrapped kivyjoy2 event
        """
        event = kivyjoy.Event(event).unwrapEvent()
        if isinstance(event, JOYSTICK_EVENTS):
            print(event)

        if isinstance(event, kivyjoy.ControllerDeviceEvent):
            if event.type == kivyjoy.CONTROLLERDEVICEADDED:
                j = kivyjoy.gameControllerOpen(event.which)
                self.controllers[event.which] = j
            elif event.type == kivyjoy.CONTROLLERDEVICEREMOVED:
                j = self.controllers.pop(event.which)
                j.gameControllerClose()

        # Just GameController for now...
        # If a controller is only a joystick, try adding a third party mapping
        # to make it show up as a GameController.

        return 0
