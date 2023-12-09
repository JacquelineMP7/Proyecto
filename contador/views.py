from django.shortcuts import render
from nltk import FreqDist
from nltk.tokenize import word_tokenize

def contar_letras(request):
    if request.method == 'POST':
        texto = request.POST.get('texto', '')
        palabras = word_tokenize(texto)
        frecuencia_letras = FreqDist(''.join(palabras))

        return render(request, 'contador/resultado.html', {'frecuencia_letras': frecuencia_letras})

    return render(request, 'contador/contar_letras.html')

