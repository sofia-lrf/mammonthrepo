from django.http import HttpResponse, JsonResponse, HttpRequest

def t1(request:HttpRequest): # 视图函数
    # env -> request __call__
    print(request.method)
    return HttpResponse("function view test") # 内部有默认的响应的header，好处是可以聚焦在正文的生成上

# 动态网页技术
content = """
<html>
<head><title></title></head>
<body>
    我是一个网页吗？我在磁盘上吗
</body>
</html>
"""

def t2(request): # 动态生成网页
    return HttpResponse(content)


def t3(request): # 静态网页，通过Python代码读取的，需要解析器，速度慢；nginx
    with open('test.html', 'rb') as f:
        return HttpResponse(f.read())

def t4(request):
    output = ''
    with open('templete.html', 'rt', encoding='utf-8') as f:
        for line in f:
            output += line.replace("<>", "我就是需要被替换的内容,可能从数据库中来")
        return HttpResponse(output)

def t5(request): # 返回内容json
    # content = [1, 2, 3]
    content = {'ids':[1,2,3,4]}
    # return JsonResponse(content, safe=False) # content-type: application/json
    return JsonResponse(content)








