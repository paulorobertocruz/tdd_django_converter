from django.shortcuts import render
from length.forms import LengthConverterForm

convert_to_metre = {
    "centimetre": 0.01,
    "metre": 1.0,
    "mile": 1609.34
}

convert_to_centimetre = {
    "centimetre": 100,
    "metre": 1.0,
    "mile": 0.000621371
}


def convert(request):
    form = LengthConverterForm()
    if request.GET:
        input_unit = request.GET['input_unit']
        input_value = request.GET['input_value']
        output_unit = request.GET['output_unit']

        try:
            metres = convert_to_metre[input_unit] * float(input_value)
            output_value = metres * convert_to_centimetre[output_unit]
            data = {
                "input_unit": input_unit,
                "input_value": input_value,
                "output_unit": output_unit,
                "output_value": round(output_value, 3)
            }
            form = LengthConverterForm(initial=data)
        except KeyError as err:
            return render(request, "length/convert.html", context={"form": form, "key": err})    
        return render(request, "length/convert.html", context={"form": form})

    return render(request, "length/convert.html", {"form": form})
