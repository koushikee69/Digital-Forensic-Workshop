import argparse as ap
import  os
import subprocess as sp

parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("toolName",type=str,help="tool required!!")
parser.add_argument("inputDirectory",type=str,help="input directory required!!")
parser.add_argument("outputDirectory",type=str,help="output directory required!!")
parser.add_argument("configFile",type=str,help="configFile required!!")

args=parser.parse_args()


def foremost():
    result=sp.run(["sudo",args.toolName,"-i",f"{args.inputDirectory}","-o",f"{args.outputDirectory}","-c",f"{args.configFile}"],stdout=sp.PIPE,stderr=sp.PIPE)
    print(f"The device or image located at {args.inputDirectory} has been recovered using {args.toolName}")
    
def scalpel():
    result=sp.run(["sudo",args.toolName,"-o",f"{args.outputDirectory}",f"{args.inputDirectory}","-c",f"{args.configFile}"],stdout=sp.PIPE,stderr=sp.PIPE)
    print(f"The device or image located at {args.inputDirectory} has been recovered using {args.toolName}")



if args.toolName=="foremost" or args.toolName=="scalpel":
    if args.toolName=="foremost":
        foremost()
    else:
        scalpel()    
else:
   print("Invalid input")
    
        


