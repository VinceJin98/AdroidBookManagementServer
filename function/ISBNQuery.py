# -*- coding:utf-8 -*-  

import urllib.request, sys,os, json,codecs
import ssl,yaml,traceback


def ISBNQuery(ISBNCode):
    
    if not ISBNCode:
        traceback.print_stack()
        return 

    FileAbsPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\config\\IsbnConfig.yaml'

    IsbnConfig = {}
    with open(FileAbsPath,'r') as f:
        IsbnConfig = yaml.load(f.read(),Loader=yaml.FullLoader)
    f.close()

    url = IsbnConfig['host'] + IsbnConfig['path'] + '?sub=' +ISBNCode + '&key=' + IsbnConfig['appkey']
    request = urllib.request.Request(url)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request,context=ctx)
    #转化为json
    reader = codecs.getreader("utf-8")
    writer = codecs.getwriter("utf-8")
    json_result = json.load(writer(reader(response)))
    #返回查询结果
    return json_result['result']
    
if __name__ == "__main__":
    ISBNCode = '9787302512608'
    print(ISBNQuery(ISBNCode))
    pass
