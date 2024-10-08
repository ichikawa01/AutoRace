# import pdfplumber

# # PDFファイルのパス
# pdf_path = "Data.pdf"

# # pdfplumberでPDFを開く
# with pdfplumber.open(pdf_path) as pdf:
#     # 全ページのテキストを抽出して表示
#     for page_number in range(len(pdf.pages)):
#         page = pdf.pages[page_number]
#         text = page.extract_text()
        
#         # ページ番号とテキストを表示
#         print(f"--- Page {page_number + 1} ---")
#         print(text)

explanation_test = """選手特長一覧表
2024.02
レースに出場する選手の特長や傾向を予め把握しておけば、レースの展開や着順を予想するのに大変役立ちますので、
「選手特長一覧表」の各項目を参考にして下さい。（各項目を５段階評価し、数字が上がるほど評価が高くなります。）
※ 下記の数値はその日のコンディション等により変わりますので、目安としてご活用下さい。
【項目の説明】
１．Ｓ（スタート）力 選手のＳ力はレース展開を一変させるほどの重要な要素。 試走タイムがよく、Ｓ力のある選手が軽ハンデに
いたら要チェック。
２．独走力 先頭を走ったときの力量。独走力がある選手が先行すると、レースのペースが上がり後続車は抜きづらくなる。
３．追い込み力 後ろから前の選手を抜いていく力量。
４．雨巧拙 湿走路での力量。雨巧者。評価が高いほど、湿走路での連対率は高くなる。
５．コース 選手が走行するコース（イン、アウト、自在）。出場する選手構成をみて軽ハンデや中間ハンデにイン走法の
巧者がいると、重ハンデ選手が苦戦することもある。"""

