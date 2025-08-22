ENC = 0; DEC = 1

def makeDisk(aa, bb):
    enc_disk = {}; dec_disk = {}

    for i in range(26):
        enc_i = (aa*i+bb)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)
    return enc_disk, dec_disk

# 아핀 암호의 메인 함수
def affine(msg, key1, key2, mode):
    nmsg = ''
    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key1, key2)

    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            nmsg += disk[c]
        else:
            nmsg += c
    return nmsg

plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext = 'The WILL OF A MAN IS HIS HAPPINESS'
key1 = 7
key2 = 3

print('Original:\t%s' %plaintext.upper())
plaintext = affine(plaintext, key1, key2, ENC)
print('Affine Cipher:\t%s' %plaintext)

plaintext = affine(plaintext, key1, key2, DEC)
print('Deciphered:\t%s' %plaintext)
