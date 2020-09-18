## First anaStruct usage notes

## Petiesmo local version Install:

Standard install was failing 
(matplotlib==3.0.3 required, but that version was not properly locating external libraries FreeType and Libpng)

Workaround Solution:
Installed matplotlib 3.1.3, 
Forked Repo & changed req & setup to allow higher than 3.0.3 - Released a development version, then installed using:
```
$ pip install --no-cache-dir -e git+https://github.com/petiesmo/anaStruct.git@v0.A-test#egg=mpl-test
```
