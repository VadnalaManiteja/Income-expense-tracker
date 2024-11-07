from django.shortcuts import render, redirect
from .models import Expenditure, Sales

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Purchase

from django.contrib import messages

from django.contrib.auth import logout

def expenditure_form(request):
    return render(request,'expenditure_form.html')

def income_form(request):
    return render(request,'income_form.html')

def index(request):
    return render(request,'index.html')

def sales_form(request):
    return render(request,'sales_form.html')

def purchases_form(request):
    return render(request,'purchases_form.html')

def add_expenditure(request):
    if request.method == 'POST':
        # Capture the form data from the request
        category = request.POST.get('category')
        type_ = request.POST.get('type')
        date = request.POST.get('date')
        amount = request.POST.get('amount')

        print("amount =",amount)
        # Create a new expenditure entry
        Expenditure.objects.create(
            category=category,
            type=type_,
            date=date,
            amount=amount
        )


    return render(request, 'expenditure_form.html')


from django.shortcuts import render, redirect
from .models import Income


# View to add new income entry
def add_income(request):
    if request.method == 'POST':
        # Capture the form data from the request
        category = request.POST.get('incomeCategory')
        source = request.POST.get('incomeSource')
        date = request.POST.get('incomeDate')
        amount = request.POST.get('incomeAmount')
        description=request.POST.get('incomeDescription')
        print("amount =",amount)
        # Create a new expenditure entry
        Income.objects.create(
            income_category=category,
             income_source=source,
             income_date=date,
            income_amount=amount,
            income_description=description
        )


    return render(request, 'income_form.html')
   
def add_sales(request):
    if request.method == 'POST':
        # Capture the form data from the request
        category = request.POST.get('salesCategory')
        customername = request.POST.get('customerName')
        customeraddress = request.POST.get('customerAddress')
        productname = request.POST.get('productName')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('salesAmount')
        date = request.POST.get('salesDate')
        description =request.POST.get('salesDescription')

        print("amount =",amount)
        # Create a new expenditure entry
        Sales.objects.create(
            sales_category=category,
            customer_name=customername,
            customer_address=customeraddress,
            product_name=productname,
            quantity=quantity,
            sales_amount=amount,
            sales_date=date,
            description=description
        )


    return render(request, 'sales_form.html')

from django.shortcuts import render
from .models import Purchase  # Make sure to import your Purchase model

def add_purchases(request):
    if request.method == 'POST':
        # Capture the form data from the request
        vendorname = request.POST.get('vendorName')
        purchasecategory = request.POST.get('purchaseCategory')
        purchasedate = request.POST.get('purchaseDate')
        productname = request.POST.get('productName')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        paymentstatus = request.POST.get('paymentStatus')
        description = request.POST.get('description')

        print("amount =", amount)  # Debug print for checking amount value

        # Create a new purchase entry
        Purchase.objects.create(
            vendor_name=vendorname,
            purchase_category=purchasecategory,
            purchase_date=purchasedate,
            product_name=productname,
            quantity=quantity,
            amount=amount,
            payment_status=paymentstatus,
            description=description
        )

    return render(request, 'purchases_form.html')



# View to list all income entries
def income_list(request):
    incomes = Income.objects.all()
    total_income = sum(income.income_amount for income in incomes)

    return render(request, 'income_list.html', {
        'incomes': incomes,
        'total_income': total_income,
    })

def expenditure_list(request):
    expenditures = Expenditure.objects.all()
    total_expenditure = sum(expenditure.amount for expenditure in expenditures)  # Calculate the total

    return render(request, 'expenditure_list.html', {
        'expenditures': expenditures,
        'total_expenditure': total_expenditure,
    })

def sales_list(request):
    sales = Sales.objects.all()
    total_sales = sum(sale.sales_amount for sale in sales)  # Corrected line
    return render(request, 'sales_list.html', {
        'sales': sales,
        'total_sale': total_sales,  # Make sure it matches the template
    })


def purchases_list(request):
    purchases = Purchase.objects.all()
    total_purchases = sum(purchase.amount for purchase in purchases)
    return render(request, 'purchases_list.html',{
        'purchases': purchases,
        'total_purchase': total_purchases, 
    })

