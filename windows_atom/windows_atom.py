import ctypes
from ctypes import wintypes

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32

# Function declarations
kernel32.GlobalAddAtomW.argtypes = [wintypes.LPCWSTR]
kernel32.GlobalAddAtomW.restype = wintypes.ATOM

kernel32.GlobalAddAtomA.argtypes = [wintypes.LPCSTR]
kernel32.GlobalAddAtomA.restype = wintypes.ATOM

kernel32.GlobalAddAtomExA.argtypes = [wintypes.LPCSTR, wintypes.DWORD]
kernel32.GlobalAddAtomExA.restype = wintypes.ATOM

kernel32.GlobalAddAtomExW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD]
kernel32.GlobalAddAtomExW.restype = wintypes.ATOM

kernel32.GlobalFindAtomA.argtypes = [wintypes.LPCSTR]
kernel32.GlobalFindAtomA.restype = wintypes.ATOM

kernel32.GlobalFindAtomW.argtypes = [wintypes.LPCWSTR]
kernel32.GlobalFindAtomW.restype = wintypes.ATOM

kernel32.GlobalGetAtomNameA.argtypes = [wintypes.ATOM, wintypes.LPSTR, wintypes.INT]
kernel32.GlobalGetAtomNameA.restype = wintypes.UINT

kernel32.GlobalGetAtomNameW.argtypes = [wintypes.ATOM, wintypes.LPWSTR, wintypes.INT]
kernel32.GlobalGetAtomNameW.restype = wintypes.UINT

kernel32.GlobalDeleteAtom.argtypes = [wintypes.ATOM]
kernel32.GlobalDeleteAtom.restype = wintypes.ATOM


# Adds input to the atom table globally
def add_atom(atomName):
    if isinstance(atomName, str):
        atom = kernel32.GlobalAddAtomW(atomName)
    elif isinstance(atomName, bytes):
        atom = kernel32.GlobalAddAtomA(atomName)
    else:
        raise TypeError("atomName must be a str (Unicode) or bytes (ANSI)")
    
    if atom == 0:
        raise ctypes.WinError()
    return atom

# Adds input to the atom table either globally or locally if the flag is 1
def add_atomEx(atomName, flags=0):
    if isinstance(atomName, str):
        atom = kernel32.GlobalAddAtomExW(atomName, flags)
    elif isinstance(atomName, bytes):
        atom = kernel32.GlobalAddAtomExA(atomName, flags)
    else:
        raise TypeError("atomName must be a str (Unicode) or bytes (ANSI)")
    
    if atom == 0:
        raise ctypes.WinError()
    return atom

# Searchs for input from the atom table
def find_atom(atomName):
    if isinstance(atomName, str):
        atom = kernel32.GlobalFindAtomW(atomName)
    elif isinstance(atomName, bytes):
        atom = kernel32.GlobalFindAtomA(atomName)
    else:
        raise TypeError("atomName must be a str (Unicode) or bytes (ANSI)")
    
    if atom == 0:
        return None  # Not found
    return atom

# Gets the atom number by name
def get_atom_name(atom, isWide=True):
    if isWide:
        buffer = ctypes.create_unicode_buffer(256)
        length = kernel32.GlobalGetAtomNameW(atom, buffer, 256)
    else:
        buffer = ctypes.create_string_buffer(256)
        length = kernel32.GlobalGetAtomNameA(atom, buffer, 256)
    
    if length == 0:
        raise ctypes.WinError()
    
    return buffer.value if isWide else buffer.value.decode('ascii')

# Deletes an atom
def delete_atom(atom):
    result = kernel32.GlobalDeleteAtom(atom)
    if result != 0:
        raise ctypes.WinError()

