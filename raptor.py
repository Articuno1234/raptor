try:
  import sys
  import os
  import subprocess
  import random
except ImportError:
  input("Raptor can not be used\n"
        "Some requirements are not installed")
  
def exit(num):
  sys.exit(num)
  
def dice():
  dice = ["1", "2", "3", "4", "5", "6"]
  random.choice(dice)

def print(args):
  print(args)
  
def pip(args):
  subprocess.call(("pip3", "install", args)
