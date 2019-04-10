# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from _kivyjoy.structs import Struct, unbox, SDLError, u8
from _kivyjoy.helpers import *
from __kivyjoy import ffi, lib

@ffi.def_extern()
def pysdl2_event_filter(userdata, event):
    """
    Use like so:

    handle = ffi.new_handle(event_filter) # keep this alive
    lib.SDL_AddEventWatch(lib.pysdl2_event_filter, handle);
    """
    return ffi.from_handle(userdata)(event)

def addEventWatch(filter, userdata):
    """
    ``void SDL_AddEventWatch(int SDL_AddEventWatch(void *, SDL_Event *), void *)``
    
    Add a function which is called when an event is added to the queue.
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_AddEventWatch(filter_c, userdata_c)

def addHintCallback(name, callback, userdata):
    """
    ``void SDL_AddHintCallback(char const *, void SDL_AddHintCallback(void *, char const *, char const *, char const *), void *)``
    """
    name_c = u8(name)
    callback_c = unbox(callback, 'void(*)(void *, char const *, char const *, char const *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_AddHintCallback(name_c, callback_c, userdata_c)

def clearHints():
    """
    ``void SDL_ClearHints(void)``
    
    Clear all hints.
    
    This function is called during SDL_Quit() to free stored hints.
    """
    lib.SDL_ClearHints()

def delEventWatch(filter, userdata):
    """
    ``void SDL_DelEventWatch(int SDL_DelEventWatch(void *, SDL_Event *), void *)``
    
    Remove an event watch function added with SDL_AddEventWatch()
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_DelEventWatch(filter_c, userdata_c)

