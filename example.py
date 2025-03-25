
from base32.decode import decode
from base32.encode import encode


content = "hello, there!"

result_rfc3548 = encode(content, variant="RFC3548")
print(result_rfc3548)  # output: NBSWY3DPFQQHI2DFOJSSC===
print(decode(result_rfc3548, variant="RFC3548").decode("utf-8") == content)  # output: True

result_rfc4648 = encode(content, variant="RFC4648")
print(result_rfc4648)  # output: NBSWY3DPFQQHI2DFOJSSC===
print(decode(result_rfc4648, variant="RFC4648"))  # output: b'hello, there!'


result_rfc4648_HEX = encode(content, variant="RFC4648-HEX")
print(result_rfc4648_HEX)  # output: D1IMOR3F5GG78Q35E9II2===
print(decode(result_rfc4648_HEX, variant="RFC4648-HEX"))  # output: b'hello, there!'


result_crockford = encode(content, variant="Crockford")
print(result_crockford)  # output: D1JPRV3F5GG78T35E9JJ2
print(decode(result_crockford, variant="Crockford"))  # output: b'hello, there!'

