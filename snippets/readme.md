安装：
有点奇葩，模块名为rest_framework,但是安装时是djangorestframework
pip install djangorestframework==3.3.1  
同步数据库 
django 1.9之前：python manage.py syncdb
django 1.9指后：python manage.py makemigrations、python manage.py migrate
#Step 1
**序列化**
snippet = Snippet(code='foo = "bar"\n')
serializer = SnippetSerializer(snippet)
serializer.data

序列化为json:
content = JSONRenderer().render(serializer.data)
content

**反序列化**
import io
stream = io.BytesIO(content)  
data = JSONParser().parse(stream)  
serializer = SnippetSerializer(data=data)  
serializer.is_valid()  
serializer.validated_data  
serializer.save()  
通过many=True查询一个集合  
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data


**使用ModelSerializers**
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))  打印所有字段


#遇到的错误
'Options' object has no attribute 'get_all_related_objects'：
pip install -U djangorestframework 即可
