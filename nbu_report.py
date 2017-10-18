#-*- coding: utf-8 -*-
import get_now_nbudata
import send_tocaro
from data_vars import server,username,password,url_id


if __name__ == '__main__':
	
	gnn = get_now_nbudata
	st  = send_tocaro
	print(server)
	print(username)
	print(password)
	print(url_id)

	# Delayed policy name.
	# TIPS: We will replace this code.
	#       get from triggered delay notice alert mail.
	policy = "iv11-sys000-vdk-003"

	# Get NBU Server data
	stdout = gnn.get_now_nbudata(server,username,password,policy)
	message = "JOBID TYPE STAT CLIENT POLICY STARTED ENDED ELAPSED\n"
	for o in stdout:
		message = message + o
	
	# Send message for tocaro
	st.send_tocaro(url_id,policy,message)
