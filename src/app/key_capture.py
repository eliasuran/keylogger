import Quartz
from AppKit import NSApplication
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app import App

#TODO: fix linter

class KeyCapture():
    def __init__(self, app: "App"):
        self.app = app
        self.event_mask = Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown) | Quartz.CGEventMaskBit(Quartz.kCGEventFlagsChanged)


    def capture(self, callback):
        tap = Quartz.CGEventTapCreate(
            Quartz.kCGSessionEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionListenOnly,
            self.event_mask,
            callback,
            None
        )
        run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None, tap, 0)
        Quartz.CFRunLoopAddSource(Quartz.CFRunLoopGetCurrent(), run_loop_source, Quartz.kCFRunLoopCommonModes)
        Quartz.CGEventTapEnable(tap, True)
