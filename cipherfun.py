# METHODS TO IMPLEMENT CIPHERS
import string

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
        sentence = sentence.lower()
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

if __name__ == "__main__":
    print(apply_cipher("zabcdefghijklmnopqrstuvwxy", "gdkkn sgdqd"))
    for i in range(26):
        print("cypher value: " + str(i))
        print(caesar_cipher(i))
        print(apply_cipher(caesar_cipher(i), "gdkkn sgdqd"))