# myhash

Inspiration for my hash function came from the SHA1 hashing algorithm. The function uses blocks of a fixed size, a pre-determined initial block, it performs multiple rounds, and uses the output from the previous round with input for the next round.

The original message is split into chunks or blocks of 8 characters, which are then converted into their ASCII integer values. Regardless of how long the message is, padding is added to ensure the last block is of the same size as the rest. For padding, the * symbol is used, followed by numbers instead of more * symbols. This is because using just the * symbol as padding could produce collisions if the original message happens to end with one or more * symbols.

Simple values for the initial block are used because, due to the complexity of the hashing function, the values for the initial block have little bearing on the message digest. In other words, even if the initial block were all zeros, the hashing algorithm would still be just as secure. 

Within the hashing algorithm itself, the words are mixed and mashed but their length remains the same. An attempt has been made to maintain the influence of each value within a word, therefore none of these values are dropped or discarded, instead they are either moved or operated on. The counters that are used in various places throughout the loops always start at zero and are incremented each time a loop runs. The use of counters means that every loop is different. The values for the number of loops are chosen simply because 3, 5, 10, and 30 do not divide equally by 4, which is the number of words being used. Split and join, the multiplication operator, and using the sum are among the biggest contributors to the security of the hash function, along with the shift left of each word at the end of each loop.

The hashing function always produces the same size blocks, therefore, regardless of the input length, the output will always be a fixed length. Even with two similar inputs, the digests are vastly different. However, the exact same input will always return the same digests. From examining the digest alone, it is difficult to determine the input and thus the requirement for pre-image resistance is satisfied. Numerous tests were performed using symbols, word lists, and number enumration to find collisions but none have been found. 

Early in the design of this hash function, I determined that because the original message is split into blocks, a longer message would be easier to secure than a shorter message. Therefore, the focus for the design of this hash function was to provide security for inputs that are very short. Perhaps the biggest contributor to the security of the hash function is that the function is run twice on the first block. Without this, the likelihood of collisions increases. Security of the hash function could be improved by having a larger output or using a larger modulus. Adding more padding, introducing more constants within the hashing function, and performing more rounds would also improve the security of the hash function.


https://github.com/lambdy/myhash/assets/109147348/13b23531-0ab2-493c-b7d0-c73658fa8ddb

