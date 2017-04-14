# -*- coding: utf-8 -*-
import re
import requests

__author__ = """John Eskew"""
__email__ = 'jeskew@edx.org'
__version__ = '0.1.0'


class APIKeyAuth(requests.auth.AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key
    def __call__(self, req):
        # Add the API key to the headers.
        req.headers['Authorization'] = 'Token {}'.format(self.api_key)
        return req


class LMSInsightsClient(object):
    """
    Class used to query Insights API data from the LMS.
    """
    def __init__(self, base_insights_api_url, api_key=None):
        # Strip trailing slash if exists.
        self.api_base_url = re.sub(r'/$', '', base_insights_api_url)
        self.api_key = api_key

    def _get_api_courses_results(self, course_id, by_filter=None):
        """
        Utility method for retrieving course info.
        """
        url = '{base_url}/courses/{course_id}/enrollment/'.format(
            base_url=self.api_base_url,
            course_id=course_id
        )
        if by_filter:
            url += by_filter + '/'
        results = requests.get(url, auth=APIKeyAuth(self.api_key))
        return results.json()

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
        return self._get_api_courses_results(course_id)[0]

    def get_current_course_enrollment_by_mode(self, course_id):
        """
        Params:
            course_id (str): Course ID for which to retrieve enrollment data by mode.

        Returns:
            Dictionary in this form:
              {
                "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                "date": "2017-03-26",
                "count": 236107,
                "cumulative_count": 269777,
                "created": "2017-03-28T010109",
                "audit": 11915,
                "credit": 0,
                "honor": 222320,
                "professional": 0,
                "verified": 1872
              }
        """
        return self._get_api_courses_results(course_id, 'mode')[0]

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
        return self._get_api_courses_results(course_id, 'birth_year')

    def get_current_course_enrollment_by_education(self, course_id):
        """
        Params:
            course_id (str): Course ID for which to retrieve enrollment data by education level.

        Returns:
            List in this form:
                [
                  ...,
                  {
                    "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                    "date": "2017-03-26",
                    "education_level": "doctorate",
                    "count": 4820,
                    "created": "2017-03-28T013248"
                  },
                  {
                    "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                    "date": "2017-03-26",
                    "education_level": "junior_secondary",
                    "count": 4101,
                    "created": "2017-03-28T013249"
                  },
                  ...
                ]
        """
        return self._get_api_courses_results(course_id, 'education')

    def get_current_course_enrollment_by_location(self, course_id):
        """
        Params:
            course_id (str): Course ID for which to retrieve enrollment data by student location.

        Returns:
            List in this form:
                [
                  ...,
                  {
                    "date": "2017-01-19",
                    "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                    "country": {
                      "alpha2": "VE",
                      "alpha3": "VEN",
                      "name": "Venezuela"
                    },
                    "count": 612,
                    "created": "2017-01-19T231938"
                  },
                  {
                    "date": "2017-01-19",
                    "course_id": "course-v1:LinuxFoundationX+LFS101x.2+1T2015",
                    "country": {
                      "alpha2": "VG",
                      "alpha3": "VGB",
                      "name": "Virgin Islands (British)"
                    },
                    "count": 4,
                    "created": "2017-01-19T231939"
                  },
                  ...
                ]
        """
        return self._get_api_courses_results(course_id, 'location')
