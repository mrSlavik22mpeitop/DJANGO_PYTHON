from django.shortcuts import render

#DataFlair
def index(request):
    return render(request, 'generalpage/GeneralPage.html')

