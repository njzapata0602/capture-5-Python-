#Nick Zapata - ch 5 - ex 5 - 2/15/18

string = "x-DSPAM-Confidence: 0.8475"
start_index = string.find(':')
num = string[start_index+1:].strip()
print (float(num))