from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Video

def lista_videos(request):
	objectos = Video.objects.all()

	return render_to_response('videos/videos_list.html', {'objects':objectos},
							 context_instance=RequestContext(request))