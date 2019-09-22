from django.db import models


# the class containing a portfolio of stocks
class PortfolioModel(models.Model):
    class Meta:
        app_label = 'api'
    cash = models.FloatField()


# the class containing your user information (including their api token and password, etc)
class UserModel(models.Model):
    class Meta:
        app_label = 'api'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # how long are our API tokens?
    api_token = models.CharField(max_length=256)
    # how long is this? I'll assume hex, 256 bit hash
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=30)
    portfolio = models.OneToOneField(PortfolioModel, on_delete=models.CASCADE)


# a class containing what happened in a purchase (who made it, when it was made, what it traded)
class PurchaseModel(models.Model):
    class Meta:
        app_label = 'api'
    timestamp = models.DateTimeField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()


# a class containing a simple set of data on a stock within a portfolio
class StockModel(models.Model):
    class Meta:
        app_label = 'api'
    portfolio = models.ForeignKey(PortfolioModel, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    quantity = models.IntegerField()
