eadator
=======

EAD2002 (DTD or XSD) universal validator

EAD2002 has a DTD version and an XSD version which are not compatible.  Firstly, they are in
different namespaces.  The DTD version is in the default xml namespace, and the XSD 
version is in {urn:isbn:1-931666-22-9}.  There are other minor differences in namespaces
and camel case.

This utility performs a universial EAD2002 validation.  It exits 0/success with no output if the 
file is a valid EAD2002.  It exits 1/failure with relevent validation error messages if the file
is not valid with respect to its intended type (XSD or DTD).

[![Build Status](https://travis-ci.org/eadhost/eadator.png)](https://travis-ci.org/eadhost/eadator)


```
pip install https://github.com/eadhost/eadator/zipball/master
```
or
```
easy_install https://github.com/eadhost/eadator/zipball/master
```

Requires `libxml2` for `lxml` and validation.  


```
usage: eadator [-h] [--dtd DTD] [--xsd XSD] eadfile

EAD validator

positional arguments:
  eadfile     EAD XML file to check

optional arguments:
  -h, --help  show this help message and exit
  --dtd DTD
  --xsd XSD
```

Comes with default `ead.dtd` and `ead.xsd`, but you can point at
your own copies on the local filesystem or at URLs on the web.

License
-------
Copyright © 2013, Regents of the University of California
All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, 
  this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, 
  this list of conditions and the following disclaimer in the documentation 
  and/or other materials provided with the distribution.
- Neither the name of the University of California nor the names of its
  contributors may be used to endorse or promote products derived from this 
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.
