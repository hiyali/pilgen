#
# Python convert: Salam Hiyali (hiyali920@gmail.com)
# Github: https:#github.com/hiyali
# 2020.2.21
#

# Author:  Muhammad Abdulla (muhammad@yulghun.com)
# Version: 1.2 (Feb. 7, 2009)
# License: GPL

import re

OQUOTE = 0x00AB; # for opening quote (oh quote)
CQUOTE = 0x00BB; # for closing quote

RCQUOTE = 0x2019; # 0x2019 is right closed curly quote
BPAD = 0x0600;

km = {} # new Array ( 128 ); // keymap
cm = {} # new Array ( 256 ); // charmap

PRIMe = 233; # 'e
PRIME = 201; # 'E
COLo  = 246; # :o
COLO  = 214; # :O
COLu  = 252; # :u
COLU  = 220; # :U
HAMZA = 0x0626;
CHEE  = 0x0686;
GHEE  = 0x063A;
NGEE  = 0x06AD;
SHEE  = 0x0634;
SZEE  = 0x0698;

def gas(code):
   return chr(code) # String.fromCharCode(code);

def gac(asc2):
   s = "" + asc2;
   return ord(s[0]) # s.charCodeAt(0);

inited = False;
def bedit_init():
    global inited
    if inited:
        return;

    inited = True;

    # zero-out all entries first
    for i in range(128): # km.length
            km[i] = 0;

    # Uyghur Unicode character map
    km[gac('a')] = 0x06BE;
    km[gac('b')] = 0x0628;
    km[gac('c')] = 0x063A;
    km[gac('D')] = 0x0698;
    km[gac('d')] = 0x062F;
    km[gac('e')] = 0x06D0;
    km[gac('F')] = 0x0641;
    km[gac('f')] = 0x0627;
    km[gac('G')] = 0x06AF;
    km[gac('g')] = 0x06D5;
    km[gac('H')] = 0x062E;
    km[gac('h')] = 0x0649;
    km[gac('i')] = 0x06AD;
    km[gac('J')] = 0x062C;
    km[gac('j')] = 0x0642;
    km[gac('K')] = 0x06C6;
    km[gac('k')] = 0x0643;
    km[gac('l')] = 0x0644;
    km[gac('m')] = 0x0645;
    km[gac('n')] = 0x0646;
    km[gac('o')] = 0x0648;
    km[gac('p')] = 0x067E;
    km[gac('q')] = 0x0686;
    km[gac('r')] = 0x0631;
    km[gac('s')] = 0x0633;
    km[gac('T')] = 0x0640; # space filler character
    km[gac('t')] = 0x062A;
    km[gac('u')] = 0x06C7;
    km[gac('v')] = 0x06C8;
    km[gac('w')] = 0x06CB;
    km[gac('x')] = 0x0634;
    km[gac('y')] = 0x064A;
    km[gac('z')] = 0x0632;
    km[gac('/')] = 0x0626;

    for i in range(128): # km.length
        if km[i] != 0:
            u = gac(gas(i).upper());
            if km[u] == 0:
                km[u] = km[i];

    # Uyghur punctuation marks
    km[gac(';')] = 0x061B;
    km[gac('?')] = 0x061F;
    km[gac(',')] = 0x060C;
    km[gac('<')] = 0x203A; # for '‹'
    km[gac('>')] = 0x2039; # for '›'
    km[gac('"')] = OQUOTE;

    # adapt parens, brackets, and braces for right-to-left typing
    km[gac('{')] = gac ( '}' );
    km[gac('}')] = gac ( '{' );
    km[gac('[')] = gac ( ']' );
    km[gac(']')] = gac ( '[' );
    km[gac('(')] = gac ( ')' );
    km[gac(')')] = gac ( '(' );

    # special handling of braces ( "{" and "}" ) for quotation in Uyghur
    km[gac('}')] = 0x00AB;
    km[gac('{')] = 0x00BB;

    # zero-out all entries first
    for i in range(256): # cm.length
            cm[i] = 0;

    cm[gac('a')] = 0x0627;
    cm[gac('b')] = 0x0628;
    cm[gac('c')] = 0x0643;
    cm[gac('d')] = 0x062F;
    cm[gac('e')] = 0x06D5;
    cm[gac('f')] = 0x0641;
    cm[gac('g')] = 0x06AF;
    cm[gac('h')] = 0x06BE;
    cm[gac('i')] = 0x0649;
    cm[gac('j')] = 0x062C;
    cm[gac('k')] = 0x0643;
    cm[gac('l')] = 0x0644;
    cm[gac('m')] = 0x0645;
    cm[gac('n')] = 0x0646;
    cm[gac('o')] = 0x0648;
    cm[gac('p')] = 0x067E;
    cm[gac('q')] = 0x0642;
    cm[gac('r')] = 0x0631;
    cm[gac('s')] = 0x0633;
    cm[gac('t')] = 0x062A;
    cm[gac('u')] = 0x06C7;
    cm[gac('v')] = 0x06CB;
    cm[gac('w')] = 0x06CB;
    cm[gac('x')] = 0x062E;
    cm[gac('y')] = 0x064A;
    cm[gac('z')] = 0x0632;

    cm[PRIMe] = 0x06D0; # 'e
    cm[PRIME] = 0x06D0; # 'E
    cm[COLo]  = 0x06C6; # :o
    cm[COLO]  = 0x06C6; # :O
    cm[COLu]  = 0x06C8; # :u
    cm[COLU]  = 0x06C8; # :U

    for i in range(256): # cm.length
        if cm[i] != 0:
            u = gac(gas(i).upper());
            if cm[u] == 0:
                cm[u] = cm[i];

    # Uyghur punctuation marks
    cm[gac(';')] = 0x061B;
    cm[gac('?')] = 0x061F;
    cm[gac(',')] = 0x060C;

