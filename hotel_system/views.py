from django.http import HttpResponse
from django.shortcuts import render

def  DefaultView(request):
    """ Show all urls in default page like a navigation """

    out = "<h1>Welcome to Hotel Reservation App</h1>"
    out += """
    <h3>Here List of all urls:</h3>
    <h4>
        <ul>
            <li><a href='reservation/allhotels'>Get all saved hotels</a></li>
            <li><a href='reservation/hotelincity'>Get all hotels In (Abu Dhabi)</a></li>
            <li><a href='reservation/reservationlist'>Get all reservations for hotel Shelton (hotel_id = 1)
        </ul>
    </h4>
    """

    #return HttpResponse(out)
    return render(request, 'welcome.html')