# -*- coding: UTF-8 -*-
from django.http import HttpResponse

def save_as_xls(request):
    tabla = request.POST['tabla']    
    response = render_to_response('xls.html', {'tabla': tabla, })
    response['Content-Disposition'] = 'attachment; filename=tabla.xls'
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Charset'] ='UTF-8'
    return response

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.replace('.'+filename.split('.')[-1], ''))
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.fileDir, filename)
