# -*- coding: utf-8 -*-
import re
import requests
from urllib import quote


class APIKeyAuth(requests.auth.AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key
    def __call__(self, req):
        # Simply return the API key.
        req.headers['Authorization'] = 'Token {}'.format(self.api_key)
        return req


class LMSInsightsClient(object):
    """
    Class used to query Insights API data from the LMS.
    """
    def __init__(self, base_insights_api_url, api_user=None, api_key=None):
        # Strip trailing slash if exists.
        self.api_base_url = re.sub(r'/$', '', base_insights_api_url)
        self.api_user = api_user
        self.api_key = api_key

    def get_current_course_enrollment(self, course_id):
        """
        Params:
            course_id (str): Course ID for which to retrieve enrollment data.

        Returns:
            Dictionary in this form:
              {
                "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                "date": "2017-03-26",
                "count": 236107,
                "created": "2017-03-28T012204"
              }
        """
        results = requests.get(
            '{base_url}/courses/{course_id}/enrollment/'.format(
                base_url=self.api_base_url,
                course_id=course_id
            ),
            auth=APIKeyAuth(self.api_key)
        )
        return results.json()[0]

    def get_current_course_enrollment_by_birth_year(self, course_id):
        """
        Params:
            course_id (str): Course ID for which to retrieve enrollment data by birth year.

        Returns:
            List in this form:
                [
                  ...,
                  {
                    "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                    "date": "2017-03-26",
                    "birth_year": 1984,
                    "count": 6698,
                    "created": "2017-03-28T014331"
                  },
                  {
                    "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                    "date": "2017-03-26",
                    "birth_year": 1985,
                    "count": 7259,
                    "created": "2017-03-28T014333"
                  },
                  ...
                ]
        """
        results = requests.get(
            '{base_url}/courses/{course_id}/enrollment/'.format(
                base_url=self.api_base_url,
                course_id=course_id
            ),
            auth=APIKeyAuth(self.api_key)
        )
        return results.json()
