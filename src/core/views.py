from django.shortcuts import render


def BootstrapFilterView(reguest):
    return render(reguest, 'bootstrap_form.html', {})


def BootstrapTest(reguest):
    return render(reguest, 'test.html', {})