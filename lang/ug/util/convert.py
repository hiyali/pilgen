#
# Python convert: Salam Hiyali (hiyali920@gmail.com)
# Github: https:#github.com/hiyali
# 2020.2.21
#

# Author:  Muhammad Abdulla (muhammad@yulghun.com)
# Common routines for text conversion
# Version: 1.1 (Apr. 20, 2009)
# License: GPL


BASELEN = 256

WDBEG = 0;
INBEG = 1;
NOBEG = 2;

CHEE  = 0x0686;
GHEE  = 0x063A;
NGEE  = 0x06AD;
SHEE  = 0x0634;
SZEE  = 0x0698;
NEE   = 0x0646;
GEE   = 0x06AF;
LA    = 0xFEFB;
_LA   = 0xFEFC;
HAMZA = 0x0626;
RCQUOTE = 0x2019;
RCODQUOTE = 0x201C;
RCCDQUOTE = 0x201D;

PRIMe = 233; # 'e
PRIME = 201; # 'E
COLo  = 246; # :o
COLO  = 214; # :O
COLu  = 252; # :u
COLU  = 220; # :U

# start and end points for Arabic basic range
BPAD = 0x0600;
BMAX = 0x06FF;
EPAD = 0xFB00; # presentation form region (extented region)
EMAX = 0xFEFF;
CPAD = 0x0400; # cyrillic
CMAX = 0x04FF; # cyrillic

cm = {} # new Array(BASELEN);
cmapinv = {} # new Array(BASELEN);
pform = {} # new Array(BASELEN);

cyrmap = {} # new Array(BASELEN);
cyrmapinv = {} # new Array(BASELEN);

pf2basic = {} # new Array(EMAX-EPAD);

def CM(x):
    return cm[gac(x)]-BPAD;

class Syn:
    def __init__(self, i, b, m, e, bt):
        self.iform = i;
        self.bform = b;
        self.mform = m;
        self.eform = e;
        self.btype = bt;

# returns a char code for a given character
def gac(asc2):
   s = "" + asc2;
   return ord(s[0]) # s.charCodeAt(0);

# returns a string from a given char code
def gas ( code ):
   return chr(code) # String.fromCharCode(code);

pfinited = 0;  # flag for initialization of presentation form

