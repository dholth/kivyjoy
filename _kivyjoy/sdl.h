// Some of SDL2; enough for controller, keyboard input.
typedef enum {
  SDL_SCANCODE_UNKNOWN = 0,
  SDL_SCANCODE_A = 4,
  SDL_SCANCODE_B = 5,
  SDL_SCANCODE_C = 6,
  SDL_SCANCODE_D = 7,
  SDL_SCANCODE_E = 8,
  SDL_SCANCODE_F = 9,
  SDL_SCANCODE_G = 10,
  SDL_SCANCODE_H = 11,
  SDL_SCANCODE_I = 12,
  SDL_SCANCODE_J = 13,
  SDL_SCANCODE_K = 14,
  SDL_SCANCODE_L = 15,
  SDL_SCANCODE_M = 16,
  SDL_SCANCODE_N = 17,
  SDL_SCANCODE_O = 18,
  SDL_SCANCODE_P = 19,
  SDL_SCANCODE_Q = 20,
  SDL_SCANCODE_R = 21,
  SDL_SCANCODE_S = 22,
  SDL_SCANCODE_T = 23,
  SDL_SCANCODE_U = 24,
  SDL_SCANCODE_V = 25,
  SDL_SCANCODE_W = 26,
  SDL_SCANCODE_X = 27,
  SDL_SCANCODE_Y = 28,
  SDL_SCANCODE_Z = 29,
  SDL_SCANCODE_1 = 30,
  SDL_SCANCODE_2 = 31,
  SDL_SCANCODE_3 = 32,
  SDL_SCANCODE_4 = 33,
  SDL_SCANCODE_5 = 34,
  SDL_SCANCODE_6 = 35,
  SDL_SCANCODE_7 = 36,
  SDL_SCANCODE_8 = 37,
  SDL_SCANCODE_9 = 38,
  SDL_SCANCODE_0 = 39,
  SDL_SCANCODE_RETURN = 40,
  SDL_SCANCODE_ESCAPE = 41,
  SDL_SCANCODE_BACKSPACE = 42,
  SDL_SCANCODE_TAB = 43,
  SDL_SCANCODE_SPACE = 44,
  SDL_SCANCODE_MINUS = 45,
  SDL_SCANCODE_EQUALS = 46,
  SDL_SCANCODE_LEFTBRACKET = 47,
  SDL_SCANCODE_RIGHTBRACKET = 48,
  SDL_SCANCODE_BACKSLASH = 49,
  SDL_SCANCODE_NONUSHASH = 50,
  SDL_SCANCODE_SEMICOLON = 51,
  SDL_SCANCODE_APOSTROPHE = 52,
  SDL_SCANCODE_GRAVE = 53,
  SDL_SCANCODE_COMMA = 54,
  SDL_SCANCODE_PERIOD = 55,
  SDL_SCANCODE_SLASH = 56,
  SDL_SCANCODE_CAPSLOCK = 57,
  SDL_SCANCODE_F1 = 58,
  SDL_SCANCODE_F2 = 59,
  SDL_SCANCODE_F3 = 60,
  SDL_SCANCODE_F4 = 61,
  SDL_SCANCODE_F5 = 62,
  SDL_SCANCODE_F6 = 63,
  SDL_SCANCODE_F7 = 64,
  SDL_SCANCODE_F8 = 65,
  SDL_SCANCODE_F9 = 66,
  SDL_SCANCODE_F10 = 67,
  SDL_SCANCODE_F11 = 68,
  SDL_SCANCODE_F12 = 69,
  SDL_SCANCODE_PRINTSCREEN = 70,
  SDL_SCANCODE_SCROLLLOCK = 71,
  SDL_SCANCODE_PAUSE = 72,
  SDL_SCANCODE_INSERT = 73,
  SDL_SCANCODE_HOME = 74,
  SDL_SCANCODE_PAGEUP = 75,
  SDL_SCANCODE_DELETE = 76,
  SDL_SCANCODE_END = 77,
  SDL_SCANCODE_PAGEDOWN = 78,
  SDL_SCANCODE_RIGHT = 79,
  SDL_SCANCODE_LEFT = 80,
  SDL_SCANCODE_DOWN = 81,
  SDL_SCANCODE_UP = 82,
  SDL_SCANCODE_NUMLOCKCLEAR = 83,
  SDL_SCANCODE_KP_DIVIDE = 84,
  SDL_SCANCODE_KP_MULTIPLY = 85,
  SDL_SCANCODE_KP_MINUS = 86,
  SDL_SCANCODE_KP_PLUS = 87,
  SDL_SCANCODE_KP_ENTER = 88,
  SDL_SCANCODE_KP_1 = 89,
  SDL_SCANCODE_KP_2 = 90,
  SDL_SCANCODE_KP_3 = 91,
  SDL_SCANCODE_KP_4 = 92,
  SDL_SCANCODE_KP_5 = 93,
  SDL_SCANCODE_KP_6 = 94,
  SDL_SCANCODE_KP_7 = 95,
  SDL_SCANCODE_KP_8 = 96,
  SDL_SCANCODE_KP_9 = 97,
  SDL_SCANCODE_KP_0 = 98,
  SDL_SCANCODE_KP_PERIOD = 99,
  SDL_SCANCODE_NONUSBACKSLASH = 100,
  SDL_SCANCODE_APPLICATION = 101,
  SDL_SCANCODE_POWER = 102,
  SDL_SCANCODE_KP_EQUALS = 103,
  SDL_SCANCODE_F13 = 104,
  SDL_SCANCODE_F14 = 105,
  SDL_SCANCODE_F15 = 106,
  SDL_SCANCODE_F16 = 107,
  SDL_SCANCODE_F17 = 108,
  SDL_SCANCODE_F18 = 109,
  SDL_SCANCODE_F19 = 110,
  SDL_SCANCODE_F20 = 111,
  SDL_SCANCODE_F21 = 112,
  SDL_SCANCODE_F22 = 113,
  SDL_SCANCODE_F23 = 114,
  SDL_SCANCODE_F24 = 115,
  SDL_SCANCODE_EXECUTE = 116,
  SDL_SCANCODE_HELP = 117,
  SDL_SCANCODE_MENU = 118,
  SDL_SCANCODE_SELECT = 119,
  SDL_SCANCODE_STOP = 120,
  SDL_SCANCODE_AGAIN = 121,
  SDL_SCANCODE_UNDO = 122,
  SDL_SCANCODE_CUT = 123,
  SDL_SCANCODE_COPY = 124,
  SDL_SCANCODE_PASTE = 125,
  SDL_SCANCODE_FIND = 126,
  SDL_SCANCODE_MUTE = 127,
  SDL_SCANCODE_VOLUMEUP = 128,
  SDL_SCANCODE_VOLUMEDOWN = 129,
  SDL_SCANCODE_KP_COMMA = 133,
  SDL_SCANCODE_KP_EQUALSAS400 = 134,
  SDL_SCANCODE_INTERNATIONAL1 = 135,
  SDL_SCANCODE_INTERNATIONAL2 = 136,
  SDL_SCANCODE_INTERNATIONAL3 = 137,
  SDL_SCANCODE_INTERNATIONAL4 = 138,
  SDL_SCANCODE_INTERNATIONAL5 = 139,
  SDL_SCANCODE_INTERNATIONAL6 = 140,
  SDL_SCANCODE_INTERNATIONAL7 = 141,
  SDL_SCANCODE_INTERNATIONAL8 = 142,
  SDL_SCANCODE_INTERNATIONAL9 = 143,
  SDL_SCANCODE_LANG1 = 144,
  SDL_SCANCODE_LANG2 = 145,
  SDL_SCANCODE_LANG3 = 146,
  SDL_SCANCODE_LANG4 = 147,
  SDL_SCANCODE_LANG5 = 148,
  SDL_SCANCODE_LANG6 = 149,
  SDL_SCANCODE_LANG7 = 150,
  SDL_SCANCODE_LANG8 = 151,
  SDL_SCANCODE_LANG9 = 152,
  SDL_SCANCODE_ALTERASE = 153,
  SDL_SCANCODE_SYSREQ = 154,
  SDL_SCANCODE_CANCEL = 155,
  SDL_SCANCODE_CLEAR = 156,
  SDL_SCANCODE_PRIOR = 157,
  SDL_SCANCODE_RETURN2 = 158,
  SDL_SCANCODE_SEPARATOR = 159,
  SDL_SCANCODE_OUT = 160,
  SDL_SCANCODE_OPER = 161,
  SDL_SCANCODE_CLEARAGAIN = 162,
  SDL_SCANCODE_CRSEL = 163,
  SDL_SCANCODE_EXSEL = 164,
  SDL_SCANCODE_KP_00 = 176,
  SDL_SCANCODE_KP_000 = 177,
  SDL_SCANCODE_THOUSANDSSEPARATOR = 178,
  SDL_SCANCODE_DECIMALSEPARATOR = 179,
  SDL_SCANCODE_CURRENCYUNIT = 180,
  SDL_SCANCODE_CURRENCYSUBUNIT = 181,
  SDL_SCANCODE_KP_LEFTPAREN = 182,
  SDL_SCANCODE_KP_RIGHTPAREN = 183,
  SDL_SCANCODE_KP_LEFTBRACE = 184,
  SDL_SCANCODE_KP_RIGHTBRACE = 185,
  SDL_SCANCODE_KP_TAB = 186,
  SDL_SCANCODE_KP_BACKSPACE = 187,
  SDL_SCANCODE_KP_A = 188,
  SDL_SCANCODE_KP_B = 189,
  SDL_SCANCODE_KP_C = 190,
  SDL_SCANCODE_KP_D = 191,
  SDL_SCANCODE_KP_E = 192,
  SDL_SCANCODE_KP_F = 193,
  SDL_SCANCODE_KP_XOR = 194,
  SDL_SCANCODE_KP_POWER = 195,
  SDL_SCANCODE_KP_PERCENT = 196,
  SDL_SCANCODE_KP_LESS = 197,
  SDL_SCANCODE_KP_GREATER = 198,
  SDL_SCANCODE_KP_AMPERSAND = 199,
  SDL_SCANCODE_KP_DBLAMPERSAND = 200,
  SDL_SCANCODE_KP_VERTICALBAR = 201,
  SDL_SCANCODE_KP_DBLVERTICALBAR = 202,
  SDL_SCANCODE_KP_COLON = 203,
  SDL_SCANCODE_KP_HASH = 204,
  SDL_SCANCODE_KP_SPACE = 205,
  SDL_SCANCODE_KP_AT = 206,
  SDL_SCANCODE_KP_EXCLAM = 207,
  SDL_SCANCODE_KP_MEMSTORE = 208,
  SDL_SCANCODE_KP_MEMRECALL = 209,
  SDL_SCANCODE_KP_MEMCLEAR = 210,
  SDL_SCANCODE_KP_MEMADD = 211,
  SDL_SCANCODE_KP_MEMSUBTRACT = 212,
  SDL_SCANCODE_KP_MEMMULTIPLY = 213,
  SDL_SCANCODE_KP_MEMDIVIDE = 214,
  SDL_SCANCODE_KP_PLUSMINUS = 215,
  SDL_SCANCODE_KP_CLEAR = 216,
  SDL_SCANCODE_KP_CLEARENTRY = 217,
  SDL_SCANCODE_KP_BINARY = 218,
  SDL_SCANCODE_KP_OCTAL = 219,
  SDL_SCANCODE_KP_DECIMAL = 220,
  SDL_SCANCODE_KP_HEXADECIMAL = 221,
  SDL_SCANCODE_LCTRL = 224,
  SDL_SCANCODE_LSHIFT = 225,
  SDL_SCANCODE_LALT = 226,
  SDL_SCANCODE_LGUI = 227,
  SDL_SCANCODE_RCTRL = 228,
  SDL_SCANCODE_RSHIFT = 229,
  SDL_SCANCODE_RALT = 230,
  SDL_SCANCODE_RGUI = 231,
  SDL_SCANCODE_MODE = 257,
  SDL_SCANCODE_AUDIONEXT = 258,
  SDL_SCANCODE_AUDIOPREV = 259,
  SDL_SCANCODE_AUDIOSTOP = 260,
  SDL_SCANCODE_AUDIOPLAY = 261,
  SDL_SCANCODE_AUDIOMUTE = 262,
  SDL_SCANCODE_MEDIASELECT = 263,
  SDL_SCANCODE_WWW = 264,
  SDL_SCANCODE_MAIL = 265,
  SDL_SCANCODE_CALCULATOR = 266,
  SDL_SCANCODE_COMPUTER = 267,
  SDL_SCANCODE_AC_SEARCH = 268,
  SDL_SCANCODE_AC_HOME = 269,
  SDL_SCANCODE_AC_BACK = 270,
  SDL_SCANCODE_AC_FORWARD = 271,
  SDL_SCANCODE_AC_STOP = 272,
  SDL_SCANCODE_AC_REFRESH = 273,
  SDL_SCANCODE_AC_BOOKMARKS = 274,
  SDL_SCANCODE_BRIGHTNESSDOWN = 275,
  SDL_SCANCODE_BRIGHTNESSUP = 276,
  SDL_SCANCODE_DISPLAYSWITCH = 277,
  SDL_SCANCODE_KBDILLUMTOGGLE = 278,
  SDL_SCANCODE_KBDILLUMDOWN = 279,
  SDL_SCANCODE_KBDILLUMUP = 280,
  SDL_SCANCODE_EJECT = 281,
  SDL_SCANCODE_SLEEP = 282,
  SDL_SCANCODE_APP1 = 283,
  SDL_SCANCODE_APP2 = 284,
  SDL_SCANCODE_AUDIOREWIND = 285,
  SDL_SCANCODE_AUDIOFASTFORWARD = 286,
  SDL_NUM_SCANCODES = 512
} SDL_Scancode;
typedef Sint32 SDL_Keycode;
enum {
  SDLK_UNKNOWN = ...,
  SDLK_RETURN = ...,
  SDLK_ESCAPE = ...,
  SDLK_BACKSPACE = ...,
  SDLK_TAB = ...,
  SDLK_SPACE = ...,
  SDLK_EXCLAIM = ...,
  SDLK_QUOTEDBL = ...,
  SDLK_HASH = ...,
  SDLK_PERCENT = ...,
  SDLK_DOLLAR = ...,
  SDLK_AMPERSAND = ...,
  SDLK_QUOTE = ...,
  SDLK_LEFTPAREN = ...,
  SDLK_RIGHTPAREN = ...,
  SDLK_ASTERISK = ...,
  SDLK_PLUS = ...,
  SDLK_COMMA = ...,
  SDLK_MINUS = ...,
  SDLK_PERIOD = ...,
  SDLK_SLASH = ...,
  SDLK_0 = ...,
  SDLK_1 = ...,
  SDLK_2 = ...,
  SDLK_3 = ...,
  SDLK_4 = ...,
  SDLK_5 = ...,
  SDLK_6 = ...,
  SDLK_7 = ...,
  SDLK_8 = ...,
  SDLK_9 = ...,
  SDLK_COLON = ...,
  SDLK_SEMICOLON = ...,
  SDLK_LESS = ...,
  SDLK_EQUALS = ...,
  SDLK_GREATER = ...,
  SDLK_QUESTION = ...,
  SDLK_AT = ...,
  SDLK_LEFTBRACKET = ...,
  SDLK_BACKSLASH = ...,
  SDLK_RIGHTBRACKET = ...,
  SDLK_CARET = ...,
  SDLK_UNDERSCORE = ...,
  SDLK_BACKQUOTE = ...,
  SDLK_a = ...,
  SDLK_b = ...,
  SDLK_c = ...,
  SDLK_d = ...,
  SDLK_e = ...,
  SDLK_f = ...,
  SDLK_g = ...,
  SDLK_h = ...,
  SDLK_i = ...,
  SDLK_j = ...,
  SDLK_k = ...,
  SDLK_l = ...,
  SDLK_m = ...,
  SDLK_n = ...,
  SDLK_o = ...,
  SDLK_p = ...,
  SDLK_q = ...,
  SDLK_r = ...,
  SDLK_s = ...,
  SDLK_t = ...,
  SDLK_u = ...,
  SDLK_v = ...,
  SDLK_w = ...,
  SDLK_x = ...,
  SDLK_y = ...,
  SDLK_z = ...,
  SDLK_CAPSLOCK = ...,
  SDLK_F1 = ...,
  SDLK_F2 = ...,
  SDLK_F3 = ...,
  SDLK_F4 = ...,
  SDLK_F5 = ...,
  SDLK_F6 = ...,
  SDLK_F7 = ...,
  SDLK_F8 = ...,
  SDLK_F9 = ...,
  SDLK_F10 = ...,
  SDLK_F11 = ...,
  SDLK_F12 = ...,
  SDLK_PRINTSCREEN = ...,
  SDLK_SCROLLLOCK = ...,
  SDLK_PAUSE = ...,
  SDLK_INSERT = ...,
  SDLK_HOME = ...,
  SDLK_PAGEUP = ...,
  SDLK_DELETE = ...,
  SDLK_END = ...,
  SDLK_PAGEDOWN = ...,
  SDLK_RIGHT = ...,
  SDLK_LEFT = ...,
  SDLK_DOWN = ...,
  SDLK_UP = ...,
  SDLK_NUMLOCKCLEAR = ...,
  SDLK_KP_DIVIDE = ...,
  SDLK_KP_MULTIPLY = ...,
  SDLK_KP_MINUS = ...,
  SDLK_KP_PLUS = ...,
  SDLK_KP_ENTER = ...,
  SDLK_KP_1 = ...,
  SDLK_KP_2 = ...,
  SDLK_KP_3 = ...,
  SDLK_KP_4 = ...,
  SDLK_KP_5 = ...,
  SDLK_KP_6 = ...,
  SDLK_KP_7 = ...,
  SDLK_KP_8 = ...,
  SDLK_KP_9 = ...,
  SDLK_KP_0 = ...,
  SDLK_KP_PERIOD = ...,
  SDLK_APPLICATION = ...,
  SDLK_POWER = ...,
  SDLK_KP_EQUALS = ...,
  SDLK_F13 = ...,
  SDLK_F14 = ...,
  SDLK_F15 = ...,
  SDLK_F16 = ...,
  SDLK_F17 = ...,
  SDLK_F18 = ...,
  SDLK_F19 = ...,
  SDLK_F20 = ...,
  SDLK_F21 = ...,
  SDLK_F22 = ...,
  SDLK_F23 = ...,
  SDLK_F24 = ...,
  SDLK_EXECUTE = ...,
  SDLK_HELP = ...,
  SDLK_MENU = ...,
  SDLK_SELECT = ...,
  SDLK_STOP = ...,
  SDLK_AGAIN = ...,
  SDLK_UNDO = ...,
  SDLK_CUT = ...,
  SDLK_COPY = ...,
  SDLK_PASTE = ...,
  SDLK_FIND = ...,
  SDLK_MUTE = ...,
  SDLK_VOLUMEUP = ...,
  SDLK_VOLUMEDOWN = ...,
  SDLK_KP_COMMA = ...,
  SDLK_KP_EQUALSAS400 = ...,
  SDLK_ALTERASE = ...,
  SDLK_SYSREQ = ...,
  SDLK_CANCEL = ...,
  SDLK_CLEAR = ...,
  SDLK_PRIOR = ...,
  SDLK_RETURN2 = ...,
  SDLK_SEPARATOR = ...,
  SDLK_OUT = ...,
  SDLK_OPER = ...,
  SDLK_CLEARAGAIN = ...,
  SDLK_CRSEL = ...,
  SDLK_EXSEL = ...,
  SDLK_KP_00 = ...,
  SDLK_KP_000 = ...,
  SDLK_THOUSANDSSEPARATOR = ...,
  SDLK_DECIMALSEPARATOR = ...,
  SDLK_CURRENCYUNIT = ...,
  SDLK_CURRENCYSUBUNIT = ...,
  SDLK_KP_LEFTPAREN = ...,
  SDLK_KP_RIGHTPAREN = ...,
  SDLK_KP_LEFTBRACE = ...,
  SDLK_KP_RIGHTBRACE = ...,
  SDLK_KP_TAB = ...,
  SDLK_KP_BACKSPACE = ...,
  SDLK_KP_A = ...,
  SDLK_KP_B = ...,
  SDLK_KP_C = ...,
  SDLK_KP_D = ...,
  SDLK_KP_E = ...,
  SDLK_KP_F = ...,
  SDLK_KP_XOR = ...,
  SDLK_KP_POWER = ...,
  SDLK_KP_PERCENT = ...,
  SDLK_KP_LESS = ...,
  SDLK_KP_GREATER = ...,
  SDLK_KP_AMPERSAND = ...,
  SDLK_KP_DBLAMPERSAND = ...,
  SDLK_KP_VERTICALBAR = ...,
  SDLK_KP_DBLVERTICALBAR = ...,
  SDLK_KP_COLON = ...,
  SDLK_KP_HASH = ...,
  SDLK_KP_SPACE = ...,
  SDLK_KP_AT = ...,
  SDLK_KP_EXCLAM = ...,
  SDLK_KP_MEMSTORE = ...,
  SDLK_KP_MEMRECALL = ...,
  SDLK_KP_MEMCLEAR = ...,
  SDLK_KP_MEMADD = ...,
  SDLK_KP_MEMSUBTRACT = ...,
  SDLK_KP_MEMMULTIPLY = ...,
  SDLK_KP_MEMDIVIDE = ...,
  SDLK_KP_PLUSMINUS = ...,
  SDLK_KP_CLEAR = ...,
  SDLK_KP_CLEARENTRY = ...,
  SDLK_KP_BINARY = ...,
  SDLK_KP_OCTAL = ...,
  SDLK_KP_DECIMAL = ...,
  SDLK_KP_HEXADECIMAL = ...,
  SDLK_LCTRL = ...,
  SDLK_LSHIFT = ...,
  SDLK_LALT = ...,
  SDLK_LGUI = ...,
  SDLK_RCTRL = ...,
  SDLK_RSHIFT = ...,
  SDLK_RALT = ...,
  SDLK_RGUI = ...,
  SDLK_MODE = ...,
  SDLK_AUDIONEXT = ...,
  SDLK_AUDIOPREV = ...,
  SDLK_AUDIOSTOP = ...,
  SDLK_AUDIOPLAY = ...,
  SDLK_AUDIOMUTE = ...,
  SDLK_MEDIASELECT = ...,
  SDLK_WWW = ...,
  SDLK_MAIL = ...,
  SDLK_CALCULATOR = ...,
  SDLK_COMPUTER = ...,
  SDLK_AC_SEARCH = ...,
  SDLK_AC_HOME = ...,
  SDLK_AC_BACK = ...,
  SDLK_AC_FORWARD = ...,
  SDLK_AC_STOP = ...,
  SDLK_AC_REFRESH = ...,
  SDLK_AC_BOOKMARKS = ...,
  SDLK_BRIGHTNESSDOWN = ...,
  SDLK_BRIGHTNESSUP = ...,
  SDLK_DISPLAYSWITCH = ...,
  SDLK_KBDILLUMTOGGLE = ...,
  SDLK_KBDILLUMDOWN = ...,
  SDLK_KBDILLUMUP = ...,
  SDLK_EJECT = ...,
  SDLK_SLEEP = ...,
  SDLK_APP1 = ...,
  SDLK_APP2 = ...,
  SDLK_AUDIOREWIND = ...,
  SDLK_AUDIOFASTFORWARD = ...
};
typedef enum {
  KMOD_NONE = 0x0000,
  KMOD_LSHIFT = 0x0001,
  KMOD_RSHIFT = 0x0002,
  KMOD_LCTRL = 0x0040,
  KMOD_RCTRL = 0x0080,
  KMOD_LALT = 0x0100,
  KMOD_RALT = 0x0200,
  KMOD_LGUI = 0x0400,
  KMOD_RGUI = 0x0800,
  KMOD_NUM = 0x1000,
  KMOD_CAPS = 0x2000,
  KMOD_MODE = 0x4000,
  KMOD_RESERVED = 0x8000
} SDL_Keymod;
typedef struct SDL_Keysym {
  SDL_Scancode scancode;
  SDL_Keycode sym;
  Uint16 mod;
  Uint32 unused;
} SDL_Keysym;
// extern SDL_Window *SDL_GetKeyboardFocus(void);
extern const Uint8 *SDL_GetKeyboardState(int *numkeys);
extern SDL_Keymod SDL_GetModState(void);
extern void SDL_SetModState(SDL_Keymod modstate);
extern SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode);
extern SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode key);
extern const char *SDL_GetScancodeName(SDL_Scancode scancode);
extern SDL_Scancode SDL_GetScancodeFromName(const char *name);
extern const char *SDL_GetKeyName(SDL_Keycode key);
extern SDL_Keycode SDL_GetKeyFromName(const char *name);
extern void SDL_StartTextInput(void);
extern SDL_bool SDL_IsTextInputActive(void);
extern void SDL_StopTextInput(void);
// extern void SDL_SetTextInputRect(SDL_Rect *rect);
extern SDL_bool SDL_HasScreenKeyboardSupport(void);
// extern SDL_bool SDL_IsScreenKeyboardShown(SDL_Window *window);
struct _SDL_Joystick;
typedef struct _SDL_Joystick SDL_Joystick;
typedef struct {
  Uint8 data[16];
} SDL_JoystickGUID;
typedef Sint32 SDL_JoystickID;
typedef enum {
  SDL_JOYSTICK_TYPE_UNKNOWN,
  SDL_JOYSTICK_TYPE_GAMECONTROLLER,
  SDL_JOYSTICK_TYPE_WHEEL,
  SDL_JOYSTICK_TYPE_ARCADE_STICK,
  SDL_JOYSTICK_TYPE_FLIGHT_STICK,
  SDL_JOYSTICK_TYPE_DANCE_PAD,
  SDL_JOYSTICK_TYPE_GUITAR,
  SDL_JOYSTICK_TYPE_DRUM_KIT,
  SDL_JOYSTICK_TYPE_ARCADE_PAD,
  SDL_JOYSTICK_TYPE_THROTTLE
} SDL_JoystickType;
typedef enum {
  SDL_JOYSTICK_POWER_UNKNOWN = -1,
  SDL_JOYSTICK_POWER_EMPTY,
  SDL_JOYSTICK_POWER_LOW,
  SDL_JOYSTICK_POWER_MEDIUM,
  SDL_JOYSTICK_POWER_FULL,
  SDL_JOYSTICK_POWER_WIRED,
  SDL_JOYSTICK_POWER_MAX
} SDL_JoystickPowerLevel;
extern void SDL_LockJoysticks(void);
extern void SDL_UnlockJoysticks(void);
extern int SDL_NumJoysticks(void);
extern const char *SDL_JoystickNameForIndex(int device_index);
extern SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int device_index);
extern Uint16 SDL_JoystickGetDeviceVendor(int device_index);
extern Uint16 SDL_JoystickGetDeviceProduct(int device_index);
extern Uint16 SDL_JoystickGetDeviceProductVersion(int device_index);
extern SDL_JoystickType SDL_JoystickGetDeviceType(int device_index);
extern SDL_JoystickID SDL_JoystickGetDeviceInstanceID(int device_index);
extern SDL_Joystick *SDL_JoystickOpen(int device_index);
extern SDL_Joystick *SDL_JoystickFromInstanceID(SDL_JoystickID joyid);
extern const char *SDL_JoystickName(SDL_Joystick *joystick);
extern SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick *joystick);
extern Uint16 SDL_JoystickGetVendor(SDL_Joystick *joystick);
extern Uint16 SDL_JoystickGetProduct(SDL_Joystick *joystick);
extern Uint16 SDL_JoystickGetProductVersion(SDL_Joystick *joystick);
extern SDL_JoystickType SDL_JoystickGetType(SDL_Joystick *joystick);
extern void SDL_JoystickGetGUIDString(SDL_JoystickGUID guid, char *pszGUID,
                                      int cbGUID);