def uly_2_ug(ustr):
    res = "";
    # i, cur, prev, next1, ch;
    # ccode, ncode;
    wdbeg = True;

    bd = '`';  # beginning delimiter
    ed = '`';  # ending delimiter

    verbatim = False;

    uly = ustr;

    # make URLs verbatim
    # regExp = /(\w+[p|s]:\/\/\S*)/gi;
    regExp = re.compile("(\w+[p|s]:\/\/\S*)")
    # uly = uly.replace(regExp, bd + "$1" + ed );
    uly = re.sub(regExp, bd + "$1" + ed, uly)

    # URLs without :#
    # regExp = /([\s|(]+\w+\.\w+\.\w+\S*)/g;
    regExp = re.compile("(\w+[p|s]:\/\/\S*)")
    # uly = uly.replace(regExp, bd + "$1" + ed );
    uly = re.sub(regExp, bd + "$1" + ed, uly)

    # two-part URLs with well-known suffixes
    # regExp = /([\s|(|,|.]+\w+\.(com|net|org|cn)[\s|)|\.|,|.|$])/g;
    regExp = re.compile("([\s|(|,|.]+\w+\.(com|net|org|cn)[\s|)|\.|,|.|$])")
    # uly = uly.replace(regExp, bd + "$1" + ed );
    uly = re.sub(regExp, bd + "$1" + ed, uly)

    # email addresses
    # regExp = /(\w+@\w+\.\w[\w|\.]*\w)/g;
    regExp = re.compile("(\w+@\w+\.\w[\w|\.]*\w)")
    # uly = uly.replace(regExp, bd + "$1" + ed );
    uly = re.sub(regExp, bd + "$1" + ed, uly)

    if not inited:
        bedit_init();

    # for i in range(len(uly)): # uly.length
    i = 0;
    while i < len(uly): # uly.length
        ch = 0;
        cur = uly[i];
        ccode = ord(uly[i]);
        next1 = "";
        ncode = None
        if i+1 < len(uly):
            next1 = uly[i+1];
            ncode = ord(uly[i+1]);

        if verbatim == True:
            if cur == ed: # ending verbatim mode
                verbatim = False;
            else:
                res += cur;
            continue;

        if cur == bd:
            verbatim = True;
            continue;

        if cur == '|' and prev == 'u' and (next1 == 'a' or next1 == 'e'):
            wdbeg = False;
            continue;

        # add hamza in front of vowels in word-beginning positions
        if wdbeg == True:
            if isvowel(cur):
                res += gas(HAMZA);
        else:
            if cur == '\'' or ccode == RCQUOTE:
                if isvowel(next1):
                    wdbeg = False; # don't add another hamza in next round
                    res += gas(HAMZA);
                    continue;
                elif isalpha(ncode):
                    continue;

        # AA, AE, and non-alpha-numeric letters makes word beginning
        if isvowel(cur) or not isalpha(ccode):
            wdbeg = True;
        else:
            wdbeg = False;

        # handle joint-letters
        if (cur == 'c' or cur == 'C') and (next1 == 'h' or next1 == 'H'):
            ch = CHEE
        elif (cur == 'g' or cur == 'G') and (next1 == 'h' or next1 == 'H'):
            ch = GHEE
        elif (cur == 'n' or cur == 'N') and (next1 == 'g' or next1 == 'G'):
            tmpch = ""
            if i+2 < len(uly):
                tmpch = uly[i+2];
            if tmpch != 'h' and tmpch != 'H':
                ch = NGEE
        elif cur == 's' or cur == 'S':
            if next1 == 'h' or next1 == 'H':
                ch = SHEE;
            elif next1 == 'z' or next1 == 'Z':
                ch = SZEE;


        if ch != 0:
            i+=1; # advance index for joint letters
            res += gas(ch);
        elif ccode < len(cm) and cm[ccode]: # cm.length
            res += gas( cm[ccode] ); # no joint letter, but valid ULY
        else:
            res += gas(ccode); # non-ULY, return whatever is entered

        prev = cur;

        i+=1;

    return res;

# isvowel -- returns true if ch is a vowel in Uyghur
def isvowel(ch):
    code = gac(ch);

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
            ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return True;

    if code == PRIMe or code == PRIME or code == COLo or \
            code == COLO or code == COLu or code == COLU:
        return True;

    return False;

def isalpha(code):
    if (gac('A') <= code and code <= gac('Z')) or (gac('a') <= code and code <= gac('z')):
        return True;
    return False;
