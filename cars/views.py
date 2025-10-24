from django.shortcuts import render, redirect
from cars.models import Car, Brand
from cars.forms import CarModelForm, BrandModelForm
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

"""def cars_view(request):
    
    search = request.GET.get('search')

    cars = Car.objects.all().order_by('-model')

    if search:
        cars = cars.filter(model__contains=search)

    return render(
        request, 
        'cars.html',
        {'cars': cars}    
    )"""

# Criando view da Classe mais básica View
"""class CarsView(View):
    def get(self, request):
        search = request.GET.get('search')
        cars = Car.objects.all().order_by('-model')

        if search:
            cars = cars.filter(model__contains=search)

        return render(
        request,
        'cars.html',
        {'cars': cars}
    )"""

"""def new_car_view(request):
    print("====================================")
    print("O método da requisição é:", request.method)
    print("Conteúdo do request.POST:", request.POST)
    print("Conteúdo do request.FILES:", request.FILES)
    print("Usuário logado:", request.user)

    # Dica de ouro: use dir() para ver TUDO que está disponível no objeto!
    print("Todos os atributos disponíveis no request:", dir(request))
    print("====================================")
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            print('--- DADOS VALIDADOS (cleaned_data): ---')
            print(new_car_form.cleaned_data)
            print('-----------------------------------------')
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )"""

"""class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request,
            "new_car.html",
            {'new_car_form': new_car_form}
        )
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid:
            new_car_form.save()
            return redirect('cars_list')
        else:
            return render(
                request,
                'new_car.html',
                {'new_car_form': new_car_form}
            )"""
    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandModelForm
    template_name = 'new_brand.html'
    success_url = '/cars/'

class CarsDetailView(DetailView):
    model = Car
    template_name = 'detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsUpdateView(UpdateView):
    model = Car
    template_name = 'update.html'
    form_class = CarModelForm
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('cars_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsDeleteView(DeleteView):
    model = Car
    template_name = 'delete.html'
    success_url = '/cars/'

