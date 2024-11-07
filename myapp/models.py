from django.db import models

class Expenditure(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Utilities', 'Utilities'),
        ('Housing', 'Housing'),
        ('Subscriptions', 'Subscriptions'),
        ('Health care', 'Health care'),
        ('Donations', 'Donations'),
        ('Entertainment', 'Entertainment'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Food')
    type = models.CharField(max_length=100, help_text="Enter the type of expenditure (e.g., grocery, taxi, etc.)")
    date = models.DateField(help_text="Enter the date of the expenditure")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the amount of expenditure")

    def _str_(self):
        return f"{self.category} - {self.type} - {self.amount}"
    
    from django.db import models

class Income(models.Model):
    INCOME_CATEGORIES = [
        ('Salary/Wages', 'Salary/Wages'),
        ('Business Income', 'Business Income'),
        ('Rental Income', 'Rental Income'),
        ('Investment Income', 'Investment Income'),
        ('Pension/Retirement Income', 'Pension/Retirement Income'),
        ('Interest Income', 'Interest Income'),
        ('Royalties', 'Royalties'),
        ('Freelance/Contractor Income', 'Freelance/Contractor Income'),
        ('Government Benefits', 'Government Benefits'),
        ('Dividends', 'Dividends'),
        ('Capital Gains', 'Capital Gains'),
        ('Annuities', 'Annuities'),
        ('Gifts/Inheritance', 'Gifts/Inheritance'),
        ('Other', 'Other'),
    ]

    income_category = models.CharField(max_length=50, choices=INCOME_CATEGORIES)
    income_source = models.CharField(max_length=255)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_date = models.DateField()
    income_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.income_category} - {self.income_amount}"

from django.db import models

class Sales(models.Model):
    SALES_CATEGORY_CHOICES = [
        ('Retail', 'Retail'), ('Wholesale', 'Wholesale'), ('Online', 'Online'), ('Export', 'Export'), ('Other', 'Other')
    ]

    sales_category = models.CharField(max_length=50, choices=SALES_CATEGORY_CHOICES, default='Retail', help_text="Select the category of sales")
    customer_name = models.CharField(max_length=100, help_text="Enter the name of the customer", default="Unknown")
    customer_address = models.CharField(max_length=100, help_text="Enter the address of the customer", blank=True, null=True)
    product_name = models.CharField(max_length=100, help_text="Enter the name of the product or service")
    quantity = models.PositiveIntegerField(help_text="Enter the quantity of the product or service")
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the total sales amount")
    sales_date = models.DateField(help_text="Enter the date of the sale")
    description = models.TextField(blank=True, help_text="Optional description of the sale")

    def __str__(self): return f"{self.sales_category} - {self.product_name} - {self.sales_amount}"

    from django.db import models

class Purchase(models.Model):
    PURCHASE_CATEGORY_CHOICES = [
        ('Office Supplies', 'Office Supplies'),
        ('Equipment', 'Equipment'),
        ('Utilities', 'Utilities'),
        ('Raw Materials', 'Raw Materials'),
        ('Miscellaneous', 'Miscellaneous'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Partial', 'Partial'),
    ]
    
    vendor_name = models.CharField(max_length=100, help_text="Enter the name of the vendor")
    purchase_category = models.CharField(max_length=50, choices=PURCHASE_CATEGORY_CHOICES, help_text="Select the category of the purchase")
    purchase_date = models.DateField(help_text="Enter the date of the purchase")
    product_name = models.CharField(max_length=100, help_text="Enter the name of the product or service purchased")
    quantity = models.PositiveIntegerField(help_text="Enter the quantity of the product or service")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the total purchase amount")
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, help_text="Select the payment status")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the purchase")

    def __str__(self):
        return f"{self.vendor_name} - {self.product_name} - {self.amount}"

