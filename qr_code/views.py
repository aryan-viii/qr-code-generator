from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data["restaurant_name"]
            url = form.cleaned_data["url"]

            # Generate QR code
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_") + "_qr.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            #create image URL to display in template
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            return render(request, "qr_code/qr_result.html", {"res_name": res_name, "qr_url": qr_url})
            
    else:
        form = QRCodeForm()
        return render(request, "qr_code/home.html", {"form": form})