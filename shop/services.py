from django.db.models import Sum, F, QuerySet


def get_sorted_product(queryset: QuerySet, order_by: str):
    if order_by == "cost":
        return queryset.order_by("cost")
    elif order_by == "-cost":
        return queryset.order_by("-cost")
    elif order_by == "sold":
        queryset = queryset.annotate(sold=Sum(F("cost") * F("purchases__count")))
        return queryset.order_by("sold")
    elif order_by == "popular":
        queryset = queryset.annotate(popular=Sum("purchases__count"))
        return queryset.order_by("popular")
    return queryset