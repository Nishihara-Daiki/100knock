#!/bin/bash

mkdir -p data
cd data
wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
gzip -d jawiki-country.json.gz
cd ..


python3 q20.py data/jawiki-country.json | head -n6
# {{redirect|UK}}
# {{基礎情報 国
# |略名 = イギリス
# |日本語国名 = グレートブリテン及び北アイルランド連合王国
# |公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
# *{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>


python3 q21.py data/jawiki-country.json
# [[Category:イギリス|*]]
# [[Category:英連邦王国|*]]
# [[Category:G8加盟国]]
# [[Category:欧州連合加盟国]]
# [[Category:海洋国家]]
# [[Category:君主国]]
# [[Category:島国|くれいとふりてん]]
# [[Category:1801年に設立された州・地域]]


python3 q22.py data/jawiki-country.json
# イギリス
# 英連邦王国
# G8加盟国
# 欧州連合加盟国
# 海洋国家
# 君主国
# 島国
# 1801年に設立された州・地域


python3 q23.py data/jawiki-country.json | head -n5
# 1	国名
# 1	歴史
# 1	地理
# 2	気候
# 1	政治


python3 q24.py data/jawiki-country.json
# PalaceOfWestminsterAtNight.jpg
# Westminster Abbey - West Door.jpg
# Edinburgh Cockburn St dsc06789.jpg
# Canterbury Cathedral - Portal Nave Cross-spire.jpeg
# Kew Gardens Palm House, London - July 2009.jpg
# 2005-06-27 - United Kingdom - England - London - Greenwich.jpg
# Stonehenge2007 07 30.jpg
# Yard2.jpg
# Durham Kathedrale Nahaufnahme.jpg
# Roman Baths in Bath Spa, England - July 2006.jpg
# Fountains Abbey view02 2005-08-27.jpg
# Blenheim Palace IMG 3673.JPG
# Liverpool Pier Head by night.jpg
# Hadrian's Wall view near Greenhead.jpg
# London Tower (1).JPG


python3 q25.py data/jawiki-country.json
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>', '国旗画像': 'Flag of the United Kingdom.svg', '国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]', '国章リンク': '（[[イギリスの国章|国章]]）', '標語': '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）', '国歌': '[[女王陛下万歳|神よ女王陛下を守り給え]]', '位置画像': 'Location_UK_EU_Europe_001.svg', '公用語': '[[英語]]（事実上）', '首都': '[[ロンドン]]', '最大都市': 'ロンドン', '元首等肩書': '[[イギリスの君主|女王]]', '元首等氏名': '[[エリザベス2世]]', '首相等肩書': '[[イギリスの首相|首相]]', '首相等氏名': '[[デーヴィッド・キャメロン]]', '面積順位': '76', '面積大きさ': '1 E11', '面積値': '244,820', '水面積率': '1.3%', '人口統計年': '2011', '人口順位': '22', '人口大きさ': '1 E7', '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>', '人口密度値': '246', 'GDP統計年元': '2012', 'GDP値元': '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>', 'GDP統計年MER': '2012', 'GDP順位MER': '5', 'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />', 'GDP統計年': '2012', 'GDP順位': '6', 'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />', 'GDP/人': '36,727<ref name="imf-statistics-gdp" />', '建国形態': '建国', '確立形態1': '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）', '確立年月日1': '[[927年]]／[[843年]]', '確立形態2': '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）', '確立年月日2': '[[1707年]]', '確立形態3': '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）', '確立年月日3': '[[1801年]]', '確立形態4': "現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更", '確立年月日4': '[[1927年]]', '通貨': '[[スターリング・ポンド|UKポンド]] (&pound;)', '通貨コード': 'GBP', '時間帯': '±0', '夏時間': '+1', 'ISO 3166-1': 'GB / GBR', 'ccTLD': '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>', '国際電話番号': '44', '注記': '<references />'}


