import re
"""
    '\tnormal string'
    >   normal string
    r'\traw string'
    >\nraw string (prints backslashes)
    
    raws strings for regular expression to be interpreted
"""
rawdata = '''
normal pattern string
NORMAL
1234567890

MetaChars (needs to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

Dr. Algo
Mr. Steve

sitiowebpro.com

32 ovejas

Ja Jaja Jajaja jaJa

316-595-6164
615.765.4934
616?651?6187
616 651 6187

pattern = re.compile(r'')
matches = pattern.finditer(rawdata)
for match in matches:
    print(match)
'''

sentence = 'Principio de una oracion con un fin'

def simplematch():
    pattern = re.compile(r'nor')
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(1, 4), match='nor'> span = beginning and end index of the match
    print(rawdata[1:4])
    #>nor

def scapedmatches():
    pattern = re.compile(r'.') #(matches every character but new lines)
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(1, 2), match='n'>
    #><re.Match object; span=(2, 3), match='o'>
    #><re.Match object; span=(3, 4), match='r'>
    #><re.Match object; span=(4, 5), match='m'>
    #><re.Match object; span=(5, 6), match='a'>
    #... (every chararcter)
    print('----')
    pattern = re.compile(r'\.') #backslash for scaped period
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #<re.Match object; span=(63, 64), match='.'>
    #<re.Match object; span=(94, 95), match='.'>
    #<re.Match object; span=(103, 104), match='.'>
    #... (only periods)

def simplescapedurlmatch():
    pattern = re.compile(r'sitiowebpro\.com') #period needs to be scaped
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(112, 127), match='sitiowebpro.com'>

def metacharmatch():
    pattern = re.compile(r'\d') #only digits
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(30, 31), match='1'>
    #><re.Match object; span=(31, 32), match='2'>
    #><re.Match object; span=(32, 33), match='3'>
    #...
    print('----')
    pattern = re.compile(r'\D') #anything but digits (even newline chars and spaces)
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(30, 31), match='1'>
    #><re.Match object; span=(31, 32), match='2'>
    #><re.Match object; span=(32, 33), match='3'>
    #...
    print('----')
    pattern = re.compile(r'\W') #not word characters
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #<re.Match object; span=(0, 1), match='\n'>
    #<re.Match object; span=(7, 8), match=' '>
    #<re.Match object; span=(15, 16), match=' '>
    #<re.Match object; span=(22, 23), match='\n'>
    #...

def banchor():
    pattern = re.compile(r'\bJa') #word boundary
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(151, 153), match='Ja'>
    #><re.Match object; span=(154, 156), match='Ja'>
    #><re.Match object; span=(159, 161), match='Ja'>

def startendanchor():
    pattern = re.compile(r'^Principio') # beginning of the sentence
    matches = pattern.finditer(sentence)
    for match in matches:
        print(match)
    #><re.Match object; span=(0, 9), match='Principio'>
    pattern = re.compile(r'fin$') # end of the sentence
    matches = pattern.finditer(sentence)
    for match in matches:
        print(match)
    #><re.Match object; span=(32, 35), match='fin'>

def simplephonenummatch():
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # period for every character
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(172, 184), match='316-595-6164'>
    #><re.Match object; span=(185, 197), match='615.765.4934'>
    #><re.Match object; span=(198, 210), match='616?651?6187'>
    #><re.Match object; span=(211, 223), match='616 651 6187'>
    print('----')
    pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # [] character set only matching dash and period
    # characters in character sets doesnt have to be scaped
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #><re.Match object; span=(172, 184), match='316-595-6164'>
    #><re.Match object; span=(185, 197), match='615.765.4934'>


def main(*args):
    simplephonenummatch()

if __name__ == '__main__':
    main()