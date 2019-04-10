"""
Call cffi to compile the extension module.
With cffi 1.0 this is only needed at build time.
"""

import cffi
import os.path
import platform

system = platform.system()

ffi = cffi.FFI()

here = os.path.dirname(__file__)
for filename in ("sdlint.h", "sdl.h", "defines.h"):
    with open(os.path.join(here, filename), "r") as header:
        ffi.cdef(header.read())

ffi.cdef("""
extern "Python" int pysdl2_event_filter(void *userdata, SDL_Event *event);
""")

# On Linux, we have to link with SDL2 explicitly, but it's easier to get Kivy to
# use the system SDL2 anyway; when they are both using the same SDL2 there's no
# problem. On OSX this can find all symbols from kivy's SDL2 without any link
# flag, as long as kivy is loaded first.

args = {}
if system not in ("Windows", "Darwin"):
    args = {"libraries":["SDL2"]}

print(system, args)

ffi.set_source("__kivyjoy",
    """
    // Cause the inline functions to be compiled
    #define SDL_FORCE_INLINE
    #include <SDL2/SDL.h>
    """,
    **args)

if __name__ == "__main__":
    ffi.compile()
