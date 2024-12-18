from sympy import gcd, mod_inverse
from math import gcd as math_gcd

N = int("12537910646286841697597818332012932328390492808344475353293600217169407216008953116963355722073048035513768521048064616655898520535836838888615630336254033633521858619221676299187822570196566020971361385821257013549220827318687891684211668767310396377849261463285860532873867811051528186744271490044909819283798977751371413497270705843270168800848578959922519337570669013159523762994566331110456632608487858749430833011936672537145715175728317276817320036555592586513187862410146141513668058234422056366164499065735599299928835243445455788315691735302873876772973263878257272502311977024766661580047669846851520876561")
e1 = 1356697
e2 = 1355503

C1 = int("8817654638041831049561997400456149959304358556945948481988034883861668359182501729621096510503421001710916550192827564670022300065597291080678584676762649553905639877232184287866994764693927447115776134900513081965862463624096465366638293209574302470775071286985707494491698155375039922475819112155271171279350399773263580254865454546599853209951154943687966699412589025332133911164315993895401348942948179530969038180909457419420449577018112976290773994596297640939085007491629334233869739927848862787600958131184448070965446049597760503871008818066288327674768569487998731199581219120620889805744641906819380588489")
C2 = int("10248651913263618333812229447776408906246726065991665411026781805452437376274050269888103482996841677715494010568428206311534414034082623129318169128499831106043124849758590608749576957786288156711219875068915173684324657941587109008278608104002047385403292712319283088024024905705467865428195943002487030346752841006699594743251859087155705855846971698452177583034204132716494070787100190618756292110997093878117803935187950131776174424995150581850247536090472326048964575807258969334051831696481581245520774166566904281314667515394730233945520918436497108141899520488714493484418210423180250658752963754829939751483")

# Расширенный алгоритм Евклида для нахождения коэффициентов a и b, таких что:
# a * e1 + b * e2 = 1
def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

# Проверка, что e1 и e2 взаимно просты
g, a, b = extended_gcd(e1, e2)
if g != 1:
    raise ValueError("e1 и e2 должны быть взаимно простыми")

if b < 0:
    C2_inv = mod_inverse(C2, N)
    m = (pow(C1, a, N) * pow(C2_inv, -b, N)) % N
else:
    m = (pow(C1, a, N) * pow(C2, b, N)) % N

def int_to_text(m):
    hex_str = hex(m)[2:]  # Преобразуем в 16-ричное представление
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str 
    return bytes.fromhex(hex_str).decode('utf-8', errors='ignore')

plaintext = int_to_text(m)
print("Расшифрованное сообщение:", plaintext)