# initialize the charmap and its inverse tables
def pfinit():
    pfinited = True;

    # zero-out all entries first
    for i in range(BASELEN): # cm.length:
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

    for i in range(BASELEN): # cm.length:
        if cm[i] != 0:
            u = gac(gas(i).upper());
            if cm[u] == 0:
                cm[u] = cm[i];

    # Uyghur punctuation marks
    cm[gac(';')] = 0x061B;
    cm[gac('?')] = 0x061F;
    cm[gac(',')] = 0x060C;

    for i in range(BASELEN): # cmapinv.length:
        wc = cm[i];
        if wc != 0:
            cmapinv [ wc - BPAD ] = i;

    # S new_syn ( wchar_t i, wchar_t b, wchar_t m, wchar_t e, begtype bt);

    for i in range(BASELEN): # pform.length:
        pform[i] = None;

    pform[ CM('a') ]    = Syn(0xFE8D, 0xFE8D, 0xFE8D, 0xFE8E, WDBEG);
    pform[ CM('e') ]    = Syn(0xFEE9, 0xFEE9, 0xFEE9, 0xFEEA, WDBEG);
    pform[ CM('b') ]    = Syn(0xFE8F, 0xFE91, 0xFE92, 0xFE90, NOBEG);
    pform[ CM('p') ]    = Syn(0xFB56, 0xFB58, 0xFB59, 0xFB57, NOBEG);
    pform[ CM('t') ]    = Syn(0xFE95, 0xFE97, 0xFE98, 0xFE96, NOBEG);
    pform[ CM('j') ]    = Syn(0xFE9D, 0xFE9F, 0xFEA0, 0xFE9E, NOBEG);
    pform[ CHEE-BPAD ]  = Syn(0xFB7A, 0xFB7C, 0xFB7D, 0xFB7B, NOBEG);
    pform[ CM('x') ]    = Syn(0xFEA5, 0xFEA7, 0xFEA8, 0xFEA6, NOBEG);
    pform[ CM('d') ]    = Syn(0xFEA9, 0xFEA9, 0xFEAA, 0xFEAA, INBEG);
    pform[ CM('r') ]    = Syn(0xFEAD, 0xFEAD, 0xFEAE, 0xFEAE, INBEG);
    pform[ CM('z') ]    = Syn(0xFEAF, 0xFEAF, 0xFEB0, 0xFEB0, INBEG);
    pform[ SZEE-BPAD ]  = Syn(0xFB8A, 0xFB8A, 0xFB8B, 0xFB8B, INBEG);
    pform[ CM('s') ]    = Syn(0xFEB1, 0xFEB3, 0xFEB4, 0xFEB2, NOBEG);
    pform[ SHEE-BPAD ]  = Syn(0xFEB5, 0xFEB7, 0xFEB8, 0xFEB6, NOBEG);
    pform[ GHEE-BPAD ]  = Syn(0xFECD, 0xFECF, 0xFED0, 0xFECE, NOBEG);
    pform[ CM('f') ]    = Syn(0xFED1, 0xFED3, 0xFED4, 0xFED2, NOBEG);
    pform[ CM('q') ]    = Syn(0xFED5, 0xFED7, 0xFED8, 0xFED6, NOBEG);
    pform[ CM('k') ]    = Syn(0xFED9, 0xFEDB, 0xFEDC, 0xFEDA, NOBEG);
    pform[ CM('g') ]    = Syn(0xFB92, 0xFB94, 0xFB95, 0xFB93, NOBEG);
    pform[ NGEE-BPAD ]  = Syn(0xFBD3, 0xFBD5, 0xFBD6, 0xFBD4, NOBEG);
    pform[ CM('l') ]    = Syn(0xFEDD, 0xFEDF, 0xFEE0, 0xFEDE, NOBEG);
    pform[ CM('m') ]    = Syn(0xFEE1, 0xFEE3, 0xFEE4, 0xFEE2, NOBEG);
    pform[ CM('n') ]    = Syn(0xFEE5, 0xFEE7, 0xFEE8, 0xFEE6, NOBEG);
    # pform[ CM('h') ]    = Syn(0xFEEB, 0xFEEB, 0xFEEC, 0xFEEC, NOBEG);
    pform[ CM('h') ]    = Syn(0xFBAA, 0xFBAA, 0xFBAD, 0xFBAD, NOBEG);
    pform[ CM('o') ]    = Syn(0xFEED, 0xFEED, 0xFEEE, 0xFEEE, INBEG);
    pform[ CM('u') ]    = Syn(0xFBD7, 0xFBD7, 0xFBD8, 0xFBD8, INBEG);
    pform[ CM('w') ]    = Syn(0xFBDE, 0xFBDE, 0xFBDF, 0xFBDF, INBEG);
    pform[ CM('i') ]    = Syn(0xFEEF, 0xFBE8, 0xFBE9, 0xFEF0, NOBEG);
    pform[ CM('y') ]    = Syn(0xFEF1, 0xFEF3, 0xFEF4, 0xFEF2, NOBEG);
    pform[ HAMZA-BPAD ] = Syn(0xFE8B, 0xFE8B, 0xFE8C, 0xFB8C, NOBEG);
    pform[ cm[COLo]-BPAD]   = Syn(0xFBD9, 0xFBD9, 0xFBDA, 0xFBDA, INBEG);
    pform[ cm[COLu]-BPAD ]   = Syn(0xFBDB, 0xFBDB, 0xFBDC, 0xFBDC, INBEG);
    pform[ cm[PRIMe]-BPAD ]  = Syn(0xFBE4, 0xFBE6, 0xFBE7, 0xFBE5, NOBEG);

    for i in range(EMAX-EPAD): # pf2basic.length:
        pf2basic[i] = [None] * 2 # new Array(2);

    # initialize presentation form to basic region mapping
    for i in range(BASELEN): # pform.length:
        lig = pform[i];
        if lig != None:
            pf2basic[lig.iform - EPAD][0] = i + BPAD;
            pf2basic[lig.bform - EPAD][0] = i + BPAD;
            pf2basic[lig.mform - EPAD][0] = i + BPAD;
            pf2basic[lig.eform - EPAD][0] = i + BPAD;

    # the letter 'h' has some other mappings
    pf2basic[0xFEEB - EPAD][0] = cm[gac('h')];
    pf2basic[0xFEEC - EPAD][0] = cm[gac('h')];

    # joint letter LA and _LA
    pf2basic[0xFEFB - EPAD][0] = cm[gac('l')];
    pf2basic[0xFEFB - EPAD][1] = cm[gac('a')];
    pf2basic[0xFEFC - EPAD][0] = cm[gac('l')];
    pf2basic[0xFEFC - EPAD][1] = cm[gac('a')];

    # joint letter AA, AE, EE, II, OO, OE, UU, UE
    # AA, _AA
    pf2basic[0xFBEA - EPAD][0] = HAMZA;
    pf2basic[0xFBEA - EPAD][1] = cm[gac('a')];
    pf2basic[0xFBEB - EPAD][0] = HAMZA;
    pf2basic[0xFBEB - EPAD][1] = cm[gac('a')];

    # AE, _AE
    pf2basic[0xFBEC - EPAD][0] = HAMZA;
    pf2basic[0xFBEC - EPAD][1] = cm[gac('e')];
    pf2basic[0xFBED - EPAD][0] = HAMZA;
    pf2basic[0xFBED - EPAD][1] = cm[gac('e')];

    # EE, _EE, _EE_
    pf2basic[0xFBF6 - EPAD][0] = HAMZA;
    pf2basic[0xFBF6 - EPAD][1] = cm[PRIMe];
    pf2basic[0xFBF7 - EPAD][0] = HAMZA;
    pf2basic[0xFBF7 - EPAD][1] = cm[PRIMe];
    pf2basic[0xFBF8 - EPAD][0] = HAMZA;
    pf2basic[0xFBF8 - EPAD][1] = cm[PRIMe];
    pf2basic[0xFBD1 - EPAD][0] = HAMZA;
    pf2basic[0xFBD1 - EPAD][1] = cm[PRIMe];

    # II, _II, _II_
    pf2basic[0xFBF9 - EPAD][0] = HAMZA;
    pf2basic[0xFBF9 - EPAD][1] = cm[gac('i')];
    pf2basic[0xFBFA - EPAD][0] = HAMZA;
    pf2basic[0xFBFA - EPAD][1] = cm[gac('i')];
    pf2basic[0xFBFB - EPAD][0] = HAMZA;
    pf2basic[0xFBFB - EPAD][1] = cm[gac('i')];

    # OO, _OO
    pf2basic[0xFBEE - EPAD][0] = HAMZA;
    pf2basic[0xFBEE - EPAD][1] = cm[gac('o')];
    pf2basic[0xFBEF - EPAD][0] = HAMZA;
    pf2basic[0xFBEF - EPAD][1] = cm[gac('o')];

    # OE, _OE
    pf2basic[0xFBF2 - EPAD][0] = HAMZA;
    pf2basic[0xFBF2 - EPAD][1] = cm[COLo];
    pf2basic[0xFBF3 - EPAD][0] = HAMZA;
    pf2basic[0xFBF3 - EPAD][1] = cm[COLo];

    # UU, _UU
    pf2basic[0xFBF0 - EPAD][0] = HAMZA;
    pf2basic[0xFBF0 - EPAD][1] = cm[gac('u')];
    pf2basic[0xFBF1 - EPAD][0] = HAMZA;
    pf2basic[0xFBF1 - EPAD][1] = cm[gac('u')];

    # UE, _UE
    pf2basic[0xFBF4 - EPAD][0] = HAMZA;
    pf2basic[0xFBF4 - EPAD][1] = cm[COLu];
    pf2basic[0xFBF5 - EPAD][0] = HAMZA;
    pf2basic[0xFBF5 - EPAD][1] = cm[COLu];

