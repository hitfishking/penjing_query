[Djang项目开发模式]
(settings) -- >[db配置/连通  |  model定义] --> [view定义 | url定义] --> template定义；
即 V<--C<--M，从右至左，三大步；  settings是第0步；
-------------------
for i in Magazine.objects(year='2011'):
  for j in i.dir:
    print j.article_name
-------------------
[假障碍]
1）MongoEngine connect() db位置很重要；可能MongoEngine受到Django框架的影响；
2）docker stop失灵，重启host；
3）{% url 'query_dir' %}多层引号嵌套不合规；
4）Class-based view中的自定义函数，不能直接通过urls引用；需要使用mixin；
   如果类内所有函数全都可以通过urls访问，一方面和function-based view没了区别，破坏了类的封装性；
   另一方面，类内函数通常要处理类内变量，外部若随便访问这些函数，有可能造成这些类内变量的不一致性；
   故，应该充分利用面向对象思想，对外只区分get()，post()，在其内部做dispatch()；
5）
-------------------
[index_**.html的几个版本]
1）index_old.html: 最初没有使用任何web框架的裸view；
2）index.html：使用bootstrap样式框架的table；
3）index2.html：使用bootstrap-table plugin;
-------------------
[pagination的算法要点]
SESSION, GET，两份inputwords;
输入合法性检查：inputwords不能为空；
大部分情况都不用重查数据库，只有少量情况，如下(重查条件自然语言表达式)：
   第1页 + [新运行(session无此key) | 新单词(与已有词不同的新词)] ；
------------------
[remote debugging设置要点]
在pycharm端设置Python Remote Debug,设置路径映射；
在code中添加import pydevd语句，用于服务器连接到客户端用；
remote debugging的总体设置思想是较为明确的；但具体使用流程，可以多样化，根据开发的问题场景变化而变化；
------------------
[docker运行模式]
docker模式；
docker-compose模式；
二者应该没有本质区别，但为什么pycharm不能设置远程docker-compose，目前仍未知；
故，只能使用docker模式，启动远程的djangocompose_web镜像容器；
docker config的结果是：
docker run -p 0.0.0.0:8000:8000 -v /home/dongz/progdata/penjing_query:/code --name penjing_query_1 djangocompose_web:latest python3 manage.py runserver 0.0.0.0:8000
------------------




