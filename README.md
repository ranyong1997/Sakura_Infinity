<div align="center">
<br/>
<br/>
<img src="static/assets/images/realm.svg" width="auto" style="margin-top:30px;"/>
  <h1 align="center">
    Skura_Infinity
  </h1>
  <h4 align="center">
    Sakura🌸后台管理
  </h4> 

  [预 览](http://layui.pearadmin.com)    
</div>

<div align="center">

[![Django CI](https://github.com/liangliangyy/DjangoBlog/actions/workflows/django.yml/badge.svg)](https://github.com/liangliangyy/DjangoBlog/actions/workflows/django.yml) [![CodeQL](https://github.com/liangliangyy/DjangoBlog/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/liangliangyy/DjangoBlog/actions/workflows/codeql-analysis.yml) [![codecov](https://codecov.io/gh/liangliangyy/DjangoBlog/branch/master/graph/badge.svg)](https://codecov.io/gh/liangliangyy/DjangoBlog)  [![license](https://img.shields.io/github/license/liangliangyy/djangoblog.svg)]() [![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)

>基于`python3.10`和`Django3.2.5`开发。

</div>
特别鸣谢:[hanwenlu2016](https://github.com/hanwenlu2016)给予帮助

## 已完成功能
- [x] 项目初始化创建
- [x] 创建数据库表
- [x] 迁移数据都到服务器
- [x] 登录页面

## 安装
```git
1 -- 下载
git clone https://github.com/ranyong1997/Sakura_Infinity.git

2 -- 安装
使用pip安装： `pip install -r requirements.txt`
清华镜像源安装：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

3 -- 修改数据库链接创建数据库
在Sakura_Infinity/settings.py中修改DATABASES里的
['NAME']['USER']['PASSWORD']['HOST']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名字',
        'USER': '数据库用户名',
        'PASSWORD': '数据库密码',
        'HOST': '数据库地址',  # 默认 localhost
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8'}
    }
}

4 --执行迁移
python manage.py makemigrations
python manage.py migrate

5 -- 创建用户
python manage.py createsuperuser

6 -- 运行
python manage.py runserver
```
## 效果 
> 数据库建表预览：
![image-20220321235727915](https://gitee.com/ran_yong/mark-down-table-upload/raw/824fecdcc123da03f632ad05d4795b812d98b407/img/image-20220321235727915.png)

> 登录页面：
![image-20220326112909886](https://gitee.com/ran_yong/mark-down-table-upload/raw/824fecdcc123da03f632ad05d4795b812d98b407/img/image-20220326112909886.png)



## 参考文献
- 【日志配置】：https://blog.csdn.net/weixin_37590093/article/details/81536372
- 【检测是否登录】：https://www.cnblogs.com/liuxuelin/p/14585677.html
- 【AES加密、解密】：https://www.cnblogs.com/namejmj/p/14747491.html
- 【FTP下载】：https://www.jianshu.com/p/055bbe9a2e7d
- 【Simple UI】：https://simpleui.72wo.com/docs/simpleui/
- 【分页】：https://blog.csdn.net/weixin_44633951/article/details/104300894
- 【BootStrap3】：https://v3.bootcss.com/
- 【bootstrap-datetimepicker】：https://getdatepicker.com/4/
- 【ajax跨域】：https://www.cnblogs.com/huangdabing/p/9249216.html
- 【漏洞扫描】：https://github.com/jeremylong/DependencyCheck
