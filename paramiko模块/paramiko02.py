# 使用paramiko模块远程执行命令，获取执行后的结果进行处理

# 使用paramiko传密码远程操作
import paramiko

# ssh = paramiko.SSHClient()			# 创建一个客户端连接实例
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 加了这一句,如果第一次ssh连接要你输入yes,也不用输入了
# ssh.connect(hostname="10.1.1.12", port=22, username="root", password="123456")  # 指定连接的ip,port,username,password
#
# stdin,stdout,stderr = ssh.exec_command("touch /tmp/123")   # 执行一个命令,有标准输入,输出和错误输出
#
#
# cor_res = stdout.read()		# 标准输出赋值
# err_res = stderr.read()		# 错误输出赋值
#
# print(cor_res.decode())	# 网络传输是二进制需要decode(我们没有讨论socket编程，所以你就直接这样做)
# print(err_res.decode())	# 不管正确的还是错误的输出,都打印出来
#
# ssh.close()				# 关闭此连接实例


# 使用paramiko空密码密钥远程登录操作
# 需要提前做好免密登录
ssh = paramiko.SSHClient()			# 创建一个客户端连接实例

private_key = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")  # 指定本机私钥路径

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 加了这一句,如果第一次ssh连接要你输入yes,也不用输入了

ssh.connect(hostname="10.1.1.12",port=22,username="root",pkey=private_key)	# 把password=123456换成pkey=private_key

stdin,stdout,stderr = ssh.exec_command("touch /tmp/321")

cor_res = stdout.read()
err_res = stderr.read()

print(cor_res.decode())
print(err_res.decode())

ssh.close()