extern SDL_JoystickGUID SDL_JoystickGetGUIDFromString(const char *pchGUID);
extern SDL_bool SDL_JoystickGetAttached(SDL_Joystick *joystick);
extern SDL_JoystickID SDL_JoystickInstanceID(SDL_Joystick *joystick);
extern int SDL_JoystickNumAxes(SDL_Joystick *joystick);
extern int SDL_JoystickNumBalls(SDL_Joystick *joystick);
extern int SDL_JoystickNumHats(SDL_Joystick *joystick);
extern int SDL_JoystickNumButtons(SDL_Joystick *joystick);
extern void SDL_JoystickUpdate(void);
extern int SDL_JoystickEventState(int state);
extern Sint16 SDL_JoystickGetAxis(SDL_Joystick *joystick, int axis);
extern SDL_bool SDL_JoystickGetAxisInitialState(SDL_Joystick *joystick,
                                                int axis, Sint16 *state);
extern Uint8 SDL_JoystickGetHat(SDL_Joystick *joystick, int hat);
extern int SDL_JoystickGetBall(SDL_Joystick *joystick, int ball, int *dx,
                               int *dy);
extern Uint8 SDL_JoystickGetButton(SDL_Joystick *joystick, int button);
extern void SDL_JoystickClose(SDL_Joystick *joystick);
extern SDL_JoystickPowerLevel
SDL_JoystickCurrentPowerLevel(SDL_Joystick *joystick);
struct _SDL_GameController;
typedef struct _SDL_GameController SDL_GameController;
typedef enum {
  SDL_CONTROLLER_BINDTYPE_NONE = 0,
  SDL_CONTROLLER_BINDTYPE_BUTTON,
  SDL_CONTROLLER_BINDTYPE_AXIS,
  SDL_CONTROLLER_BINDTYPE_HAT
} SDL_GameControllerBindType;
typedef struct SDL_GameControllerButtonBind {
  SDL_GameControllerBindType bindType;
  union {
    int button;
    int axis;
    struct {
      int hat;
      int hat_mask;
    } hat;
  } value;
} SDL_GameControllerButtonBind;
// extern int SDL_GameControllerAddMappingsFromRW(SDL_RWops *rw, int freerw);
extern int SDL_GameControllerAddMapping(const char *mappingString);
extern int SDL_GameControllerNumMappings(void);
extern char *SDL_GameControllerMappingForIndex(int mapping_index);
extern char *SDL_GameControllerMappingForGUID(SDL_JoystickGUID guid);
extern char *SDL_GameControllerMapping(SDL_GameController *gamecontroller);
extern SDL_bool SDL_IsGameController(int joystick_index);
extern const char *SDL_GameControllerNameForIndex(int joystick_index);
extern SDL_GameController *SDL_GameControllerOpen(int joystick_index);
extern SDL_GameController *
SDL_GameControllerFromInstanceID(SDL_JoystickID joyid);
extern const char *SDL_GameControllerName(SDL_GameController *gamecontroller);
extern Uint16 SDL_GameControllerGetVendor(SDL_GameController *gamecontroller);
extern Uint16 SDL_GameControllerGetProduct(SDL_GameController *gamecontroller);
extern Uint16
SDL_GameControllerGetProductVersion(SDL_GameController *gamecontroller);
extern SDL_bool
SDL_GameControllerGetAttached(SDL_GameController *gamecontroller);
extern SDL_Joystick *
SDL_GameControllerGetJoystick(SDL_GameController *gamecontroller);
extern int SDL_GameControllerEventState(int state);
extern void SDL_GameControllerUpdate(void);
typedef enum {
  SDL_CONTROLLER_AXIS_INVALID = -1,
  SDL_CONTROLLER_AXIS_LEFTX,
  SDL_CONTROLLER_AXIS_LEFTY,
  SDL_CONTROLLER_AXIS_RIGHTX,
  SDL_CONTROLLER_AXIS_RIGHTY,
  SDL_CONTROLLER_AXIS_TRIGGERLEFT,
  SDL_CONTROLLER_AXIS_TRIGGERRIGHT,
  SDL_CONTROLLER_AXIS_MAX
} SDL_GameControllerAxis;
extern SDL_GameControllerAxis
SDL_GameControllerGetAxisFromString(const char *pchString);
extern const char *
SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis axis);
extern SDL_GameControllerButtonBind
SDL_GameControllerGetBindForAxis(SDL_GameController *gamecontroller,
                                 SDL_GameControllerAxis axis);
