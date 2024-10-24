# windows_atom

`windows_atom` is a Python library that provides an interface for interacting with the Windows atom table using a `ctypes` module wrapper. This library allows for adding, finding, retrieving, and deleting global or local atoms.

## Features

- Add atoms globally using `add_atom`
- Add atoms with local or global flags using `add_atomEx`
- Search for an atom with `find_atom`
- Retrieve the name of an atom with `get_atom_name`
- Delete an atom using `delete_atom`

## Installation
You can install through pypi with:

`pip install windows_atom`


You can install the package after downloading or cloning the repository:

- git clone https://github.com/Mohamed-Adil-Cyber/windows_atom.git
- cd windows_atom
- python setup.py install


If you dont want to build you can download the release from github then use this command:

`pip windows_atom-1.0-py3-none-any.whl`


## Usage

You can import the files with:

`from windows_atom import *`

Adding an Atom :

`add_atom("Hello world")` #Will return an atom id

Add an Atom with local or global Flags:

`global_atom = add_atomEx("example_global_atom")`  # Global atom
`local_atom = add_atomEx("example_local_atom", flags=1)`  # Local atom


Find an Atom using id:

`get_atom_name(atom)`

Find an Atom using name:

`find_atom("example_unicode_atom") `

Delete an Atom:

`delete_atom(atom)`