cyrinited = False;
def cyrinit():
    # TODO: check below pfinit is neccessary here
    if not pfinited:
        pfinit();

    cyrinited = True;

    # For Cyrillic. This maps between ULY and Cyrillic.
    for i in range(BASELEN): # cyrmap.length:
        cyrmap[i] = 0;

    for i in range(BASELEN): # cyrmapinv.length:
        cyrmapinv[i] = 0;

    cyrmap[gac('А')-CPAD] = cm[gac('a')];
    cyrmap[gac('а')-CPAD] = cm[gac('a')];
    cyrmap[gac('Б')-CPAD] = cm[gac('b')];
    cyrmap[gac('б')-CPAD] = cm[gac('b')];
    cyrmap[gac('Д')-CPAD] = cm[gac('d')];
    cyrmap[gac('д')-CPAD] = cm[gac('d')];
    cyrmap[gac('Ә')-CPAD] = cm[gac('e')];
    cyrmap[gac('ә')-CPAD] = cm[gac('e')];
    cyrmap[gac('Ф')-CPAD] = cm[gac('f')];
    cyrmap[gac('ф')-CPAD] = cm[gac('f')];
    cyrmap[gac('Г')-CPAD] = cm[gac('g')];
    cyrmap[gac('г')-CPAD] = cm[gac('g')];
    cyrmap[gac('Һ')-CPAD] = cm[gac('h')];
    cyrmap[gac('һ')-CPAD] = cm[gac('h')];
    cyrmap[gac('И')-CPAD] = cm[gac('i')];
    cyrmap[gac('и')-CPAD] = cm[gac('i')];
    cyrmap[gac('Җ')-CPAD] = cm[gac('j')];
    cyrmap[gac('җ')-CPAD] = cm[gac('j')];
    cyrmap[gac('К')-CPAD] = cm[gac('k')];
    cyrmap[gac('к')-CPAD] = cm[gac('k')];
    cyrmap[gac('Л')-CPAD] = cm[gac('l')];
    cyrmap[gac('л')-CPAD] = cm[gac('l')];
    cyrmap[gac('М')-CPAD] = cm[gac('m')];
    cyrmap[gac('м')-CPAD] = cm[gac('m')];
    cyrmap[gac('Н')-CPAD] = cm[gac('n')];
    cyrmap[gac('н')-CPAD] = cm[gac('n')];
    cyrmap[gac('О')-CPAD] = cm[gac('o')];
    cyrmap[gac('о')-CPAD] = cm[gac('o')];
    cyrmap[gac('П')-CPAD] = cm[gac('p')];
    cyrmap[gac('п')-CPAD] = cm[gac('p')];
    cyrmap[gac('Қ')-CPAD] = cm[gac('q')];
    cyrmap[gac('қ')-CPAD] = cm[gac('q')];
    cyrmap[gac('Р')-CPAD] = cm[gac('r')];
    cyrmap[gac('р')-CPAD] = cm[gac('r')];
    cyrmap[gac('С')-CPAD] = cm[gac('s')];
    cyrmap[gac('с')-CPAD] = cm[gac('s')];
    cyrmap[gac('Т')-CPAD] = cm[gac('t')];
    cyrmap[gac('т')-CPAD] = cm[gac('t')];
    cyrmap[gac('У')-CPAD] = cm[gac('u')];
    cyrmap[gac('у')-CPAD] = cm[gac('u')];
    cyrmap[gac('В')-CPAD] = cm[gac('v')];
    cyrmap[gac('в')-CPAD] = cm[gac('v')];
    cyrmap[gac('Х')-CPAD] = cm[gac('x')];
    cyrmap[gac('х')-CPAD] = cm[gac('x')];
    cyrmap[gac('Й')-CPAD] = cm[gac('y')];
    cyrmap[gac('й')-CPAD] = cm[gac('y')];
    cyrmap[gac('З')-CPAD] = cm[gac('z')];
    cyrmap[gac('з')-CPAD] = cm[gac('z')];
    cyrmap[gac('е')-CPAD] = cm[PRIMe];
    cyrmap[gac('Е')-CPAD] = cm[PRIMe];
    cyrmap[gac('Ө')-CPAD] = cm[COLo];
    cyrmap[gac('ө')-CPAD] = cm[COLo];
    cyrmap[gac('Ү')-CPAD] = cm[COLu];
    cyrmap[gac('ү')-CPAD] = cm[COLu];
    cyrmap[gac('Ж')-CPAD] = SZEE;
    cyrmap[gac('ж')-CPAD] = SZEE;
    cyrmap[gac('Ғ')-CPAD] = GHEE;
    cyrmap[gac('ғ')-CPAD] = GHEE;
    cyrmap[gac('Ң')-CPAD] = NGEE;
    cyrmap[gac('ң')-CPAD] = NGEE;
    cyrmap[gac('Ч')-CPAD] = CHEE;
    cyrmap[gac('ч')-CPAD] = CHEE;
    cyrmap[gac('Ш')-CPAD] = SHEE;
    cyrmap[gac('ш')-CPAD] = SHEE;

    # the inverse of cyrmap table, to speed up lookups (without wasting much space)
    for i in range(BASELEN): # cyrmapinv.length:
        ch = cyrmap[i];
        if ch != 0:
            cyrmapinv[ch - BPAD] = i;

