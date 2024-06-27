from django.shortcuts import render,redirect
from .models import Food,Consume

def index(request):
    if request.method == "POST":
        food_consume = request.POST['food_consumed']
        food = Food.objects.get(name=food_consume)
        user = request.user
        consume = Consume(user=user,food_consumed=food)
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)
    context = {
        'foods':foods,
        'consumed_food':consumed_food,
    }
    return render(request,'food/index.html',context)

def delete_consumed(request,id):
    consume = Consume.objects.get(id=id)
    if request.method=="POST":
        consume.delete()
        return redirect('/')
    return render(request,'food/delete.html')