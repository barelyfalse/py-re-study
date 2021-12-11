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
    #> <re.Match object; span=(186, 205), match='name.mail@gmail.com'>
    #> <re.Match object; span=(206, 230), match='name.opmail@gmail.com.ar'>
    #> <re.Match object; span=(276, 302), match='adriel_hammes@gmail.com.sv'>
    #> <re.Match object; span=(400, 421), match='ethyl.wiza5@gmail.com'>
    #> <re.Match object; span=(469, 491), match='caterina.feil@gmail.es'>
    #> <re.Match object; span=(492, 512), match='terrence68@gmail.com'>
    #> <re.Match object; span=(558, 584), match='katelynn.murazik@gmail.com'>
    #> <re.Match object; span=(629, 657), match='gregory.bergnaum65@gmail.com'>

def edurecog():
    pattern = re.compile(r'.+@.+\.edu(\..+)?')
    matches = pattern.finditer(rawdata)
    for match in matches:
        print(match) 
    #> <re.Match object; span=(103, 126), match='adl.erick@robinhood.edu'>
    #> <re.Match object; span=(127, 147), match='supermail@ufg.edu.sv'>
    #> <re.Match object; span=(148, 166), match='ia.stud@ufg.edu.sv'>

def main(*args):
    edurecog()

if __name__ == '__main__':
    main()