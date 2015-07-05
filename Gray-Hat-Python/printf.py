from ctypes import *
libc = CDLL("/lib/i386-linux-gnu/libc.so.6")

message = "Hello Python!"
libc.printf("Message : %s\n",message)