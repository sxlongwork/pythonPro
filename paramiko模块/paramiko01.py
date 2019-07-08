# paramiko模块支持以加密和认证的方式连接远程服务器。可以实现远程文件的上传,下载或通过**==ssh==**远程执行命令。

# 安装： pip3.6 install paramiko


# paramiko模块远程上传下载文件
import paramiko								# 导入import模块

# trans = paramiko.Transport(("10.1.1.12",22))	# 产生连接10.1.1.12的22的传输,赋值给trans
#
# trans.connect(username="root",password="123456") # 指定连接用户名与密码
#
# sftp = paramiko.SFTPClient.from_transport(trans) # 指定为sftp传输方式
#
# sftp.get("/etc/fstab","/tmp/fstab")	    # 把对方机器的/etc/fstab下载到本地为/tmp/fstab(注意不能只写/tmp,必须要命名)
# sftp.put("/etc/inittab","/tmp/inittab") # 本地的上传,也一样要命令
#
# trans.close()


# paramiko模块实现文件的上传下载(免密登录)
# 需要提前做好免密登录(ssh-keygen,ssh-copy-id xx)

trans = paramiko.Transport(("10.1.1.12",22))	# 产生连接10.1.1.12的22的传输,赋值给trans

private_key = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa") # 指定本机私钥路径

trans.connect(username="root",pkey=private_key)		# 提前使用ssh-keygen做好免密登录

sftp = paramiko.SFTPClient.from_transport(trans)

sftp.get("/etc/fstab","/tmp/fstab2")
sftp.put("/etc/inittab","/tmp/inittab2")

trans.close()



