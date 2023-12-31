# views.py
from django.shortcuts import render, redirect
from .forms import ContributionForm
from .models import Contribution
from django.http import JsonResponse
from .serializers import ContributionSerializer


def create_contribution(request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_success')  # You'll define this URL
    else:
        form = ContributionForm()

    return render(request, 'contribution_form.html', {'form': form})


def input_success(request):
    return render(request, 'input_success.html')


def contribution_list(request):
    contributions = Contribution.objects.all()
    return render(request, 'contribution_list.html', {'contributions': contributions})


def contribution_data_as_json(request):
    contributions = Contribution.objects.all()
    serializer = ContributionSerializer(contributions, many=True)
    return JsonResponse(serializer.data, safe=False)
