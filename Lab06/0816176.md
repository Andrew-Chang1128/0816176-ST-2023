# 2023 NYCU Software Testing - Lab6
0816176 張辰宇

# Environment
gcc version 11.3.0 (Ubuntu 11.3.0-1ubuntu1~22.04) 

---

### Heap out-of-bounds read/write
##### source code
```
#include <stdio.h>
#include <stdlib.h>

int main() {
    int len = 5;
    int *arr = (int *)malloc(len * sizeof(int));
    

    arr[10] = 10;

    free(arr);
    return 0;
}
```
#### ASan report

```
gcc -fsanitize=address -g -o1 heapOutOfBound.cpp -o t1
./t1

=================================================================
==3108==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x603000000068 at pc 0x555e78b19230 bp 0x7ffcf25de9e0 sp 0x7ffcf25de9d0
WRITE of size 4 at 0x603000000068 thread T0
    #0 0x555e78b1922f in main /lab5/lab6/heapOutOfBound.cpp:9
    #1 0x7f5613280d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f5613280e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x555e78b19104 in _start (/lab5/lab6/t1+0x1104)

0x603000000068 is located 20 bytes to the right of 20-byte region [0x603000000040,0x603000000054)
allocated by thread T0 here:
    #0 0x7f5613533867 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x555e78b191ec in main /lab5/lab6/heapOutOfBound.cpp:6
    #2 0x7f5613280d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-buffer-overflow /lab5/lab6/heapOutOfBound.cpp:9 in main
Shadow bytes around the buggy address:
  0x0c067fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c067fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c067fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c067fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c067fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c067fff8000: fa fa 00 00 00 fa fa fa 00 00 04 fa fa[fa]fa fa
  0x0c067fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c067fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==3108==ABORTING
```
##### valgrind report
```
gcc -o t2 heapOutOfBound.cpp 
valgrind ./t2

==3117== Memcheck, a memory error detector
==3117== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==3117== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==3117== Command: ./t2
==3117== 
==3117== Invalid write of size 4
==3117==    at 0x109199: main (in /lab5/lab6/t2)
==3117==  Address 0x4a8a068 is 20 bytes after a block of size 20 alloc'd
==3117==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==3117==    by 0x10918C: main (in /lab5/lab6/t2)
==3117== 
==3117== 
==3117== HEAP SUMMARY:
==3117==     in use at exit: 0 bytes in 0 blocks
==3117==   total heap usage: 1 allocs, 1 frees, 20 bytes allocated
==3117== 
==3117== All heap blocks were freed -- no leaks are possible
==3117== 
==3117== For lists of detected and suppressed errors, rerun with: -s
==3117== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

ASan 能 , valgrind 能

---
### Stack out-of-bounds read/write
##### source code
```
#include <stdio.h>

int main() {
    int arr[15];

    arr[20] = 20;

    return 0;
}
```
#### ASan report
```
=================================================================
==3128==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fffd7d3cfe0 at pc 0x55e290c32291 bp 0x7fffd7d3cf60 sp 0x7fffd7d3cf50
WRITE of size 4 at 0x7fffd7d3cfe0 thread T0
    #0 0x55e290c32290 in main /lab5/lab6/stackOutOfBound.cpp:6
    #1 0x7f9d52ca1d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f9d52ca1e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x55e290c32104 in _start (/lab5/lab6/t1+0x1104)

Address 0x7fffd7d3cfe0 is located in stack of thread T0 at offset 112 in frame
    #0 0x55e290c321d8 in main /lab5/lab6/stackOutOfBound.cpp:3

  This frame has 1 object(s):
    [32, 92) 'arr' (line 4) <== Memory access at offset 112 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /lab5/lab6/stackOutOfBound.cpp:6 in main
Shadow bytes around the buggy address:
  0x10007af9f9a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9f9b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9f9c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9f9d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9f9e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1
=>0x10007af9f9f0: f1 f1 00 00 00 00 00 00 00 04 f3 f3[f3]f3 00 00
  0x10007af9fa00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9fa10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9fa20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9fa30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10007af9fa40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==3128==ABORTING
