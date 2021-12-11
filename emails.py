import re

rawdata = '''
normal pattern string
NORMAL
1234567890

MetaChars (needs to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

adl.erick@robinhood.edu
supermail@ufg.edu.sv
ia.stud@ufg.edu.sv
mailop@outlook.com
name.mail@gmail.com
name.opmail@gmail.com.ar
mable.oconnell@hotmail.com
kylie62@yahoo.com
adriel_hammes@gmail.com.sv
dashawn42@hotmail.com
trevion.homenick46@hotmail.com
cody97@hotmail.com
kaela_schumm1@hotmail.es
ethyl.wiza5@gmail.com
carter_purdy9@hotmail.es
karelle_orn@yahoo.com
caterina.feil@gmail.es
terrence68@gmail.com
maxie_kub94@yahoo.com.sv
jaunita76@yahoo.com
katelynn.murazik@gmail.com
wyman_dooley@yahoo.com.ru
percy20@yahoo.com
gregory.bergnaum65@gmail.com
emilie.hand@yahoo.com
sigurd55@hotmail.ar

pattern = re.compile(r'')
matches = pattern.finditer(rawdata)
for match in matches:
    print(match)
'''

def hostrecog(host):
    #> hostrecog('gmail')
    pattern = re.compile(r'.+@'+host+r'\..+')
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)

def edurecog():
    pattern = re.compile(r'.+@.+\.edu(\..+)?')
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match)  

def main(*args):
    hostrecog('gmail')

if __name__ == '__main__':
    main()