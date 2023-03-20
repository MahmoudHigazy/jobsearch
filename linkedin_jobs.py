from jobsearch import settings
import linkedin
from linkedin import server
from linkedin import auth

# Set up the OAuth2 authentication
authentication = linkedin.OAuth2Authentication(
    settings.LINKEDIN_CLIENT_ID,
    settings.LINKEDIN_CLIENT_SECRET,
    settings.LINKEDIN_REDIRECT_URI,
    linkedin.PERMISSIONS.enums.values()
)

# Set up the LinkedIn application
application = linkedin.LinkedInApplication(authentication)

# Get jobs by degree
jobs = application.search_job(
    params={'degree': 'Bachelors'},
    fields=[
        'company',
        'position',
        'location',
        'description'
    ],
    start=0,
    count=10
)

# Display the results
for job in jobs['values']:
    print('Company:', job['company']['name'])
    print('Position:', job['position']['title'])
    print('Location:', job['location']['name'])
    print('Description:', job['description'])
    print('')