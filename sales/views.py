from django.shortcuts import render
from .models import Sale
from django.db.models import Sum
from products.models import Product

# Create your views here.

def sales_history(request):
    sales = Sale.objects.all().order_by('-sold_at')

    for sale in sales:
            sale.total_amount = sale.quantity * sale.selling_price

    return render(request, 'sales/history.html', {'sales': sales})



def sales_analysis(request):
    products = Product.objects.all()

    for product in products:
        sales = Sale.objects.filter(product=product)
        total_sold = sum(sale.quantity for sale in sales)

        if sales:
            first_sale = sales.order_by('sold_at').first()
            last_sale = sales.order_by('-sold_at').first()
            days = (last_sale.sold_at.date() - first_sale.sold_at.date()).days + 1
            average_daily_sales = total_sold / days
        else:
            total_sold = 0
            average_daily_sales = 0
        product.total_sold = total_sold
        product.average_daily_sales = round(average_daily_sales, 2)



        
        if product.average_daily_sales > 0:
            product.days_remaining = round(
                product.stock_quantity / product.average_daily_sales, 2
            )
        else:
            product.days_remaining = None

        if product.stock_quantity == 0:
            product.stock_warning = "Out of stock"
        elif product.days_remaining is not None and product.days_remaining <= product.supplier_lead_time:
            product.stock_warning = "Low stock risk"
        else:
            product.stock_warning = "Stock is okay"
        expected_demand = (
            product.average_daily_sales * product.supplier_lead_time
        )



        
        if product.stock_quantity < expected_demand:
            product.reorder_recommended = True
        else:
            product.reorder_recommended = False



        if product.reorder_recommended:
            product.reorder_quantity = round(
                expected_demand - product.stock_quantity
                )
        else:
            product.reorder_quantity = 0



        if product.average_daily_sales >= 3:
            product.sales_speed = "Fast-moving"
        else:
            product.sales_speed = "Slow-moving"    
            
    return render(request, 'sales/analysis.html', {'products': products})

def dashboard(request):
    total_products = Product.objects.count()
    total_sales = Sale.objects.count()

    total_revenue = sum(
        sale.quantity * sale.selling_price
        for sale in Sale.objects.all()
)

    total_stock = sum(
        product.stock_quantity
        for product in Product.objects.all()
    )

    out_of_stock = Product.objects.filter(stock_quantity=0).count()
    return render(request,'sales/dashboard.html',
        {
            'total_products': total_products,
            'total_sales': total_sales,
            'total_stock': total_stock,
            'low_stock': out_of_stock,
            'total_revenue': total_revenue,
        }
    )


