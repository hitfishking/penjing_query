db配置/连通-->model定义--> [view定义 | url定义] --> template定义
-------------------
for i in Magazine.objects(year='2011'):
  for j in i.dir:
    print j.article_name
-------------------
[假障碍]
1）MongoEngine connect() db位置很重要；可能MongoEngine受到Django框架的影响；
2）docker stop失灵，重启host；
3）{% url 'query_dir' %}多层引号嵌套不合规；
