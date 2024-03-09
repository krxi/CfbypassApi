

## Setup
We used our server for compilation and a VM for testing. We provide the binaries for easier testing.

### Compilation
System: Windows 10
Python: 11.0

```
#cfbypass.py
pip install playwright==1.27.0
py -m playwright install  firefox
pip install gevent

#main.py
pip install fastapi
pip install "uvicorn[standard]"

pip install annotated
pip install typing

#for cpp files
vcpkg install cpr
vcpkg install openssl

#Run
uvicorn main:app --reload
GET http://127.0.0.1:8000/kuymaks1:kuymaks1@206.41.168.204:6869&www.blackhatworld.com
works fine ++
```

