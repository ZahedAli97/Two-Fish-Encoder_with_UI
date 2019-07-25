from twofish import Twofish
import binascii
import math
import pandas


def main():
    inputmessage = raw_input()
    inputs = []
    for i in range(0, len(inputmessage), 16):
        tempinput = inputmessage[i:i+16]
        inputs.append(tempinput)
    # print(inputs)
    for i in range(len(inputs)):
        if (len(inputs[i]) < 16):
            addinginput = inputs[i]
            while(len(addinginput) < 16):
                addinginput = addinginput + ' '
            inputs[i] = addinginput

    print(inputs)

    len_of_input = len(inputmessage)
    print('Lentght of inputmessage is : ' + str(len_of_input))

    T = Twofish(b'*secret*')

    encryptedinput = []

    for i in range(len(inputs)):
        tempencrypted = T.encrypt(inputs[i])
        encryptedinput.append(tempencrypted)

    print(encryptedinput)

    decryptedinput = []

    for i in range(len(encryptedinput)):
        tempdecrypted = T.decrypt(encryptedinput[i])
        decryptedinput.append(tempdecrypted)

    print(decryptedinput)

    for i in range(len(decryptedinput)):
        countspace = decryptedinput[i].count(" ")
        if countspace > 3:
            decryptedinput[i] = str.rstrip(decryptedinput[i])

        # if i != 0 and decryptedinput[i][0] != ' ':
        #     decryptedinput[i] = decryptedinput[i].rjust(
        #         len(decryptedinput[i])+1)

    print(decryptedinput)


if __name__ == '__main__':
    main()


# space = ' '
# print(len(space))
# count = 0
# if(len(inputmessage) < 16):
#     while(len(inputmessage) < 16):
#         inputmessage = inputmessage + ' '
#         count = count + 1
# elif(len(inputmessage) > 16):
#     divs = float(len(inputmessage))/16
#     # print(divs)
#     no_of_divs = math.ceil(divs)
#     no_of_divs = int(no_of_divs)
#     # print(no_of_divs)
#     i = 0
#     count = 0
#     while(i < no_of_divs):
#         tempinputs = ''
#         startingpoint = count * 16
#         for c in inputmessage:
#             cc = 0
#             if(cc == startingpoint):
#                 tempinputs += c
#                 if(len(tempinputs) == 16):
#                     break
#             cc += 1
#         print(len(tempinputs))
#         print(tempinputs)
#         i += 1
#         count += 1

# print(count)
# print(inputmessage)
# print(len(inputmessage))
# bininput = bin(int(binascii.hexlify(inputmessage), 16))
# print(bininput)

# print(b'YELLOWSUBMARINES')

# T = Twofish(b'*secret*')
# # meets zahed at the center of all things.')
# x = T.encrypt(b'YELLOWSUBMARINES')
# y = T.encrypt(b'BlueeeSUBMARINES')
# z = T.encrypt(inputmessage)
# # inputencrypt = T.encrypt(b(inputmessage))
# # print(len(y))
# # print(T.decrypt(x))  # .decode())
# print(x)
# print(y)
# print(T.decrypt(x))
# print(T.decrypt(y))
# print(T.decrypt(z))
# z = x+y
# print(z)
# zprint = T.decrypt(x) + T.decrypt(y)
# print(zprint)

#myciphertext = open('myciphertext.txt', 'w')
# myciphertext.write(x)
# myciphertext.close()