```
#### valgrind report
```
==3137== Memcheck, a memory error detector
==3137== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==3137== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==3137== Command: ./t2
==3137== 
==3137== 
==3137== HEAP SUMMARY:
==3137==     in use at exit: 0 bytes in 0 blocks
==3137==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
==3137== 
==3137== All heap blocks were freed -- no leaks are possible
==3137== 
==3137== For lists of detected and suppressed errors, rerun with: -s
==3137== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```
ASan 能 , valgrind 不能

---
### Global out-of-bounds read/write
##### source code
```
#include <stdio.h>

int arr[10];

int main() {
    arr[20] = 20;

    return 0;
}
```
#### ASan report
```
==3153==ERROR: AddressSanitizer: global-buffer-overflow on address 0x56232f2150f0 at pc 0x56232f212203 bp 0x7ffc88026d10 sp 0x7ffc88026d00
WRITE of size 4 at 0x56232f2150f0 thread T0
    #0 0x56232f212202 in main /lab5/lab6/globalOutOfBound.cpp:6
    #1 0x7f5ec5e83d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f5ec5e83e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x56232f212104 in _start (/lab5/lab6/t1+0x1104)

0x56232f2150f0 is located 40 bytes to the right of global variable 'arr' defined in 'globalOutOfBound.cpp:3:5' (0x56232f2150a0) of size 40
SUMMARY: AddressSanitizer: global-buffer-overflow /lab5/lab6/globalOutOfBound.cpp:6 in main
Shadow bytes around the buggy address:
  0x0ac4e5e3a9c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3a9d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3a9e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3a9f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3aa00: 00 00 00 00 00 00 00 00 f9 f9 f9 f9 f9 f9 f9 f9
=>0x0ac4e5e3aa10: 00 00 00 00 00 00 00 00 00 f9 f9 f9 f9 f9[f9]f9
  0x0ac4e5e3aa20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3aa30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3aa40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3aa50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ac4e5e3aa60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==3153==ABORTING
```
#### valgrind report
```
==3161== Memcheck, a memory error detector
==3161== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==3161== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==3161== Command: ./t2
==3161== 
==3161== 
==3161== HEAP SUMMARY:
==3161==     in use at exit: 0 bytes in 0 blocks
==3161==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
==3161== 
==3161== All heap blocks were freed -- no leaks are possible
==3161== 
==3161== For lists of detected and suppressed errors, rerun with: -s
==3161== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```
ASan 能 , valgrind 不能

--- 
### Use-after-free
##### source code
```
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int *)malloc(10 * sizeof(int));
    
    free(arr);
    arr[2] = 3;
    return 0;
}
```
#### ASan report
```
=================================================================
==3170==ERROR: AddressSanitizer: heap-use-after-free on address 0x604000000018 at pc 0x560ad513c22e bp 0x7ffe9568c600 sp 0x7ffe9568c5f0
WRITE of size 4 at 0x604000000018 thread T0
    #0 0x560ad513c22d in main /lab5/lab6/useAfterFree.cpp:8
    #1 0x7f31c1f58d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f31c1f58e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x560ad513c104 in _start (/lab5/lab6/t1+0x1104)

0x604000000018 is located 8 bytes inside of 40-byte region [0x604000000010,0x604000000038)
freed by thread T0 here:
    #0 0x7f31c220b517 in __interceptor_free ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:127
    #1 0x560ad513c1ee in main /lab5/lab6/useAfterFree.cpp:7
    #2 0x7f31c1f58d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

previously allocated by thread T0 here:
    #0 0x7f31c220b867 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x560ad513c1de in main /lab5/lab6/useAfterFree.cpp:5
    #2 0x7f31c1f58d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-use-after-free /lab5/lab6/useAfterFree.cpp:8 in main
Shadow bytes around the buggy address:
  0x0c087fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c087fff8000: fa fa fd[fd]fd fd fd fa fa fa fa fa fa fa fa fa
  0x0c087fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==3170==ABORTING
