from noticias.models import Portada, FotosPortadas

#prueba de prueba
def globales(request):
    noti_foto = Portada.objects.all()[0]
    
    fotos_portada = noti_foto._fotos_traer()
   

    return {'fotos_portada': fotos_portada}