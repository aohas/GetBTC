# GetBTC
在亿万比特币地址中摸金,目前全世界已经产出的比特币中约有五分之一丢失，差不多近500万个，也许可以把这五百万个找回来，而且谁找到就算谁的

脚本使用python3,通过bitcoin库生比特币私钥，通过生成的私钥获取到公钥，然后用公钥地址去碰撞网络上已有的比特币数据库。
建议使用abe项目生成本地数据库 --- https://github.com/bitcoin-abe/bitcoin-abe 
碰撞速度更快

###安装及运行
建议使用python3.7及以上版本
######pip3 安装
pip3 install bitcoin
pip3 install requests
###### 运行
python3 GetBtcCoin.py

###参考查询到比特币公私钥地址
['57c617d9b4e1f7af6ec97ca2ff57e94a28279a7eedd4d12a99fa11170e94f5a4', '1CQLd3bhw4EzaURHbKCwM5YZbUQfA4ReY6', '1EHw4jytKnzMSX8szNrXJ9FQiahKYnuuji', 1]
1CQLd3bhw4EzaURHbKCwM5YZbUQfA4ReY6 中有存在交易记录


###碰撞的网络接口
https://api.blockcypher.com/v1/btc/main/addrs/
https://chain.api.btc.com
https://www.bitgo.com/api/v1/address/
https://sochain.com/api/v2/get_address_balance/BTC/

####可参考碰撞网络接口地址 https://cloud.tencent.com/developer/article/1423879
1、blockchain.com比特币api
blockchain.com的比特币api是最受欢迎的比特币开发第三方api之一，提供支付处理、 钱包服务、市场行情数据等功能。blockchain.com的比特币api同时还提供了 针对多种语言的封装开发包，例如python、java、.net(c#)、ruby、php和node。
地址：https://www.blockchain.com/api

2、chain.so比特币api
chain.so的特色是除了提供比特币api，还额外提供的一些山寨币的api， 例如莱特币、达世币等。
chian.so的比特币api，提供了获取地址、区块、市场行情等方面的功能，也支持 交易广播。免费用户有5次请求/秒的限流。
地址：https://chain.so/api

3、block.io比特币api
block.io的比特币api包括基本的钱包服务、实时通知与即时支付转发等功能，支持 web hook和websocket。对于免费用户，有3次/秒的限流。
地址：https://www.block.io/docs

4、chainquery.com比特币api
chainquery.com提供了比特币rpc api的web访问接口，你可以在网页里直接输入并 执行标准的比特币rpc命令。
地址：http://chainquery.com/bitcoin-api

5、coinbase.com比特币api
作为老牌的交易所，coinbase.com也提供比特币api，功能包括生成比特币地址、买/卖比特币、 钱包服务、实时行情接收、支付到账通知等。
接入coinbase.com的比特币api需要使用OAuth2，这是令人不开心的一点。
地址：https://developers.coinbase.com/

6、blockcypher.com比特币api
blockcyper.com提供rest风格的比特币api，功能涵盖地址、钱包、交易等常见需求， 同时提供事件和hook机制，以便应用实时得到通知。
地址： https://www.blockcypher.com/dev/bitcoin/

7、bitcoinchain.com比特币api
bitcoinchain.com提供rest和stream两种方式的比特币api，功能包括基本的比特币区块链 数据交互和市场行情通知。免费用户有1次请求/秒的限流。
地址：https://bitcoinchain.com/api

8、coindesk.com比特币api
coindesk.com专注于提供比特币价格指数方面的api，包括实时BPI数据和历史BPI数据。 coindesk.com的比特币api不支持与比特币区块链的交互。
地址：https://www.coindesk.com/api

9、blockchain.info比特币api
作为专业的比特币区块链浏览服务提供商，blockchain.info专注于提供比特币区块数据查询api， 如果你希望查询某个地址相关的历史交易信息，bitchain.info的比特币api是最佳选择。
地址：https://blockchain.info/q

10、btc.com比特币api
btc.com的比特币api主要提供比特币区块链交易数据的查询功能，但是不支持比特币交易的广播。
地址： https://btc.com/api-doc


##### 其它信息 www.aohas.com