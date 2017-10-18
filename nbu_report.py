#-*- coding: utf-8 -*-
import get_now_nbudata
import send_tocaro


if __name__ == '__main__':
	gnn = get_now_nbudata
	st  = send_tocaro

	# Delayed policy name.
	# TIPS: We will replace this code.
	#       get from triggered delay notice alert mail.
	policy = "iv11-sys000-vdk-003"

	# Get NBU Server data
	stdout = gnn.get_now_nbudata(policy)
	message = ""
	for o in stdout:
		message = message + o
	
	# Send message for tocaro
	st.send_tocaro("9ulhvcjkc8iux8cec8twdiicxxn56hjz",policy,message)
