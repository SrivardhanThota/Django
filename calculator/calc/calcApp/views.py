from django.shortcuts import render

# Create your views here.

def cal(request):

    output=""

    if request.method=="POST":
        num1 = eval(request.POST.get("Fn"))
        num2 = eval(request.POST.get('Sn'))
        opr = (request.POST.get("opr"))

        if opr=="+":
            output=num1+num2
        elif opr=="-":
            output=num1-num2
        elif opr=="*":
            output=num1*num2
        elif opr=="/":
            output=num1/num2

    return render(request,'calc.html',{'Ans':output})