extern Sint16 SDL_GameControllerGetAxis(SDL_GameController *gamecontroller,
                                        SDL_GameControllerAxis axis);
typedef enum {
  SDL_CONTROLLER_BUTTON_INVALID = -1,
  SDL_CONTROLLER_BUTTON_A,
  SDL_CONTROLLER_BUTTON_B,
  SDL_CONTROLLER_BUTTON_X,
  SDL_CONTROLLER_BUTTON_Y,
  SDL_CONTROLLER_BUTTON_BACK,
  SDL_CONTROLLER_BUTTON_GUIDE,
  SDL_CONTROLLER_BUTTON_START,
  SDL_CONTROLLER_BUTTON_LEFTSTICK,
  SDL_CONTROLLER_BUTTON_RIGHTSTICK,
  SDL_CONTROLLER_BUTTON_LEFTSHOULDER,
  SDL_CONTROLLER_BUTTON_RIGHTSHOULDER,
  SDL_CONTROLLER_BUTTON_DPAD_UP,
  SDL_CONTROLLER_BUTTON_DPAD_DOWN,
  SDL_CONTROLLER_BUTTON_DPAD_LEFT,
  SDL_CONTROLLER_BUTTON_DPAD_RIGHT,
  SDL_CONTROLLER_BUTTON_MAX
} SDL_GameControllerButton;
extern SDL_GameControllerButton
SDL_GameControllerGetButtonFromString(const char *pchString);
extern const char *
SDL_GameControllerGetStringForButton(SDL_GameControllerButton button);
extern SDL_GameControllerButtonBind
SDL_GameControllerGetBindForButton(SDL_GameController *gamecontroller,
                                   SDL_GameControllerButton button);
