# My WIndows 10 Rtty  45.45 170 Hz
# ...and it works
import pysine

mark = 1675
space = 1500
bit_time = 0.022  # 45.45 baud

textboxValue = '   ...   CQ CQ CQ CALLSIGN CALLSIGN CALLSIGN PSE K  ABCDEFGHIJKLMNOPQRSTUVWXYZ  0123456789 ...'

Rtty = { # lead START with a space, 0 STOP with two marks 11
    "A" : "01100011", # 11000
    "B" : "01001111", # 10011
    "C" : "00111011", # 01110
    "D" : "01001011", # 10010
    "E" : "01000011", # 10000
    "F" : "01011011", # 10110
    "G" : "00101111", # 01011
    "H" : "00010111", # 00101
    "I" : "00110011", # 01100
    "J" : "01101011", # 11010
    "K" : "01111011", # 11110
    "L" : "00100111", # 01001
    "M" : "00011111", # 00111
    "N" : "00011011", # 00110
    "O" : "00001111", # 00011
    "P" : "00110111", # 01101
    "Q" : "01110111", # 11101
    "R" : "00101011", # 01010
    "S" : "01010011", # 10100
    "T" : "00000111", # 00001
    "U" : "01110011", # 11100
    "V" : "00111111", # 01111
    "W" : "01100111", # 11001
    "X" : "01011111", # 10111
    "Y" : "01010111", # 10101
    "Z" : "01000111", # 10001
    " " : "00010011", # 00100 - OK
    "0" : "011011110011011101111111", # FIGURE 11011 P 01101 LETTERS 11111 - OK
    "1" : "011011110111011101111111", # FIGURE 11011 Q 11101 LETTERS 11111 - OK
    "2" : "011011110110011101111111", # FIGURE 11011 W 11001 LETTERS 11111 - OK
    "3" : "011011110100001101111111", # FIGURE 11011 E 10000 LETTERS 11111 - OK
    "4" : "011011110010101101111111", # FIGURE 11011 R 01010 LETTERS 11111 - OK
    "5" : "011011110000011101111111", # FIGURE 11011 T 00001 LETTERS 11111 - OK
    "6" : "011011110101011101111111", # FIGURE 11011 Y 10101 LETTERS 11111 - OK
    "7" : "011011110111001101111111", # FIGURE 11011 U 11100 LETTERS 11111 - OK
    "8" : "011011110011001101111111", # FIGURE 11011 I 01100 LETTERS 11111 - OK
    "9" : "011011110000111101111111", # FIGURE 11011 O 00011 LETTERS 11111 - OK
    "." : "011011110001111101111111", # FIGURE 11011 M 00111 LETTERS 11111 - OK
    "?" : "011011110100111101111111", # FIGURE 11011 B 10011 LETTERS 11111 - OK
    "!" : "011011110101101101111111", # FIGURE 11011 F 10110 LETTERS 11111 - OK
    "&" : "011011110010111101111111", # FIGURE 11011 G 01011 LETTERS 11111 - OK
    "#" : "011011110001011101111111", # FIGURE 11011 H 00101 LETTERS 11111 - OK
    "+" : "011011110100011101111111", # FIGURE 11011 Z 10001 LETTERS 11111 -- double quote ???
    "-" : "011011110110001101111111", # FIGURE 11011 A 11000 LETTERS 11111 - OK
    "/" : "011011110101111101111111", # FIGURE 11011 X 10111 LETTERS 11111 - OK
    "=" : "011011110011111101111111", # FIGURE 11011 V 01111 LETTERS 11111 -- semicoln
    ":" : "011011110011101101111111", # FIGURE 11011 C 01110 LETTERS 11111 - OK
    ";" : "011011110110111001111111", # FIGURE 11011 P 01101 LETTERS 11111 - OK
    "," : "011011110001101101111111", # FIGURE 11011 N 00110 LETTERS 11111 - OK
    "'" : "011011110101001101111111", # FIGURE 11011 S 10100 LETTERS 11111 - may be OK in GNU Radio
    "$" : "011011110100101101111111", # FIGURE 11011 D 10010 LETTERS 11111 - OK
    "(" : "011011110111101101111111", # FIGURE 11011 K 11110 LETTERS 11111 - OK
    ")" : "011011110010011101111111", # FIGURE 11011 L 01001 LETTERS 11111 - OK
    "\"" : "011011110100011101111111", # FIGURE 11011 Z 10001 LETTERS 11111 - OK
    "~" : "011011110110101101111111", # FIGURE 11011 J 11010 LETTERS 11111 -  BELL ???  Nothing
    }

class MyCode():      
    #def work(self, input_items, output_items):
    def MyWork():
        global Rtty
        global textboxValue
        bit_stream = ""
        output_items = ""
        if (len(textboxValue) > 0):
            for in0 in textboxValue:
                inChar = str (in0)
                ch = inChar.upper()
                if (not(ch in Rtty)):
                    ch = "?"
                _dots = str( Rtty.get(ch)) # 
                bit_stream += (_dots)
            _len = len(bit_stream)
            _num_elem = int((_len+1) / 2)
            textboxValue = ""
            rttyChar = list(bit_stream)
            for thing in rttyChar:
                if thing == '1':
                    pysine.sine(frequency=mark, duration=bit_time)
                else:
                    pysine.sine(frequency=space, duration=bit_time)
        else:
            _num_elem = 0
        return(_num_elem)

print(textboxValue)
MyCode.MyWork()


                
        




