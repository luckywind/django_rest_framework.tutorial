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