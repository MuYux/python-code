# coding: utf-8
import pymysql
def create_db():
    db = pymysql.connect("localhost","root","","random",charset="utf8")
    cursor = db.cursor()
    cursor.execute("drop table if exists psw")
    sql = """create table psw(
            id long,
            password varchar(10)
            )default charset = utf8"""
    cursor.execute(sql)
    db.close()
def insert_db(n,i):
    db = pymysql.connect("localhost","root","","random",charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO psw(id,password) VALUES ({},'{}')".format(n,i)
    cursor.execute(sql)
    db.commit()
    db.close()
def ins_psw(password):
    n = 1
    for i in password:
        insert_db(n, i)
        n = n + 1
create_db()
password=['ncnlhfbhlb', 'ynczuwenwh', 'ruclqpkdvn', 'yzucjjsktp', 'kdrsvzldqp', 'ghpljgmofh', 'jyuiwlzgmc', 'qvoyizmuvq', 'jfzntpyytw', 'erxkbjvhpz', 'ijsknothou', 'rtxasfpqhr', 'pncabnkchn', 'pcxmlgtdsx', 'epygmvxzxs', 'podghrbees', 'exbokebcif', 'kfngswqwoh', 'hkyignmwek', 'vaaifkuhma', 'upxjpqgard', 'obrzhmdpbj', 'zzaywnhjcn', 'jhwjwvbylb', 'rxymexdnnw', 'zzglvhtlxm', 'ztwjpfisyi', 'unwlrgltmj', 'gipdekaaux', 'zprcokxqof', 'odlcskdovh', 'lihukjbdct', 'fdqfgxuaoe', 'nqdqiiibeb', 'yutkrdjyhj', 'ujlpcemidb', 'auartunflt', 'vicuskpoci', 'niufjghefc', 'xzdqukwkkw', 'xfztrafkuu', 'agizuvzgyd', 'oxrfxbjjbj', 'dzjbpxulyr', 'ffzwdjundw', 'fflqircqqp', 'wvhaarveem', 'adoxncnwwy', 'asunltxmdw', 'zezftsffbs', 'ovwqrpypec', 'oahpnblwlj', 'pfsrjcsmsu', 'pykhqpqwhw', 'rhdugifdlh', 'wiqzdtiqdq', 'qehjzgiuam', 'hpnhvcmkkd', 'bkzujnlgls', 'cdsmfggmwv', 'lstapawocr', 'lcnonklxmd', 'uicpvbtwmm', 'oifzbmlmjq', 'lqmquqlqmv', 'xvgnuwmquu', 'cliqzmffbq', 'shcupzejct', 'lsidenolrq', 'eosvicpiad', 'zagxckozkk', 'akvsrkxosc', 'sfrtvdcjts', 'hghxurrwgc', 'vsweoyvdsb', 'bejlycfwna', 'wksjhpdizl', 'xisppkvfnb', 'jddbohbjfy', 'chzggdhihy', 'bbgekhgdrc', 'ueowxgveun', 'caufyyvuns', 'pctvzammrm', 'wujwkzafme', 'epdczksocu', 'mfzhgcrfon', 'srahffioet', 'utopksvcyw', 'siiszzsyol', 'wxjqztgtph', 'yihycxukfb', 'oljezvguxw', 'rrzcqgggdx', 'zoksixepen', 'yjwmzarpft', 'dtzatpxlzr', 'wxekyejuus', 'fzqayqbowf', 'ziedqktgwc', 'cehwuyaqzw', 'pjagsfezdr', 'utlbikyobe', 'tiuiqttfmg', 'xelrrljxca', 'gdcfolsnzv', 'cjaqahwadh', 'oewnzaeict', 'vccvzntkdo', 'tkhmeiyymw', 'qfdxtshsxp', 'hdpyohyqcg', 'fvfyoiuhew', 'lbuvzjjaid', 'mzbtudtcvk', 'ehqhmutkkr', 'ybgpvxtyoz', 'qsqlmrvmqx', 'ofsqevytve', 'qlphpbbcpz', 'bfopoobmmo', 'mzfjgwduth', 'qtygbizlhv', 'vvyfelklqe', 'xxhinjooao', 'daybdnrcnx', 'kfwzlquiqb', 'gdyctkvlcl', 'dgaqifkgap', 'lsaeumdcsd', 'bmahdwqxav', 'hkmhjvaaxp', 'hmajaaaeyg', 'koywicudcm', 'pyvpijifpd', 'wmmawxdrbq', 'lreringfii', 'qkbtksaepc', 'wwxnvzlapb', 'tbfujnnxnr', 'wfdzhntqxs', 'wqbyawithq', 'hxxpucgdff', 'jpveaolvmn', 'gbohulbfkb', 'rkdvblbaqy', 'watwiavaxa', 'hzabicsrqj', 'jzocveilik', 'bnvtwuafam', 'quiesogzsm', 'twxqeabxxu', 'ppsumcdcyn', 'lrxihbetuh', 'czszgcmqwx', 'incqrvyaph', 'utxcmpuedu', 'sbjngperlt', 'pikghrxmhs', 'nkoflhvdtr', 'npmlokvzga', 'qkhhcvpjtj', 'yubemefihg', 'hkpzeanync', 'tkzqghhmxl', 'bmwhjfmzdx', 'nxblypjqbn', 'dyrditqgqs', 'zbquhukxvb', 'nmfjhsewqq', 'guktkkozeb', 'enrhtrgwyl', 'hjgxpzizve', 'lsdwntmeci', 'bsfsjviopb', 'igqmwuyopi', 'onmdvxnjvd', 'bbzxprmelx', 'kecyarcsjw', 'knbawmptya', 'nlcgrqpszs', 'fyneoauhrs', 'gltszxozuc', 'rzgeglnrdg', 'faizrskelg', 'waeluukkki', 'qcpnyjwpqn', 'rmgqdunrqw', 'htqvuphzvi', 'pyzuicwqqk', 'sgetmcwfwr', 'wgvwzebnrk', 'ziqgsgzjmk', 'rlciuaxgwb', 'zdjajgrjne', 'bklsqtcwlu', 'cnnjtmmvls', 'shwzthseze', 'fbuqlpnmgh', 'snchjobzka']
ins_psw(password)
