from noticias.models import Portada, FotosPortadas

#prueba de prueba
def globales(request):
    noti_foto  = []
    fotos_portada =[]
    try:
        noti_foto = Portada.objects.all()[0]
    except:
        pass
    if noti_foto:
        fotos_portada = noti_foto._fotos_traer()

    return {'fotos_portada': fotos_portada}