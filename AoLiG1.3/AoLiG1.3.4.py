import random
from playsound import playsound
from time import sleep
食材 = ['粑粑','扒鸭屁股','奥利给','白菜',\
        '臭豆腐','臭卤虾','葱','大地瓜','大辣椒',\
            '俘虏','嘎嘣脆','哈密瓜','胡罗贝',\
                '黄瓜丝','火鸡面','火龙果','加柠檬','老干妈'\
                    ,'馒头','米肠','米饭','蒜','香蕉']
print ('支持语音的食材：',食材)
音频目录 = ['baba','paya','aoligei','baicai',\
    'choudoufu','chouluxia','cong','dadigua','dalajiao',\
        'furu','gabengcui','hamigua','huluobei',\
            'huangguasi','huojimian','huolongguo','jianingmeng','laoganma',\
                'mantou','michang','mifan','suan','xiangjiao']
while 1:
    print ('一日三餐没烦恼，今天就吃老八秘制小汉堡，既实惠，还管饱')
    playsound('deta\sound\yirisancan.mp3')
    playsound('deta\sound\jishihui.mp3')
    time = 0
    x = 5
    y = 0
    lbwnb = []
    while 1:
        a = input('输入食材或完成>>>')
        if a == '完成':
            break
        if a in 食材:
            目录 = 食材.index(a)
            url = 音频目录[目录]
            playsound('deta\sound\\' + url + '.mp3')
        if (len(a) > x):
            x = (len(a) * 3)
        lbwnb.append(a)
        time += 1
        y += 1
    print (('     ') + ('_' * x),'\n',('   /') + ('_' * x) + ('\\'))
    for i in range(0,y):
        p = random.randint(3,x)
        print (' ' * p + '['+lbwnb[i] + ']')
    print (('    ') + ('-' * x),'\n',('  |') + ('_' * x) + ('|'))
    print ('你看这汉堡做滴彳亍不彳亍')
    playsound('deta\sound\\xingbuxing.mp3')
    if '粑粑' in lbwnb:
        print ('老八的评价：呕呕呕  呕 呕呕')
        playsound('deta\sound\ou.mp3')
    b = input('再次制作?  [是] [否] \n>>>')
    if b == '否':
        break
    elif b != '是':
        print ('错误，即将退出')
        sleep (3)
        break
