import random #随机数生成模块
from playsound import playsound #声音播放模块
from time import sleep #延时模块
食材 = ('粑粑','扒鸭屁股','奥利给','白菜',\
        '臭豆腐','臭卤虾','葱','大地瓜','大辣椒',\
            '俘虏','嘎嘣脆','哈密瓜','胡罗贝',\
                '黄瓜丝','火鸡面','火龙果','加柠檬','老干妈'\
                    ,'馒头','米肠','米饭','蒜','香蕉')
sound = ('baba','paya','aoligei','baicai',\
    'choudoufu','chouluxia','cong','dadigua','dalajiao',\
        'furu','gabengcui','hamigua','huluobei',\
            'huangguasi','huojimian','huolongguo','jianingmeng','laoganma',\
                'mantou','michang','mifan','suan','xiangjiao','ou','xingbuxing','yirisancan','jishihui')
def play(x):
    playin = sound[x]
    playsound('deta\sound\\' + playin + '.mp3')
while True:
    print ('一日三餐没烦恼，今天就吃老八秘制小汉堡，既实惠，还管饱')
    play(-2);play(-1)
    eat = []
    big = 0
    while True:
        inputx = input('输入食材或完成>>>')
        if inputx == '完成':
            break
        eat.append(inputx)
        if inputx in 食材:
            play(食材.index(inputx))
        if len(inputx) * 3 > big:
            big = len(inputx) * 3
    hum_high = len(eat)+1
    for now_high in range(0,hum_high):
        sleep(0.5)
        print('\n' * 20)
        print(('     ') + ('_' * big),'\n',('   /') + ('_' * big) + ('\\'))
        for t in range(0,now_high):
            h = random.randint(3,big)
            print((' ' * h) + ('['+eat[t]+']'))
        print(('    ') + ('-' * big),'\n',('  |') + ('_' * big) + ('|'))
    play(-3)
    if '粑粑' in eat:
        play(-4)
    off = input('回车再次制作，或输入其他退出')
    if off != '':
        break