extern Uint8 SDL_GameControllerGetButton(SDL_GameController *gamecontroller,
                                         SDL_GameControllerButton button);
extern void SDL_GameControllerClose(SDL_GameController *gamecontroller);
typedef enum {
  SDL_FIRSTEVENT = 0,
  SDL_QUIT = 0x100,
  SDL_APP_TERMINATING,
  SDL_APP_LOWMEMORY,
  SDL_APP_WILLENTERBACKGROUND,
  SDL_APP_DIDENTERBACKGROUND,
  SDL_APP_WILLENTERFOREGROUND,
  SDL_APP_DIDENTERFOREGROUND,
  SDL_WINDOWEVENT = 0x200,
  SDL_SYSWMEVENT,
  SDL_KEYDOWN = 0x300,
  SDL_KEYUP,
  SDL_TEXTEDITING,
  SDL_TEXTINPUT,
  SDL_KEYMAPCHANGED,
  SDL_MOUSEMOTION = 0x400,
  SDL_MOUSEBUTTONDOWN,
  SDL_MOUSEBUTTONUP,
  SDL_MOUSEWHEEL,
  SDL_JOYAXISMOTION = 0x600,
  SDL_JOYBALLMOTION,
  SDL_JOYHATMOTION,
  SDL_JOYBUTTONDOWN,
  SDL_JOYBUTTONUP,
  SDL_JOYDEVICEADDED,
  SDL_JOYDEVICEREMOVED,
  SDL_CONTROLLERAXISMOTION = 0x650,
  SDL_CONTROLLERBUTTONDOWN,
  SDL_CONTROLLERBUTTONUP,
  SDL_CONTROLLERDEVICEADDED,
  SDL_CONTROLLERDEVICEREMOVED,
  SDL_CONTROLLERDEVICEREMAPPED,
  SDL_FINGERDOWN = 0x700,
  SDL_FINGERUP,
  SDL_FINGERMOTION,
  SDL_DOLLARGESTURE = 0x800,
  SDL_DOLLARRECORD,
  SDL_MULTIGESTURE,
  SDL_CLIPBOARDUPDATE = 0x900,
  SDL_DROPFILE = 0x1000,
  SDL_DROPTEXT,
  SDL_DROPBEGIN,
  SDL_DROPCOMPLETE,
  SDL_AUDIODEVICEADDED = 0x1100,
  SDL_AUDIODEVICEREMOVED,
  SDL_RENDER_TARGETS_RESET = 0x2000,
  SDL_RENDER_DEVICE_RESET,
  SDL_USEREVENT = 0x8000,
  SDL_LASTEVENT = 0xFFFF
} SDL_EventType;
typedef struct SDL_CommonEvent {
  Uint32 type;
  Uint32 timestamp;
} SDL_CommonEvent;
typedef struct SDL_WindowEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  Uint8 event;
  Uint8 padding1;
  Uint8 padding2;
  Uint8 padding3;
  Sint32 data1;
  Sint32 data2;
} SDL_WindowEvent;
typedef struct SDL_KeyboardEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  Uint8 state;
  Uint8 repeat;
  Uint8 padding2;
  Uint8 padding3;
  SDL_Keysym keysym;
} SDL_KeyboardEvent;
typedef struct SDL_TextEditingEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  char text[(32)];
  Sint32 start;
  Sint32 length;
} SDL_TextEditingEvent;
typedef struct SDL_TextInputEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  char text[(32)];
} SDL_TextInputEvent;
typedef struct SDL_MouseMotionEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  Uint32 which;
  Uint32 state;
  Sint32 x;
  Sint32 y;
  Sint32 xrel;
  Sint32 yrel;
} SDL_MouseMotionEvent;
typedef struct SDL_MouseButtonEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  Uint32 which;
  Uint8 button;
  Uint8 state;
  Uint8 clicks;
  Uint8 padding1;
  Sint32 x;
  Sint32 y;
} SDL_MouseButtonEvent;
typedef struct SDL_MouseWheelEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  Uint32 which;
  Sint32 x;
  Sint32 y;
  Uint32 direction;
} SDL_MouseWheelEvent;
typedef struct SDL_JoyAxisEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_JoystickID which;
  Uint8 axis;
  Uint8 padding1;
  Uint8 padding2;
  Uint8 padding3;
  Sint16 value;
  Uint16 padding4;
} SDL_JoyAxisEvent;
typedef struct SDL_JoyBallEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_JoystickID which;
  Uint8 ball;
  Uint8 padding1;
  Uint8 padding2;
  Uint8 padding3;
  Sint16 xrel;
  Sint16 yrel;
} SDL_JoyBallEvent;
typedef struct SDL_JoyHatEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_JoystickID which;
  Uint8 hat;
  Uint8 value;
  Uint8 padding1;
  Uint8 padding2;
} SDL_JoyHatEvent;
typedef struct SDL_JoyButtonEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_JoystickID which;
  Uint8 button;
  Uint8 state;
  Uint8 padding1;
  Uint8 padding2;
} SDL_JoyButtonEvent;
typedef struct SDL_JoyDeviceEvent {
  Uint32 type;
  Uint32 timestamp;
  Sint32 which;
} SDL_JoyDeviceEvent;
typedef struct SDL_ControllerAxisEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_JoystickID which;
  Uint8 axis;
  Uint8 padding1;
  Uint8 padding2;
  Uint8 padding3;
  Sint16 value;
  Uint16 padding4;
} SDL_ControllerAxisEvent;
typedef struct SDL_ControllerButtonEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_JoystickID which;
  Uint8 button;
  Uint8 state;
  Uint8 padding1;
  Uint8 padding2;
} SDL_ControllerButtonEvent;
typedef struct SDL_ControllerDeviceEvent {
  Uint32 type;
  Uint32 timestamp;
  Sint32 which;
} SDL_ControllerDeviceEvent;
typedef struct SDL_AudioDeviceEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 which;
  Uint8 iscapture;
  Uint8 padding1;
  Uint8 padding2;
  Uint8 padding3;
} SDL_AudioDeviceEvent;
typedef struct SDL_TouchFingerEvent {
  Uint32 type;
  ...;
} SDL_TouchFingerEvent;
typedef struct SDL_MultiGestureEvent {
  Uint32 type;
  ...;
} SDL_MultiGestureEvent;
typedef struct SDL_DollarGestureEvent {
  Uint32 type;
  ...;
} SDL_DollarGestureEvent;
typedef struct SDL_DropEvent {
  Uint32 type;
  Uint32 timestamp;
  char *file;
  Uint32 windowID;
} SDL_DropEvent;
typedef struct SDL_QuitEvent {
  Uint32 type;
  Uint32 timestamp;
} SDL_QuitEvent;
typedef struct SDL_OSEvent {
  Uint32 type;
  Uint32 timestamp;
} SDL_OSEvent;
typedef struct SDL_UserEvent {
  Uint32 type;
  Uint32 timestamp;
  Uint32 windowID;
  Sint32 code;
  void *data1;
  void *data2;
} SDL_UserEvent;
struct SDL_SysWMmsg;
typedef struct SDL_SysWMmsg SDL_SysWMmsg;
typedef struct SDL_SysWMEvent {
  Uint32 type;
  Uint32 timestamp;
  SDL_SysWMmsg *msg;
} SDL_SysWMEvent;
typedef union SDL_Event {
  Uint32 type;
  SDL_CommonEvent common;
  SDL_WindowEvent window;
  SDL_KeyboardEvent key;
  SDL_TextEditingEvent edit;
  SDL_TextInputEvent text;
  SDL_MouseMotionEvent motion;
  SDL_MouseButtonEvent button;
  SDL_MouseWheelEvent wheel;
  SDL_JoyAxisEvent jaxis;
  SDL_JoyBallEvent jball;
  SDL_JoyHatEvent jhat;
  SDL_JoyButtonEvent jbutton;
  SDL_JoyDeviceEvent jdevice;
  SDL_ControllerAxisEvent caxis;
  SDL_ControllerButtonEvent cbutton;
  SDL_ControllerDeviceEvent cdevice;
  SDL_AudioDeviceEvent adevice;
  SDL_QuitEvent quit;
  SDL_UserEvent user;
  SDL_SysWMEvent syswm;
  SDL_TouchFingerEvent tfinger;
  SDL_MultiGestureEvent mgesture;
  SDL_DollarGestureEvent dgesture;
  SDL_DropEvent drop;
  Uint8 padding[56];
} SDL_Event;
extern void SDL_PumpEvents(void);
typedef enum { SDL_ADDEVENT, SDL_PEEKEVENT, SDL_GETEVENT } SDL_eventaction;
extern int SDL_PeepEvents(SDL_Event *events, int numevents,
                          SDL_eventaction action, Uint32 minType,
                          Uint32 maxType);
