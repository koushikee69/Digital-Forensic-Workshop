import argparse as ap
import  os
import subprocess as sp

parser=ap.ArgumentParser(description="sample argument")
parser.add_argument("toolName",type=str,help="tool required!!")
parser.add_argument("inputDirectory",type=str,help="input directory required!!")
parser.add_argument("outputDirectory",type=str,help="output directory required!!")
parser.add_argument("configFile",type=str,help="configFile required!!")

args=parser.parse_args()

def magicrescue(recipeType):
    os.mkdir(f"{args.outputDirectory}")
    
    result=sp.run(["sudo",args.toolName,"-r",f"{recipeType}","-d",f"{args.outputDirectory}",f"{args.inputDirectory}"],stdout=sp.PIPE,stderr=sp.PIPE)
    print(f"The device or image located at {args.inputDirectory} has been recovered using {args.toolName}")



def foremost(fileType):
   
    result=sp.run(["sudo",args.toolName,"-i",f"{args.inputDirectory}","-o",f"{args.outputDirectory}","-t",f"{fileType}"],stdout=sp.PIPE,stderr=sp.PIPE)
    print(f"The device or image located at {args.inputDirectory} has been recovered using {args.toolName}")



if args.toolName=="foremost" or args.toolName=="magicrescue":
    if args.toolName=="foremost":
        fileType=args.configFile;
        foremost(fileType)
    else:
        recipeType=args.configFile;
        magicrescue(recipeType)
else:
   print("Invalid input")
    
        


