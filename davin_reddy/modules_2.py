import sys

def main():
    # print( " Python v is {}.{}.{}.{}".format(*sys.version_info))
    # print(sys.platform)
    # import os
    # print(os.getenv('PATH'))
    # print( os.name)
    # print(os.getcwd())
    # print(os.urandom(25))

    import urllib.request
    page=urllib.request.urlopen('https://www.parsonline.com/')   
    print(page)

    # for line in page:
    #     print(str(line,encoding='utf-8'),end='***')
    import random
    x=list(range(0,15))
    print(x)
    random.shuffle(x)
    print(x)
    import datetime
    now=datetime.datetime.now()
    print(now)
    print(x,now.year,now.month,now.day,now.hour,now.minute,now.second,sep="***",end="###\n")
if __name__=="__main__":main()