```
#### valgrind report
```
==3177== Memcheck, a memory error detector
==3177== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==3177== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==3177== Command: ./t2
==3177== 
==3177== Invalid write of size 4
==3177==    at 0x109197: main (in /lab5/lab6/t2)
==3177==  Address 0x4a8a048 is 8 bytes inside a block of size 40 free'd
==3177==    at 0x484B27F: free (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==3177==    by 0x10918E: main (in /lab5/lab6/t2)
==3177==  Block was alloc'd at
==3177==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==3177==    by 0x10917E: main (in /lab5/lab6/t2)
==3177== 
==3177== 
==3177== HEAP SUMMARY:
==3177==     in use at exit: 0 bytes in 0 blocks
==3177==   total heap usage: 1 allocs, 1 frees, 40 bytes allocated
==3177== 
==3177== All heap blocks were freed -- no leaks are possible
==3177== 
==3177== For lists of detected and suppressed errors, rerun with: -s
==3177== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```
ASan 能 , valgrind 能
--- 
### Use-after-return
##### source code
```
#include <stdio.h>
#include <stdlib.h>

int *x;

void foo() {
    int a[20];
    x = &a[3];
}

int main() {
    foo();
    *x = 13;
    return 0;
}
```
#### ASan report
```
gcc -fsanitize=address -g -o  t1 useAfterRetutn.cpp

ASAN_OPTIONS=detect_stack_use_after_return=1 ./t1 

==3190==ERROR: AddressSanitizer: stack-use-after-return on address 0x7f4a785c203c at pc 0x55cffd968372 bp 0x7ffcd8083240 sp 0x7ffcd8083230
WRITE of size 4 at 0x7f4a785c203c thread T0
    #0 0x55cffd968371 in main /lab5/lab6/useAfterRetutn.cpp:14
    #1 0x7f4a7bb61d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f4a7bb61e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x55cffd968144 in _start (/lab5/lab6/t1+0x1144)

Address 0x7f4a785c203c is located in stack of thread T0 at offset 60 in frame
    #0 0x55cffd968218 in foo() /lab5/lab6/useAfterRetutn.cpp:6

  This frame has 1 object(s):
    [48, 128) 'num' (line 7) <== Memory access at offset 60 is inside this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-use-after-return /lab5/lab6/useAfterRetutn.cpp:14 in main
Shadow bytes around the buggy address:
  0x0fe9cf0b03b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b03c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b03d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b03e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b03f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0fe9cf0b0400: f5 f5 f5 f5 f5 f5 f5[f5]f5 f5 f5 f5 f5 f5 f5 f5
  0x0fe9cf0b0410: f5 f5 f5 f5 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b0420: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b0430: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b0440: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0fe9cf0b0450: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==3190==ABORTING
```
#### valgrind report
```
==3199== Memcheck, a memory error detector
==3199== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==3199== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==3199== Command: ./t2
==3199== 
==3199== 
==3199== HEAP SUMMARY:
==3199==     in use at exit: 0 bytes in 0 blocks
==3199==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
==3199== 
==3199== All heap blocks were freed -- no leaks are possible
==3199== 
==3199== For lists of detected and suppressed errors, rerun with: -s
==3199== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```
ASan 能 , valgrind 不能

---

| Test                 | Valgrind | ASan |
| -------------------- | -------- | ---- |
| Heap out-of-bounds   | 能       | 能   |
| Stack out-of-bounds  | 不能     | 能   |
| Global out-of-bounds | 不能     | 能   |
| Use-after-free       | 能       | 能   |
| Use-after-return     | 不能     | 能   |


---

寫一個簡單程式 with ASan，Stack buffer overflow 剛好越過 redzone(並沒有對 redzone 做讀寫)，並說明 ASan 能否找的出來？

##### source code
```
#include <stdio.h>

int main(){
    int arr[8];
    arr[8+ 8] = 8;
    // arr[8+ 7] = 9;
    return 0; 
}
```
ASan
```
gcc -fsanitize=address -g -o  t1 redzone.cpp 
./t1
```
ASan 抓不到錯
因為只有在redzone內 (arr[0~7])抓得到(註解部分)，超過之後便抓不到。除非再進入下一段redzone才又會抓得到。