extern SDL_bool SDL_HasEvent(Uint32 type);
extern SDL_bool SDL_HasEvents(Uint32 minType, Uint32 maxType);
extern void SDL_FlushEvent(Uint32 type);
extern void SDL_FlushEvents(Uint32 minType, Uint32 maxType);
extern int SDL_PollEvent(SDL_Event *event);
extern int SDL_WaitEvent(SDL_Event *event);
extern int SDL_WaitEventTimeout(SDL_Event *event, int timeout);
extern int SDL_PushEvent(SDL_Event *event);
typedef int (*SDL_EventFilter)(void *userdata, SDL_Event *event);
extern void SDL_SetEventFilter(SDL_EventFilter filter, void *userdata);
extern SDL_bool SDL_GetEventFilter(SDL_EventFilter *filter, void **userdata);
extern void SDL_AddEventWatch(SDL_EventFilter filter, void *userdata);
extern void SDL_DelEventWatch(SDL_EventFilter filter, void *userdata);
extern void SDL_FilterEvents(SDL_EventFilter filter, void *userdata);
extern Uint8 SDL_EventState(Uint32 type, int state);
extern Uint32 SDL_RegisterEvents(int numevents);
struct _SDL_Haptic;
typedef struct _SDL_Haptic SDL_Haptic;
typedef struct SDL_HapticDirection {
  Uint8 type;
  Sint32 dir[3];
} SDL_HapticDirection;
typedef struct SDL_HapticConstant {
  Uint16 type;
  SDL_HapticDirection direction;
  Uint32 length;
  Uint16 delay;
  Uint16 button;
  Uint16 interval;
  Sint16 level;
  Uint16 attack_length;
  Uint16 attack_level;
  Uint16 fade_length;
  Uint16 fade_level;
} SDL_HapticConstant;
typedef struct SDL_HapticPeriodic {
  Uint16 type;
  SDL_HapticDirection direction;
  Uint32 length;
  Uint16 delay;
  Uint16 button;
  Uint16 interval;
  Uint16 period;
  Sint16 magnitude;
  Sint16 offset;
  Uint16 phase;
  Uint16 attack_length;
  Uint16 attack_level;
  Uint16 fade_length;
  Uint16 fade_level;
} SDL_HapticPeriodic;
typedef struct SDL_HapticCondition {
  Uint16 type;
  SDL_HapticDirection direction;
  Uint32 length;
  Uint16 delay;
  Uint16 button;
  Uint16 interval;
  Uint16 right_sat[3];
  Uint16 left_sat[3];
  Sint16 right_coeff[3];
  Sint16 left_coeff[3];
  Uint16 deadband[3];
  Sint16 center[3];
} SDL_HapticCondition;
typedef struct SDL_HapticRamp {
  Uint16 type;
  SDL_HapticDirection direction;
  Uint32 length;
  Uint16 delay;
  Uint16 button;
  Uint16 interval;
  Sint16 start;
  Sint16 end;
  Uint16 attack_length;
  Uint16 attack_level;
  Uint16 fade_length;
  Uint16 fade_level;
} SDL_HapticRamp;
typedef struct SDL_HapticLeftRight {
  Uint16 type;
  Uint32 length;
  Uint16 large_magnitude;
  Uint16 small_magnitude;
} SDL_HapticLeftRight;
typedef struct SDL_HapticCustom {
  Uint16 type;
  SDL_HapticDirection direction;
  Uint32 length;
  Uint16 delay;
  Uint16 button;
  Uint16 interval;
  Uint8 channels;
  Uint16 period;
  Uint16 samples;
  Uint16 *data;
  Uint16 attack_length;
  Uint16 attack_level;
  Uint16 fade_length;
  Uint16 fade_level;
} SDL_HapticCustom;
typedef union SDL_HapticEffect {
  Uint16 type;
  SDL_HapticConstant constant;
  SDL_HapticPeriodic periodic;
  SDL_HapticCondition condition;
  SDL_HapticRamp ramp;
  SDL_HapticLeftRight leftright;
  SDL_HapticCustom custom;
} SDL_HapticEffect;
extern int SDL_NumHaptics(void);
extern const char *SDL_HapticName(int device_index);
extern SDL_Haptic *SDL_HapticOpen(int device_index);
extern int SDL_HapticOpened(int device_index);
extern int SDL_HapticIndex(SDL_Haptic *haptic);
extern int SDL_MouseIsHaptic(void);
extern SDL_Haptic *SDL_HapticOpenFromMouse(void);
extern int SDL_JoystickIsHaptic(SDL_Joystick *joystick);
extern SDL_Haptic *SDL_HapticOpenFromJoystick(SDL_Joystick *joystick);
extern void SDL_HapticClose(SDL_Haptic *haptic);
extern int SDL_HapticNumEffects(SDL_Haptic *haptic);
extern int SDL_HapticNumEffectsPlaying(SDL_Haptic *haptic);
extern unsigned int SDL_HapticQuery(SDL_Haptic *haptic);
extern int SDL_HapticNumAxes(SDL_Haptic *haptic);
extern int SDL_HapticEffectSupported(SDL_Haptic *haptic,
                                     SDL_HapticEffect *effect);
