# Winiata Lambert

class hash():
    def run(self,message=None):
        return self.hash_structure(self.get_plaintext(message))

    # converts string of plaintext to blocks of 8 integers with padding for last block
    def get_plaintext(self, message=None):
        if message==None: message=input('Insert message to hash: ')
        message=str(message)
        full_plaintext=[]
        while len(message)>=8:
            full_plaintext.append([ord(item) for item in message[:8]])
            message=message[8:]
        message+='*'
        while len(message)<8:
            message+=str(8-len(message))
        full_plaintext.append([ord(item) for item in message])
        return full_plaintext

    # hashing function, round 1 for first block and init, round 2 for first block and digest, subsequent rounds for digest and remaining blocks
    def hash_structure(self, full_message):
        init=[1,2,3,4,5,6,7,8]
        first=full_message.pop(0)
        digest=self.hash_function(init, first)
        digest=self.hash_function(digest, first)
        while full_message:
            digest=self.hash_function(digest, full_message.pop(0))
        return ''.join([f'{num:0>4X}' for num in digest])

    def hash_function(self, block1, block2):
        word1,word2,word3,word4=block1[:4],block1[4:],block2[:4],block2[4:]
        for j in range(3):
            for i in range(5):
                word1=self.xor(word1,[107,59,181,13])
                word2[j]=sum(word2)%65535
                word3=[(num*(i+2))%65535 for num in word3]         
                word4=self.xor(word4,block1[j:(j+4)])
                word1,word2,word3,word4=word2,word3,word4,word1
            for i in range(5):
                word1.append(word1.pop(0))
                word1,word2=(word2[2:]+word1[:2]),(word2[:2]+word1[2:])
                word3.append(word3.pop(j))
                word4=self.xor(word4,word3)
                word1,word2,word3,word4=word2,word3,word4,word1
        newblock1,newblock2=word1+word3,word2+word4
        return self.xor(newblock1, newblock2)

    def xor(self, block1, block2):
        return [(block1[i]^block2[i]) for i in range(len(block1))]

print("Welcome to my hash function")
main=hash()
while True:
    value=input("Insert message to hash ('x' to quit): ")
    if value.lower() == 'x': break
    else: print(main.run(value))