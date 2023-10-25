class Encriptation :

    def __init__(self):
        self.pass3 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 "
        self.pass4 = " 0987654321zyxwvutsrqpoñnmlkjihgfedcbaZYXWVUTSRQPOÑNMLKJIHGFEDCBA"
        self.v3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
        self.v4 = [" ", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1", "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "ñ", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", "Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "Ñ", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]

    def encript(self, password):
        encript = ""

        for i in range(len(password)):
            if self.pass3.find(password[i]) == False:
                encript = encript + password[i]
            else:
                for j in range(len(self.v3)):
                    if self.v3[j] == password[i]:
                        encript = encript + self.v4[j]
                        break

        return encript


    def decrypt(self, password):
        encript = ""

        for i in range(len(password)):
            if self.pass4.find(password[i]) == False:
                encript = encript + password[i]
            else:
                for j in range(len(self.v4)):
                    if self.v4[j] == password[i]:
                        encript = encript + self.v3[j]
                        break
        return encript