extern int SDL_HapticNewEffect(SDL_Haptic *haptic, SDL_HapticEffect *effect);
extern int SDL_HapticUpdateEffect(SDL_Haptic *haptic, int effect,
                                  SDL_HapticEffect *data);
extern int SDL_HapticRunEffect(SDL_Haptic *haptic, int effect,
                               Uint32 iterations);
extern int SDL_HapticStopEffect(SDL_Haptic *haptic, int effect);
extern void SDL_HapticDestroyEffect(SDL_Haptic *haptic, int effect);
extern int SDL_HapticGetEffectStatus(SDL_Haptic *haptic, int effect);
extern int SDL_HapticSetGain(SDL_Haptic *haptic, int gain);
extern int SDL_HapticSetAutocenter(SDL_Haptic *haptic, int autocenter);
extern int SDL_HapticPause(SDL_Haptic *haptic);
extern int SDL_HapticUnpause(SDL_Haptic *haptic);
extern int SDL_HapticStopAll(SDL_Haptic *haptic);
extern int SDL_HapticRumbleSupported(SDL_Haptic *haptic);
extern int SDL_HapticRumbleInit(SDL_Haptic *haptic);
extern int SDL_HapticRumblePlay(SDL_Haptic *haptic, float strength,
                                Uint32 length);
extern int SDL_HapticRumbleStop(SDL_Haptic *haptic);
typedef enum {
  SDL_HINT_DEFAULT,
  SDL_HINT_NORMAL,
  SDL_HINT_OVERRIDE
} SDL_HintPriority;
extern SDL_bool SDL_SetHintWithPriority(const char *name, const char *value,
                                        SDL_HintPriority priority);
extern SDL_bool SDL_SetHint(const char *name, const char *value);
extern const char *SDL_GetHint(const char *name);
extern SDL_bool SDL_GetHintBoolean(const char *name, SDL_bool default_value);
typedef void (*SDL_HintCallback)(void *userdata, const char *name,
                                 const char *oldValue, const char *newValue);
extern void SDL_AddHintCallback(const char *name, SDL_HintCallback callback,
                                void *userdata);
extern void SDL_DelHintCallback(const char *name, SDL_HintCallback callback,
                                void *userdata);
extern void SDL_ClearHints(void);
extern int SDL_Init(Uint32 flags);
extern int SDL_InitSubSystem(Uint32 flags);
extern void SDL_QuitSubSystem(Uint32 flags);
extern Uint32 SDL_WasInit(Uint32 flags);
extern void SDL_Quit(void);
