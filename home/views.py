from django.shortcuts import render
from django.http import HttpResponse
import sys

def home(request):
    return render(request,'base.html')
def OnCLICKSUBMIT(request):
    return render(request,'codereview.html')
def editor(request):
    return render(request,'code.html')
def runcode(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print(output)
    res = render(request,'code.html',{"code":code_part,"input":y,"output":output})
    return res
def input(request):
    pass

# Create your views here.
