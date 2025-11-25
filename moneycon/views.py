from django.shortcuts import render
import requests



API_KEY = "f003a4b6ee54e7bfdeb50858"



def currency_converter_view(request):
    result = None
    rate = None

    if request.method == 'POST':

        amount = request.POST.get('amount')

        from_currency = request.POST.get('from_currency')

        to_currency = request.POST.get('to_currency')



        # 🌍 API endpoint (using your API key)

        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"



        try:

            response = requests.get(url)

            data = response.json()



            # ✅ Check if request was successful

            if data.get('result') == 'success':

                conversion_rate = data['conversion_rates'].get(to_currency)

                if conversion_rate:

                    rate = round(conversion_rate, 2)

                    result = round(float(amount) * conversion_rate, 2)

                else:

                    result = "Invalid currency selected."

            else:

                result = "API error. Please try again later."



        except Exception as e:

            result = f"Error: {str(e)}"



    return render(request, 'moneycon\home.html', {'result': result, 'rate': rate})






