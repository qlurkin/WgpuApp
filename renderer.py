import wgpu
import wgpu.backends.rs
import numpy as np
from wgpu.gui.base import WgpuCanvasInterface
import sys

class Canvas(WgpuCanvasInterface):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._window = window

    def get_window_id(self):
        if sys.platform.startswith("win"):
            return int(glfw.get_win32_window(self._window))
        elif sys.platform.startswith("darwin"):
            return int(glfw.get_cocoa_window(self._window))
        elif sys.platform.startswith("linux"):
            if is_wayland:
                return int(glfw.get_wayland_window(self._window))
            else:
                return int(glfw.get_x11_window(self._window))
        else:
            raise RuntimeError(f"Cannot get GLFW window id on {sys.platform}.")

    def get_physical_size(self):
        """Get the physical size in integer pixels."""
        raise NotImplementedError()


