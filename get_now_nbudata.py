# -*- coding:utf-8 -*-
import paramiko
import sys

def get_now_nbudata(policy):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("take-nbudev", 22, username="root", password="oldmind")

	stdin, stdout, stderr = ssh.exec_command('/usr/openv/netbackup/bin/admincmd/bpdbjobs | grep %s' % policy)
	return stdout

if __name__ == '__main__':

	argvs = sys.argv
	stdout = get_now_nbudata(argvs[1])

	message = ""
	for o in stdout:
		message = message + o
	print(message)

