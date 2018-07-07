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
index_old.html: 最初没有使用任何web框架的裸view；
index.html：使用bootstrap样式框架的table；
