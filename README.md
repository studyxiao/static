## 文件管理

简单的文件上传和下载。

指定文件名（访问名）和文件，即可通过url下载文件。
如果文件名重复，则会覆盖掉原来的文件链接（文件还是在服务器上）。

## 部署

1. 在项目目录下新建.env文件，写入用户名和密码，简单的项目不存在用户管理，就没有在数据库中存储用户名密码。
```
USERNAME=username
PASSWORD=password
```

2. 修改uwsgi.ini

base = 实际项目目录

3. 修改 static_nginx.conf

server unix:///home/path/static/static.sock;  // 真实路径
server_name: 指定域名;

4. 创建虚拟环境

```bash
python3 -m venv venv
```
*第二个venv指定虚拟环境未当前路径下的venv文件夹，对应uwsgi.ini文件中的home值*

```bash
source venv/bin/activate  # 激活当前虚拟环境
pip install -r requirements.txt

flask db upgrade
```

5. 启动



```bash
# 软链接到nginx
sudo ln -s /home/path/static/static_nginx.conf /etc/nginx/sites-enabled/
# 启动uwsgi
uwsgi -i uwsgi.ini
```

现在访问域名应该就能看到网页了。
