# # jobs/views.py

# from django.shortcuts import render
# from jobsearch import settings
# from linkedin import linkedin

# def job_search(request):
#     if request.method == 'POST':
#         # Get the search query from the form data
#         degree = request.POST['degree']

#         # Authenticate with the LinkedIn API using the user's access token
#         authentication = linkedin.LinkedInAuthentication(
#             settings.LINKEDIN_CLIENT_ID,
#             settings.LINKEDIN_CLIENT_SECRET,
#             settings.LINKEDIN_REDIRECT_URI,
#             settings.LINKEDIN_SCOPE,
#         )
#         authentication.access_token = request.session['access_token']

#         # Initialize the LinkedIn API client
#         application = linkedin.LinkedInApplication(authentication)

#         # Search for job listings based on the user's degree
#         job_results = application.search_job(
#             {'keywords': degree, 'sort': 'DD'}
#         )

#         # Render the search results template with the job listings
#         return render(request, 'results.html', {'job_results': job_results})
#     else:
#         # Render the job search form template
#         return render(request, 'search.html')

from django.shortcuts import render
from jobsearch import settings
from linkedin import linkedin

def search_jobs(request):
    if request.method == 'POST':
        degree = request.POST.get('degree')

        # Initialize the LinkedInApplication object with the Client Id and Client Secret
        app = linkedin.LinkedInApplication(token=None, 
            consumer_key=settings.LINKEDIN_CLIENT_ID,
            consumer_secret=settings.LINKEDIN_CLIENT_SECRET)

        # Use the jobs API to search for jobs based on the degree
        jobs = app.search_job(
            params={'keywords': degree, 'count': 10, 'sort': 'DD'})

        # Render the results in the template
        context = {'jobs': jobs}
        return render(request, 'jobs.html', context)

    return render(request, 'search.html')