def delete_purchase(request, purchase_id):
    if request.method == 'POST':
        print("Attempting to delete purchase with ID:", purchase_id)
        purchase = get_object_or_404(Purchase, id=purchase_id)
        purchase.delete()
        return redirect('purchases_list')  # Redirect after deletion
    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_sale(request, sale_id):
    if request.method == 'POST':
        print("Attempting to delete sale with ID:", sale_id)
        sale = get_object_or_404(Sales, id=sale_id)
        sale.delete()
        return redirect('sales_list')  
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_income(request, income_id):
    if request.method == 'POST':
        print("Attempting to delete income with ID:", income_id)
        income = get_object_or_404(Income, id=income_id)
        income.delete()
        return redirect('income_list')  
    return JsonResponse({'error': 'Invalid request'}, status=400)

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

def delete_expenditure(request, expenditure_id):
    if request.method == 'POST':
        print("Attempting to delete expenditure with ID:", expenditure_id)
        expenditure = get_object_or_404(Expenditure, id=expenditure_id)
        expenditure.delete()
        return redirect('expenditure_list')  # Make sure 'expenditure_list' matches the name in your URLs
    return JsonResponse({'error': 'Invalid request'}, status=400)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Income
from django.shortcuts import render, get_object_or_404, redirect
from .models import Income

def update_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)
    if request.method == 'POST':
        income.income_category = request.POST.get('income_category')
        income.income_source = request.POST.get('income_source')
        income.income_amount = request.POST.get('income_amount')
        income.income_date = request.POST.get('income_date')
        income.income_description = request.POST.get('income_description')
        
        income.save()
        return redirect('income_list')
    
    return render(request, 'update_income_form.html', {'income': income})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Expenditure

def update_expenditure(request, expenditure_id):
    expenditure = get_object_or_404(Expenditure, id=expenditure_id)
    if request.method == 'POST':
        expenditure.category = request.POST.get('category')
        expenditure.type = request.POST.get('type')
        expenditure.date = request.POST.get('date')
        expenditure.amount = request.POST.get('amount')
        
        expenditure.save()
        return redirect('expenditure_list')  # Make sure you have this view and template
    
    return render(request, 'update_expenditure_form.html', {'expenditure': expenditure})

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Sales

def update_sale(request, sale_id):
    sales = get_object_or_404(Sales, id=sale_id)  # Retrieve the specific Sales record by ID

    if request.method == 'POST':
        # Update the sales record with data from the request
        sales.sales_category = request.POST.get('sales_category')
        sales.customer_name = request.POST.get('customer_name')
        sales.customer_address = request.POST.get('customer_address')
        sales.product_name = request.POST.get('product_name')
        sales.quantity = request.POST.get('quantity')
        sales.sales_amount = request.POST.get('sales_amount')
        sales.sales_date = request.POST.get('sales_date')
        sales.description = request.POST.get('description')
        
        sales.save()  # Save the updated record
        return redirect('sales_list')  # Redirect to the sales list view

    return render(request, 'update_sales_form.html', {'sales': sales})  # Render the update form

from django.shortcuts import render, get_object_or_404, redirect
from .models import Purchase

def update_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    
    if request.method == 'POST':
        purchase.vendor_name = request.POST.get('vendor_name')
        purchase.purchase_category = request.POST.get('purchase_category')
        purchase.purchase_date = request.POST.get('purchase_date')
        purchase.product_name = request.POST.get('product_name')
        purchase.quantity = request.POST.get('quantity')
        purchase.amount = request.POST.get('amount')
        purchase.payment_status = request.POST.get('payment_status')
        purchase.description = request.POST.get('description', '')  # Default to empty string if not provided
        
        purchase.save()
        return redirect('purchases_list')  # Redirect to the list view after successful update
    
    return render(request, 'update_purchase_form.html', {'purchase': purchase})

#from django.shortcuts import render
#from .models import Expenditure, Income, Sales, Purchase  # Import all necessary models

def dashboard(request):
    expenditures = Expenditure.objects.all()
    total_expenditure = sum(expenditure.amount for expenditure in expenditures)
    incomes = Income.objects.all()  
    total_income = sum(income.income_amount for income in incomes)
    sales = Sales.objects.all()
    total_sales = sum(sale.sales_amount for sale in sales)
    purchases = Purchase.objects.all()
    total_purchases = sum(purchase.amount for purchase in purchases)
    total_balance=total_income-total_expenditure
    # Render the dashboard with all totals
    return render(request, 'dashboard.html', {
        'total_expenditure': total_expenditure,
        'total_income': total_income,
        'total_sale': total_sales,
        'total_purchase': total_purchases,
        'total_balance':total_balance
    })

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the entered credentials match the hardcoded ones
        if email == "admin@gmail.com" and password == "Admin@123":
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")





