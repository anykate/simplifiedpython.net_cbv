from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product
from .forms import ProductForm


# Create your views here.
class ProductListView(generic.ListView):
    context_object_name = 'product_list'
    template_name = 'genericviews/index.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'genericviews/details.html'

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['product_id'])


def saveproducttodb(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')

            product = Product(title=title, description=description)
            product.save()

        return redirect('/')

    else:
        form = ProductForm()

    return render(request, 'genericviews/save_product.html', {'form': form})
