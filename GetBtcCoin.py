import sys
import bitcoin
import requests
import json
import time
import random


webheader = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}


class NetCheck():
    networkError = False;
    # 检查公钥地址是否有币，或者公钥是址是否有交易记录 ，
    def getCoinIs0(numc):
        if(isinstance(numc,int) and numc !=0 ):
            return True;
        if (isinstance(numc,str) and float(numc) != 0):
            return True;
        return False;
    def getBlockHaveCoins(jsdata):
        try:
            networkError = False;
            if (jsdata and (None != jsdata)):
                if (('total_received' in jsdata) and NetCheck.getCoinIs0(jsdata['total_received'])):
                    return 1;
                elif (('unconfirmed_balance' in jsdata) and NetCheck.getCoinIs0(jsdata['unconfirmed_balance'])):
                    return 2;
            return 0;
        except Exception as e:
            print(e)
            networkError = True;
            return -1;

    # 地址： https: // www.blockcypher.com / dev / bitcoin /
    # https://api.blockcypher.com/v1/btc/main/addrs/
    def getBlockExplorer(pubkey):
        # while 1:
        blockmsg = None;
        try:
            blockmsg = requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + pubkey, timeout=4)
        except requests.RequestException or requests.exceptions.Timeout as e:
            print(e);
            # continue;
        else:
            try:
                blockdic = json.loads(blockmsg.text);
            except json.decoder.JSONDecodeError as e:
                print(e);
            else:
                # print(jsondata + "\n");
                if (None == blockdic or (not ('total_received' in blockdic))):
                    networkError = True;
                return blockdic;
            networkError = True;
            return None;

    # chain.api.btc.com接口解析  https://chain.api.btc.com/v3/address/15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew
    def getChain(pubkey):
        try:
            chainmsg = requests.get("https://chain.api.btc.com/v3/address/" + pubkey, timeout=4)
            chaindic = json.loads(chainmsg.text);
            if (None == chaindic or (not ('data' in chaindic))):
                networkError = True;
                return -1;
            chaindata = chaindic['data']
            networkError = False;
            if (('received' in chaindata) and NetCheck.getCoinIs0(chaindata['received'])):
                return 1;
            elif (('unconfirmed_received' in chaindata) and NetCheck.getCoinIs0(chaindata['unconfirmed_received'])):
                return 2;
            # if ((chaindic['received'])!= 0):
            #     return 1;
            # elif ((chaindic['data'])['received'] != 0):
            #     return 2;
            return 0;
        except:
            networkError = True;
            return -1;

    # blockchain网站接口解析  https://blockchain.info/rawaddr/15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew
    # https://www.blockchain.com/btc/address/1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s
    # https://www.bitgo.com/api/v1/address/1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s
    def getBlockChain(pubkey):
        try:
            blockchainmsg = requests.get("https://www.bitgo.com/api/v1/address/" + pubkey, timeout=6)
            blockchaindic = json.loads(blockchainmsg.text);
            if (None == blockchaindic or (not ('received' in blockchaindic))):
                networkError = True;
                return -1;
            networkError = False;
            if (('received' in blockchaindic) and NetCheck.getCoinIs0(blockchaindic['received'])):
                return 1;
            elif (('confirmedBalance' in blockchaindic) and NetCheck.getCoinIs0(blockchaindic['confirmedBalance'])):
                return 2;
            return 0;
        except Exception as e:
            print(e)
            networkError = True;
            return -1;

    # https: // sochain.com / api  # get-balance
    # https://sochain.com/api/v2/get_address_balance/BTC/1NcXPMRaanz43b1kokpPuYDdk6GGDvxT2T
    def getBitaps(pubkey):
        try:
            bitapsmsg = requests.get("https://sochain.com/api/v2/get_address_balance/BTC/" + pubkey, timeout=4)
            bitapsdic = json.loads(bitapsmsg.text);
            if (None == bitapsdic or (not ('data' in bitapsdic))):
                networkError = True;
                return -1;
            networkError = False;
            bitdata = bitapsdic['data'];
            if ('confirmed_balance' in bitdata and NetCheck.getCoinIs0(bitdata['confirmed_balance'])):
                return 1;
            elif ('unconfirmed_balance' in bitdata and NetCheck.getCoinIs0(bitdata['unconfirmed_balance'])):
                return 2;
            return 0;
        except Exception as e:
            print(e)
            networkError = True;
            return -1;
# msgs = [
#     '所有的「压缩」，都表示公钥坐标转换为公钥值时的压缩',
#     '压缩密钥不是把密钥压缩，而是指仅用来生成压缩公钥的密钥',
#     '压缩地址也不是把地址压缩，而是用压缩公钥生成的地址'
# ]

# long256 = 0x57c617d9b4e1f7af6ec97ca2ff57e94a28279a7eedd4d12a99fa11170e94f5a4
    long256 = 0x57c617d9b4e1f7af6ec97ca2ff57e94a28279a7eedd4d12a99fa11170e94f5ab
def getRanPrivateHex():
    global long256
    decoded_private_key = None;
    while True:
        # 生成一个用十六进制表示的长 256 位的私钥（str类型）
        decoded_private_key = bitcoin.random_key()
        # 解码为十进制的整形密钥
        long256 = bitcoin.decode_privkey(decoded_private_key, 'hex')
        # decoded_private_key = bitcoin.decode_privkey(hex(long256).replace('0x','',1), 'hex')
        if 0 < long256 < bitcoin.N:
            break
    return decoded_private_key;