S1 = """
青木 治親 4 3 3 5 イン 青山 周平 5 5 5 5 自在
秋田 貴弘 2 4 3 3 アウト 浅香 潤 4 4 3 3 アウト
阿久津正夫 3 1 1 1 イン 新井 恵匠 4 4 4 4 アウト
阿部 剛士 3 4 3 3 アウト 新井 淳 5 3 3 2 イン
五十嵐一夫 4 3 4 4 イン 新井 日和 4 4 2 2 アウト
池田 政和 4 5 5 2 自在 新井 裕貴 3 3 2 3 イン
石井 大志 2 3 2 3 アウト 荒川 哲也 3 3 2 2 アウト
石井 大輔 4 3 3 2 アウト 石川 岳彦 2 2 2 2 イン
泉田 修佑 4 4 3 4 イン 石川 哲也 3 5 3 2 アウト
伊東 玲衣 3 2 1 2 イン 伊藤 正司 3 3 3 2 イン
稲川 聖也 3 4 3 4 アウト 伊藤 正真 4 4 4 3 アウト
岩佐 常義 2 3 3 2 イン 伊藤 弘幸 3 2 2 4 アウト
岩田 裕臣 4 3 3 3 イン 伊藤 幸人 3 1 1 2 イン
牛沢 和彦 3 2 2 4 イン 猪熊 龍太 2 3 2 2 アウト
梅内 幹雄 2 3 3 4 アウト 岩田 行雄 4 3 3 3 イン
大木 光 4 4 4 4 イン 岩沼 靖郎 4 3 2 3 アウト
岡崎 秀二 3 1 1 2 イン 内越 忠徳 3 2 2 3 アウト
小椋 華恋 3 3 2 2 アウト 内山 高秀 4 4 4 3 自在
押田 幸夫 3 3 2 2 アウト 生方 将人 2 3 2 3 アウト
加賀谷建明 4 5 5 5 自在 大月 渉 3 3 3 3 イン
掛川 和人 4 4 3 3 アウト 押田 和也 3 3 3 3 アウト
影山 伸 3 4 4 4 アウト 小田雄一朗 1 3 2 1 アウト
片野 利沙 3 2 2 2 アウト 落合 淳 3 3 3 4 イン
金子 和裕 2 2 2 3 イン 笠原 三義 3 2 2 2 アウト
上和田拓海 4 4 3 3 イン 金山 周平 3 3 2 4 イン
川原 剛 2 3 3 2 イン 亀井 政和 3 3 2 2 アウト
君和田裕二 3 3 2 4 アウト 菅野 仁翔 3 4 2 3 アウト
木村 悦教 3 2 2 2 イン 北爪 勝義 3 3 2 2 イン
黒川 京介 5 5 4 4 自在 北渡瀬 充 3 3 2 3 アウト
高塚 義明 3 3 3 4 アウト 木部 匡作 3 2 2 2 アウト
小原 望 3 4 3 3 イン 木村 享平 2 4 2 2 アウト
小林 瑞季 4 4 4 4 自在 木村 義明 4 2 3 3 イン
斎藤 撤二 3 3 3 4 イン 清岡 優一 3 3 2 3 アウト
佐々木敏夫 3 2 2 2 イン 栗原 勝測 3 2 2 4 イン
佐藤 摩弥 5 4 4 4 自在 栗原 俊介 3 4 3 3 アウト
佐藤 裕二 4 4 5 3 イン 小林 晃 2 2 2 2 イン
佐藤 励 4 5 4 4 自在 佐久間健光 3 4 4 3 アウト
宍戸 繁 2 2 1 2 イン 桜井 晴光 3 4 3 3 アウト
篠崎 実 4 3 3 4 イン 猿谷 敦史 3 2 2 3 イン
柴山 信行 3 3 3 4 アウト 宍戸 幸雄 2 2 2 2 イン
島田 健一 2 2 2 3 イン 芝崎 茂信 3 2 3 3 イン
清水 雄平 2 2 2 2 アウト 渋沢 憲司 4 3 3 2 アウト
鈴木 清 4 3 4 3 イン 清水 卓 4 2 2 3 イン
相馬 康夫 2 4 2 4 アウト 白次 義孝 2 4 2 2 アウト
高石 光将 4 4 2 2 アウト 鈴木 幸治 3 3 2 4 アウト
高橋 祐一 3 2 2 2 アウト 鈴木 清市 3 3 3 3 イン
高橋 義弘 4 4 4 3 アウト 鈴木 聡太 3 4 3 2 アウト
田辺 誠 4 3 3 4 イン 鈴木 将光 3 4 4 4 イン
塚本 浩司 2 2 2 2 アウト 高橋絵莉子 5 3 2 4 イン
中野 憲人 3 4 4 3 イン 高橋 貢 5 5 5 5 自在
中村 雅人 4 5 5 5 自在 高橋 義徳 3 3 2 4 アウト
中山 透 2 5 4 5 アウト 滝沢 健 2 1 1 1 イン
中山 光 3 5 4 4 アウト 竹内 正浩 3 3 2 2 アウト
永井 大介 5 5 5 3 自在 竹島 繁夫 3 1 1 1 イン
縫田 雅一 2 2 1 2 アウト 竹本 修 3 3 2 2 アウト
信沢 綾乃 3 3 2 2 アウト 田崎 萌 3 4 2 2 アウト
長谷川 啓 3 2 2 4 イン 田中 賢 4 4 3 4 アウト
早津 康介 4 4 2 2 アウト 田中 哲 3 3 4 3 イン
早船 歩 4 4 3 3 イン 谷川 一貴 2 3 2 3 アウト
平川 博康 3 4 2 1 アウト 谷津 圭治 4 4 4 3 イン
平田 雅崇 4 5 5 4 イン 田村 治郎 4 4 4 4 イン
広瀬 勝光 4 3 2 4 アウト 千葉 泰将 3 3 2 1 アウト
深沢 隆 3 2 2 2 イン 塚越 浩之 3 3 3 3 イン
深谷 輝 3 4 3 4 アウト 戸塚 尚起 3 3 2 2 イン
福田 裕二 4 3 2 4 アウト 仲田恵一朗 3 4 3 3 アウト
福村 唯倫 3 3 3 3 イン 中野 光公 2 4 3 4 イン
古木 賢 4 3 2 4 アウト 中村 浩章 2 2 2 1 イン
本田 仁恵 3 3 2 4 アウト 西原 智昭 5 4 4 4 アウト
牧野 貴博 3 4 3 3 アウト 野沢 守弘 3 2 2 2 アウト
増田 伸一 3 3 2 5 アウト 野本 佳章 5 3 3 4 イン
松永 幸二 2 2 1 1 アウト 早川清太郎 4 5 5 3 イン
間中 大輔 3 3 3 4 イン 林 稔哲 3 3 2 3 アウト
丸山 浩信 3 2 2 2 イン 原田 富夫 2 2 1 1 イン
武藤 博臣 3 4 3 2 イン 深沢 悟 2 2 2 2 イン
森 且行 4 4 4 4 アウト 藤本 梨恵 3 3 2 3 アウト
森谷 隼人 4 4 3 4 アウト 保永 高男 3 2 2 2 アウト
谷島 俊行 3 3 2 4 イン 松村 真 2 2 2 1 アウト
山際 真介 4 4 3 4 アウト 松本 康 4 4 4 4 イン
山田 達也 3 5 5 4 アウト 松本 渉 2 2 1 2 イン
山田 徹 2 3 3 1 アウト 三浦 康平 4 4 4 3 イン
山田 真弘 4 4 4 3 アウト 森村 亮 3 4 3 3 アウト
吉田 幸司 5 3 2 1 アウト 矢内 昌木 4 3 2 2 イン
吉田 祐也 4 4 3 2 イン 山中 充智 2 3 2 1 アウト
若井 友和 3 4 5 5 イン 湯浅 浩 3 3 2 3 イン
渡辺 稔 3 2 2 2 イン 横田 翔紀 4 4 3 4 アウト
イン 吉田 恵輔 4 3 3 5 イン
イン 吉原 恭佑 5 4 4 4 イン
イン 米里 信秀 4 2 2 2 アウト
イン 渡辺 京二 2 2 2 1 イン
"""

