1) pjquery项目框架，是用django-admin startapp/startproject 命令构建的；
   注意：  startproject是创建项目；startapp是创建app；先建立项目再建立app，一个项目中可以有多个app；
   django中，一个项目(project)中可以安装/开发多个应用(app);
2) django项目默认包含migrations/static/templates等目录；
3) templates目录下，还可以建立子目录，管理不同子项目的页面；
4) 页面template有3个版本：
   a) index.html, index_1.html; 是bootstrap默认table方案；
   b) index_2.html; 是bootstrap-table.js JQuery插件方案；
   c) index_0.html; 是无表格，纯测试页面；
5) 启动django开发服务器：python manage.py runserver 127.0.0.1:8888
6) 启动服务器之前，还应该运行migrate，即：python manage.py migrate
7) Class-based view 和 function-based view可以混合使用；