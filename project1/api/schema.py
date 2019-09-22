import graphene
from graphene_django import DjangoObjectType

from .models import PurchaseModel, UserModel, PortfolioModel, StockModel

class Purchase(DjangoObjectType):
    class Meta:
        model = PurchaseModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Portfolio(DjangoObjectType):
    class Meta:
        model = PortfolioModel


class Stock(DjangoObjectType):
    class Meta:
        model = StockModel


class Query(graphene.ObjectType):
    purchases = graphene.List(Purchase)
    users = graphene.List(User)
    portfolios = graphene.List(Portfolio)
    stocks = graphene.List(Stock)

    def resolve_purchases(self, info):
        return PurchaseModel.objects.all()

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_portfolios(self, info):
        return PortfolioModel.objects.all()

    def resolve_stocks(self, info):
        return StockModel.objects.all()