S2 = """
青嶋 裕治 2 3 2 3 アウト 青山 文敏 3 3 2 3 イン
青島 正樹 4 4 4 4 イン 秋吉 忠幸 3 2 2 3 イン
赤堀 翼 3 3 2 2 アウト 阿部 仁志 4 3 3 4 イン
浅田 真吾 3 4 3 4 イン 荒尾 聡 5 4 4 5 イン
浅野 浩幸 3 3 2 1 アウト 有吉 辰也 5 4 4 5 自在
石貝 武之 4 3 2 2 アウト 石本 圭耶 4 3 3 2 アウト
伊藤 信夫 4 5 5 3 自在 稲原 瑞穂 2 2 1 2 アウト
今田 真輔 2 3 2 2 イン 井上 智詞 2 3 2 2 アウト
岩科 鮮太 3 4 4 4 イン 井村 淳一 3 3 4 3 イン
岩本 君男 3 2 1 3 アウト 岩見 貴史 5 4 4 4 自在
遠藤 誠 4 3 3 4 イン 岩元 毅 2 2 1 2 イン
岡谷美由紀 3 3 2 2 アウト 内山 雄介 3 3 3 3 イン
落合 巧 3 4 3 2 アウト 浦田 信輔 5 4 4 3 イン
笠木 美孝 4 4 3 4 イン 占部 健太 3 3 2 3 イン
片岡 信之 2 1 1 1 イン 大久保哲司 2 1 1 1 アウト
金子 大輔 4 5 5 5 自在 越智 尚寿 4 3 3 3 アウト
金田 悠伽 3 3 2 2 イン 片岡 賢児 4 2 2 2 アウト
上村 敏明 3 1 1 3 イン 鐘ケ江将平 4 4 3 4 アウト
木村 武之 5 5 5 4 自在 川口 裕司 3 4 3 3 イン
木村 直幸 3 2 2 2 イン 川端 孝 3 2 2 2 イン
栗原 佳祐 3 5 2 3 アウト 北原 岳哲 3 4 3 4 イン
小林 悠樹 3 3 3 1 アウト 城戸 徹 2 2 1 1 アウト
小林 頼介 2 2 2 2 アウト 木山 優輝 3 4 4 3 イン
斎藤 正悟 3 3 2 4 イン 小里 健太 2 2 2 3 アウト
斎藤 努 3 2 2 3 アウト 桜木 公和 3 3 4 4 イン
佐藤 貴也 5 4 5 5 イン 佐藤 裕児 3 3 2 3 アウト
佐藤 大地 4 4 3 3 アウト 篠原 睦 5 4 4 4 イン
柴田 健治 4 3 3 3 イン 新村 嘉之 3 3 2 4 アウト
柴田 紘志 2 3 3 4 アウト 高林 亮 3 4 2 3 アウト
下平 佳輝 4 2 2 4 イン 高宗 良次 4 4 3 4 アウト
城山 英文 2 1 1 2 イン 滝下 隼平 3 5 5 3 自在
鈴木 章夫 3 3 2 3 イン 竹谷 隆 4 4 3 5 アウト
鈴木 一馬 3 4 2 3 アウト 竹中 修二 3 2 2 2 イン
鈴木圭一郎 5 5 5 5 自在 田島 敏徳 2 3 2 3 アウト
鈴木 啓示 2 2 1 2 アウト 田中 茂 3 4 4 4 イン
鈴木 健吾 3 3 3 2 アウト 田中 進 3 5 3 3 アウト
鈴木 静二 4 3 3 3 イン 田中 輝義 3 3 3 4 アウト
鈴木 辰己 4 2 2 2 イン 田中 正樹 4 4 3 3 アウト
鈴木 宏和 5 5 4 3 イン 辻 大樹 4 4 3 4 アウト
関口 隆広 2 3 3 2 イン 道智 亮介 3 3 2 3 アウト
辰巳 裕樹 4 3 3 2 アウト 中尾 貴志 4 4 3 4 アウト
田中 竜二 3 1 1 3 アウト 中原 誠 3 3 2 2 アウト
筒井 健太 3 4 2 2 アウト 中村 杏亮 4 5 4 4 自在
角貝 拓海 3 2 1 1 アウト 中村 颯斗 3 4 2 2 アウト
戸塚 茂 3 2 1 2 アウト 長田 稚也 4 5 5 3 自在
仲口 武志 3 3 3 4 イン 西村 昭紀 2 3 1 3 アウト
中野 肇 1 1 1 3 アウト 丹村 司 3 4 3 3 アウト
中村 友和 3 4 4 2 アウト 根本 将人 3 3 3 3 イン
中村 晋典 3 3 2 2 アウト 花元 初美 2 2 2 2 イン
西 翔子 3 4 2 4 アウト 浜野 翼 1 3 1 4 アウト
西川 頼臣 2 3 2 2 アウト 東小野正道 4 3 3 3 イン
野上 史豪 2 2 1 4 アウト 久門 徹 5 3 3 3 アウト
野田 光宏 3 2 2 3 イン 藤川 幸宏 4 3 2 4 アウト
橋本 優一 3 2 2 2 イン 藤川 竜 4 3 2 3 アウト
橋本 陽介 2 1 1 1 イン 別府 敬剛 4 4 4 4 イン
長谷 晴久 2 3 3 3 アウト 帆景 岬 1 2 1 1 アウト
花田 一輝 3 4 3 2 アウト 牧瀬 嘉葵 3 4 4 4 アウト
早津 圭介 1 1 1 1 アウト 桝崎 陽介 3 4 3 4 イン
馬場 雄二 2 1 1 1 イン 町田 龍駿 3 3 2 3 アウト
兵頭 寛和 1 1 1 1 アウト 松尾 隆広 3 4 3 4 アウト
平塚 雅樹 4 3 2 4 イン 松尾 学 3 1 1 2 イン
広瀬 豪彦 2 2 1 3 アウト 水口 寿治 3 3 1 3 イン
深谷 俊太 3 4 3 2 アウト 水崎 正二 3 2 2 3 イン
藤波 直也 3 3 3 3 イン 水本 竜二 2 3 3 3 イン
牧野 竜人 1 2 1 1 アウト 宮地 朗 3 2 2 1 イン
交川 陽子 3 2 1 2 アウト 村瀬月乃丞 2 4 2 3 アウト
桝崎 星名 4 2 1 2 アウト 室田 泰利 3 3 1 3 アウト
松山 茂靖 4 4 3 3 アウト 本門 延唯 3 2 1 2 イン
山浦 博幸 3 4 3 2 アウト 森本 優佑 3 3 4 4 イン
山脇 孝志 2 3 2 1 アウト 吉川 麻季 2 2 1 2 アウト
吉田 富重 1 1 1 2 イン 吉松 優輝 4 4 2 2 アウト
吉林 直都 2 4 2 2 アウト 佳元 光義 3 3 2 2 アウト
米里 崇徳 4 4 3 3 アウト イン
渡辺 篤 4 4 3 3 アウト イン
和田 健吾 3 3 3 2 アウト 
"""

