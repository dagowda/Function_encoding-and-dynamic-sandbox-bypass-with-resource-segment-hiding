# The command to compile 

```bash
x86_64-w64-mingw32-g++ --static -o pay.exe full2.cpp resources.res -fpermissive -lws2_32
x86_64-w64-mingw32-windres resources.rc -O coff -o resources.res
```