def pf2br ( pfstr ):
    if not pfinited:
        pfinit();

    arr = {} # [None] * (len(pfstr) * 2) # new Array(pfstr.length * 2);

    j = 0;
    for i in range(len(pfstr)): # pfstr.length
        ch = ord(pfstr[i]) # pfstr.charCodeAt(i);

        if ch >= EPAD and ch < EMAX and pf2basic[ch - EPAD][0]:
            arr[j] = pf2basic[ch - EPAD][0];
            j+=1

            if pf2basic[ch - EPAD][1]:
                arr[j] = pf2basic[ch - EPAD][1];
                j+=1
        else:
            arr[j] = ch;
            j+=1

    for i in range(j): # j
        arr[i] = chr(arr[i]) # String.fromCharCode(arr[i]);

    return ''.join(arr.values());

def br_2_pf(br):
    # wc, pfwc, prevwc, ppfwc;
    # i, j, n;
    # syn, tsyn, lsyn;

    if not pfinited:
        pfinit();

    if type(br) != str:
        return "";

    pfwp = {} # new Array ( br.length);

    lsyn = pform[ CM('l') ];

    bt = WDBEG;
    j = 0;
    for i in range(len(br)): # br.length
        wc  = ord(br[i]) # br.charCodeAt(i);
        if BPAD <= wc and wc < BMAX:
            syn = pform [ wc - BPAD ];

            if syn != None:
                pfwc = {
                    WDBEG: syn.iform,
                    INBEG: syn.iform,
                    NOBEG: syn.eform,
                }.get(bt)

                # /* previous letter does not ask for word-beginning form,
                #  * and we have to change it to either medial or beginning form,
                #  * depending on the previous letter's current form.
                #  */
                #this means the previous letter was a joinable Uyghur letter
                if bt != WDBEG:
                    tsyn = pform [ prevwc - BPAD ];

                    # special cases for LA and _LA
                    if ppfwc == lsyn.iform and wc == cm[gac('a')]:
                        pfwp[j-1] = LA;
                        bt = WDBEG;
                        continue;
                    elif ppfwc == lsyn.eform and wc == cm[gac('a')]:
                        pfwp[j-1] = _LA;
                        bt = WDBEG;
                        continue;

                    # update previous character
                    if ppfwc == tsyn.iform:
                        pfwp[j-1] = tsyn.bform;
                    elif ppfwc == tsyn.eform:
                        pfwp[j-1] = tsyn.mform;
                bt = syn.btype; # we will need this in next round
            else: # a non-Uyghur char in basic range
                pfwc = wc;
                bt = WDBEG;
        else: # not in basic Arabic range ( 0x0600-0x06FF )
            pfwc = wc;
            bt = WDBEG;

        pfwp[j] = pfwc;
        ppfwc   = pfwc; # previous presentation form wide character
        prevwc  = wc;
        j+=1

    # str = ""; # TODO: check this line is not used
    for i in range(j): # j
        pfwp[i] = gas(pfwp[i]);

    return ''.join(pfwp.values());

