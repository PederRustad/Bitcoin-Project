
from hashlib import sha256


# English wordlist
class MnemonicGenerator:
    def __init__(self):
        self.wordlist_file = 'english.txt'
        with open(self.wordlist_file, 'r') as file:
            self.wl = [word.strip() for word in file.readlines()]

    def entropy_to_mnemonic24(self, entropy):
        # Apply BIP39 to convert entropy into seed words
        assert len(entropy) == 32
        # entropy converted into an integer, v
        v = int.from_bytes(entropy, 'big') << 8

        indexes = []
        for i in range(24):
            # devide integer by 2048 24 times. remainder will be index (m) of mnemonic word
            v, m = divmod(v, 2048)
            indexes.insert(0, m)
        assert not v

        # final 8 bits are a checksum

        indexes[-1] |= sha256(entropy).digest()[0]


        #print(len(indexes_byte), indexes_byte)
        return [self.wl[i] for i in indexes]


    def main(self):
        # Read input, remove whitespace around it
        r = input("insert dice rolls: ").strip()
        # Calc sha256
        h = sha256(r.encode()).digest()
        # Show the hash

        # Sanity check for empty input
        empty = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        if h.hex() == empty:
            print('WARNING: Input is empty. This is a known wallet\n')
        # Warnings for short length
        if len(r) < 99:
            ae = 2.585 * len(r)
            print('WARNING: Input is only %d bits of entropy\n' % ae)
        
        mnemonic = self.entropy_to_mnemonic24(h)
        mnemonic_string= " ".join(mnemonic)
        return mnemonic_string

        # Print index number and each word (24)
        #print('\n'.join('%4d: %s' % (n + 1, word) for n, word in enumerate(mnemonic)))

#generate = MnemonicGenerator()
#print(generate.main())