# from locations.models import GeoDistrict
#
#
# def index(request):
#     pass
#
#
# def geodistrict_detail(request):
#     context = {}
#     district = GeoDistrict.objects.get(1)
#     context['voters'] = district
#
#     return render_to_response('locations/geo_districts_detail.html', context)
#
#
# def import_tool(request):
#     return render_to_response('locations/import_tool.html')
#
#
# def geo_districts_index(request):
#     context = {}
#     # TODO: there might be more efficient ways to do this
#     districts = GeoDistrict.objects.filter(parent=None)
#     context['districts'] = districts
#
#     return render_to_response('locations/geo_districts_index.html', context)