def getPrivate16L256():
    # 生成一个随机的密钥
    global long256
    while True:
        # 生成一个用十六进制表示的长 256 位的私钥（str类型）
        # long256 = long256+1; # long256 = bitcoin.random_key()
        # 解码为十进制的整形密钥
        # decoded_private_key = bitcoin.decode_privkey(hex(long256).replace('0x','',1), 'hex')
        # if 0 < decoded_private_key < bitcoin.N:
        if 0 < long256 < bitcoin.N:
            break
        else:
            getRanPrivateHex();
    # longde = decoded_private_key;
    print(f'密钥（十六进制）：{hex(long256)} （长 256 位）')
    # print(f'密钥（十进制）：{long256} （0 到 1.158*10**77 之间）')
    return [hex(long256).replace('0x','',1),long256];
#生成 二个公钥
def getPublicKey(privatekey):
    # 用 WIF 格式编码密钥
    wif_encoded_private_key = bitcoin.encode_privkey(privatekey[1], 'wif')
    # print(f'密钥（WIF）：{wif_encoded_private_key} （5 开头，长 51 字符）')

    # 用 01 标识的压缩密钥
    compressed_private_key = privatekey[0] + '01'
    # print(f'压缩密钥（十六进制）：{compressed_private_key} （01 结尾，长 264 位）')

    # 生成 WIF的压缩格式
    wif_compressed_private_key = bitcoin.encode_privkey(
        bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
    # print(f'压缩密钥（WIF）：{wif_compressed_private_key} （L/K 开头）')

    # 计算公钥坐标 K = k * G
    public_key = bitcoin.fast_multiply(bitcoin.G, privatekey[1])
    # print(f'公钥（坐标）：{public_key}')
    # # 转十六也可用 bitcoin.encode(xxx, 16)
    # print(f'公钥（坐标的十六进制）：{tuple(hex(i) for i in public_key)}')

    # 计算公钥
    hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
    # print(f'公钥（十六进制）：{hex_encoded_public_key} （04 x y）')

    # 计算压缩公钥
    # if public_key[1] % 2 == 0:  # 两种方式均可
    if public_key[1] & 1 == 0:
        compressed_prefix = '02'
    else:
        compressed_prefix = '03'
    # 转十六也可用 bitcoin.encode(xxx, 16)
    hex_compressed_public_key = compressed_prefix + hex(public_key[0])[2:]
    # print(f'压缩公钥（十六进制）{hex_compressed_public_key} '
    #       '（02 开头代表 y 是偶数，03 开头代表 y 是奇数）')

    # 计算地址
    # 传入公钥坐标对象/十六进制公钥值，输出同样的地址
    # 传入压缩公钥值，输出与⬆️不同的地址
    # print(f'地址（b58check）：{bitcoin.pubkey_to_address(public_key)} （1 开头）')
    # print(hex_compressed_public_key)
    compkey = None;
    try:
        compkey = bitcoin.pubkey_to_address(hex_compressed_public_key)
    except Exception as e:
        # print(e)
        compkey = None;
    # print('压缩地址（b58check）：'
    #       f'{compkey} （1 开头）')
    return [privatekey[0],bitcoin.pubkey_to_address(public_key),compkey,0]

# getPublicKey(getPrivate16L256())
def savePublicKeyCoin(keys):
    params = {"pubkey":keys[1],"pubkey1":keys[2],
              "privatekey":keys[0],"connum":keys[3]}

    # print(response)
ranintnet = 0;##
def getHasCoin(level,keys):
    global ranintnet;
    if None == keys:
        return 0;
    # ranint = random.randint(1, 3);  # 随机在不同服务器间切换获取数据， 避免 封掉IP 地址
    hasCoin = 0;

    # hasCoin = NetCheck.getBlockHaveCoins(NetCheck.getBlockExplorer(keys));
    # hasCoin = NetCheck.getChain(keys);
    # hasCoin = NetCheck.getBlockChain(keys);
    # hasCoin = NetCheck.getBitaps(keys);
    if ranintnet >=4:
        ranintnet=0;
    if (ranintnet == 0):
        hasCoin = NetCheck.getBlockHaveCoins(NetCheck.getBlockExplorer(keys));
    elif (ranintnet == 1):
        hasCoin = NetCheck.getChain(keys);
    elif (ranintnet == 2):
        hasCoin = NetCheck.getBlockChain(keys);
    elif (ranintnet == 3):
        hasCoin = NetCheck.getBitaps(keys);
    ranintnet=ranintnet+1;
    print(str(hasCoin) + ":::" + str(keys));
    if (NetCheck.networkError and level<=1):
        time.sleep(1);
        hasCoin = getHasCoin(level+1,keys)
        # hasCoin = NetCheck.NetCheck.getChain(keys);
    return hasCoin;
def writefile(private):
    hc = open("./keymsg/" + (private[0:10] + ".md"), "w");
    hc.write(str(private));
    hc.close();
#存储到数据库
def checkKeyCoin(keys):
    global long256
    writefile(getRanPrivateHex());
    while True:
        keys = getPublicKey(getPrivate16L256());
        keys[3] = getHasCoin(0,keys[1]);
        if keys[3] <= 0:
            keys[3] = getHasCoin(0,keys[2]);
        savePublicKeyCoin(keys);
        # # 将有钱的地址 公私钥进行存储到指定目录
        if (keys[3] >= 1):
            hc = open("./keymsg/" + (keys[1] + "." + str(keys[3])), "w");
            hc.write(str(keys));
            hc.close();
        long256 = long256 + 1;

checkKeyCoin(None);
#http://127.0.0.1:8080/updatebtckey?pubkey=1HVccNgvMsjSakqZfVxre7PDWuk4npFpRu&pubkey1=1613EUm4j3gCgJcUCM6zczPFuiAqqtNYLL&privatekey=340e338b218be0753483279c81aa340264cbb828a00e5a4eb9032134ca61738e&connum=0