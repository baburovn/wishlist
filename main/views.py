from django.shortcuts import render, get_object_or_404

from .models import  WishList

def index(request):
    return render(request, 'index.html', {})

def about_us(request):
    return render(request, "about.html", {})

def list_page(request, pk):
    """
    FBV - veiws основаны на функциях
    CBV - veiws основаны на классах
    print("[PK]", pk)
    """
    wishlist = get_object_or_404(WishList, pk=pk)
    print(wishlist)
    return render(
        request,
        "wish_list.html",
        {
            "wishlist": wishlist,
            "is_owner_list": wishlist.owner == request.user,
        }
                )