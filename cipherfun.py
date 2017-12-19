# METHODS TO IMPLEMENT CIPHERS
import string
import sys

try:
    import enchant
    d = enchant.Dict("en_US")
except:
    print("Unable to import enchant. Please try installing the library.")

# CONTAINS THE STRING abcdefghijklmnopqrstuvwxyz
ltrs = list(string.ascii_lowercase)

# MAIN FUNCTION
def apply_cipher(cipher_dna, sentence):

    # DNA IS OF THE FORM "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # CREATES A HASH TABLE FOR THE DNA CIPHER
    def make_dictionary(cipher_dna):
        if len(set(cipher_dna)) != 26 or len(cipher_dna) != 26:
            raise ValueError("Cipher DNA must be 26 letters.")
        return {cipher_dna[i] : ltrs[i] for i in range(len(ltrs))}

    # APPLIES DICTIONARY
    def apply_dictionary(cipher_dna, sentence):
        if len(sentence) == 0:
            raise ValueError("Sentence cannot be empty.")
        sentence = ''.join([i for i in sentence.lower() if i in ltrs or i == " "])
        items = make_dictionary(cipher_dna)
        return list(map(lambda x: ''.join(x), list(map(lambda x: list(map(lambda y: items[y], x)), sentence.split()))))

    # TAKES INPUT OF LIST OF WORDS, OUTPUTS A SENTENCE
    def make_sentence(ls):
        x = str(ls[0])
        for i in range(1, len(ls)): x += ' ' + str(ls[i])
        return x

    # RETURN STRING OF THE SENTENCE AFTER APPLYING THE CIPHER
    return make_sentence(apply_dictionary(cipher_dna, sentence))

# SHIFTS THE ORIGINAL DNA K CHARACTERS
def caesar_cipher(k):
    lsc = [i for i in ltrs]
    for i in range(k):
        lscc = list(map(lambda x: lsc[x], [i for i in range(1, 26)]))
        lscc.append(lsc[0])
        lsc = lscc
    return "".join(lsc)

if 'enchant' in sys.modules:
    def check_cipher(cipher_dna, sentence):
        return len(list(filter(lambda z: d.check(z), apply_cipher(cipher_dna, sentence).split())))
    def unencrypt(sentence):
        x = [(caesar_cipher(k), check_cipher(caesar_cipher(k), sentence)) for k in range(26)]
        return apply_cipher(max(x, key=lambda y: y[1])[0], sentence)

if 'enchant' not in sys.modules:
    def unencrypt(sentence):
        x = ""
        for i in range(26):
            x += "cypher value: " + str(i) + "\n"
            x += str(apply_cipher(caesar_cipher(i), sentence)) + "\n"
        return x

if __name__ == "__main__":
    sentence = "gzo'n epno ovfz v hjhzio oj vkkmzxdvoz njhzjiz wmjrndib /m/jncv rcj yjzni'o fijr rcvo kkz noviyn ajm."
    print(unencrypt(sentence))