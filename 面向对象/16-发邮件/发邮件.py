# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText

# SMTP服务器
SMTPServer = "smtp.sina.com"

# 发邮件的地址
Sender = "sxlong_work@sina.com"

# 发送者邮箱密码(不是登录密码，是授权密码)
passwd = "sxl19911222!"


# 设置发送内容
message = "life is short, you need python."
# 转换为邮件文本
msg = MIMEText(message)

# 邮件主题
msg["Subject"] = "from python"

# 发送者
msg["From"] = Sender


# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
# 登录邮箱
mailServer.login(Sender, passwd)
# 发送邮件
# "244086420@qq.com", "706943518@qq.com"
mailServer.sendmail(Sender, ["403726815@qq.com",],
                    msg.as_string())

# 退出邮箱
mailServer.quit()

