import glfw
import wgpu
from wgpu.gui.glfw import run as mainloop, WgpuCanvas
import wgpu.backends.rs
import logging
import sys
import asyncio

logger = logging.getLogger("wgpu")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))
print(logger.handlers)

logger.critical("LOG this message")

def stop():
    loop = asyncio.get_event_loop()
    """Cleanup tasks tied to the service's shutdown."""
    #tasks = [t for t in asyncio.all_tasks() if t is not
    #         asyncio.current_task()]

    #[task.cancel() for task in tasks]
    #await asyncio.gather(*tasks)
    loop.stop()

def app(size, title):
    if not glfw.init():
        return

    canvas = WgpuCanvas(title=title, size=size)
    # # Create a wgpu device
    # adapter = wgpu.request_adapter(canvas=canvas, power_preference="high-performance")
    # device = adapter.request_device()

    # # Prepare present context
    # present_context = canvas.get_context()
    # render_texture_format = present_context.get_preferred_format(device.adapter)
    # present_context.configure(device=device, format=render_texture_format)

    def run(fun, state):
        print('RUN CALLED')

        def frame():
            nonlocal state
            state = fun(state)
            canvas.request_draw()

        canvas.request_draw(frame)

        mainloop()

    return run