def delHintCallback(name, callback, userdata):
    """
    ``void SDL_DelHintCallback(char const *, void SDL_DelHintCallback(void *, char const *, char const *, char const *), void *)``
    
    Remove a function watching a particular hint.
    
    :param name: The hint being watched
    :param callback: The function being called when the hint value changes
    :param userdata: A pointer being passed to the callback function
    """
    name_c = u8(name)
    callback_c = unbox(callback, 'void(*)(void *, char const *, char const *, char const *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_DelHintCallback(name_c, callback_c, userdata_c)

def eventState(type, state):
    """
    ``uint8_t SDL_EventState(uint32_t, int)``
    
    This function allows you to set the state of processing certain
    events.If state is set to SDL_IGNORE, that event will be automatically
    dropped from the event queue and will not event be filtered.
    
    If state is set to SDL_ENABLE, that event will be processed normally.
    
    If state is set to SDL_QUERY, SDL_EventState() will return the current
    processing state of the specified event.
    """
    type_c = type
    state_c = state
    rc = lib.SDL_EventState(type_c, state_c)
    return rc

def filterEvents(filter, userdata):
    """
    ``void SDL_FilterEvents(int SDL_FilterEvents(void *, SDL_Event *), void *)``
    
    Run the filter function on the current event queue, removing any
    events for which the filter returns 0.
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_FilterEvents(filter_c, userdata_c)

def flushEvent(type):
    """
    ``void SDL_FlushEvent(uint32_t)``
    
    This function clears events from the event queue
    """
    type_c = type
    lib.SDL_FlushEvent(type_c)

def flushEvents(minType, maxType):
    """
    ``void SDL_FlushEvents(uint32_t, uint32_t)``
    """
    minType_c = minType
    maxType_c = maxType
    lib.SDL_FlushEvents(minType_c, maxType_c)

def gameControllerAddMapping(mappingString):
    """
    ``int SDL_GameControllerAddMapping(char const *)``
    
    Add or update an existing mapping configuration
    
    :return: 1 if mapping is added, 0 if updated, -1 on error
    """
    mappingString_c = u8(mappingString)
    rc = lib.SDL_GameControllerAddMapping(mappingString_c)
    if rc == -1: raise SDLError()
    return rc

def gameControllerClose(gamecontroller):
    """
    ``void SDL_GameControllerClose(SDL_GameController *)``
    
    Close a controller previously opened with SDL_GameControllerOpen().
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    lib.SDL_GameControllerClose(gamecontroller_c)

def gameControllerEventState(state):
    """
    ``int SDL_GameControllerEventState(int)``
    
    Enable/disable controller event polling.
    
    If controller events are disabled, you must call
    SDL_GameControllerUpdate() yourself and check the state of the
    controller when you want controller information.
    
    The state can be one of SDL_QUERY, SDL_ENABLE or SDL_IGNORE.
    """
    state_c = state
    rc = lib.SDL_GameControllerEventState(state_c)
    return rc

def gameControllerFromInstanceID(joyid):
    """
    ``SDL_GameController * SDL_GameControllerFromInstanceID(int32_t)``
    """
    joyid_c = joyid
    rc = lib.SDL_GameControllerFromInstanceID(joyid_c)
    return GameController(rc)

def gameControllerGetAttached(gamecontroller):
    """
    ``int SDL_GameControllerGetAttached(SDL_GameController *)``
    
    Returns SDL_TRUE if the controller has been opened and currently
    connected, or SDL_FALSE if it has not.
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetAttached(gamecontroller_c)
    return rc

def gameControllerGetAxis(gamecontroller, axis):
    """
    ``int16_t SDL_GameControllerGetAxis(SDL_GameController *, SDL_GameControllerAxis)``
    
    Get the current state of an axis control on a game controller.
    
    The state is a value ranging from -32768 to 32767.
    
    The axis indices start at index 0.
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    axis_c = axis
    rc = lib.SDL_GameControllerGetAxis(gamecontroller_c, axis_c)
    return rc

def gameControllerGetAxisFromString(pchString):
    """
    ``SDL_GameControllerAxis SDL_GameControllerGetAxisFromString(char const *)``
    
    turn this string into a axis mapping
    """
    pchString_c = u8(pchString)
    rc = lib.SDL_GameControllerGetAxisFromString(pchString_c)
    return rc

def gameControllerGetBindForAxis(gamecontroller, axis):
    """
    ``SDL_GameControllerButtonBind SDL_GameControllerGetBindForAxis(SDL_GameController *, SDL_GameControllerAxis)``
    
    Get the SDL joystick layer binding for this controller button mapping
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    axis_c = axis
    rc = lib.SDL_GameControllerGetBindForAxis(gamecontroller_c, axis_c)
    return GameControllerButtonBind(rc)

def gameControllerGetBindForButton(gamecontroller, button):
    """
    ``SDL_GameControllerButtonBind SDL_GameControllerGetBindForButton(SDL_GameController *, SDL_GameControllerButton)``
    
    Get the SDL joystick layer binding for this controller button mapping
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    button_c = button
    rc = lib.SDL_GameControllerGetBindForButton(gamecontroller_c, button_c)
    return GameControllerButtonBind(rc)

def gameControllerGetButton(gamecontroller, button):
    """
    ``uint8_t SDL_GameControllerGetButton(SDL_GameController *, SDL_GameControllerButton)``
    
    Get the current state of a button on a game controller.
    
    The button indices start at index 0.
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    button_c = button
    rc = lib.SDL_GameControllerGetButton(gamecontroller_c, button_c)
    return rc

def gameControllerGetButtonFromString(pchString):
    """
    ``SDL_GameControllerButton SDL_GameControllerGetButtonFromString(char const *)``
    
    turn this string into a button mapping
    """
    pchString_c = u8(pchString)
    rc = lib.SDL_GameControllerGetButtonFromString(pchString_c)
    return rc

def gameControllerGetJoystick(gamecontroller):
    """
    ``SDL_Joystick * SDL_GameControllerGetJoystick(SDL_GameController *)``
    
    Get the underlying joystick object used by a controller
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetJoystick(gamecontroller_c)
    return Joystick(rc)

def gameControllerGetProduct(gamecontroller):
    """
    ``uint16_t SDL_GameControllerGetProduct(SDL_GameController *)``
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetProduct(gamecontroller_c)
    return rc

def gameControllerGetProductVersion(gamecontroller):
    """
    ``uint16_t SDL_GameControllerGetProductVersion(SDL_GameController *)``
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetProductVersion(gamecontroller_c)
    return rc

def gameControllerGetStringForAxis(axis):
    """
    ``char const * SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis)``
    
    turn this axis enum into a string mapping
    """
    axis_c = axis
    rc = lib.SDL_GameControllerGetStringForAxis(axis_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerGetStringForButton(button):
    """
    ``char const * SDL_GameControllerGetStringForButton(SDL_GameControllerButton)``
    
    turn this button enum into a string mapping
    """
    button_c = button
    rc = lib.SDL_GameControllerGetStringForButton(button_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerGetVendor(gamecontroller):
    """
    ``uint16_t SDL_GameControllerGetVendor(SDL_GameController *)``
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetVendor(gamecontroller_c)
    return rc

def gameControllerMapping(gamecontroller):
    """
    ``char * SDL_GameControllerMapping(SDL_GameController *)``
    
    Get a mapping string for an open GameController
    
    :return: the mapping string. Must be freed with SDL_free. Returns NULL
        if no mapping is available
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerMapping(gamecontroller_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerMappingForGUID(guid):
    """
    ``char * SDL_GameControllerMappingForGUID(SDL_JoystickGUID)``
    
    Get a mapping string for a GUID
    
    :return: the mapping string. Must be freed with SDL_free. Returns NULL
        if no mapping is available
    """
    guid_c = unbox(guid, 'SDL_JoystickGUID')
    rc = lib.SDL_GameControllerMappingForGUID(guid_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerMappingForIndex(mapping_index):
    """
    ``char * SDL_GameControllerMappingForIndex(int)``
    """
    mapping_index_c = mapping_index
    rc = lib.SDL_GameControllerMappingForIndex(mapping_index_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerName(gamecontroller):
    """
    ``char const * SDL_GameControllerName(SDL_GameController *)``
    
    Return the name for this currently opened controller
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerName(gamecontroller_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerNameForIndex(joystick_index):
    """
    ``char const * SDL_GameControllerNameForIndex(int)``
    
    Get the implementation dependent name of a game controller. This can
    be called before any controllers are opened. If no name can be found,
    this function returns NULL.
    """
    joystick_index_c = joystick_index
    rc = lib.SDL_GameControllerNameForIndex(joystick_index_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def gameControllerNumMappings():
    """
    ``int SDL_GameControllerNumMappings(void)``
    """
    rc = lib.SDL_GameControllerNumMappings()
    return rc

def gameControllerOpen(joystick_index):
    """
    ``SDL_GameController * SDL_GameControllerOpen(int)``
    
    Open a game controller for use. The index passed as an argument refers
    to the N'th game controller on the system. This index is the value
    which will identify this controller in future controller events.
    
    :return: A controller identifier, or NULL if an error occurred.
    """
    joystick_index_c = joystick_index
    rc = lib.SDL_GameControllerOpen(joystick_index_c)
    if rc == ffi.NULL: raise SDLError()
    return GameController(rc)

def gameControllerUpdate():
    """
    ``void SDL_GameControllerUpdate(void)``
    
    Update the current state of the open game controllers.
    
    This is called automatically by the event loop if any game controller
    events are enabled.
    """
    lib.SDL_GameControllerUpdate()

def getEventFilter(filter, userdata):
    """
    ``int SDL_GetEventFilter(int(* *)(void *, SDL_Event *), void * *)``
    
    Return the current event filter - can be used to "chain" filters. If
    there is no event filter set, this function returns SDL_FALSE.
    """
    filter_c = unbox(filter, 'int(* *)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void * *')
    rc = lib.SDL_GetEventFilter(filter_c, userdata_c)
    return rc

def getHint(name):
    """
    ``char const * SDL_GetHint(char const *)``
    
    Get a hint.
    
    :return: The string value of a hint variable.
    """
    name_c = u8(name)
    rc = lib.SDL_GetHint(name_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def getHintBoolean(name, default_value):
    """
    ``int SDL_GetHintBoolean(char const *, int)``
    """
    name_c = u8(name)
    default_value_c = default_value
    rc = lib.SDL_GetHintBoolean(name_c, default_value_c)
    return rc

def getKeyFromName(name):
    """
    ``int32_t SDL_GetKeyFromName(char const *)``
    
    Get a key code from a human-readable name.
    
    :return: key code, or SDLK_UNKNOWN if the name wasn't recognized
    
    See also SDL_Keycode
    """
    name_c = u8(name)
    rc = lib.SDL_GetKeyFromName(name_c)
    return rc

def getKeyFromScancode(scancode):
    """
    ``int32_t SDL_GetKeyFromScancode(SDL_Scancode)``
    
    Get the key code corresponding to the given scancode according to the
    current keyboard layout.
    
    See SDL_Keycode for details.
    
    See also SDL_GetKeyName()
    """
    scancode_c = scancode
    rc = lib.SDL_GetKeyFromScancode(scancode_c)
    return rc

def getKeyName(key):
    """
    ``char const * SDL_GetKeyName(int32_t)``
    
    Get a human-readable name for a key.
    
    :return: A pointer to a UTF-8 string that stays valid at least until
        the next call to this function. If you need it around any longer,
        you must copy it. If the key doesn't have a name, this function
        returns an empty string ("").
    
    See also SDL_Key
    """
    key_c = key
    rc = lib.SDL_GetKeyName(key_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def getKeyboardState(numkeys=None):
    """
    ``uint8_t const * SDL_GetKeyboardState(int *)``
    
    Get a snapshot of the current state of the keyboard.
    
    :param numkeys: if non-NULL, receives the length of the returned
        array.
    :return: An array of key states. Indexes into this array are obtained
        by using
    
    Example:::
    
       const Uint8 *state = SDL_GetKeyboardState(NULL);
       if ( state[SDL_SCANCODE_RETURN] )   {
           printf("<RETURN> is pressed.\n");
       }
    
    """
    numkeys_c = unbox(numkeys, 'int *')
    rc = lib.SDL_GetKeyboardState(numkeys_c)
    return (rc, numkeys_c[0])

def getModState():
    """
    ``SDL_Keymod SDL_GetModState(void)``
    
    Get the current key modifier state for the keyboard.
    """
    rc = lib.SDL_GetModState()
    return rc

def getScancodeFromKey(key):
    """
    ``SDL_Scancode SDL_GetScancodeFromKey(int32_t)``
    
    Get the scancode corresponding to the given key code according to the
    current keyboard layout.
    
    See SDL_Scancode for details.
    
    See also SDL_GetScancodeName()
    """
    key_c = key
    rc = lib.SDL_GetScancodeFromKey(key_c)
    return rc

def getScancodeFromName(name):
    """
    ``SDL_Scancode SDL_GetScancodeFromName(char const *)``
    
    Get a scancode from a human-readable name.
    
    :return: scancode, or SDL_SCANCODE_UNKNOWN if the name wasn't
        recognized
    
    See also SDL_Scancode
    """
    name_c = u8(name)
    rc = lib.SDL_GetScancodeFromName(name_c)
    return rc

def getScancodeName(scancode):
    """
    ``char const * SDL_GetScancodeName(SDL_Scancode)``
    
    Get a human-readable name for a scancode.
    
    :return: A pointer to the name for the scancode. If the scancode
        doesn't have a name, this function returns an empty string ("").
    
    See also SDL_Scancode
    """
    scancode_c = scancode
    rc = lib.SDL_GetScancodeName(scancode_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def hapticClose(haptic):
    """
    ``void SDL_HapticClose(SDL_Haptic *)``
    
    Closes a Haptic device previously opened with SDL_HapticOpen().
    
    :param haptic: Haptic device to close.
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    lib.SDL_HapticClose(haptic_c)

def hapticDestroyEffect(haptic, effect):
    """
    ``void SDL_HapticDestroyEffect(SDL_Haptic *, int)``
    
    Destroys a haptic effect on the device.
    
    This will stop the effect if it's running. Effects are automatically
    destroyed when the device is closed.
    
    :param haptic: Device to destroy the effect on.
    :param effect: Identifier of the effect to destroy.
    
    See also SDL_HapticNewEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    lib.SDL_HapticDestroyEffect(haptic_c, effect_c)

def hapticEffectSupported(haptic, effect):
    """
    ``int SDL_HapticEffectSupported(SDL_Haptic *, SDL_HapticEffect *)``
    
    Checks to see if effect is supported by haptic.
    
    :param haptic: Haptic device to check on.
    :param effect: Effect to check to see if it is supported.
    :return: SDL_TRUE if effect is supported, SDL_FALSE if it isn't or -1
        on error.
    
    See also SDL_HapticQuery
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = unbox(effect, 'SDL_HapticEffect *')
    rc = lib.SDL_HapticEffectSupported(haptic_c, effect_c)
    return rc

def hapticGetEffectStatus(haptic, effect):
    """
    ``int SDL_HapticGetEffectStatus(SDL_Haptic *, int)``
    
    Gets the status of the current effect on the haptic device.
    
    Device must support the SDL_HAPTIC_STATUS feature.
    
    :param haptic: Haptic device to query the effect status on.
    :param effect: Identifier of the effect to query its status.
    :return: 0 if it isn't playing, 1 if it is playing or -1 on error.
    
    See also SDL_HapticRunEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    rc = lib.SDL_HapticGetEffectStatus(haptic_c, effect_c)
    if rc == -1: raise SDLError()
    return rc

def hapticIndex(haptic):
    """
    ``int SDL_HapticIndex(SDL_Haptic *)``
    
    Gets the index of a haptic device.
    
    :param haptic: Haptic device to get the index of.
    :return: The index of the haptic device or -1 on error.
    
    See also SDL_HapticOpen
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticIndex(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticName(device_index):
    """
    ``char const * SDL_HapticName(int)``
    
    Get the implementation dependent name of a Haptic device.
    
    This can be called before any joysticks are opened. If no name can be
    found, this function returns NULL.
    
    :param device_index: Index of the device to get its name.
    :return: Name of the device or NULL on error.
    
    See also SDL_NumHaptics
    """
    device_index_c = device_index
    rc = lib.SDL_HapticName(device_index_c)
    if rc == ffi.NULL: raise SDLError()
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def hapticNewEffect(haptic, effect):
    """
    ``int SDL_HapticNewEffect(SDL_Haptic *, SDL_HapticEffect *)``
    
    Creates a new haptic effect on the device.
    
    :param haptic: Haptic device to create the effect on.
    :param effect: Properties of the effect to create.
    :return: The id of the effect on success or -1 on error.
    
    See also SDL_HapticUpdateEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = unbox(effect, 'SDL_HapticEffect *')
    rc = lib.SDL_HapticNewEffect(haptic_c, effect_c)
    if rc == -1: raise SDLError()
    return rc

def hapticNumAxes(haptic):
    """
    ``int SDL_HapticNumAxes(SDL_Haptic *)``
    
    Gets the number of haptic axes the device has.
    
    See also SDL_HapticDirection
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticNumAxes(haptic_c)
    return rc

def hapticNumEffects(haptic):
    """
    ``int SDL_HapticNumEffects(SDL_Haptic *)``
    
    Returns the number of effects a haptic device can store.
    
    On some platforms this isn't fully supported, and therefore is an
    approximation. Always check to see if your created effect was actually
    created and do not rely solely on SDL_HapticNumEffects().
    
    :param haptic: The haptic device to query effect max.
    :return: The number of effects the haptic device can store or -1 on
        error.
    
    See also SDL_HapticNumEffectsPlaying
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticNumEffects(haptic_c)
    return rc

def hapticNumEffectsPlaying(haptic):
    """
    ``int SDL_HapticNumEffectsPlaying(SDL_Haptic *)``
    
    Returns the number of effects a haptic device can play at the same
    time.
    
    This is not supported on all platforms, but will always return a
    value. Added here for the sake of completeness.
    
    :param haptic: The haptic device to query maximum playing effects.
    :return: The number of effects the haptic device can play at the same
        time or -1 on error.
    
    See also SDL_HapticNumEffects
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticNumEffectsPlaying(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticOpen(device_index):
    """
    ``SDL_Haptic * SDL_HapticOpen(int)``
    
    Opens a Haptic device for usage.
    
    The index passed as an argument refers to the N'th Haptic device on
    this system.
    
    When opening a haptic device, its gain will be set to maximum and
    autocenter will be disabled. To modify these values use
    SDL_HapticSetGain() and SDL_HapticSetAutocenter().
    
    :param device_index: Index of the device to open.
    :return: Device identifier or NULL on error.
    
    See also SDL_HapticIndex
    """
    device_index_c = device_index
    rc = lib.SDL_HapticOpen(device_index_c)
    if rc == ffi.NULL: raise SDLError()
    return Haptic(rc)

def hapticOpenFromJoystick(joystick):
    """
    ``SDL_Haptic * SDL_HapticOpenFromJoystick(SDL_Joystick *)``
    
    Opens a Haptic device for usage from a Joystick device.
    
    You must still close the haptic device seperately. It will not be
    closed with the joystick.
    
    When opening from a joystick you should first close the haptic device
    before closing the joystick device. If not, on some implementations
    the haptic device will also get unallocated and you'll be unable to
    use force feedback on that device.
    
    :param joystick: Joystick to create a haptic device from.
    :return: A valid haptic device identifier on success or NULL on error.
    
    See also SDL_HapticOpen
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_HapticOpenFromJoystick(joystick_c)
    if rc == ffi.NULL: raise SDLError()
    return Haptic(rc)

def hapticOpenFromMouse():
    """
    ``SDL_Haptic * SDL_HapticOpenFromMouse(void)``
    
    Tries to open a haptic device from the current mouse.
    
    :return: The haptic device identifier or NULL on error.
    
    See also SDL_MouseIsHaptic
    """
    rc = lib.SDL_HapticOpenFromMouse()
    if rc == ffi.NULL: raise SDLError()
    return Haptic(rc)

def hapticOpened(device_index):
    """
    ``int SDL_HapticOpened(int)``
    
    Checks if the haptic device at index has been opened.
    
    :param device_index: Index to check to see if it has been opened.
    :return: 1 if it has been opened or 0 if it hasn't.
    
    See also SDL_HapticOpen
    """
    device_index_c = device_index
    rc = lib.SDL_HapticOpened(device_index_c)
    return rc

def hapticPause(haptic):
    """
    ``int SDL_HapticPause(SDL_Haptic *)``
    
    Pauses a haptic device.
    
    Device must support the SDL_HAPTIC_PAUSE feature. Call
    SDL_HapticUnpause() to resume playback.
    
    Do not modify the effects nor add new ones while the device is paused.
    That can cause all sorts of weird errors.
    
    :param haptic: Haptic device to pause.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticUnpause
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticPause(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticQuery(haptic):
    """
    ``unsigned int SDL_HapticQuery(SDL_Haptic *)``
    
    Gets the haptic devices supported features in bitwise matter.
    
    Example: ::
    
       if (SDL_HapticQuery(haptic) & SDL_HAPTIC_CONSTANT) {
           printf("We have constant haptic effect!");
       }
    
    
    :param haptic: The haptic device to query.
    :return: Haptic features in bitwise manner (OR'd).
    
    See also SDL_HapticNumEffects
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticQuery(haptic_c)
    return rc

def hapticRumbleInit(haptic):
    """
    ``int SDL_HapticRumbleInit(SDL_Haptic *)``
    
    Initializes the haptic device for simple rumble playback.
    
    :param haptic: Haptic device to initialize for simple rumble playback.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticOpen
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticRumbleInit(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticRumblePlay(haptic, strength, length):
    """
    ``int SDL_HapticRumblePlay(SDL_Haptic *, float, uint32_t)``
    
    Runs simple rumble on a haptic device.
    
    :param haptic: Haptic device to play rumble effect on.
    :param strength: Strength of the rumble to play as a 0-1 float value.
    :param length: Length of the rumble to play in milliseconds.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticRumbleSupported
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    strength_c = strength
    length_c = length
    rc = lib.SDL_HapticRumblePlay(haptic_c, strength_c, length_c)
    if rc == -1: raise SDLError()
    return rc

def hapticRumbleStop(haptic):
    """
    ``int SDL_HapticRumbleStop(SDL_Haptic *)``
    
    Stops the simple rumble on a haptic device.
    
    :param haptic: Haptic to stop the rumble on.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticRumbleSupported
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticRumbleStop(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticRumbleSupported(haptic):
    """
    ``int SDL_HapticRumbleSupported(SDL_Haptic *)``
    
    Checks to see if rumble is supported on a haptic device.
    
    :param haptic: Haptic device to check to see if it supports rumble.
    :return: SDL_TRUE if effect is supported, SDL_FALSE if it isn't or -1
        on error.
    
    See also SDL_HapticRumbleInit
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticRumbleSupported(haptic_c)
    return rc

def hapticRunEffect(haptic, effect, iterations):
    """
    ``int SDL_HapticRunEffect(SDL_Haptic *, int, uint32_t)``
    
    Runs the haptic effect on its associated haptic device.
    
    If iterations are SDL_HAPTIC_INFINITY, it'll run the effect over and
    over repeating the envelope (attack and fade) every time. If you only
    want the effect to last forever, set SDL_HAPTIC_INFINITY in the
    effect's length parameter.
    
    :param haptic: Haptic device to run the effect on.
    :param effect: Identifier of the haptic effect to run.
    :param iterations: Number of iterations to run the effect. Use
        SDL_HAPTIC_INFINITY for infinity.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticStopEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    iterations_c = iterations
    rc = lib.SDL_HapticRunEffect(haptic_c, effect_c, iterations_c)
    if rc == -1: raise SDLError()
    return rc

def hapticSetAutocenter(haptic, autocenter):
    """
    ``int SDL_HapticSetAutocenter(SDL_Haptic *, int)``
    
    Sets the global autocenter of the device.
    
    Autocenter should be between 0 and 100. Setting it to 0 will disable
    autocentering.
    
    Device must support the SDL_HAPTIC_AUTOCENTER feature.
    
    :param haptic: Haptic device to set autocentering on.
    :param autocenter: Value to set autocenter to, 0 disables
        autocentering.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticQuery
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    autocenter_c = autocenter
    rc = lib.SDL_HapticSetAutocenter(haptic_c, autocenter_c)
    if rc == -1: raise SDLError()
    return rc

def hapticSetGain(haptic, gain):
    """
    ``int SDL_HapticSetGain(SDL_Haptic *, int)``
    
    Sets the global gain of the device.
    
    Device must support the SDL_HAPTIC_GAIN feature.
    
    The user may specify the maximum gain by setting the environment
    variable SDL_HAPTIC_GAIN_MAX which should be between 0 and 100. All
    calls to SDL_HapticSetGain() will scale linearly using
    SDL_HAPTIC_GAIN_MAX as the maximum.
    
    :param haptic: Haptic device to set the gain on.
    :param gain: Value to set the gain to, should be between 0 and 100.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticQuery
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    gain_c = gain
    rc = lib.SDL_HapticSetGain(haptic_c, gain_c)
    if rc == -1: raise SDLError()
    return rc

def hapticStopAll(haptic):
    """
    ``int SDL_HapticStopAll(SDL_Haptic *)``
    
    Stops all the currently playing effects on a haptic device.
    
    :param haptic: Haptic device to stop.
    :return: 0 on success or -1 on error.
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticStopAll(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticStopEffect(haptic, effect):
    """
    ``int SDL_HapticStopEffect(SDL_Haptic *, int)``
    
    Stops the haptic effect on its associated haptic device.
    
    :param haptic: Haptic device to stop the effect on.
    :param effect: Identifier of the effect to stop.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticRunEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    rc = lib.SDL_HapticStopEffect(haptic_c, effect_c)
    if rc == -1: raise SDLError()
    return rc

def hapticUnpause(haptic):
    """
    ``int SDL_HapticUnpause(SDL_Haptic *)``
    
    Unpauses a haptic device.
    
    Call to unpause after SDL_HapticPause().
    
    :param haptic: Haptic device to pause.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticPause
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticUnpause(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticUpdateEffect(haptic, effect, data):
    """
    ``int SDL_HapticUpdateEffect(SDL_Haptic *, int, SDL_HapticEffect *)``
    
    Updates the properties of an effect.
    
    Can be used dynamically, although behaviour when dynamically changing
    direction may be strange. Specifically the effect may reupload itself
    and start playing from the start. You cannot change the type either
    when running SDL_HapticUpdateEffect().
    
    :param haptic: Haptic device that has the effect.
    :param effect: Effect to update.
    :param data: New effect properties to use.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticNewEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    data_c = unbox(data, 'SDL_HapticEffect *')
    rc = lib.SDL_HapticUpdateEffect(haptic_c, effect_c, data_c)
    if rc == -1: raise SDLError()
    return rc

def hasEvent(type):
    """
    ``int SDL_HasEvent(uint32_t)``
    
    Checks to see if certain event types are in the event queue.
    """
    type_c = type
    rc = lib.SDL_HasEvent(type_c)
    return rc

def hasEvents(minType, maxType):
    """
    ``int SDL_HasEvents(uint32_t, uint32_t)``
    """
    minType_c = minType
    maxType_c = maxType
    rc = lib.SDL_HasEvents(minType_c, maxType_c)
    return rc

def hasScreenKeyboardSupport():
    """
    ``int SDL_HasScreenKeyboardSupport(void)``
    
    Returns whether the platform has some screen keyboard support.
    
    :return: SDL_TRUE if some keyboard support is available else
        SDL_FALSE.
    
    Not all screen keyboard functions are supported on all platforms.
    
    See also SDL_IsScreenKeyboardShown()
    """
    rc = lib.SDL_HasScreenKeyboardSupport()
    return rc

def init(flags):
    """
    ``int SDL_Init(uint32_t)``
    
    This function initializes the subsystems specified by flags Unless the
    SDL_INIT_NOPARACHUTE flag is set, it will install cleanup signal
    handlers for some commonly ignored fatal signals (like SIGSEGV).
    """
    flags_c = flags
    rc = lib.SDL_Init(flags_c)
    return rc

def initSubSystem(flags):
    """
    ``int SDL_InitSubSystem(uint32_t)``
    
    This function initializes specific SDL subsystems
    """
    flags_c = flags
    rc = lib.SDL_InitSubSystem(flags_c)
    return rc

def isGameController(joystick_index):
    """
    ``int SDL_IsGameController(int)``
    
    Is the joystick on this index supported by the game controller
    interface?
    """
    joystick_index_c = joystick_index
    rc = lib.SDL_IsGameController(joystick_index_c)
    return rc

def isTextInputActive():
    """
    ``int SDL_IsTextInputActive(void)``
    
    Return whether or not Unicode text input events are enabled.
    
    See also SDL_StartTextInput()
    """
    rc = lib.SDL_IsTextInputActive()
    return rc

def joystickClose(joystick):
    """
    ``void SDL_JoystickClose(SDL_Joystick *)``
    
    Close a joystick previously opened with SDL_JoystickOpen().
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    lib.SDL_JoystickClose(joystick_c)

def joystickCurrentPowerLevel(joystick):
    """
    ``SDL_JoystickPowerLevel SDL_JoystickCurrentPowerLevel(SDL_Joystick *)``
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickCurrentPowerLevel(joystick_c)
    return rc

def joystickEventState(state):
    """
    ``int SDL_JoystickEventState(int)``
    
    Enable/disable joystick event polling.
    
    If joystick events are disabled, you must call SDL_JoystickUpdate()
    yourself and check the state of the joystick when you want joystick
    information.
    
    The state can be one of SDL_QUERY, SDL_ENABLE or SDL_IGNORE.
    """
    state_c = state
    rc = lib.SDL_JoystickEventState(state_c)
    return rc

def joystickFromInstanceID(joyid):
    """
    ``SDL_Joystick * SDL_JoystickFromInstanceID(int32_t)``
    """
    joyid_c = joyid
    rc = lib.SDL_JoystickFromInstanceID(joyid_c)
    return Joystick(rc)

def joystickGetAttached(joystick):
    """
    ``int SDL_JoystickGetAttached(SDL_Joystick *)``
    
    Returns SDL_TRUE if the joystick has been opened and currently
    connected, or SDL_FALSE if it has not.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetAttached(joystick_c)
    return rc

def joystickGetAxis(joystick, axis):
    """
    ``int16_t SDL_JoystickGetAxis(SDL_Joystick *, int)``
    
    Get the current state of an axis control on a joystick.
    
    The state is a value ranging from -32768 to 32767.
    
    The axis indices start at index 0.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    axis_c = axis
    rc = lib.SDL_JoystickGetAxis(joystick_c, axis_c)
    return rc

def joystickGetAxisInitialState(joystick, axis, state=None):
    """
    ``int SDL_JoystickGetAxisInitialState(SDL_Joystick *, int, int16_t *)``
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    axis_c = axis
    state_c = unbox(state, 'int16_t *')
    rc = lib.SDL_JoystickGetAxisInitialState(joystick_c, axis_c, state_c)
    return (rc, state_c[0])

def joystickGetBall(joystick, ball, dx=None, dy=None):
    """
    ``int SDL_JoystickGetBall(SDL_Joystick *, int, int *, int *)``
    
    Get the ball axis change since the last poll.
    
    :return: 0, or -1 if you passed it invalid parameters.
    
    The ball indices start at index 0.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    ball_c = ball
    dx_c = unbox(dx, 'int *')
    dy_c = unbox(dy, 'int *')
    rc = lib.SDL_JoystickGetBall(joystick_c, ball_c, dx_c, dy_c)
    return (rc, dx_c[0], dy_c[0])

def joystickGetButton(joystick, button):
    """
    ``uint8_t SDL_JoystickGetButton(SDL_Joystick *, int)``
    
    Get the current state of a button on a joystick.
    
    The button indices start at index 0.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    button_c = button
    rc = lib.SDL_JoystickGetButton(joystick_c, button_c)
    return rc

def joystickGetDeviceGUID(device_index):
    """
    ``SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int)``
    
    Return the GUID for the joystick at this index
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceGUID(device_index_c)
    return JoystickGUID(rc)

def joystickGetDeviceInstanceID(device_index):
    """
    ``int32_t SDL_JoystickGetDeviceInstanceID(int)``
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceInstanceID(device_index_c)
    return rc

def joystickGetDeviceProduct(device_index):
    """
    ``uint16_t SDL_JoystickGetDeviceProduct(int)``
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceProduct(device_index_c)
    return rc

def joystickGetDeviceProductVersion(device_index):
    """
    ``uint16_t SDL_JoystickGetDeviceProductVersion(int)``
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceProductVersion(device_index_c)
    return rc

def joystickGetDeviceType(device_index):
    """
    ``SDL_JoystickType SDL_JoystickGetDeviceType(int)``
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceType(device_index_c)
    return rc

def joystickGetDeviceVendor(device_index):
    """
    ``uint16_t SDL_JoystickGetDeviceVendor(int)``
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceVendor(device_index_c)
    return rc

def joystickGetGUID(joystick):
    """
    ``SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick *)``
    
    Return the GUID for this opened joystick
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetGUID(joystick_c)
    return JoystickGUID(rc)

def joystickGetGUIDFromString(pchGUID):
    """
    ``SDL_JoystickGUID SDL_JoystickGetGUIDFromString(char const *)``
    
    convert a string into a joystick formatted guid
    """
    pchGUID_c = u8(pchGUID)
    rc = lib.SDL_JoystickGetGUIDFromString(pchGUID_c)
    return JoystickGUID(rc)

def joystickGetGUIDString(guid, pszGUID, cbGUID):
    """
    ``void SDL_JoystickGetGUIDString(SDL_JoystickGUID, char *, int)``
    
    Return a string representation for this guid. pszGUID must point to at
    least 33 bytes (32 for the string plus a NULL terminator).
    """
    guid_c = unbox(guid, 'SDL_JoystickGUID')
    pszGUID_c = u8(pszGUID)
    cbGUID_c = cbGUID
    lib.SDL_JoystickGetGUIDString(guid_c, pszGUID_c, cbGUID_c)

def joystickGetHat(joystick, hat):
    """
    ``uint8_t SDL_JoystickGetHat(SDL_Joystick *, int)``
    
    Get the current state of a POV hat on a joystick.
    
    The hat indices start at index 0.
    
    :return: The return value is one of the following positions:
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    hat_c = hat
    rc = lib.SDL_JoystickGetHat(joystick_c, hat_c)
    return rc

def joystickGetProduct(joystick):
    """
    ``uint16_t SDL_JoystickGetProduct(SDL_Joystick *)``
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetProduct(joystick_c)
    return rc

def joystickGetProductVersion(joystick):
    """
    ``uint16_t SDL_JoystickGetProductVersion(SDL_Joystick *)``
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetProductVersion(joystick_c)
    return rc

def joystickGetType(joystick):
    """
    ``SDL_JoystickType SDL_JoystickGetType(SDL_Joystick *)``
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetType(joystick_c)
    return rc

def joystickGetVendor(joystick):
    """
    ``uint16_t SDL_JoystickGetVendor(SDL_Joystick *)``
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetVendor(joystick_c)
    return rc

def joystickInstanceID(joystick):
    """
    ``int32_t SDL_JoystickInstanceID(SDL_Joystick *)``
    
    Get the instance ID of an opened joystick or -1 if the joystick is
    invalid.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickInstanceID(joystick_c)
    return rc

def joystickIsHaptic(joystick):
    """
    ``int SDL_JoystickIsHaptic(SDL_Joystick *)``
    
    Checks to see if a joystick has haptic features.
    
    :param joystick: Joystick to test for haptic capabilities.
    :return: 1 if the joystick is haptic, 0 if it isn't or -1 if an error
        ocurred.
    
    See also SDL_HapticOpenFromJoystick
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickIsHaptic(joystick_c)
    return rc

def joystickName(joystick):
    """
    ``char const * SDL_JoystickName(SDL_Joystick *)``
    
    Return the name for this currently opened joystick. If no name can be
    found, this function returns NULL.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickName(joystick_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def joystickNameForIndex(device_index):
    """
    ``char const * SDL_JoystickNameForIndex(int)``
    
    Get the implementation dependent name of a joystick. This can be
    called before any joysticks are opened. If no name can be found, this
    function returns NULL.
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickNameForIndex(device_index_c)
    return ffi.string(rc).decode('utf-8') if rc != ffi.NULL else None

def joystickNumAxes(joystick):
    """
    ``int SDL_JoystickNumAxes(SDL_Joystick *)``
    
    Get the number of general axis controls on a joystick.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumAxes(joystick_c)
    return rc

def joystickNumBalls(joystick):
    """
    ``int SDL_JoystickNumBalls(SDL_Joystick *)``
    
    Get the number of trackballs on a joystick.
    
    Joystick trackballs have only relative motion events associated with
    them and their state cannot be polled.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumBalls(joystick_c)
    return rc

def joystickNumButtons(joystick):
    """
    ``int SDL_JoystickNumButtons(SDL_Joystick *)``
    
    Get the number of buttons on a joystick.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumButtons(joystick_c)
    return rc

def joystickNumHats(joystick):
    """
    ``int SDL_JoystickNumHats(SDL_Joystick *)``
    
    Get the number of POV hats on a joystick.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumHats(joystick_c)
    return rc

def joystickOpen(device_index):
    """
    ``SDL_Joystick * SDL_JoystickOpen(int)``
    
    Open a joystick for use. The index passed as an argument refers tothe
    N'th joystick on the system. This index is the value which will
    identify this joystick in future joystick events.
    
    :return: A joystick identifier, or NULL if an error occurred.
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickOpen(device_index_c)
    if rc == ffi.NULL: raise SDLError()
    return Joystick(rc)

def joystickUpdate():
    """
    ``void SDL_JoystickUpdate(void)``
    
    Update the current state of the open joysticks.
    
    This is called automatically by the event loop if any joystick events
    are enabled.
    """
    lib.SDL_JoystickUpdate()

def lockJoysticks():
    """
    ``void SDL_LockJoysticks(void)``
    """
    lib.SDL_LockJoysticks()

def mouseIsHaptic():
    """
    ``int SDL_MouseIsHaptic(void)``
    
    Gets whether or not the current mouse has haptic capabilities.
    
    :return: SDL_TRUE if the mouse is haptic, SDL_FALSE if it isn't.
    
    See also SDL_HapticOpenFromMouse
    """
    rc = lib.SDL_MouseIsHaptic()
    return rc

def numHaptics():
    """
    ``int SDL_NumHaptics(void)``
    
    Count the number of haptic devices attached to the system.
    
    :return: Number of haptic devices detected on the system.
    """
    rc = lib.SDL_NumHaptics()
    return rc

def numJoysticks():
    """
    ``int SDL_NumJoysticks(void)``
    
    Count the number of joysticks attached to the system right now
    """
    rc = lib.SDL_NumJoysticks()
    return rc

def peepEvents(events, numevents, action, minType, maxType):
    """
    ``int SDL_PeepEvents(SDL_Event *, int, SDL_eventaction, uint32_t, uint32_t)``
    
    Checks the event queue for messages and optionally returns them.
    
    If action is SDL_ADDEVENT, up to numevents events will be added to the
    back of the event queue.
    
    If action is SDL_PEEKEVENT, up to numevents events at the front of the
    event queue, within the specified minimum and maximum type, will be
    returned and will not be removed from the queue.
    
    If action is SDL_GETEVENT, up to numevents events at the front of the
    event queue, within the specified minimum and maximum type, will be
    returned and will be removed from the queue.
    
    :return: The number of events actually stored, or -1 if there was an
        error.
    
    This function is thread-safe.
    """
    events_c = unbox(events, 'SDL_Event *')
    numevents_c = numevents
    action_c = action
    minType_c = minType
    maxType_c = maxType
    rc = lib.SDL_PeepEvents(events_c, numevents_c, action_c, minType_c, maxType_c)
    return rc

def pollEvent(event):
    """
    ``int SDL_PollEvent(SDL_Event *)``
    
    Polls for currently pending events.
    
    :return: 1 if there are any pending events, or 0 if there are none
        available.
    :param event: If not NULL, the next event is removed from the queue
        and stored in that area.
    """
    event_c = unbox(event, 'SDL_Event *')
    rc = lib.SDL_PollEvent(event_c)
    return rc

def pumpEvents():
    """
    ``void SDL_PumpEvents(void)``
    
    Pumps the event loop, gathering events from the input devices.
    
    This function updates the event queue and internal input device state.
    
    This should only be run in the thread that sets the video mode.
    """
    lib.SDL_PumpEvents()

def pushEvent(event):
    """
    ``int SDL_PushEvent(SDL_Event *)``
    
    Add an event to the event queue.
    
    :return: 1 on success, 0 if the event was filtered, or -1 if the event
        queue was full or there was some other error.
    """
    event_c = unbox(event, 'SDL_Event *')
    rc = lib.SDL_PushEvent(event_c)
    return rc

def quit():
    """
    ``void SDL_Quit(void)``
    
    This function cleans up all initialized subsystems. You should call it
    upon all exit conditions.
    """
    lib.SDL_Quit()

def quitSubSystem(flags):
    """
    ``void SDL_QuitSubSystem(uint32_t)``
    
    This function cleans up specific SDL subsystems
    """
    flags_c = flags
    lib.SDL_QuitSubSystem(flags_c)

def registerEvents(numevents):
    """
    ``uint32_t SDL_RegisterEvents(int)``
    
    This function allocates a set of user-defined events, and returns the
    beginning event number for that set of events.
    
    If there aren't enough user-defined events left, this function returns
    (Uint32)-1
    """
    numevents_c = numevents
    rc = lib.SDL_RegisterEvents(numevents_c)
    return rc

def setEventFilter(filter, userdata):
    """
    ``void SDL_SetEventFilter(int SDL_SetEventFilter(void *, SDL_Event *), void *)``
    
    Sets up a filter to process all events before they change internal
    state and are posted to the internal event queue.
    
    The filter is prototyped as: ::
    
           int SDL_EventFilter(void *userdata, SDL_Event * event);
    
    
    If the filter returns 1, then the event will be added to the internal
    queue. If it returns 0, then the event will be dropped from the queue,
    but the internal state will still be updated. This allows selective
    filtering of dynamically arriving events.
    
    Be very careful of what you do in the event filter function, as it may
    run in a different thread!
    
    There is one caveat when dealing with the SDL_QuitEvent event type.
    The event filter is only called when the window manager desires to
    close the application window. If the event filter returns 1, then the
    window will be closed, otherwise the window will remain open if
    possible.
    
    If the quit event is generated by an interrupt signal, it will bypass
    the internal queue and be delivered to the application at the next
    event poll.
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_SetEventFilter(filter_c, userdata_c)

def setHint(name, value):
    """
    ``int SDL_SetHint(char const *, char const *)``
    
    Set a hint with normal priority.
    
    :return: SDL_TRUE if the hint was set, SDL_FALSE otherwise
    """
    name_c = u8(name)
    value_c = u8(value)
    rc = lib.SDL_SetHint(name_c, value_c)
    return rc

def setHintWithPriority(name, value, priority):
    """
    ``int SDL_SetHintWithPriority(char const *, char const *, SDL_HintPriority)``
    
    Set a hint with a specific priority.
    
    The priority controls the behavior when setting a hint that already
    has a value. Hints will replace existing hints of their priority and
    lower. Environment variables are considered to have override priority.
    
    :return: SDL_TRUE if the hint was set, SDL_FALSE otherwise
    """
    name_c = u8(name)
    value_c = u8(value)
    priority_c = priority
    rc = lib.SDL_SetHintWithPriority(name_c, value_c, priority_c)
    return rc

def setModState(modstate):
    """
    ``void SDL_SetModState(SDL_Keymod)``
    
    Set the current key modifier state for the keyboard.
    
    This does not change the keyboard state, only the key modifier flags.
    """
    modstate_c = modstate
    lib.SDL_SetModState(modstate_c)

def startTextInput():
    """
    ``void SDL_StartTextInput(void)``
    
    Start accepting Unicode text input events. This function will show the
    on-screen keyboard if supported.
    
    See also SDL_StopTextInput()
    """
    lib.SDL_StartTextInput()

def stopTextInput():
    """
    ``void SDL_StopTextInput(void)``
    
    Stop receiving any text input events. This function will hide the on-
    screen keyboard if supported.
    
    See also SDL_StartTextInput()
    """
    lib.SDL_StopTextInput()

def unlockJoysticks():
    """
    ``void SDL_UnlockJoysticks(void)``
    """
    lib.SDL_UnlockJoysticks()

def waitEvent(event):
    """
    ``int SDL_WaitEvent(SDL_Event *)``
    
    Waits indefinitely for the next available event.
    
    :return: 1, or 0 if there was an error while waiting for events.
    :param event: If not NULL, the next event is removed from the queue
        and stored in that area.
    """
    event_c = unbox(event, 'SDL_Event *')
    rc = lib.SDL_WaitEvent(event_c)
    return rc

def waitEventTimeout(event, timeout):
    """
    ``int SDL_WaitEventTimeout(SDL_Event *, int)``
    
    Waits until the specified timeout (in milliseconds) for the next
    available event.
    
    :return: 1, or 0 if there was an error while waiting for events.
    :param event: If not NULL, the next event is removed from the queue
        and stored in that area.
    :param timeout: The timeout (in milliseconds) to wait for next event.
    """
    event_c = unbox(event, 'SDL_Event *')
    timeout_c = timeout
    rc = lib.SDL_WaitEventTimeout(event_c, timeout_c)
    return rc

def wasInit(flags):
    """
    ``uint32_t SDL_WasInit(uint32_t)``
    
    This function returns a mask of the specified subsystems which have
    previously been initialized.
    
    If flags is 0, it returns a mask of all initialized subsystems.
    """
    flags_c = flags
    rc = lib.SDL_WasInit(flags_c)
    return rc

K_UNKNOWN = lib.SDLK_UNKNOWN
K_RETURN = lib.SDLK_RETURN
K_ESCAPE = lib.SDLK_ESCAPE
K_BACKSPACE = lib.SDLK_BACKSPACE
K_TAB = lib.SDLK_TAB
K_SPACE = lib.SDLK_SPACE
K_EXCLAIM = lib.SDLK_EXCLAIM
K_QUOTEDBL = lib.SDLK_QUOTEDBL
K_HASH = lib.SDLK_HASH
K_PERCENT = lib.SDLK_PERCENT
K_DOLLAR = lib.SDLK_DOLLAR
K_AMPERSAND = lib.SDLK_AMPERSAND
K_QUOTE = lib.SDLK_QUOTE
K_LEFTPAREN = lib.SDLK_LEFTPAREN
K_RIGHTPAREN = lib.SDLK_RIGHTPAREN
K_ASTERISK = lib.SDLK_ASTERISK
K_PLUS = lib.SDLK_PLUS
K_COMMA = lib.SDLK_COMMA
K_MINUS = lib.SDLK_MINUS
K_PERIOD = lib.SDLK_PERIOD
K_SLASH = lib.SDLK_SLASH
K_0 = lib.SDLK_0
K_1 = lib.SDLK_1
K_2 = lib.SDLK_2
K_3 = lib.SDLK_3
K_4 = lib.SDLK_4
K_5 = lib.SDLK_5
K_6 = lib.SDLK_6
K_7 = lib.SDLK_7
K_8 = lib.SDLK_8
K_9 = lib.SDLK_9
K_COLON = lib.SDLK_COLON
K_SEMICOLON = lib.SDLK_SEMICOLON
K_LESS = lib.SDLK_LESS
K_EQUALS = lib.SDLK_EQUALS
K_GREATER = lib.SDLK_GREATER
K_QUESTION = lib.SDLK_QUESTION
K_AT = lib.SDLK_AT
K_LEFTBRACKET = lib.SDLK_LEFTBRACKET
K_BACKSLASH = lib.SDLK_BACKSLASH
K_RIGHTBRACKET = lib.SDLK_RIGHTBRACKET
K_CARET = lib.SDLK_CARET
K_UNDERSCORE = lib.SDLK_UNDERSCORE
K_BACKQUOTE = lib.SDLK_BACKQUOTE
K_a = lib.SDLK_a
K_b = lib.SDLK_b
K_c = lib.SDLK_c
K_d = lib.SDLK_d
K_e = lib.SDLK_e
K_f = lib.SDLK_f
K_g = lib.SDLK_g
K_h = lib.SDLK_h
K_i = lib.SDLK_i
K_j = lib.SDLK_j
K_k = lib.SDLK_k
K_l = lib.SDLK_l
K_m = lib.SDLK_m
K_n = lib.SDLK_n
K_o = lib.SDLK_o
K_p = lib.SDLK_p
K_q = lib.SDLK_q
K_r = lib.SDLK_r
K_s = lib.SDLK_s
K_t = lib.SDLK_t
K_u = lib.SDLK_u
K_v = lib.SDLK_v
K_w = lib.SDLK_w
K_x = lib.SDLK_x
K_y = lib.SDLK_y
K_z = lib.SDLK_z
K_CAPSLOCK = lib.SDLK_CAPSLOCK
K_F1 = lib.SDLK_F1
K_F2 = lib.SDLK_F2
K_F3 = lib.SDLK_F3
K_F4 = lib.SDLK_F4
K_F5 = lib.SDLK_F5
K_F6 = lib.SDLK_F6
K_F7 = lib.SDLK_F7
K_F8 = lib.SDLK_F8
K_F9 = lib.SDLK_F9
K_F10 = lib.SDLK_F10
K_F11 = lib.SDLK_F11
K_F12 = lib.SDLK_F12
K_PRINTSCREEN = lib.SDLK_PRINTSCREEN
K_SCROLLLOCK = lib.SDLK_SCROLLLOCK
K_PAUSE = lib.SDLK_PAUSE
K_INSERT = lib.SDLK_INSERT
K_HOME = lib.SDLK_HOME
K_PAGEUP = lib.SDLK_PAGEUP
K_DELETE = lib.SDLK_DELETE
K_END = lib.SDLK_END
K_PAGEDOWN = lib.SDLK_PAGEDOWN
K_RIGHT = lib.SDLK_RIGHT
K_LEFT = lib.SDLK_LEFT
K_DOWN = lib.SDLK_DOWN
K_UP = lib.SDLK_UP
K_NUMLOCKCLEAR = lib.SDLK_NUMLOCKCLEAR
K_KP_DIVIDE = lib.SDLK_KP_DIVIDE
K_KP_MULTIPLY = lib.SDLK_KP_MULTIPLY
K_KP_MINUS = lib.SDLK_KP_MINUS
K_KP_PLUS = lib.SDLK_KP_PLUS
K_KP_ENTER = lib.SDLK_KP_ENTER
K_KP_1 = lib.SDLK_KP_1
K_KP_2 = lib.SDLK_KP_2
K_KP_3 = lib.SDLK_KP_3
K_KP_4 = lib.SDLK_KP_4
K_KP_5 = lib.SDLK_KP_5
K_KP_6 = lib.SDLK_KP_6
K_KP_7 = lib.SDLK_KP_7
K_KP_8 = lib.SDLK_KP_8
K_KP_9 = lib.SDLK_KP_9
K_KP_0 = lib.SDLK_KP_0
K_KP_PERIOD = lib.SDLK_KP_PERIOD
K_APPLICATION = lib.SDLK_APPLICATION
K_POWER = lib.SDLK_POWER
K_KP_EQUALS = lib.SDLK_KP_EQUALS
K_F13 = lib.SDLK_F13
K_F14 = lib.SDLK_F14
K_F15 = lib.SDLK_F15
K_F16 = lib.SDLK_F16
K_F17 = lib.SDLK_F17
K_F18 = lib.SDLK_F18
K_F19 = lib.SDLK_F19
K_F20 = lib.SDLK_F20
K_F21 = lib.SDLK_F21
K_F22 = lib.SDLK_F22
K_F23 = lib.SDLK_F23
K_F24 = lib.SDLK_F24
K_EXECUTE = lib.SDLK_EXECUTE
K_HELP = lib.SDLK_HELP
K_MENU = lib.SDLK_MENU
K_SELECT = lib.SDLK_SELECT
K_STOP = lib.SDLK_STOP
K_AGAIN = lib.SDLK_AGAIN
K_UNDO = lib.SDLK_UNDO
K_CUT = lib.SDLK_CUT
K_COPY = lib.SDLK_COPY
K_PASTE = lib.SDLK_PASTE
K_FIND = lib.SDLK_FIND
K_MUTE = lib.SDLK_MUTE
K_VOLUMEUP = lib.SDLK_VOLUMEUP
K_VOLUMEDOWN = lib.SDLK_VOLUMEDOWN
K_KP_COMMA = lib.SDLK_KP_COMMA
K_KP_EQUALSAS400 = lib.SDLK_KP_EQUALSAS400
K_ALTERASE = lib.SDLK_ALTERASE
K_SYSREQ = lib.SDLK_SYSREQ
K_CANCEL = lib.SDLK_CANCEL
K_CLEAR = lib.SDLK_CLEAR
K_PRIOR = lib.SDLK_PRIOR
K_RETURN2 = lib.SDLK_RETURN2
K_SEPARATOR = lib.SDLK_SEPARATOR
K_OUT = lib.SDLK_OUT
K_OPER = lib.SDLK_OPER
K_CLEARAGAIN = lib.SDLK_CLEARAGAIN
K_CRSEL = lib.SDLK_CRSEL
K_EXSEL = lib.SDLK_EXSEL
K_KP_00 = lib.SDLK_KP_00
K_KP_000 = lib.SDLK_KP_000
K_THOUSANDSSEPARATOR = lib.SDLK_THOUSANDSSEPARATOR
K_DECIMALSEPARATOR = lib.SDLK_DECIMALSEPARATOR
K_CURRENCYUNIT = lib.SDLK_CURRENCYUNIT
K_CURRENCYSUBUNIT = lib.SDLK_CURRENCYSUBUNIT
K_KP_LEFTPAREN = lib.SDLK_KP_LEFTPAREN
K_KP_RIGHTPAREN = lib.SDLK_KP_RIGHTPAREN
K_KP_LEFTBRACE = lib.SDLK_KP_LEFTBRACE
K_KP_RIGHTBRACE = lib.SDLK_KP_RIGHTBRACE
K_KP_TAB = lib.SDLK_KP_TAB
K_KP_BACKSPACE = lib.SDLK_KP_BACKSPACE
K_KP_A = lib.SDLK_KP_A
K_KP_B = lib.SDLK_KP_B
K_KP_C = lib.SDLK_KP_C
K_KP_D = lib.SDLK_KP_D
K_KP_E = lib.SDLK_KP_E
K_KP_F = lib.SDLK_KP_F
K_KP_XOR = lib.SDLK_KP_XOR
K_KP_POWER = lib.SDLK_KP_POWER
K_KP_PERCENT = lib.SDLK_KP_PERCENT
K_KP_LESS = lib.SDLK_KP_LESS
K_KP_GREATER = lib.SDLK_KP_GREATER
K_KP_AMPERSAND = lib.SDLK_KP_AMPERSAND
K_KP_DBLAMPERSAND = lib.SDLK_KP_DBLAMPERSAND
K_KP_VERTICALBAR = lib.SDLK_KP_VERTICALBAR
K_KP_DBLVERTICALBAR = lib.SDLK_KP_DBLVERTICALBAR
K_KP_COLON = lib.SDLK_KP_COLON
K_KP_HASH = lib.SDLK_KP_HASH
K_KP_SPACE = lib.SDLK_KP_SPACE
K_KP_AT = lib.SDLK_KP_AT
K_KP_EXCLAM = lib.SDLK_KP_EXCLAM
K_KP_MEMSTORE = lib.SDLK_KP_MEMSTORE
K_KP_MEMRECALL = lib.SDLK_KP_MEMRECALL
K_KP_MEMCLEAR = lib.SDLK_KP_MEMCLEAR
K_KP_MEMADD = lib.SDLK_KP_MEMADD
K_KP_MEMSUBTRACT = lib.SDLK_KP_MEMSUBTRACT
K_KP_MEMMULTIPLY = lib.SDLK_KP_MEMMULTIPLY
K_KP_MEMDIVIDE = lib.SDLK_KP_MEMDIVIDE
K_KP_PLUSMINUS = lib.SDLK_KP_PLUSMINUS
K_KP_CLEAR = lib.SDLK_KP_CLEAR
K_KP_CLEARENTRY = lib.SDLK_KP_CLEARENTRY
K_KP_BINARY = lib.SDLK_KP_BINARY
K_KP_OCTAL = lib.SDLK_KP_OCTAL
K_KP_DECIMAL = lib.SDLK_KP_DECIMAL
K_KP_HEXADECIMAL = lib.SDLK_KP_HEXADECIMAL
K_LCTRL = lib.SDLK_LCTRL
K_LSHIFT = lib.SDLK_LSHIFT
K_LALT = lib.SDLK_LALT
K_LGUI = lib.SDLK_LGUI
K_RCTRL = lib.SDLK_RCTRL
K_RSHIFT = lib.SDLK_RSHIFT
K_RALT = lib.SDLK_RALT
K_RGUI = lib.SDLK_RGUI
K_MODE = lib.SDLK_MODE
K_AUDIONEXT = lib.SDLK_AUDIONEXT
K_AUDIOPREV = lib.SDLK_AUDIOPREV
K_AUDIOSTOP = lib.SDLK_AUDIOSTOP
K_AUDIOPLAY = lib.SDLK_AUDIOPLAY
K_AUDIOMUTE = lib.SDLK_AUDIOMUTE
K_MEDIASELECT = lib.SDLK_MEDIASELECT
K_WWW = lib.SDLK_WWW
K_MAIL = lib.SDLK_MAIL
K_CALCULATOR = lib.SDLK_CALCULATOR
K_COMPUTER = lib.SDLK_COMPUTER
K_AC_SEARCH = lib.SDLK_AC_SEARCH
K_AC_HOME = lib.SDLK_AC_HOME
K_AC_BACK = lib.SDLK_AC_BACK
K_AC_FORWARD = lib.SDLK_AC_FORWARD
K_AC_STOP = lib.SDLK_AC_STOP
K_AC_REFRESH = lib.SDLK_AC_REFRESH
K_AC_BOOKMARKS = lib.SDLK_AC_BOOKMARKS
K_BRIGHTNESSDOWN = lib.SDLK_BRIGHTNESSDOWN
K_BRIGHTNESSUP = lib.SDLK_BRIGHTNESSUP
K_DISPLAYSWITCH = lib.SDLK_DISPLAYSWITCH
K_KBDILLUMTOGGLE = lib.SDLK_KBDILLUMTOGGLE
K_KBDILLUMDOWN = lib.SDLK_KBDILLUMDOWN
K_KBDILLUMUP = lib.SDLK_KBDILLUMUP
K_EJECT = lib.SDLK_EJECT
K_SLEEP = lib.SDLK_SLEEP
K_APP1 = lib.SDLK_APP1
K_APP2 = lib.SDLK_APP2
K_AUDIOREWIND = lib.SDLK_AUDIOREWIND
K_AUDIOFASTFORWARD = lib.SDLK_AUDIOFASTFORWARD

FIRSTEVENT = lib.SDL_FIRSTEVENT
QUIT = lib.SDL_QUIT
APP_TERMINATING = lib.SDL_APP_TERMINATING
APP_LOWMEMORY = lib.SDL_APP_LOWMEMORY
APP_WILLENTERBACKGROUND = lib.SDL_APP_WILLENTERBACKGROUND
APP_DIDENTERBACKGROUND = lib.SDL_APP_DIDENTERBACKGROUND
APP_WILLENTERFOREGROUND = lib.SDL_APP_WILLENTERFOREGROUND
APP_DIDENTERFOREGROUND = lib.SDL_APP_DIDENTERFOREGROUND
WINDOWEVENT = lib.SDL_WINDOWEVENT
SYSWMEVENT = lib.SDL_SYSWMEVENT
KEYDOWN = lib.SDL_KEYDOWN
KEYUP = lib.SDL_KEYUP
TEXTEDITING = lib.SDL_TEXTEDITING
TEXTINPUT = lib.SDL_TEXTINPUT
KEYMAPCHANGED = lib.SDL_KEYMAPCHANGED
MOUSEMOTION = lib.SDL_MOUSEMOTION
MOUSEBUTTONDOWN = lib.SDL_MOUSEBUTTONDOWN
MOUSEBUTTONUP = lib.SDL_MOUSEBUTTONUP
MOUSEWHEEL = lib.SDL_MOUSEWHEEL
JOYAXISMOTION = lib.SDL_JOYAXISMOTION
JOYBALLMOTION = lib.SDL_JOYBALLMOTION
JOYHATMOTION = lib.SDL_JOYHATMOTION
JOYBUTTONDOWN = lib.SDL_JOYBUTTONDOWN
JOYBUTTONUP = lib.SDL_JOYBUTTONUP
JOYDEVICEADDED = lib.SDL_JOYDEVICEADDED
JOYDEVICEREMOVED = lib.SDL_JOYDEVICEREMOVED
CONTROLLERAXISMOTION = lib.SDL_CONTROLLERAXISMOTION
CONTROLLERBUTTONDOWN = lib.SDL_CONTROLLERBUTTONDOWN
CONTROLLERBUTTONUP = lib.SDL_CONTROLLERBUTTONUP
CONTROLLERDEVICEADDED = lib.SDL_CONTROLLERDEVICEADDED
CONTROLLERDEVICEREMOVED = lib.SDL_CONTROLLERDEVICEREMOVED
CONTROLLERDEVICEREMAPPED = lib.SDL_CONTROLLERDEVICEREMAPPED
FINGERDOWN = lib.SDL_FINGERDOWN
FINGERUP = lib.SDL_FINGERUP
FINGERMOTION = lib.SDL_FINGERMOTION
DOLLARGESTURE = lib.SDL_DOLLARGESTURE
DOLLARRECORD = lib.SDL_DOLLARRECORD
MULTIGESTURE = lib.SDL_MULTIGESTURE
CLIPBOARDUPDATE = lib.SDL_CLIPBOARDUPDATE
DROPFILE = lib.SDL_DROPFILE
DROPTEXT = lib.SDL_DROPTEXT
DROPBEGIN = lib.SDL_DROPBEGIN
DROPCOMPLETE = lib.SDL_DROPCOMPLETE
AUDIODEVICEADDED = lib.SDL_AUDIODEVICEADDED
AUDIODEVICEREMOVED = lib.SDL_AUDIODEVICEREMOVED
RENDER_TARGETS_RESET = lib.SDL_RENDER_TARGETS_RESET
RENDER_DEVICE_RESET = lib.SDL_RENDER_DEVICE_RESET
USEREVENT = lib.SDL_USEREVENT
LASTEVENT = lib.SDL_LASTEVENT

CONTROLLER_AXIS_INVALID = lib.SDL_CONTROLLER_AXIS_INVALID
CONTROLLER_AXIS_LEFTX = lib.SDL_CONTROLLER_AXIS_LEFTX
CONTROLLER_AXIS_LEFTY = lib.SDL_CONTROLLER_AXIS_LEFTY
CONTROLLER_AXIS_RIGHTX = lib.SDL_CONTROLLER_AXIS_RIGHTX
CONTROLLER_AXIS_RIGHTY = lib.SDL_CONTROLLER_AXIS_RIGHTY
CONTROLLER_AXIS_TRIGGERLEFT = lib.SDL_CONTROLLER_AXIS_TRIGGERLEFT
CONTROLLER_AXIS_TRIGGERRIGHT = lib.SDL_CONTROLLER_AXIS_TRIGGERRIGHT
CONTROLLER_AXIS_MAX = lib.SDL_CONTROLLER_AXIS_MAX

CONTROLLER_BINDTYPE_NONE = lib.SDL_CONTROLLER_BINDTYPE_NONE
CONTROLLER_BINDTYPE_BUTTON = lib.SDL_CONTROLLER_BINDTYPE_BUTTON
CONTROLLER_BINDTYPE_AXIS = lib.SDL_CONTROLLER_BINDTYPE_AXIS
CONTROLLER_BINDTYPE_HAT = lib.SDL_CONTROLLER_BINDTYPE_HAT

CONTROLLER_BUTTON_INVALID = lib.SDL_CONTROLLER_BUTTON_INVALID
CONTROLLER_BUTTON_A = lib.SDL_CONTROLLER_BUTTON_A
CONTROLLER_BUTTON_B = lib.SDL_CONTROLLER_BUTTON_B
CONTROLLER_BUTTON_X = lib.SDL_CONTROLLER_BUTTON_X
CONTROLLER_BUTTON_Y = lib.SDL_CONTROLLER_BUTTON_Y
CONTROLLER_BUTTON_BACK = lib.SDL_CONTROLLER_BUTTON_BACK
CONTROLLER_BUTTON_GUIDE = lib.SDL_CONTROLLER_BUTTON_GUIDE
CONTROLLER_BUTTON_START = lib.SDL_CONTROLLER_BUTTON_START
CONTROLLER_BUTTON_LEFTSTICK = lib.SDL_CONTROLLER_BUTTON_LEFTSTICK
CONTROLLER_BUTTON_RIGHTSTICK = lib.SDL_CONTROLLER_BUTTON_RIGHTSTICK
CONTROLLER_BUTTON_LEFTSHOULDER = lib.SDL_CONTROLLER_BUTTON_LEFTSHOULDER
CONTROLLER_BUTTON_RIGHTSHOULDER = lib.SDL_CONTROLLER_BUTTON_RIGHTSHOULDER
CONTROLLER_BUTTON_DPAD_UP = lib.SDL_CONTROLLER_BUTTON_DPAD_UP
CONTROLLER_BUTTON_DPAD_DOWN = lib.SDL_CONTROLLER_BUTTON_DPAD_DOWN
CONTROLLER_BUTTON_DPAD_LEFT = lib.SDL_CONTROLLER_BUTTON_DPAD_LEFT
CONTROLLER_BUTTON_DPAD_RIGHT = lib.SDL_CONTROLLER_BUTTON_DPAD_RIGHT
CONTROLLER_BUTTON_MAX = lib.SDL_CONTROLLER_BUTTON_MAX

HINT_DEFAULT = lib.SDL_HINT_DEFAULT
HINT_NORMAL = lib.SDL_HINT_NORMAL
HINT_OVERRIDE = lib.SDL_HINT_OVERRIDE

JOYSTICK_POWER_UNKNOWN = lib.SDL_JOYSTICK_POWER_UNKNOWN
JOYSTICK_POWER_EMPTY = lib.SDL_JOYSTICK_POWER_EMPTY
JOYSTICK_POWER_LOW = lib.SDL_JOYSTICK_POWER_LOW
JOYSTICK_POWER_MEDIUM = lib.SDL_JOYSTICK_POWER_MEDIUM
JOYSTICK_POWER_FULL = lib.SDL_JOYSTICK_POWER_FULL
JOYSTICK_POWER_WIRED = lib.SDL_JOYSTICK_POWER_WIRED
JOYSTICK_POWER_MAX = lib.SDL_JOYSTICK_POWER_MAX

JOYSTICK_TYPE_UNKNOWN = lib.SDL_JOYSTICK_TYPE_UNKNOWN
JOYSTICK_TYPE_GAMECONTROLLER = lib.SDL_JOYSTICK_TYPE_GAMECONTROLLER
JOYSTICK_TYPE_WHEEL = lib.SDL_JOYSTICK_TYPE_WHEEL
JOYSTICK_TYPE_ARCADE_STICK = lib.SDL_JOYSTICK_TYPE_ARCADE_STICK
JOYSTICK_TYPE_FLIGHT_STICK = lib.SDL_JOYSTICK_TYPE_FLIGHT_STICK
JOYSTICK_TYPE_DANCE_PAD = lib.SDL_JOYSTICK_TYPE_DANCE_PAD
JOYSTICK_TYPE_GUITAR = lib.SDL_JOYSTICK_TYPE_GUITAR
JOYSTICK_TYPE_DRUM_KIT = lib.SDL_JOYSTICK_TYPE_DRUM_KIT
JOYSTICK_TYPE_ARCADE_PAD = lib.SDL_JOYSTICK_TYPE_ARCADE_PAD
JOYSTICK_TYPE_THROTTLE = lib.SDL_JOYSTICK_TYPE_THROTTLE

KMOD_NONE = lib.KMOD_NONE
KMOD_LSHIFT = lib.KMOD_LSHIFT
KMOD_RSHIFT = lib.KMOD_RSHIFT
KMOD_LCTRL = lib.KMOD_LCTRL
KMOD_RCTRL = lib.KMOD_RCTRL
KMOD_LALT = lib.KMOD_LALT
KMOD_RALT = lib.KMOD_RALT
KMOD_LGUI = lib.KMOD_LGUI
KMOD_RGUI = lib.KMOD_RGUI
KMOD_NUM = lib.KMOD_NUM
KMOD_CAPS = lib.KMOD_CAPS
KMOD_MODE = lib.KMOD_MODE
KMOD_RESERVED = lib.KMOD_RESERVED

SCANCODE_UNKNOWN = lib.SDL_SCANCODE_UNKNOWN
SCANCODE_A = lib.SDL_SCANCODE_A
SCANCODE_B = lib.SDL_SCANCODE_B
SCANCODE_C = lib.SDL_SCANCODE_C
SCANCODE_D = lib.SDL_SCANCODE_D
SCANCODE_E = lib.SDL_SCANCODE_E
SCANCODE_F = lib.SDL_SCANCODE_F
SCANCODE_G = lib.SDL_SCANCODE_G
SCANCODE_H = lib.SDL_SCANCODE_H
SCANCODE_I = lib.SDL_SCANCODE_I
SCANCODE_J = lib.SDL_SCANCODE_J
SCANCODE_K = lib.SDL_SCANCODE_K
SCANCODE_L = lib.SDL_SCANCODE_L
SCANCODE_M = lib.SDL_SCANCODE_M
SCANCODE_N = lib.SDL_SCANCODE_N
SCANCODE_O = lib.SDL_SCANCODE_O
SCANCODE_P = lib.SDL_SCANCODE_P
SCANCODE_Q = lib.SDL_SCANCODE_Q
SCANCODE_R = lib.SDL_SCANCODE_R
SCANCODE_S = lib.SDL_SCANCODE_S
SCANCODE_T = lib.SDL_SCANCODE_T
SCANCODE_U = lib.SDL_SCANCODE_U
SCANCODE_V = lib.SDL_SCANCODE_V
SCANCODE_W = lib.SDL_SCANCODE_W
SCANCODE_X = lib.SDL_SCANCODE_X
SCANCODE_Y = lib.SDL_SCANCODE_Y
SCANCODE_Z = lib.SDL_SCANCODE_Z
SCANCODE_1 = lib.SDL_SCANCODE_1
SCANCODE_2 = lib.SDL_SCANCODE_2
SCANCODE_3 = lib.SDL_SCANCODE_3
SCANCODE_4 = lib.SDL_SCANCODE_4
SCANCODE_5 = lib.SDL_SCANCODE_5
SCANCODE_6 = lib.SDL_SCANCODE_6
SCANCODE_7 = lib.SDL_SCANCODE_7
SCANCODE_8 = lib.SDL_SCANCODE_8
SCANCODE_9 = lib.SDL_SCANCODE_9
SCANCODE_0 = lib.SDL_SCANCODE_0
SCANCODE_RETURN = lib.SDL_SCANCODE_RETURN
SCANCODE_ESCAPE = lib.SDL_SCANCODE_ESCAPE
SCANCODE_BACKSPACE = lib.SDL_SCANCODE_BACKSPACE
SCANCODE_TAB = lib.SDL_SCANCODE_TAB
SCANCODE_SPACE = lib.SDL_SCANCODE_SPACE
SCANCODE_MINUS = lib.SDL_SCANCODE_MINUS
SCANCODE_EQUALS = lib.SDL_SCANCODE_EQUALS
SCANCODE_LEFTBRACKET = lib.SDL_SCANCODE_LEFTBRACKET
SCANCODE_RIGHTBRACKET = lib.SDL_SCANCODE_RIGHTBRACKET
SCANCODE_BACKSLASH = lib.SDL_SCANCODE_BACKSLASH
SCANCODE_NONUSHASH = lib.SDL_SCANCODE_NONUSHASH
SCANCODE_SEMICOLON = lib.SDL_SCANCODE_SEMICOLON
SCANCODE_APOSTROPHE = lib.SDL_SCANCODE_APOSTROPHE
SCANCODE_GRAVE = lib.SDL_SCANCODE_GRAVE
SCANCODE_COMMA = lib.SDL_SCANCODE_COMMA
SCANCODE_PERIOD = lib.SDL_SCANCODE_PERIOD
SCANCODE_SLASH = lib.SDL_SCANCODE_SLASH
SCANCODE_CAPSLOCK = lib.SDL_SCANCODE_CAPSLOCK
SCANCODE_F1 = lib.SDL_SCANCODE_F1
SCANCODE_F2 = lib.SDL_SCANCODE_F2
SCANCODE_F3 = lib.SDL_SCANCODE_F3
SCANCODE_F4 = lib.SDL_SCANCODE_F4
SCANCODE_F5 = lib.SDL_SCANCODE_F5
SCANCODE_F6 = lib.SDL_SCANCODE_F6
SCANCODE_F7 = lib.SDL_SCANCODE_F7
SCANCODE_F8 = lib.SDL_SCANCODE_F8
SCANCODE_F9 = lib.SDL_SCANCODE_F9
SCANCODE_F10 = lib.SDL_SCANCODE_F10
SCANCODE_F11 = lib.SDL_SCANCODE_F11
SCANCODE_F12 = lib.SDL_SCANCODE_F12
SCANCODE_PRINTSCREEN = lib.SDL_SCANCODE_PRINTSCREEN
SCANCODE_SCROLLLOCK = lib.SDL_SCANCODE_SCROLLLOCK
SCANCODE_PAUSE = lib.SDL_SCANCODE_PAUSE
SCANCODE_INSERT = lib.SDL_SCANCODE_INSERT
SCANCODE_HOME = lib.SDL_SCANCODE_HOME
SCANCODE_PAGEUP = lib.SDL_SCANCODE_PAGEUP
SCANCODE_DELETE = lib.SDL_SCANCODE_DELETE
SCANCODE_END = lib.SDL_SCANCODE_END
SCANCODE_PAGEDOWN = lib.SDL_SCANCODE_PAGEDOWN
SCANCODE_RIGHT = lib.SDL_SCANCODE_RIGHT
SCANCODE_LEFT = lib.SDL_SCANCODE_LEFT
SCANCODE_DOWN = lib.SDL_SCANCODE_DOWN
SCANCODE_UP = lib.SDL_SCANCODE_UP
SCANCODE_NUMLOCKCLEAR = lib.SDL_SCANCODE_NUMLOCKCLEAR
SCANCODE_KP_DIVIDE = lib.SDL_SCANCODE_KP_DIVIDE
SCANCODE_KP_MULTIPLY = lib.SDL_SCANCODE_KP_MULTIPLY
SCANCODE_KP_MINUS = lib.SDL_SCANCODE_KP_MINUS
SCANCODE_KP_PLUS = lib.SDL_SCANCODE_KP_PLUS
SCANCODE_KP_ENTER = lib.SDL_SCANCODE_KP_ENTER
SCANCODE_KP_1 = lib.SDL_SCANCODE_KP_1
SCANCODE_KP_2 = lib.SDL_SCANCODE_KP_2
SCANCODE_KP_3 = lib.SDL_SCANCODE_KP_3
SCANCODE_KP_4 = lib.SDL_SCANCODE_KP_4
SCANCODE_KP_5 = lib.SDL_SCANCODE_KP_5
SCANCODE_KP_6 = lib.SDL_SCANCODE_KP_6
SCANCODE_KP_7 = lib.SDL_SCANCODE_KP_7
SCANCODE_KP_8 = lib.SDL_SCANCODE_KP_8
SCANCODE_KP_9 = lib.SDL_SCANCODE_KP_9
SCANCODE_KP_0 = lib.SDL_SCANCODE_KP_0
SCANCODE_KP_PERIOD = lib.SDL_SCANCODE_KP_PERIOD
SCANCODE_NONUSBACKSLASH = lib.SDL_SCANCODE_NONUSBACKSLASH
SCANCODE_APPLICATION = lib.SDL_SCANCODE_APPLICATION
SCANCODE_POWER = lib.SDL_SCANCODE_POWER
SCANCODE_KP_EQUALS = lib.SDL_SCANCODE_KP_EQUALS
SCANCODE_F13 = lib.SDL_SCANCODE_F13
SCANCODE_F14 = lib.SDL_SCANCODE_F14
SCANCODE_F15 = lib.SDL_SCANCODE_F15
SCANCODE_F16 = lib.SDL_SCANCODE_F16
SCANCODE_F17 = lib.SDL_SCANCODE_F17
SCANCODE_F18 = lib.SDL_SCANCODE_F18
SCANCODE_F19 = lib.SDL_SCANCODE_F19
SCANCODE_F20 = lib.SDL_SCANCODE_F20
SCANCODE_F21 = lib.SDL_SCANCODE_F21
SCANCODE_F22 = lib.SDL_SCANCODE_F22
SCANCODE_F23 = lib.SDL_SCANCODE_F23
SCANCODE_F24 = lib.SDL_SCANCODE_F24
SCANCODE_EXECUTE = lib.SDL_SCANCODE_EXECUTE
SCANCODE_HELP = lib.SDL_SCANCODE_HELP
SCANCODE_MENU = lib.SDL_SCANCODE_MENU
SCANCODE_SELECT = lib.SDL_SCANCODE_SELECT
SCANCODE_STOP = lib.SDL_SCANCODE_STOP
SCANCODE_AGAIN = lib.SDL_SCANCODE_AGAIN
SCANCODE_UNDO = lib.SDL_SCANCODE_UNDO
SCANCODE_CUT = lib.SDL_SCANCODE_CUT
SCANCODE_COPY = lib.SDL_SCANCODE_COPY
SCANCODE_PASTE = lib.SDL_SCANCODE_PASTE
SCANCODE_FIND = lib.SDL_SCANCODE_FIND
SCANCODE_MUTE = lib.SDL_SCANCODE_MUTE
SCANCODE_VOLUMEUP = lib.SDL_SCANCODE_VOLUMEUP
SCANCODE_VOLUMEDOWN = lib.SDL_SCANCODE_VOLUMEDOWN
SCANCODE_KP_COMMA = lib.SDL_SCANCODE_KP_COMMA
SCANCODE_KP_EQUALSAS400 = lib.SDL_SCANCODE_KP_EQUALSAS400
SCANCODE_INTERNATIONAL1 = lib.SDL_SCANCODE_INTERNATIONAL1
SCANCODE_INTERNATIONAL2 = lib.SDL_SCANCODE_INTERNATIONAL2
SCANCODE_INTERNATIONAL3 = lib.SDL_SCANCODE_INTERNATIONAL3
SCANCODE_INTERNATIONAL4 = lib.SDL_SCANCODE_INTERNATIONAL4
SCANCODE_INTERNATIONAL5 = lib.SDL_SCANCODE_INTERNATIONAL5
SCANCODE_INTERNATIONAL6 = lib.SDL_SCANCODE_INTERNATIONAL6
SCANCODE_INTERNATIONAL7 = lib.SDL_SCANCODE_INTERNATIONAL7
SCANCODE_INTERNATIONAL8 = lib.SDL_SCANCODE_INTERNATIONAL8
SCANCODE_INTERNATIONAL9 = lib.SDL_SCANCODE_INTERNATIONAL9
SCANCODE_LANG1 = lib.SDL_SCANCODE_LANG1
SCANCODE_LANG2 = lib.SDL_SCANCODE_LANG2
SCANCODE_LANG3 = lib.SDL_SCANCODE_LANG3
SCANCODE_LANG4 = lib.SDL_SCANCODE_LANG4
SCANCODE_LANG5 = lib.SDL_SCANCODE_LANG5
SCANCODE_LANG6 = lib.SDL_SCANCODE_LANG6
SCANCODE_LANG7 = lib.SDL_SCANCODE_LANG7
SCANCODE_LANG8 = lib.SDL_SCANCODE_LANG8
SCANCODE_LANG9 = lib.SDL_SCANCODE_LANG9
SCANCODE_ALTERASE = lib.SDL_SCANCODE_ALTERASE
SCANCODE_SYSREQ = lib.SDL_SCANCODE_SYSREQ
SCANCODE_CANCEL = lib.SDL_SCANCODE_CANCEL
SCANCODE_CLEAR = lib.SDL_SCANCODE_CLEAR
SCANCODE_PRIOR = lib.SDL_SCANCODE_PRIOR
SCANCODE_RETURN2 = lib.SDL_SCANCODE_RETURN2
SCANCODE_SEPARATOR = lib.SDL_SCANCODE_SEPARATOR
SCANCODE_OUT = lib.SDL_SCANCODE_OUT
SCANCODE_OPER = lib.SDL_SCANCODE_OPER
SCANCODE_CLEARAGAIN = lib.SDL_SCANCODE_CLEARAGAIN
SCANCODE_CRSEL = lib.SDL_SCANCODE_CRSEL
SCANCODE_EXSEL = lib.SDL_SCANCODE_EXSEL
SCANCODE_KP_00 = lib.SDL_SCANCODE_KP_00
SCANCODE_KP_000 = lib.SDL_SCANCODE_KP_000
SCANCODE_THOUSANDSSEPARATOR = lib.SDL_SCANCODE_THOUSANDSSEPARATOR
SCANCODE_DECIMALSEPARATOR = lib.SDL_SCANCODE_DECIMALSEPARATOR
SCANCODE_CURRENCYUNIT = lib.SDL_SCANCODE_CURRENCYUNIT
SCANCODE_CURRENCYSUBUNIT = lib.SDL_SCANCODE_CURRENCYSUBUNIT
SCANCODE_KP_LEFTPAREN = lib.SDL_SCANCODE_KP_LEFTPAREN
SCANCODE_KP_RIGHTPAREN = lib.SDL_SCANCODE_KP_RIGHTPAREN
SCANCODE_KP_LEFTBRACE = lib.SDL_SCANCODE_KP_LEFTBRACE
SCANCODE_KP_RIGHTBRACE = lib.SDL_SCANCODE_KP_RIGHTBRACE
SCANCODE_KP_TAB = lib.SDL_SCANCODE_KP_TAB
SCANCODE_KP_BACKSPACE = lib.SDL_SCANCODE_KP_BACKSPACE
SCANCODE_KP_A = lib.SDL_SCANCODE_KP_A
SCANCODE_KP_B = lib.SDL_SCANCODE_KP_B
SCANCODE_KP_C = lib.SDL_SCANCODE_KP_C
SCANCODE_KP_D = lib.SDL_SCANCODE_KP_D
SCANCODE_KP_E = lib.SDL_SCANCODE_KP_E
SCANCODE_KP_F = lib.SDL_SCANCODE_KP_F
SCANCODE_KP_XOR = lib.SDL_SCANCODE_KP_XOR
SCANCODE_KP_POWER = lib.SDL_SCANCODE_KP_POWER
SCANCODE_KP_PERCENT = lib.SDL_SCANCODE_KP_PERCENT
SCANCODE_KP_LESS = lib.SDL_SCANCODE_KP_LESS
SCANCODE_KP_GREATER = lib.SDL_SCANCODE_KP_GREATER
SCANCODE_KP_AMPERSAND = lib.SDL_SCANCODE_KP_AMPERSAND
SCANCODE_KP_DBLAMPERSAND = lib.SDL_SCANCODE_KP_DBLAMPERSAND
SCANCODE_KP_VERTICALBAR = lib.SDL_SCANCODE_KP_VERTICALBAR
SCANCODE_KP_DBLVERTICALBAR = lib.SDL_SCANCODE_KP_DBLVERTICALBAR
SCANCODE_KP_COLON = lib.SDL_SCANCODE_KP_COLON
SCANCODE_KP_HASH = lib.SDL_SCANCODE_KP_HASH
SCANCODE_KP_SPACE = lib.SDL_SCANCODE_KP_SPACE
SCANCODE_KP_AT = lib.SDL_SCANCODE_KP_AT
SCANCODE_KP_EXCLAM = lib.SDL_SCANCODE_KP_EXCLAM
SCANCODE_KP_MEMSTORE = lib.SDL_SCANCODE_KP_MEMSTORE
SCANCODE_KP_MEMRECALL = lib.SDL_SCANCODE_KP_MEMRECALL
SCANCODE_KP_MEMCLEAR = lib.SDL_SCANCODE_KP_MEMCLEAR
SCANCODE_KP_MEMADD = lib.SDL_SCANCODE_KP_MEMADD
SCANCODE_KP_MEMSUBTRACT = lib.SDL_SCANCODE_KP_MEMSUBTRACT
SCANCODE_KP_MEMMULTIPLY = lib.SDL_SCANCODE_KP_MEMMULTIPLY
SCANCODE_KP_MEMDIVIDE = lib.SDL_SCANCODE_KP_MEMDIVIDE
SCANCODE_KP_PLUSMINUS = lib.SDL_SCANCODE_KP_PLUSMINUS
SCANCODE_KP_CLEAR = lib.SDL_SCANCODE_KP_CLEAR
SCANCODE_KP_CLEARENTRY = lib.SDL_SCANCODE_KP_CLEARENTRY
SCANCODE_KP_BINARY = lib.SDL_SCANCODE_KP_BINARY
SCANCODE_KP_OCTAL = lib.SDL_SCANCODE_KP_OCTAL
SCANCODE_KP_DECIMAL = lib.SDL_SCANCODE_KP_DECIMAL
SCANCODE_KP_HEXADECIMAL = lib.SDL_SCANCODE_KP_HEXADECIMAL
SCANCODE_LCTRL = lib.SDL_SCANCODE_LCTRL
SCANCODE_LSHIFT = lib.SDL_SCANCODE_LSHIFT
SCANCODE_LALT = lib.SDL_SCANCODE_LALT
SCANCODE_LGUI = lib.SDL_SCANCODE_LGUI
SCANCODE_RCTRL = lib.SDL_SCANCODE_RCTRL
SCANCODE_RSHIFT = lib.SDL_SCANCODE_RSHIFT
SCANCODE_RALT = lib.SDL_SCANCODE_RALT
SCANCODE_RGUI = lib.SDL_SCANCODE_RGUI
SCANCODE_MODE = lib.SDL_SCANCODE_MODE
SCANCODE_AUDIONEXT = lib.SDL_SCANCODE_AUDIONEXT
SCANCODE_AUDIOPREV = lib.SDL_SCANCODE_AUDIOPREV
SCANCODE_AUDIOSTOP = lib.SDL_SCANCODE_AUDIOSTOP
SCANCODE_AUDIOPLAY = lib.SDL_SCANCODE_AUDIOPLAY
SCANCODE_AUDIOMUTE = lib.SDL_SCANCODE_AUDIOMUTE
SCANCODE_MEDIASELECT = lib.SDL_SCANCODE_MEDIASELECT
SCANCODE_WWW = lib.SDL_SCANCODE_WWW
SCANCODE_MAIL = lib.SDL_SCANCODE_MAIL
SCANCODE_CALCULATOR = lib.SDL_SCANCODE_CALCULATOR
SCANCODE_COMPUTER = lib.SDL_SCANCODE_COMPUTER
SCANCODE_AC_SEARCH = lib.SDL_SCANCODE_AC_SEARCH
SCANCODE_AC_HOME = lib.SDL_SCANCODE_AC_HOME
SCANCODE_AC_BACK = lib.SDL_SCANCODE_AC_BACK
SCANCODE_AC_FORWARD = lib.SDL_SCANCODE_AC_FORWARD
SCANCODE_AC_STOP = lib.SDL_SCANCODE_AC_STOP
SCANCODE_AC_REFRESH = lib.SDL_SCANCODE_AC_REFRESH
SCANCODE_AC_BOOKMARKS = lib.SDL_SCANCODE_AC_BOOKMARKS
SCANCODE_BRIGHTNESSDOWN = lib.SDL_SCANCODE_BRIGHTNESSDOWN
SCANCODE_BRIGHTNESSUP = lib.SDL_SCANCODE_BRIGHTNESSUP
SCANCODE_DISPLAYSWITCH = lib.SDL_SCANCODE_DISPLAYSWITCH
SCANCODE_KBDILLUMTOGGLE = lib.SDL_SCANCODE_KBDILLUMTOGGLE
SCANCODE_KBDILLUMDOWN = lib.SDL_SCANCODE_KBDILLUMDOWN
SCANCODE_KBDILLUMUP = lib.SDL_SCANCODE_KBDILLUMUP
SCANCODE_EJECT = lib.SDL_SCANCODE_EJECT
SCANCODE_SLEEP = lib.SDL_SCANCODE_SLEEP
SCANCODE_APP1 = lib.SDL_SCANCODE_APP1
SCANCODE_APP2 = lib.SDL_SCANCODE_APP2
SCANCODE_AUDIOREWIND = lib.SDL_SCANCODE_AUDIOREWIND
SCANCODE_AUDIOFASTFORWARD = lib.SDL_SCANCODE_AUDIOFASTFORWARD
NUM_SCANCODES = lib.SDL_NUM_SCANCODES

ADDEVENT = lib.SDL_ADDEVENT
PEEKEVENT = lib.SDL_PEEKEVENT
GETEVENT = lib.SDL_GETEVENT

BUTTON_LEFT = lib.SDL_BUTTON_LEFT

BUTTON_LMASK = lib.SDL_BUTTON_LMASK

BUTTON_MIDDLE = lib.SDL_BUTTON_MIDDLE

BUTTON_MMASK = lib.SDL_BUTTON_MMASK

BUTTON_RIGHT = lib.SDL_BUTTON_RIGHT

BUTTON_RMASK = lib.SDL_BUTTON_RMASK

BUTTON_X1 = lib.SDL_BUTTON_X1

BUTTON_X1MASK = lib.SDL_BUTTON_X1MASK

BUTTON_X2 = lib.SDL_BUTTON_X2

BUTTON_X2MASK = lib.SDL_BUTTON_X2MASK

COMPILEDVERSION = lib.SDL_COMPILEDVERSION

DISABLE = lib.SDL_DISABLE

DONTFREE = lib.SDL_DONTFREE

ENABLE = lib.SDL_ENABLE

HAPTIC_AUTOCENTER = lib.SDL_HAPTIC_AUTOCENTER

HAPTIC_CARTESIAN = lib.SDL_HAPTIC_CARTESIAN

HAPTIC_CONSTANT = lib.SDL_HAPTIC_CONSTANT

HAPTIC_CUSTOM = lib.SDL_HAPTIC_CUSTOM

HAPTIC_DAMPER = lib.SDL_HAPTIC_DAMPER

HAPTIC_FRICTION = lib.SDL_HAPTIC_FRICTION

HAPTIC_GAIN = lib.SDL_HAPTIC_GAIN

HAPTIC_INERTIA = lib.SDL_HAPTIC_INERTIA

HAPTIC_INFINITY = lib.SDL_HAPTIC_INFINITY

HAPTIC_LEFTRIGHT = lib.SDL_HAPTIC_LEFTRIGHT

HAPTIC_PAUSE = lib.SDL_HAPTIC_PAUSE

HAPTIC_POLAR = lib.SDL_HAPTIC_POLAR

HAPTIC_RAMP = lib.SDL_HAPTIC_RAMP

HAPTIC_SAWTOOTHDOWN = lib.SDL_HAPTIC_SAWTOOTHDOWN

HAPTIC_SAWTOOTHUP = lib.SDL_HAPTIC_SAWTOOTHUP

HAPTIC_SINE = lib.SDL_HAPTIC_SINE

HAPTIC_SPHERICAL = lib.SDL_HAPTIC_SPHERICAL

HAPTIC_SPRING = lib.SDL_HAPTIC_SPRING

HAPTIC_STATUS = lib.SDL_HAPTIC_STATUS

HAPTIC_TRIANGLE = lib.SDL_HAPTIC_TRIANGLE

HAT_CENTERED = lib.SDL_HAT_CENTERED

HAT_DOWN = lib.SDL_HAT_DOWN

HAT_LEFT = lib.SDL_HAT_LEFT

HAT_LEFTDOWN = lib.SDL_HAT_LEFTDOWN

HAT_LEFTUP = lib.SDL_HAT_LEFTUP

HAT_RIGHT = lib.SDL_HAT_RIGHT

HAT_RIGHTDOWN = lib.SDL_HAT_RIGHTDOWN

HAT_RIGHTUP = lib.SDL_HAT_RIGHTUP

HAT_UP = lib.SDL_HAT_UP

IGNORE = lib.SDL_IGNORE

INIT_AUDIO = lib.SDL_INIT_AUDIO

INIT_EVENTS = lib.SDL_INIT_EVENTS

INIT_EVERYTHING = lib.SDL_INIT_EVERYTHING

INIT_GAMECONTROLLER = lib.SDL_INIT_GAMECONTROLLER

INIT_HAPTIC = lib.SDL_INIT_HAPTIC

INIT_JOYSTICK = lib.SDL_INIT_JOYSTICK

INIT_NOPARACHUTE = lib.SDL_INIT_NOPARACHUTE

INIT_TIMER = lib.SDL_INIT_TIMER

INIT_VIDEO = lib.SDL_INIT_VIDEO

LINE = lib.SDL_LINE

MAJOR_VERSION = lib.SDL_MAJOR_VERSION

MAX_LOG_MESSAGE = lib.SDL_MAX_LOG_MESSAGE

MINOR_VERSION = lib.SDL_MINOR_VERSION

NULL_WHILE_LOOP_CONDITION = lib.SDL_NULL_WHILE_LOOP_CONDITION

PATCHLEVEL = lib.SDL_PATCHLEVEL

PREALLOC = lib.SDL_PREALLOC

PRESSED = lib.SDL_PRESSED

QUERY = lib.SDL_QUERY

RELEASED = lib.SDL_RELEASED

RLEACCEL = lib.SDL_RLEACCEL

RWOPS_JNIFILE = lib.SDL_RWOPS_JNIFILE

RWOPS_MEMORY = lib.SDL_RWOPS_MEMORY

RWOPS_MEMORY_RO = lib.SDL_RWOPS_MEMORY_RO

RWOPS_STDFILE = lib.SDL_RWOPS_STDFILE

RWOPS_UNKNOWN = lib.SDL_RWOPS_UNKNOWN

RWOPS_WINFILE = lib.SDL_RWOPS_WINFILE

SWSURFACE = lib.SDL_SWSURFACE

TEXTEDITINGEVENT_TEXT_SIZE = lib.SDL_TEXTEDITINGEVENT_TEXT_SIZE

TEXTINPUTEVENT_TEXT_SIZE = lib.SDL_TEXTINPUTEVENT_TEXT_SIZE

TOUCH_MOUSEID = lib.SDL_TOUCH_MOUSEID

WINDOWPOS_CENTERED = lib.SDL_WINDOWPOS_CENTERED

WINDOWPOS_CENTERED_MASK = lib.SDL_WINDOWPOS_CENTERED_MASK

WINDOWPOS_UNDEFINED = lib.SDL_WINDOWPOS_UNDEFINED

WINDOWPOS_UNDEFINED_MASK = lib.SDL_WINDOWPOS_UNDEFINED_MASK

class AudioDeviceEvent(Struct):
    """Wrap `SDL_AudioDeviceEvent`"""
    __ctype__ = 'SDL_AudioDeviceEvent'
    _fields = ('type', 'timestamp', 'which', 'iscapture', 'padding1',
        'padding2', 'padding3')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def iscapture(self):
        return self.cdata.iscapture

    @iscapture.setter
    def iscapture(self, value):
        self.cdata.iscapture = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

class CommonEvent(Struct):
    """Wrap `SDL_CommonEvent`"""
    __ctype__ = 'SDL_CommonEvent'
    _fields = 'type', 'timestamp'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

class ControllerAxisEvent(Struct):
    """Wrap `SDL_ControllerAxisEvent`"""
    __ctype__ = 'SDL_ControllerAxisEvent'
    _fields = ('type', 'timestamp', 'which', 'axis', 'padding1', 'padding2',
        'padding3', 'value', 'padding4')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def axis(self):
        return self.cdata.axis

    @axis.setter
    def axis(self, value):
        self.cdata.axis = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

    @property
    def padding4(self):
        return self.cdata.padding4

    @padding4.setter
    def padding4(self, value):
        self.cdata.padding4 = value

class ControllerButtonEvent(Struct):
    """Wrap `SDL_ControllerButtonEvent`"""
    __ctype__ = 'SDL_ControllerButtonEvent'
    _fields = ('type', 'timestamp', 'which', 'button', 'state', 'padding1',
        'padding2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

class ControllerDeviceEvent(Struct):
    """Wrap `SDL_ControllerDeviceEvent`"""
    __ctype__ = 'SDL_ControllerDeviceEvent'
    _fields = 'type', 'timestamp', 'which'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

class DollarGestureEvent(Struct):
    """Wrap `SDL_DollarGestureEvent`"""
    __ctype__ = 'SDL_DollarGestureEvent'
    _fields = 'type',

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

class DropEvent(Struct):
    """Wrap `SDL_DropEvent`"""
    __ctype__ = 'SDL_DropEvent'
    _fields = 'type', 'timestamp', 'file', 'windowID'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def file(self):
        return self.cdata.file

    @file.setter
    def file(self, value):
        self.cdata.file = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

class Event(Struct):
    """Wrap `SDL_Event`"""
    __ctype__ = 'SDL_Event'
    _fields = ('type', 'common', 'window', 'key', 'edit', 'text', 'motion',
        'button', 'wheel', 'jaxis', 'jball', 'jhat', 'jbutton', 'jdevice',
        'caxis', 'cbutton', 'cdevice', 'adevice', 'quit', 'user', 'syswm',
        'tfinger', 'mgesture', 'dgesture', 'drop', 'padding')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def common(self):
        return CommonEvent(self.cdata.common) if self.cdata.common else None

    @common.setter
    def common(self, value):
        try:
            self.cdata.common = value.cdata
        except:
            self.cdata.common = ffi.new('SDL_CommonEvent *', value)

    @property
    def window(self):
        return WindowEvent(self.cdata.window) if self.cdata.window else None

    @window.setter
    def window(self, value):
        try:
            self.cdata.window = value.cdata
        except:
            self.cdata.window = ffi.new('SDL_WindowEvent *', value)

    @property
    def key(self):
        return KeyboardEvent(self.cdata.key) if self.cdata.key else None

    @key.setter
    def key(self, value):
        try:
            self.cdata.key = value.cdata
        except:
            self.cdata.key = ffi.new('SDL_KeyboardEvent *', value)

    @property
    def edit(self):
        return TextEditingEvent(self.cdata.edit) if self.cdata.edit else None

    @edit.setter
    def edit(self, value):
        try:
            self.cdata.edit = value.cdata
        except:
            self.cdata.edit = ffi.new('SDL_TextEditingEvent *', value)

    @property
    def text(self):
        return TextInputEvent(self.cdata.text) if self.cdata.text else None

    @text.setter
    def text(self, value):
        try:
            self.cdata.text = value.cdata
        except:
            self.cdata.text = ffi.new('SDL_TextInputEvent *', value)

    @property
    def motion(self):
        return MouseMotionEvent(self.cdata.motion
            ) if self.cdata.motion else None

    @motion.setter
    def motion(self, value):
        try:
            self.cdata.motion = value.cdata
        except:
            self.cdata.motion = ffi.new('SDL_MouseMotionEvent *', value)

    @property
    def button(self):
        return MouseButtonEvent(self.cdata.button
            ) if self.cdata.button else None

    @button.setter
    def button(self, value):
        try:
            self.cdata.button = value.cdata
        except:
            self.cdata.button = ffi.new('SDL_MouseButtonEvent *', value)

    @property
    def wheel(self):
        return MouseWheelEvent(self.cdata.wheel) if self.cdata.wheel else None

    @wheel.setter
    def wheel(self, value):
        try:
            self.cdata.wheel = value.cdata
        except:
            self.cdata.wheel = ffi.new('SDL_MouseWheelEvent *', value)

    @property
    def jaxis(self):
        return JoyAxisEvent(self.cdata.jaxis) if self.cdata.jaxis else None

    @jaxis.setter
    def jaxis(self, value):
        try:
            self.cdata.jaxis = value.cdata
        except:
            self.cdata.jaxis = ffi.new('SDL_JoyAxisEvent *', value)

    @property
    def jball(self):
        return JoyBallEvent(self.cdata.jball) if self.cdata.jball else None

    @jball.setter
    def jball(self, value):
        try:
            self.cdata.jball = value.cdata
        except:
            self.cdata.jball = ffi.new('SDL_JoyBallEvent *', value)

    @property
    def jhat(self):
        return JoyHatEvent(self.cdata.jhat) if self.cdata.jhat else None

    @jhat.setter
    def jhat(self, value):
        try:
            self.cdata.jhat = value.cdata
        except:
            self.cdata.jhat = ffi.new('SDL_JoyHatEvent *', value)

    @property
    def jbutton(self):
        return JoyButtonEvent(self.cdata.jbutton
            ) if self.cdata.jbutton else None

    @jbutton.setter
    def jbutton(self, value):
        try:
            self.cdata.jbutton = value.cdata
        except:
            self.cdata.jbutton = ffi.new('SDL_JoyButtonEvent *', value)

    @property
    def jdevice(self):
        return JoyDeviceEvent(self.cdata.jdevice
            ) if self.cdata.jdevice else None

    @jdevice.setter
    def jdevice(self, value):
        try:
            self.cdata.jdevice = value.cdata
        except:
            self.cdata.jdevice = ffi.new('SDL_JoyDeviceEvent *', value)

    @property
    def caxis(self):
        return ControllerAxisEvent(self.cdata.caxis
            ) if self.cdata.caxis else None

    @caxis.setter
    def caxis(self, value):
        try:
            self.cdata.caxis = value.cdata
        except:
            self.cdata.caxis = ffi.new('SDL_ControllerAxisEvent *', value)

    @property
    def cbutton(self):
        return ControllerButtonEvent(self.cdata.cbutton
            ) if self.cdata.cbutton else None

    @cbutton.setter
    def cbutton(self, value):
        try:
            self.cdata.cbutton = value.cdata
        except:
            self.cdata.cbutton = ffi.new('SDL_ControllerButtonEvent *', value)

    @property
    def cdevice(self):
        return ControllerDeviceEvent(self.cdata.cdevice
            ) if self.cdata.cdevice else None

    @cdevice.setter
    def cdevice(self, value):
        try:
            self.cdata.cdevice = value.cdata
        except:
            self.cdata.cdevice = ffi.new('SDL_ControllerDeviceEvent *', value)

    @property
    def adevice(self):
        return AudioDeviceEvent(self.cdata.adevice
            ) if self.cdata.adevice else None

    @adevice.setter
    def adevice(self, value):
        try:
            self.cdata.adevice = value.cdata
        except:
            self.cdata.adevice = ffi.new('SDL_AudioDeviceEvent *', value)

    @property
    def quit(self):
        return QuitEvent(self.cdata.quit) if self.cdata.quit else None

    @quit.setter
    def quit(self, value):
        try:
            self.cdata.quit = value.cdata
        except:
            self.cdata.quit = ffi.new('SDL_QuitEvent *', value)

    @property
    def user(self):
        return UserEvent(self.cdata.user) if self.cdata.user else None

    @user.setter
    def user(self, value):
        try:
            self.cdata.user = value.cdata
        except:
            self.cdata.user = ffi.new('SDL_UserEvent *', value)

    @property
    def syswm(self):
        return SysWMEvent(self.cdata.syswm) if self.cdata.syswm else None

    @syswm.setter
    def syswm(self, value):
        try:
            self.cdata.syswm = value.cdata
        except:
            self.cdata.syswm = ffi.new('SDL_SysWMEvent *', value)

    @property
    def tfinger(self):
        return TouchFingerEvent(self.cdata.tfinger
            ) if self.cdata.tfinger else None

    @tfinger.setter
    def tfinger(self, value):
        try:
            self.cdata.tfinger = value.cdata
        except:
            self.cdata.tfinger = ffi.new('SDL_TouchFingerEvent *', value)

    @property
    def mgesture(self):
        return MultiGestureEvent(self.cdata.mgesture
            ) if self.cdata.mgesture else None

    @mgesture.setter
    def mgesture(self, value):
        try:
            self.cdata.mgesture = value.cdata
        except:
            self.cdata.mgesture = ffi.new('SDL_MultiGestureEvent *', value)

    @property
    def dgesture(self):
        return DollarGestureEvent(self.cdata.dgesture
            ) if self.cdata.dgesture else None

    @dgesture.setter
    def dgesture(self, value):
        try:
            self.cdata.dgesture = value.cdata
        except:
            self.cdata.dgesture = ffi.new('SDL_DollarGestureEvent *', value)

    @property
    def drop(self):
        return DropEvent(self.cdata.drop) if self.cdata.drop else None

    @drop.setter
    def drop(self, value):
        try:
            self.cdata.drop = value.cdata
        except:
            self.cdata.drop = ffi.new('SDL_DropEvent *', value)

    @property
    def padding(self):
        return self.cdata.padding

    @padding.setter
    def padding(self, value):
        self.cdata.padding = value
    peepEvents = peepEvents
    pollEvent = pollEvent
    pushEvent = pushEvent
    waitEvent = waitEvent
    waitEventTimeout = waitEventTimeout

class GameController(Struct):
    """Wrap `SDL_GameController`"""
    __ctype__ = 'SDL_GameController'
    _fields = ()
    gameControllerClose = gameControllerClose
    gameControllerGetAttached = gameControllerGetAttached
    gameControllerGetAxis = gameControllerGetAxis
    gameControllerGetBindForAxis = gameControllerGetBindForAxis
    gameControllerGetBindForButton = gameControllerGetBindForButton
    gameControllerGetButton = gameControllerGetButton
    gameControllerGetJoystick = gameControllerGetJoystick
    gameControllerGetProduct = gameControllerGetProduct
    gameControllerGetProductVersion = gameControllerGetProductVersion
    gameControllerGetVendor = gameControllerGetVendor
    gameControllerMapping = gameControllerMapping
    gameControllerName = gameControllerName

class GameControllerButtonBind(Struct):
    """Wrap `SDL_GameControllerButtonBind`"""
    __ctype__ = 'SDL_GameControllerButtonBind'
    _fields = 'bindType', 'value'

    @property
    def bindType(self):
        return self.cdata.bindType

    @bindType.setter
    def bindType(self, value):
        self.cdata.bindType = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

class Haptic(Struct):
    """Wrap `SDL_Haptic`"""
    __ctype__ = 'SDL_Haptic'
    _fields = ()
    hapticClose = hapticClose
    hapticDestroyEffect = hapticDestroyEffect
    hapticEffectSupported = hapticEffectSupported
    hapticGetEffectStatus = hapticGetEffectStatus
    hapticIndex = hapticIndex
    hapticNewEffect = hapticNewEffect
    hapticNumAxes = hapticNumAxes
    hapticNumEffects = hapticNumEffects
    hapticNumEffectsPlaying = hapticNumEffectsPlaying
    hapticPause = hapticPause
    hapticQuery = hapticQuery
    hapticRumbleInit = hapticRumbleInit
    hapticRumblePlay = hapticRumblePlay
    hapticRumbleStop = hapticRumbleStop
    hapticRumbleSupported = hapticRumbleSupported
    hapticRunEffect = hapticRunEffect
    hapticSetAutocenter = hapticSetAutocenter
    hapticSetGain = hapticSetGain
    hapticStopAll = hapticStopAll
    hapticStopEffect = hapticStopEffect
    hapticUnpause = hapticUnpause
    hapticUpdateEffect = hapticUpdateEffect

class HapticCondition(Struct):
    """Wrap `SDL_HapticCondition`"""
    __ctype__ = 'SDL_HapticCondition'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'right_sat', 'left_sat', 'right_coeff', 'left_coeff', 'deadband',
        'center')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def right_sat(self):
        return self.cdata.right_sat

    @right_sat.setter
    def right_sat(self, value):
        self.cdata.right_sat = value

    @property
    def left_sat(self):
        return self.cdata.left_sat

    @left_sat.setter
    def left_sat(self, value):
        self.cdata.left_sat = value

    @property
    def right_coeff(self):
        return self.cdata.right_coeff

    @right_coeff.setter
    def right_coeff(self, value):
        self.cdata.right_coeff = value

    @property
    def left_coeff(self):
        return self.cdata.left_coeff

    @left_coeff.setter
    def left_coeff(self, value):
        self.cdata.left_coeff = value

    @property
    def deadband(self):
        return self.cdata.deadband

    @deadband.setter
    def deadband(self, value):
        self.cdata.deadband = value

    @property
    def center(self):
        return self.cdata.center

    @center.setter
    def center(self, value):
        self.cdata.center = value

class HapticConstant(Struct):
    """Wrap `SDL_HapticConstant`"""
    __ctype__ = 'SDL_HapticConstant'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'level', 'attack_length', 'attack_level', 'fade_length', 'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def level(self):
        return self.cdata.level

    @level.setter
    def level(self, value):
        self.cdata.level = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class HapticCustom(Struct):
    """Wrap `SDL_HapticCustom`"""
    __ctype__ = 'SDL_HapticCustom'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'channels', 'period', 'samples', 'data', 'attack_length',
        'attack_level', 'fade_length', 'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def channels(self):
        return self.cdata.channels

    @channels.setter
    def channels(self, value):
        self.cdata.channels = value

    @property
    def period(self):
        return self.cdata.period

    @period.setter
    def period(self, value):
        self.cdata.period = value

    @property
    def samples(self):
        return self.cdata.samples

    @samples.setter
    def samples(self, value):
        self.cdata.samples = value

    @property
    def data(self):
        return self.cdata.data

    @data.setter
    def data(self, value):
        self.cdata.data = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class HapticDirection(Struct):
    """Wrap `SDL_HapticDirection`"""
    __ctype__ = 'SDL_HapticDirection'
    _fields = 'type', 'dir'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def dir(self):
        return self.cdata.dir

    @dir.setter
    def dir(self, value):
        self.cdata.dir = value

class HapticEffect(Struct):
    """Wrap `SDL_HapticEffect`"""
    __ctype__ = 'SDL_HapticEffect'
    _fields = ('type', 'constant', 'periodic', 'condition', 'ramp',
        'leftright', 'custom')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def constant(self):
        return HapticConstant(self.cdata.constant
            ) if self.cdata.constant else None

    @constant.setter
    def constant(self, value):
        try:
            self.cdata.constant = value.cdata
        except:
            self.cdata.constant = ffi.new('SDL_HapticConstant *', value)

    @property
    def periodic(self):
        return HapticPeriodic(self.cdata.periodic
            ) if self.cdata.periodic else None

    @periodic.setter
    def periodic(self, value):
        try:
            self.cdata.periodic = value.cdata
        except:
            self.cdata.periodic = ffi.new('SDL_HapticPeriodic *', value)

    @property
    def condition(self):
        return HapticCondition(self.cdata.condition
            ) if self.cdata.condition else None

    @condition.setter
    def condition(self, value):
        try:
            self.cdata.condition = value.cdata
        except:
            self.cdata.condition = ffi.new('SDL_HapticCondition *', value)

    @property
    def ramp(self):
        return HapticRamp(self.cdata.ramp) if self.cdata.ramp else None

    @ramp.setter
    def ramp(self, value):
        try:
            self.cdata.ramp = value.cdata
        except:
            self.cdata.ramp = ffi.new('SDL_HapticRamp *', value)

    @property
    def leftright(self):
        return HapticLeftRight(self.cdata.leftright
            ) if self.cdata.leftright else None

    @leftright.setter
    def leftright(self, value):
        try:
            self.cdata.leftright = value.cdata
        except:
            self.cdata.leftright = ffi.new('SDL_HapticLeftRight *', value)

    @property
    def custom(self):
        return HapticCustom(self.cdata.custom) if self.cdata.custom else None

    @custom.setter
    def custom(self, value):
        try:
            self.cdata.custom = value.cdata
        except:
            self.cdata.custom = ffi.new('SDL_HapticCustom *', value)

class HapticLeftRight(Struct):
    """Wrap `SDL_HapticLeftRight`"""
    __ctype__ = 'SDL_HapticLeftRight'
    _fields = 'type', 'length', 'large_magnitude', 'small_magnitude'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def large_magnitude(self):
        return self.cdata.large_magnitude

    @large_magnitude.setter
    def large_magnitude(self, value):
        self.cdata.large_magnitude = value

    @property
    def small_magnitude(self):
        return self.cdata.small_magnitude

    @small_magnitude.setter
    def small_magnitude(self, value):
        self.cdata.small_magnitude = value

class HapticPeriodic(Struct):
    """Wrap `SDL_HapticPeriodic`"""
    __ctype__ = 'SDL_HapticPeriodic'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'period', 'magnitude', 'offset', 'phase', 'attack_length',
        'attack_level', 'fade_length', 'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def period(self):
        return self.cdata.period

    @period.setter
    def period(self, value):
        self.cdata.period = value

    @property
    def magnitude(self):
        return self.cdata.magnitude

    @magnitude.setter
    def magnitude(self, value):
        self.cdata.magnitude = value

    @property
    def offset(self):
        return self.cdata.offset

    @offset.setter
    def offset(self, value):
        self.cdata.offset = value

    @property
    def phase(self):
        return self.cdata.phase

    @phase.setter
    def phase(self, value):
        self.cdata.phase = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class HapticRamp(Struct):
    """Wrap `SDL_HapticRamp`"""
    __ctype__ = 'SDL_HapticRamp'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'start', 'end', 'attack_length', 'attack_level', 'fade_length',
        'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def start(self):
        return self.cdata.start

    @start.setter
    def start(self, value):
        self.cdata.start = value

    @property
    def end(self):
        return self.cdata.end

    @end.setter
    def end(self, value):
        self.cdata.end = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class JoyAxisEvent(Struct):
    """Wrap `SDL_JoyAxisEvent`"""
    __ctype__ = 'SDL_JoyAxisEvent'
    _fields = ('type', 'timestamp', 'which', 'axis', 'padding1', 'padding2',
        'padding3', 'value', 'padding4')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def axis(self):
        return self.cdata.axis

    @axis.setter
    def axis(self, value):
        self.cdata.axis = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

    @property
    def padding4(self):
        return self.cdata.padding4

    @padding4.setter
    def padding4(self, value):
        self.cdata.padding4 = value

class JoyBallEvent(Struct):
    """Wrap `SDL_JoyBallEvent`"""
    __ctype__ = 'SDL_JoyBallEvent'
    _fields = ('type', 'timestamp', 'which', 'ball', 'padding1', 'padding2',
        'padding3', 'xrel', 'yrel')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def ball(self):
        return self.cdata.ball

    @ball.setter
    def ball(self, value):
        self.cdata.ball = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def xrel(self):
        return self.cdata.xrel

    @xrel.setter
    def xrel(self, value):
        self.cdata.xrel = value

    @property
    def yrel(self):
        return self.cdata.yrel

    @yrel.setter
    def yrel(self, value):
        self.cdata.yrel = value

class JoyButtonEvent(Struct):
    """Wrap `SDL_JoyButtonEvent`"""
    __ctype__ = 'SDL_JoyButtonEvent'
    _fields = ('type', 'timestamp', 'which', 'button', 'state', 'padding1',
        'padding2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

class JoyDeviceEvent(Struct):
    """Wrap `SDL_JoyDeviceEvent`"""
    __ctype__ = 'SDL_JoyDeviceEvent'
    _fields = 'type', 'timestamp', 'which'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

class JoyHatEvent(Struct):
    """Wrap `SDL_JoyHatEvent`"""
    __ctype__ = 'SDL_JoyHatEvent'
    _fields = ('type', 'timestamp', 'which', 'hat', 'value', 'padding1',
        'padding2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def hat(self):
        return self.cdata.hat

    @hat.setter
    def hat(self, value):
        self.cdata.hat = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

class Joystick(Struct):
    """Wrap `SDL_Joystick`"""
    __ctype__ = 'SDL_Joystick'
    _fields = ()
    hapticOpenFromJoystick = hapticOpenFromJoystick
    joystickClose = joystickClose
    joystickCurrentPowerLevel = joystickCurrentPowerLevel
    joystickGetAttached = joystickGetAttached
    joystickGetAxis = joystickGetAxis
    joystickGetAxisInitialState = joystickGetAxisInitialState
    joystickGetBall = joystickGetBall
    joystickGetButton = joystickGetButton
    joystickGetGUID = joystickGetGUID
    joystickGetHat = joystickGetHat
    joystickGetProduct = joystickGetProduct
    joystickGetProductVersion = joystickGetProductVersion
    joystickGetType = joystickGetType
    joystickGetVendor = joystickGetVendor
    joystickInstanceID = joystickInstanceID
    joystickIsHaptic = joystickIsHaptic
    joystickName = joystickName
    joystickNumAxes = joystickNumAxes
    joystickNumBalls = joystickNumBalls
    joystickNumButtons = joystickNumButtons
    joystickNumHats = joystickNumHats

class JoystickGUID(Struct):
    """Wrap `SDL_JoystickGUID`"""
    __ctype__ = 'SDL_JoystickGUID'
    _fields = 'data',

    @property
    def data(self):
        return self.cdata.data

    @data.setter
    def data(self, value):
        self.cdata.data = value

class KeyboardEvent(Struct):
    """Wrap `SDL_KeyboardEvent`"""
    __ctype__ = 'SDL_KeyboardEvent'
    _fields = ('type', 'timestamp', 'windowID', 'state', 'repeat',
        'padding2', 'padding3', 'keysym')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def repeat(self):
        return self.cdata.repeat

    @repeat.setter
    def repeat(self, value):
        self.cdata.repeat = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def keysym(self):
        return Keysym(self.cdata.keysym) if self.cdata.keysym else None

    @keysym.setter
    def keysym(self, value):
        try:
            self.cdata.keysym = value.cdata
        except:
            self.cdata.keysym = ffi.new('SDL_Keysym *', value)

class Keysym(Struct):
    """Wrap `SDL_Keysym`"""
    __ctype__ = 'SDL_Keysym'
    _fields = 'scancode', 'sym', 'mod', 'unused'

    @property
    def scancode(self):
        return self.cdata.scancode

    @scancode.setter
    def scancode(self, value):
        self.cdata.scancode = value

    @property
    def sym(self):
        return self.cdata.sym

    @sym.setter
    def sym(self, value):
        self.cdata.sym = value

    @property
    def mod(self):
        return self.cdata.mod

    @mod.setter
    def mod(self, value):
        self.cdata.mod = value

    @property
    def unused(self):
        return self.cdata.unused

    @unused.setter
    def unused(self, value):
        self.cdata.unused = value

class MouseButtonEvent(Struct):
    """Wrap `SDL_MouseButtonEvent`"""
    __ctype__ = 'SDL_MouseButtonEvent'
    _fields = ('type', 'timestamp', 'windowID', 'which', 'button', 'state',
        'clicks', 'padding1', 'x', 'y')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def clicks(self):
        return self.cdata.clicks

    @clicks.setter
    def clicks(self, value):
        self.cdata.clicks = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

class MouseMotionEvent(Struct):
    """Wrap `SDL_MouseMotionEvent`"""
    __ctype__ = 'SDL_MouseMotionEvent'
    _fields = ('type', 'timestamp', 'windowID', 'which', 'state', 'x', 'y',
        'xrel', 'yrel')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def xrel(self):
        return self.cdata.xrel

    @xrel.setter
    def xrel(self, value):
        self.cdata.xrel = value

    @property
    def yrel(self):
        return self.cdata.yrel

    @yrel.setter
    def yrel(self, value):
        self.cdata.yrel = value

class MouseWheelEvent(Struct):
    """Wrap `SDL_MouseWheelEvent`"""
    __ctype__ = 'SDL_MouseWheelEvent'
    _fields = 'type', 'timestamp', 'windowID', 'which', 'x', 'y', 'direction'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def direction(self):
        return self.cdata.direction

    @direction.setter
    def direction(self, value):
        self.cdata.direction = value

class MultiGestureEvent(Struct):
    """Wrap `SDL_MultiGestureEvent`"""
    __ctype__ = 'SDL_MultiGestureEvent'
    _fields = 'type',

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

class OSEvent(Struct):
    """Wrap `SDL_OSEvent`"""
    __ctype__ = 'SDL_OSEvent'
    _fields = 'type', 'timestamp'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

class QuitEvent(Struct):
    """Wrap `SDL_QuitEvent`"""
    __ctype__ = 'SDL_QuitEvent'
    _fields = 'type', 'timestamp'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

class SysWMEvent(Struct):
    """Wrap `SDL_SysWMEvent`"""
    __ctype__ = 'SDL_SysWMEvent'
    _fields = 'type', 'timestamp', 'msg'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def msg(self):
        return SysWMmsg(self.cdata.msg) if self.cdata.msg else None

    @msg.setter
    def msg(self, value):
        try:
            self.cdata.msg = value.cdata
        except:
            self.cdata.msg = ffi.new('SDL_SysWMmsg *', value)

class SysWMmsg(Struct):
    """Wrap `SDL_SysWMmsg`"""
    __ctype__ = 'SDL_SysWMmsg'
    _fields = ()

class TextEditingEvent(Struct):
    """Wrap `SDL_TextEditingEvent`"""
    __ctype__ = 'SDL_TextEditingEvent'
    _fields = 'type', 'timestamp', 'windowID', 'text', 'start', 'length'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def text(self):
        return self.cdata.text

    @text.setter
    def text(self, value):
        self.cdata.text = value

    @property
    def start(self):
        return self.cdata.start

    @start.setter
    def start(self, value):
        self.cdata.start = value

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

class TextInputEvent(Struct):
    """Wrap `SDL_TextInputEvent`"""
    __ctype__ = 'SDL_TextInputEvent'
    _fields = 'type', 'timestamp', 'windowID', 'text'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def text(self):
        return self.cdata.text

    @text.setter
    def text(self, value):
        self.cdata.text = value

class TouchFingerEvent(Struct):
    """Wrap `SDL_TouchFingerEvent`"""
    __ctype__ = 'SDL_TouchFingerEvent'
    _fields = 'type',

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

class UserEvent(Struct):
    """Wrap `SDL_UserEvent`"""
    __ctype__ = 'SDL_UserEvent'
    _fields = 'type', 'timestamp', 'windowID', 'code', 'data1', 'data2'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def code(self):
        return self.cdata.code

    @code.setter
    def code(self, value):
        self.cdata.code = value

    @property
    def data1(self):
        return self.cdata.data1

    @data1.setter
    def data1(self, value):
        self.cdata.data1 = value

    @property
    def data2(self):
        return self.cdata.data2

    @data2.setter
    def data2(self, value):
        self.cdata.data2 = value

class WindowEvent(Struct):
    """Wrap `SDL_WindowEvent`"""
    __ctype__ = 'SDL_WindowEvent'
    _fields = ('type', 'timestamp', 'windowID', 'event', 'padding1',
        'padding2', 'padding3', 'data1', 'data2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def event(self):
        return self.cdata.event

    @event.setter
    def event(self, value):
        self.cdata.event = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def data1(self):
        return self.cdata.data1

    @data1.setter
    def data1(self, value):
        self.cdata.data1 = value

    @property
    def data2(self):
        return self.cdata.data2

    @data2.setter
    def data2(self, value):
        self.cdata.data2 = value