# function uy2uly ( str ) {
#    i;
#    j = 0;
#    arr = new Array(str.length * 2);
#    pc = 0;
#    pwc = 0;

#    if ( !pfinited ) {
#       pfinit();
#    }

#    for ( i = 0; i < str.length; i++ ) {
#       wc = str.charCodeAt(i);

#       if ( wc == HAMZA ) {
#          continue;
#       }

#       # first handle Uyghur letters that become joint letters in Latin
#       if ( wc == CHEE ) {
#          arr[j++] = gac('c');
#          arr[j] = gac('h');
#       } else if ( wc == GHEE ) {
#          arr[j++] = gac('g');
#          arr[j] = gac('h');
#       } else if ( wc == NGEE ) {
#          arr[j++] = gac('n');
#          arr[j] = gac('g');
#       } else if ( wc == SHEE ) {
#          arr[j++] = gac('s');
#          arr[j] = gac('h');
#       } else if ( wc == SZEE ) {
#          arr[j] = gac('j');
#       } else if ( BPAD <= wc && wc < BMAX && cmapinv[wc-BPAD] != 0 ) {
#          # put an apostrophe when there are two-consecutive vowels, or NEE is followed by GEE
#          if ((is_vowel(pc) && is_vowel(cmapinv[wc-BPAD])) ||
#              (pwc == NEE && wc == GEE) ) {
#             arr[j++] = gac("'");
#          }

