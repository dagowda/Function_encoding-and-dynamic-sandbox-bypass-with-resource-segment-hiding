# The commands to compile 

```bash
x86_64-w64-mingw32-windres resources.rc -O coff -o resources.res
x86_64-w64-mingw32-g++ --static -o pay.exe encode_dynamic.cpp resources.res -fpermissive -lws2_32
```
