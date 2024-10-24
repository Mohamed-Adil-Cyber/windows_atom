import windows_atom

atomW = add_atom("TestAtomW")
print(f"Global Atom (W): {atomW}")
    
atomA = add_atom(b"TestAtomA")
print(f"Global Atom (A): {atomA}")
    
atomExW = add_atomEx("TestAtomExW", 0)
print(f"Global Atom Ex (W): {atomExW}")
    
atomExA = add_atomEx(b"TestAtomExA", 0)
print(f"Global Atom Ex (A): {atomExA}")
    
foundAtomW = find_atom("TestAtomW")
print(f"Found Atom (W): {foundAtomW}")
    
foundAtomA = find_atom(b"TestAtomA")
print(f"Found Atom (A): {foundAtomA}")
    
atomNameW = get_atom_name(atomW, isWide=True)
print(f"Atom Name (W): {atomNameW}")
    
atomNameA = get_atom_name(atomA, isWide=False)
print(f"Atom Name (A): {atomNameA}")
    
delete_atom(atomW)
print(f"Deleted Atom (W): {atomW}")