S3 = """
青木 隆浩 3 3 2 3 アウト
穴見 和正 3 3 3 4 イン
安東 久隆 3 2 2 2 イン
池浦 一博 3 2 2 3 イン
池田 康範 4 2 2 3 イン
石田 啓貴 2 3 2 2 アウト
石橋 大 3 2 2 2 イン
磯部 真樹 2 3 2 1 アウト
稲原良太郎 3 3 2 1 イン
岩崎 亮一 4 4 4 4 自在
岩永 清文 1 2 3 2 イン
畦坪 孝雄 2 2 2 1 アウト
岡部 聡 3 4 4 4 イン
岡松 忠 4 3 3 2 イン
岡本 信一 2 2 1 2 イン
緒方 浩一 4 4 2 4 アウト
小栗 勝太 4 3 2 2 アウト
古城龍之介 4 4 3 3 アウト
五所 淳 4 3 3 4 イン
斎藤 隆充 3 3 2 3 イン
佐伯 拓実 2 3 1 1 アウト
佐々木 啓 3 4 4 4 自在
重富 英雄 3 3 2 1 アウト
杉本 雅彦 2 2 2 1 イン
祐定 響 1 1 1 1 アウト
角南 一如 3 5 5 4 アウト
角 翔太郎 4 4 3 2 アウト
高木健太郎 2 3 3 3 アウト
田方 秀和 3 2 2 4 イン
竹中 一成 2 3 2 2 アウト
田斎 英世 3 2 1 2 アウト
中野 政則 2 3 3 3 アウト
永島潤太郎 3 4 3 4 アウト
長田 恭徳 3 4 4 3 アウト
西久保英幸 3 1 1 2 イン
西崎洋一郎 3 2 1 3 イン
西村 義正 3 2 2 2 イン
西村龍太郎 4 3 3 4 イン
丹村 飛竜 5 5 4 4 自在
浜田 忠司 1 1 1 2 イン
浜野 淳 4 4 4 3 自在
林 弘明 3 3 3 4 イン
原 菊太郎 1 1 1 1 アウト
春本 綾斗 3 3 3 2 イン
番田 隆弘 3 3 2 4 アウト
人見 剛志 3 4 3 2 自在
日室 志郎 3 3 2 2 イン
福田 義久 3 2 1 2 イン
福永 貴史 2 4 4 4 イン
藤岡 一樹 4 4 4 4 アウト
藤本 剛 2 2 2 2 アウト
古谷 匠 1 1 1 1 アウト
別府 末彦 3 1 1 3 イン
前田 淳 4 4 3 3 イン
松井 大和 3 3 2 2 アウト
松尾 彩 3 4 3 2 アウト
松尾 啓史 4 5 5 4 自在
松生 信二 3 3 2 3 アウト
丸山 智史 4 4 4 3 自在
満村 陽司 3 3 2 2 アウト
三宅 真央 1 1 1 1 アウト
森園 数敏 2 1 1 1 イン
矢野 正剛 3 3 2 2 アウト
山崎 進 3 3 3 3 アウト
山下 知秀 3 2 2 2 アウト
山本 翔 4 4 3 4 アウト
山本 智大 3 2 2 4 イン
山本 将之 4 4 3 4 アウト
吉松 憲治 2 3 3 2 アウト
"""