#          arr[j] = cmapinv[wc-BPAD];
#       } else {
#          arr[j] = wc;
#       }

#       pc = arr[j];
#       pwc = wc;

#       j++;
#    }

#    for ( i = 0; i < j; i++ ) {
#       arr[i] = String.fromCharCode(arr[i]);
#    }

#    return arr.join('');
# }

# function uy2cyr ( uystr ) {
#    i, j;
#    ch;
#    arr = new Array(uystr.length);

#    if ( !cyrinited ) {
#       cyrinit();
#    }

#    str = uystr.replace(new RegExp('يا', 'g'), "я");
#    str = str.replace(new RegExp('يۇ', 'g'), "ю");

#    j = 0;
#    for ( i = 0; i < str.length; i++ ) {
#       ch = str.charCodeAt(i);

#       if ( ch == HAMZA ) {
#           continue;
#       }

#       if ( BPAD <= ch && ch < (BPAD+cyrmapinv.length) && cyrmapinv[ch-BPAD]) {
#           arr[j++] = CPAD + cyrmapinv[ch-BPAD];
#       } else {
#           if ( ch == cm[gac('?')] ) {
#               arr[j++] = gac('?');
#           } else if ( ch == cm[gac(',')] ) {
#               arr[j++] = gac(',');
#           } else if ( ch == cm[gac(';')] ) {
#               arr[j++] = gac(';');
#           } else if ( ch == OQUOTE || ch == CQUOTE ) {
#               arr[j++] = gac('"');
#           } else {
#               arr[j++] = ch;
#           }
#       }
#    }

#    for ( i = 0; i < j; i++ ) {
#       arr[i] = String.fromCharCode(arr[i]);
#    }

