# 271. Encode and Decode Strings

def encode( stringToEncode: list) -> str:
    encoded = ""
    
    for word in stringToEncode:
        wordLength = len(word)
        encoded += f"{wordLength}#{word}"
        
    print(encoded)
    return encoded
    
        
def decode(encoded: str) -> list:
    decoded = []
    i = 0
    
    while i < len(encoded):
        j = i
        
        while encoded[j] != '#':
            j += 1 
        
        length = int(encoded[i:j])
        word_start = j + 1
        word_end = word_start + length
        
        decoded.append(encoded[word_start:word_end])
        
        i = word_end
        
    return decoded
        
                 

stringToEncode = ["hello", ""]


encoded = encode(stringToEncode)

decode(encoded)