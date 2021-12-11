import re

rawdata = '''
MetaChars (needs to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

(+505)3625-1368
(+504) 5046-9535
(+504)81049651
(+503)7625-1628
+503 7627-1785
(503) 2235 6813
503 6136-6831
2238-6183
7145 6196
73656541

pattern = re.compile(r'')
matches = pattern.finditer(rawdata)
for match in matches:
    print(match)
'''

def svphonenum():
    pattern = re.compile(r'(\(?\+?503\)?\s?)?[276]\d{3}[-\s]?\d{4}')
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)
    #> <re.Match object; span=(110, 125), match='(+503)7625-1628'>
    #> <re.Match object; span=(126, 140), match='+503 7627-1785'>
    #> <re.Match object; span=(141, 156), match='(503) 2235 6813'>
    #> <re.Match object; span=(157, 170), match='503 6136-6831'>
    #> <re.Match object; span=(171, 180), match='2238-6183'>
    #> <re.Match object; span=(181, 190), match='7145 6196'>
    #> <re.Match object; span=(191, 199), match='73656541'>

def main(*args):
    svphonenum()

if __name__ == '__main__':
    main()