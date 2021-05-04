
from rpc import *
# import rpc

port = '127.0.0.1'
host = 9999

# robj = rpccopy.rpc(port,host)
robj = rpc_connect(port,host)

# res = robj.add(11,2)
# print("\nresult of addition is "+str(res))

res = robj.pratik(20,2)
print("\nresult of pratik is "+str(res))

# res = robj.mul(11,2)
# print("\n",res)

# res = robj.mul(9,9)
# print("\n",res)

# msg = 'anchal'
# res = robj.concat(msg)
# print("\n",res)

# msg = 'anchal'
# res = robj.sen(msg)
# print("\n",res)

# msg = 'varun'
# res = robj.sen(msg)
# print("\n",res)

# msg = 'utkarsh mk'
# res = robj.sen(msg)
# print("\n",res)

# msg = 'testing'
# res = robj.sen2(msg)
# print("\n",res)

# res = robj.newfunc(4)
# print("\n",res)

print()
robj.close_conn()
