from datetime import datetime

import pdfkit
import qrcode
import os
from django.conf import settings
from django.template.loader import render_to_string


def generate_pdf(items, filename):
    items_data = [
        {
            'title': item.title,
            'quantity': 1,
            'total_price': item.price
        } for item in items
    ]
    total_price = sum(item.price for item in items)
    receipt_date = datetime.now().strftime("%d.%m.%Y %H:%M")

    html_content = render_to_string('receipt_template.html', {
        'items': items_data,
        'total_price': total_price,
        'receipt_date': receipt_date
    })

    pdf_path = os.path.join(settings.MEDIA_ROOT, filename)

    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    options = {
        'page-size': 'A7',
        'margin-top': '2mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'no-outline': None,
        'encoding': "UTF-8"
    }

    pdfkit.from_string(html_content, pdf_path, configuration=config, options=options)

    return pdf_path


def generate_qr_code(pdf_url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pdf_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    qr_path = os.path.join(settings.MEDIA_ROOT, filename)

    img.save(qr_path)

    return qr_path