next_data = ['イン', 'アウト', '自在']
S1_list = S1.split()
S2_list = S2.split()
S3_list = S3.split()
kawaguchi = []
isezaki = []
hamamatsu = []
iizuka = []
sanyo = []

# 川口、伊勢崎
kawaguchi_flag = 1
for s in S1_list:
    if s in next_data:
        kawaguchi_flag ^= 1
    if kawaguchi_flag:
        kawaguchi.append(s)
    else:
        isezaki.append(s)

# 浜松、飯塚
hama_flag = 1
for s in S2_list:
    if s in next_data:
        hama_flag ^= 1
    if hama_flag:
        hamamatsu.append(s)
    else:
        iizuka.append(s)

# 山陽
for s in S3_list:
    sanyo.append(s)

kawa_text = ''.join(kawaguchi)
ise_text = ''.join(isezaki)
hama_text = ''.join(hamamatsu)
ii_text = ''.join(iizuka)
san_text = ''.join(sanyo)

import pandas as pd

def string_data_to_csv(kawa_text, csv_name):
    dod_data = ['ン', 'ト', '在']
    kawaguchi = []
    count = 0
    for kawa in kawa_text:
        if kawa.isdecimal() or kawa in next_data:
            kawaguchi.append(',')
            count += 1
        kawaguchi.append(kawa)
        if count == 4:
            kawaguchi.append(',')
            count = 0
        if kawa in dod_data:
            kawaguchi.append(',')

    kawaguchi = ''.join(kawaguchi).split(',')
    kawaguchi_dict = {}
    flag = True
    for kawa in kawaguchi:
        if flag:
            flag = False
            name = kawa
            kawaguchi_dict[name] = []
        else:
            if kawa.isdecimal():
                kawa = int(kawa)
            kawaguchi_dict[name].append(kawa)
        if kawa in next_data:
            flag = True

    kawaguchi_dict.pop('イン', None)
    kawaguchi_dict.pop('アウト', None)
    kawaguchi_dict.pop('自在', None)
    kawaguchi_dict.pop('', None)

    kawaguchi = pd.DataFrame(kawaguchi_dict)
    kawaguchi = kawaguchi.transpose()
    kawaguchi.to_csv(csv_name + '.csv')

data_name = [(kawa_text, 'kawaguchi'), (ise_text, 'isezaki'), (hama_text, 'hamamatsu'), (ii_text, 'iizuka'), (san_text, 'sanyo')]
for data, name in data_name:
    string_data_to_csv(data, name)
