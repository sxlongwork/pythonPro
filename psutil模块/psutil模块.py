'''
psutil模块是一个跨平台库，可以实现获取系统运行的进程和系统利用率（CPU,内存，磁盘，网络等）信息
它主要用于系统监控，分析和限制系统资源及进程的管理

安装模块：pip3.6 install psutil
'''

import psutil
# cpu
print(psutil.cpu_times())			# 查看cpu状态,类型为tuple
print(psutil.cpu_count())			# 查看cpu核数,类型为int

# memory(内存)
print(psutil.virtual_memory())		# 查看内存状态,类型为tuple
print(psutil.swap_memory())			# 查看swap状态,类型为tuple

# partition(分区)
print(psutil.disk_partitions())		# 查看所有分区的信息,类型为list,内部为tuple
print(psutil.disk_usage("/"))		# 查看/分区的信息，类型为tuple
print(psutil.disk_usage("/boot"))	# 查看/boot分区的信息，类型为tuple

# io(磁盘读写)
print(psutil.disk_io_counters())	# 查看所有的io信息（read,write等)，类型为tuple
print(psutil.disk_io_counters(perdisk=True)) # 查看每一个分区的io信息，类型为dict,内部为tuple

# network(网络)
print(psutil.net_io_counters())		# 查看所有网卡的总信息(发包，收包等)，类型为tuple
print(psutil.net_io_counters(pernic=True))	# 查看每一个网卡的信息，类型为dict,内部为tuple

# process(进程)
print(psutil.pids())				# 查看系统上所有进程pid，类型为list
print(psutil.pid_exists(1))			# 判断pid是否存在，类型为bool
print(psutil.Process(1))			# 查看进程的相关信息,类型为tuple

# user(用户)
print(psutil.users())				# 查看当前登录用户相关信息，类型为list
