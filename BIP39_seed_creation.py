import binascii
import hashlib
import unicodedata
from Entropy_mnemonic_generation_rev_2_class import MnemonicGenerator



generate = MnemonicGenerator()
mnemonic = generate.main()
print(mnemonic)

normalized_mnemonic = unicodedata.normalize("NFKD", mnemonic)
password = "kkk121324"
normalized_passphrase = unicodedata.normalize("NFKD", password)

passphrase = "mnemonic" + normalized_passphrase
mnemonic = normalized_mnemonic.encode("utf-8")
passphrase = passphrase.encode("utf-8")

bin_seed = hashlib.pbkdf2_hmac("sha512", mnemonic, passphrase, 2048)
print(bin_seed, binascii.hexlify(bin_seed[:64]))