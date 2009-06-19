import sys
import re

types = {
 'void': 'None',
 'void*': 'ctypes.c_void_p',
 'ALvoid*': 'ctypes.c_void_p',
 'char': 'ctypes.c_char',
 'char*': 'ctypes.c_char_p',
 'char**': 'ctypes.POINTER(ctypes.c_char_p)',
 'int': 'ctypes.c_int',
 'int*': 'ctypes.POINTER(ctypes.c_int)',
 'unsignedint': 'ctypes.c_uint',
 'unsignedint*': 'ctypes.POINTER(ctypes.c_uint)',
 'float': 'ctypes.c_float',
 'float*': 'ctypes.POINTER(ctypes.c_float)',
 'double': 'ctypes.c_double',
 'double*': 'ctypes.POINTER(ctypes.c_double)',
}
st = sys.argv[2]
for line in open(sys.argv[1]):
    line = line.strip()
    line = re.match('(.*) (.*)\((.*)\)', line)
    ret, name, parms = line.groups()
    parms = [x.strip() for x in parms.split(',')]
    assert name.startswith(st)
    name2 = name[len(st):]
    #print ret, name2, parms
    parms = filter(None, parms)
    parms = [[x.strip() for x in re.match('(.*[ *])([a-zA-Z]+)', p).groups()] for p in parms]
    parms2 = [types[x[0].replace(' ', '')] for x in parms]
    ret = types[ret.replace(' ', '')]
    print """
%s = lib.%s
%s.argtypes = [%s]
%s.restype = %s
%s.errcheck = check_error""" % (name2, name, name2, ', '.join(parms2), name2, ret, name2)
