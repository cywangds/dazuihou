
import paramiko

# 添加公钥密钥文件
private_key = paramiko.RSAKey.from_private_key_file('C:/Users/Administrator/Desktop/linuxyr')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='jump.jimijiayuan.cn', port=28239, username='wangchaoyue',pkey=private_key)
# 执行命令
# 执行多条命令时需要将各个命令用‘；’隔开，最后将get_pty设为True；如果是单条命令的则只传入命令即可
stdin, stdout, stderr = ssh.exec_command('cd dw/2020-06-02/;ls',get_pty=True)
# 多条命令的话会将执行结果一起返回，所以建议遍历打印。也可以直接打印：print(stdout.read().decode('utf-8'))
files = stdout.readlines()
for i in files:
    # 打印执行反馈结果
    print(i.encode().decode('utf-8').split()[0])
# 打印报错信息
print(stderr.read().decode('utf-8'))
# 关闭连接