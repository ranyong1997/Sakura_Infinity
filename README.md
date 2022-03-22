# Sakura🌸后台管理
[![Django CI](https://github.com/liangliangyy/DjangoBlog/actions/workflows/django.yml/badge.svg)](https://github.com/liangliangyy/DjangoBlog/actions/workflows/django.yml) [![CodeQL](https://github.com/liangliangyy/DjangoBlog/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/liangliangyy/DjangoBlog/actions/workflows/codeql-analysis.yml) [![codecov](https://codecov.io/gh/liangliangyy/DjangoBlog/branch/master/graph/badge.svg)](https://codecov.io/gh/liangliangyy/DjangoBlog)  [![license](https://img.shields.io/github/license/liangliangyy/djangoblog.svg)]()  

>基于`python3.10`和`Django3.2.5`开发。

## 已完成功能
- [x] 项目初始化创建
- [x] 创建数据库表
- [x] 迁移数据都到服务器
- [ ] 前端页面

## 安装
```git
1 -- 下载
git clone https://github.com/ranyong1997/Sakura_Infinity.git

2 -- 安装
使用pip安装： `pip install -r requirements.txt`
清华镜像源安装：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

3 -- 修改数据库链接创建数据库


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

![image-20220321235727915](https://gitee.com/ran_yong/mark-down-table-upload/raw/master/img/image-20220321235727915.png)


## 参考文献
- 【日志配置】：https://blog.csdn.net/weixin_37590093/article/details/81536372
- 【检测是否登录】：https://www.cnblogs.com/liuxuelin/p/14585677.html
- 【AES加密、解密】：https://www.cnblogs.com/namejmj/p/14747491.html
- 【FTP下载】：https://www.jianshu.com/p/055bbe9a2e7d