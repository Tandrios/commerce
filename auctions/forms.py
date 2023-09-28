from django import forms

from .models import Auction, Bid

class AuctionForm(forms.ModelForm):
    
    class Meta:
        model = Auction
        fields = ["title", "description", "category", "image", "opening_bid"]


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:75%', 'placeholder': 'Think of a name that sells your product.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:75%', 'placeholder': 'Tell potential bidders more about this item...'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:75%', 'placeholder': 'https://cutebunnyrabbits.jpg'}),
            'category': forms.Select(attrs={'class': 'form-control text-capitalize', 'style': 'width:75%'}),
            'opening_bid': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:75%'})
        }