python3 q26.py data/jawiki-country.json
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（[[アイルランド語]]）<br/>*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（[[コーンウォール語]]）<br/>*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（[[スコットランド語]]）<br/>**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>', '国旗画像': 'Flag of the United Kingdom.svg', '国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]', '国章リンク': '（[[イギリスの国章|国章]]）', '標語': '{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）', '国歌': '[[女王陛下万歳|神よ女王陛下を守り給え]]', '位置画像': 'Location_UK_EU_Europe_001.svg', '公用語': '[[英語]]（事実上）', '首都': '[[ロンドン]]', '最大都市': 'ロンドン', '元首等肩書': '[[イギリスの君主|女王]]', '元首等氏名': '[[エリザベス2世]]', '首相等肩書': '[[イギリスの首相|首相]]', '首相等氏名': '[[デーヴィッド・キャメロン]]', '面積順位': '76', '面積大きさ': '1 E11', '面積値': '244,820', '水面積率': '1.3%', '人口統計年': '2011', '人口順位': '22', '人口大きさ': '1 E7', '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>', '人口密度値': '246', 'GDP統計年元': '2012', 'GDP値元': '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>', 'GDP統計年MER': '2012', 'GDP順位MER': '5', 'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />', 'GDP統計年': '2012', 'GDP順位': '6', 'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />', 'GDP/人': '36,727<ref name="imf-statistics-gdp" />', '建国形態': '建国', '確立形態1': '[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）', '確立年月日1': '[[927年]]／[[843年]]', '確立形態2': '[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）', '確立年月日2': '[[1707年]]', '確立形態3': '[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）', '確立年月日3': '[[1801年]]', '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更', '確立年月日4': '[[1927年]]', '通貨': '[[スターリング・ポンド|UKポンド]] (&pound;)', '通貨コード': 'GBP', '時間帯': '±0', '夏時間': '+1', 'ISO 3166-1': 'GB / GBR', 'ccTLD': '[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>', '国際電話番号': '44', '注記': '<references />'}


python3 q27.py data/jawiki-country.json
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（スコットランド・ゲール語）<br/>*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（ウェールズ語）<br/>*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（アイルランド語）<br/>*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（コーンウォール語）<br/>*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（スコットランド語）<br/>**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>', '国旗画像': 'Flag of the United Kingdom.svg', '国章画像': 'ファイル:Royal Coat of Arms of the United Kingdom.svg', '国章リンク': '（イギリスの国章）', '標語': '{{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）', '国歌': '女王陛下万歳', '位置画像': 'Location_UK_EU_Europe_001.svg', '公用語': '英語（事実上）', '首都': 'ロンドン', '最大都市': 'ロンドン', '元首等肩書': 'イギリスの君主', '元首等氏名': 'エリザベス2世', '首相等肩書': 'イギリスの首相', '首相等氏名': 'デーヴィッド・キャメロン', '面積順位': '76', '面積大きさ': '1 E11', '面積値': '244,820', '水面積率': '1.3%', '人口統計年': '2011', '人口順位': '22', '人口大きさ': '1 E7', '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>', '人口密度値': '246', 'GDP統計年元': '2012', 'GDP値元': '1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>', 'GDP統計年MER': '2012', 'GDP順位MER': '5', 'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />', 'GDP統計年': '2012', 'GDP順位': '6', 'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />', 'GDP/人': '36,727<ref name="imf-statistics-gdp" />', '建国形態': '建国', '確立形態1': 'イングランド王国／スコットランド王国<br />（両国とも連合法 (1707年)まで）', '確立年月日1': '927年／843年', '確立形態2': 'グレートブリテン王国建国<br />（連合法 (1707年)）', '確立年月日2': '1707年', '確立形態3': 'グレートブリテン及びアイルランド連合王国建国<br />（連合法 (1800年)）', '確立年月日3': '1801年', '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更', '確立年月日4': '1927年', '通貨': 'スターリング・ポンド (&pound;)', '通貨コード': 'GBP', '時間帯': '±0', '夏時間': '+1', 'ISO 3166-1': 'GB / GBR', 'ccTLD': '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>', '国際電話番号': '44', '注記': '<references />'}


python3 q28.py data/jawiki-country.json
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（スコットランド・ゲール語）<br/>*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（ウェールズ語）<br/>*{{lang|ga|Ríocht Aontaithe na Breataine Móire agus Tuaisceart na hÉireann}}（アイルランド語）<br/>*{{lang|kw|An Rywvaneth Unys a Vreten Veur hag Iwerdhon Glédh}}（コーンウォール語）<br/>*{{lang|sco|Unitit Kinrick o Great Breetain an Northren Ireland}}（スコットランド語）<br/>**{{lang|sco|Claught Kängrick o Docht Brätain an Norlin Airlann}}、{{lang|sco|Unitet Kängdom o Great Brittain an Norlin Airlann}}（アルスター・スコットランド語）</ref>', '国旗画像': 'Flag of the United Kingdom.svg', '国章画像': 'ファイル:Royal Coat of Arms of the United Kingdom.svg', '国章リンク': '（イギリスの国章）', '標語': '{{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）', '国歌': '女王陛下万歳', '位置画像': 'Location_UK_EU_Europe_001.svg', '公用語': '英語（事実上）', '首都': 'ロンドン', '最大都市': 'ロンドン', '元首等肩書': 'イギリスの君主', '元首等氏名': 'エリザベス2世', '首相等肩書': 'イギリスの首相', '首相等氏名': 'デーヴィッド・キャメロン', '面積順位': '76', '面積大きさ': '1 E11', '面積値': '244,820', '水面積率': '1.3%', '人口統計年': '2011', '人口順位': '22', '人口大きさ': '1 E7', '人口値': '63,181,775<ref>http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population</ref>', '人口密度値': '246', 'GDP統計年元': '2012', 'GDP値元': '1兆5478億<ref name="imf-statistics-gdp">http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom</ref>', 'GDP統計年MER': '2012', 'GDP順位MER': '5', 'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />', 'GDP統計年': '2012', 'GDP順位': '6', 'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />', 'GDP/人': '36,727<ref name="imf-statistics-gdp" />', '建国形態': '建国', '確立形態1': 'イングランド王国／スコットランド王国<br />（両国とも連合法 (1707年)まで）', '確立年月日1': '927年／843年', '確立形態2': 'グレートブリテン王国建国<br />（連合法 (1707年)）', '確立年月日2': '1707年', '確立形態3': 'グレートブリテン及びアイルランド連合王国建国<br />（連合法 (1800年)）', '確立年月日3': '1801年', '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更', '確立年月日4': '1927年', '通貨': 'スターリング・ポンド (&pound;)', '通貨コード': 'GBP', '時間帯': '±0', '夏時間': '+1', 'ISO 3166-1': 'GB / GBR', 'ccTLD': '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>', '国際電話番号': '44', '注記': '<references />'}


python3 q29.py data/jawiki-country.json


