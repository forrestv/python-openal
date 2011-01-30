import ctypes
import ctypes.util

lib = ctypes.CDLL(ctypes.util.find_library("openal"))

class device(ctypes.Structure):
    pass
device_p = ctypes.POINTER(device)

class context(ctypes.Structure):
    pass
context_p = ctypes.POINTER(context)

FALSE = 0
TRUE = 1
FREQUENCY = 0x1007
REFRESH = 0x1008
SYNC = 0x1009
MONO_SOURCES = 0x1010
STEREO_SOURCES = 0x1011
NO_ERROR = FALSE
INVALID_DEVICE = 0xA001
INVALID_CONTEXT = 0xA002
INVALID_ENUM = 0xA003
INVALID_VALUE = 0xA004
OUT_OF_MEMORY = 0xA005
DEFAULT_DEVICE_SPECIFIER = 0x1004
DEVICE_SPECIFIER = 0x1005
EXTENSIONS = 0x1006
MAJOR_VERSION = 0x1000
MINOR_VERSION = 0x1001
ATTRIBUTES_SIZE = 0x1002
ALL_ATTRIBUTES = 0x1003
CAPTURE_DEVICE_SPECIFIER = 0x310
CAPTURE_DEFAULT_DEVICE_SPECIFIER = 0x311
CAPTURE_SAMPLES = 0x312

errors = {}
for k, v in locals().items():
    if not isinstance(v, int) or not v: continue
    assert v not in errors
    errors[v] = k.replace('_', ' ').lower()

class Error(Exception):
    pass

def check_error(result, func, arguments):
    err = GetError(None)
    if err:
        raise Error(errors[err])
    return result

CreateContext = lib.alcCreateContext
CreateContext.argtypes = [device_p, ctypes.POINTER(ctypes.c_int)]
CreateContext.restype = context_p
CreateContext.errcheck = check_error

MakeContextCurrent = lib.alcMakeContextCurrent
MakeContextCurrent.argtypes = [context_p]
MakeContextCurrent.restype = ctypes.c_bool
MakeContextCurrent.errcheck = check_error

ProcessContext = lib.alcProcessContext
ProcessContext.argtypes = [context_p]
ProcessContext.restype = None
ProcessContext.errcheck = check_error

SuspendContext = lib.alcSuspendContext
SuspendContext.argtypes = [context_p]
SuspendContext.restype = None
SuspendContext.errcheck = check_error

DestroyContext = lib.alcDestroyContext
DestroyContext.argtypes = [context_p]
DestroyContext.restype = None
DestroyContext.errcheck = check_error

GetCurrentContext = lib.alcGetCurrentContext
GetCurrentContext.argtypes = []
GetCurrentContext.restype = context_p
GetCurrentContext.errcheck = check_error

GetContextsDevice = lib.alcGetContextsDevice
GetContextsDevice.argtypes = [context_p]
GetContextsDevice.restype = device_p
GetContextsDevice.errcheck = check_error

OpenDevice = lib.alcOpenDevice
OpenDevice.argtypes = [ctypes.c_char_p]
OpenDevice.restype = device_p
OpenDevice.errcheck = check_error

CloseDevice = lib.alcCloseDevice
CloseDevice.argtypes = [device_p]
CloseDevice.restype = ctypes.c_bool
CloseDevice.errcheck = check_error

GetError = lib.alcGetError
GetError.argtypes = [device_p]
GetError.restype = ctypes.c_int

IsExtensionPresent = lib.alcIsExtensionPresent
IsExtensionPresent.argtypes = [device_p, ctypes.c_char_p]
IsExtensionPresent.restype = ctypes.c_bool
IsExtensionPresent.errcheck = check_error

GetProcAddress = lib.alcGetProcAddress
GetProcAddress.argtypes = [device_p, ctypes.c_char_p]
GetProcAddress.restype = ctypes.c_void_p
GetProcAddress.errcheck = check_error

GetEnumValue = lib.alcGetEnumValue
GetEnumValue.argtypes = [device_p, ctypes.c_char_p]
GetEnumValue.restype = ctypes.c_int
GetEnumValue.errcheck = check_error

GetString = lib.alcGetString
GetString.argtypes = [device_p, ctypes.c_int]
GetString.restype = ctypes.c_char_p
GetString.errcheck = check_error

GetIntegerv = lib.alcGetIntegerv
GetIntegerv.argtypes = [device_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
GetIntegerv.restype = None
GetIntegerv.errcheck = check_error

CaptureOpenDevice = lib.alcCaptureOpenDevice
CaptureOpenDevice.argtypes = [ctypes.c_char_p, ctypes.c_uint, ctypes.c_int, ctypes.c_int]
CaptureOpenDevice.restype = device_p
CaptureOpenDevice.errcheck = check_error

CaptureCloseDevice = lib.alcCaptureCloseDevice
CaptureCloseDevice.argtypes = [device_p]
CaptureCloseDevice.restype = ctypes.c_bool
CaptureCloseDevice.errcheck = check_error

CaptureStart = lib.alcCaptureStart
CaptureStart.argtypes = [device_p]
CaptureStart.restype = None
CaptureStart.errcheck = check_error

CaptureStop = lib.alcCaptureStop
CaptureStop.argtypes = [device_p]
CaptureStop.restype = None
CaptureStop.errcheck = check_error

CaptureSamples = lib.alcCaptureSamples
CaptureSamples.argtypes = [device_p, ctypes.c_void_p, ctypes.c_int]
CaptureSamples.restype = None
CaptureSamples.errcheck = check_error
