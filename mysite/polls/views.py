from django.http import HttpResponse


def hello_name(request, question_id):
    return HttpResponse(("Hello %s." % question_id))


def times2(request, question_id):
    return HttpResponse(("The product times 2 is : ",(question_id*2)))


def sums(request, num):
    sumNum = 1
    total = 0
    while sumNum <= num:
        total = total + sumNum
        sumNum += 1
        print("Number of times it has looped: ", sumNum)
    return HttpResponse(("Sum is:", total))