#    return arr.join('');
# }

def cyr2uy (s):
    if not cyrinited:
        cyrinit();

    changeQuote = False;
    putHamza = True;
    openBrack = True;

    arr = {} # new Array(s.length*2);
    # uch;
    # code;

    j = 0;
    for i in range(len(s)): # s.length
        code = ord(s[i]) # s.charCodeAt(i);

        if code >= CPAD and code < CMAX and (cyrmap[code-CPAD] or code == gac('Я') \
                                             or code == gac('я') or code == gac('Ю') or code == gac('ю')):
            if code == gac('Я') or code == gac('я'): # YA in Cyrillic
                arr[j] = cm[gac('y')];
                j+=1
                arr[j] = cm[gac('a')];
                j+=1
                putHamza = True;
            elif code == gac('Ю') or code == gac('ю'): # YU in Cyrillic
                arr[j] = cm[gac('y')];
                j+=1
                arr[j] = cm[gac('u')];
                j+=1
            else:
                uch = cyrmap[code-CPAD];

                if is_uy_vowel(uch): # decide if we should put hamza
                    if putHamza:
                        arr[j] = HAMZA;
                        j+=1
                    else:
                        putHamza = True;
                else:
                    putHamza = False;

                arr[j] = uch;
                j+=1
        else: # non-cyrillic letters
            if code == gac(','):
                arr[j] = cm[gac(',')];
                j+=1
            elif code == gac('?'):
                arr[j] = cm[gac('?')];
                j+=1
            elif code == gac(';'):
                arr[j] = cm[gac(';')];
                j+=1
            elif code == gac('"') and changeQuote:
                if openBrack:
                    arr[j] = OQUOTE;
                    j+=1
                    openBrack = False;
                else:
                    arr[j] = CQUOTE;
                    j+=1
                    openBrack = True;
            elif code == RCODQUOTE: # opening double curly quote
                if changeQuote:
                    arr[j] = OQUOTE;
                    j+=1
                else:
                    arr[j] = gac('"');
                    j+=1
            elif code == RCCDQUOTE: # closing double curly quote
                if changeQuote:
                    arr[j] = OQUOTE;
                    j+=1
                else:
                    arr[j] = gac('"');
                    j+=1
            else:
                arr[j] = code;
                j+=1

            # check to to see if we should put hamza before next letter
            if code < BPAD or code > BMAX or is_uy_vowel(arr[j-1]):
                putHamza = True;

    for i in range(j): # j
        arr[i] = chr(arr[i]) # String.fromCharCode(arr[i]);

    return ''.join(arr.values())

def is_uy_vowel ( ch ):
    s = chr(ch) # String.fromCharCode(ch);

    if s == 'ا' or s == 'ە' or s == 'ى' or s == 'ې' or \
            s == 'و' or s == 'ۇ' or s == 'ۆ' or s == 'ۈ':
        return True;
    return False;

def is_vowel ( ch ):
    if ch == gac('a') or ch == gac('A') or ch == gac('e') or ch == gac('E') or \
            ch == PRIMe or ch == PRIME or ch == gac('i') or ch == gac('I') or \
            ch == gac('o') or ch == gac('O') or ch == COLo or ch == COLO or \
            ch == gac('u') or ch == gac('U') or ch == COLu or ch == COLU:
        return True;

    return False;

def uniq(l):
    m = {}
    for i in l:
        m[i] = 1
    return list(m.keys())

def get_syn_list(syn):
    return [chr(syn.iform), chr(syn.bform), chr(syn.mform), chr(syn.eform)]

def get_char_list():
    global pfinited
    if not pfinited:
        pfinit();

    char_list = []
    for k in cm:
        if cm[k] == 0:
            continue
        # print(k, cm[k], chr(int(cm[k])))
        char_list += [chr(int(cm[k]))]

    for k in pform:
        syn = pform[k]
        if not syn:
            continue
        char_list += get_syn_list(syn)

    char_list = uniq(char_list)

    return char_list
