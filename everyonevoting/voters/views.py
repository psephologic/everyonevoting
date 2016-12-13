__author__ = 'eronlloyd'

from django.shortcuts import render_to_response

from voters.models import VoterRegistration, GeoDistrict


def index(request):
    context = {}
    voter_registrations = VoterRegistration.objects.all()
    context['voters'] = voter_registrations

    return render_to_response('voters/index.html', context)


def geodistrict_detail(request):
    context = {}
    district = GeoDistrict.objects.get(1)
    context['voters'] = district

    return render_to_response('voters/geo_districts_detail.html.html', context)


def import_tool(request):
    return render_to_response('voters/import_tool.html')
