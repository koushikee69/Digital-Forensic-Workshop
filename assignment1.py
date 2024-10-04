import sys
import subprocess
path1=sys.argv[1]
path2=sys.argv[2]
hash=sys.argv[3]
r1=subprocess.run([hash, path1], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
r2=subprocess.run([hash, path2], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
if r1.stdout.split()[0]==r2.stdout.split()[0]:
	print("Same")
else:
	print("Not same")
