import http.client as httplib
import json

from django.http import JsonResponse


def form_error_json_response(errors):
    '''
    Transform from django form errors to Server API response format errors.
    Output Format:
        [
            {
                'field': <field>,
                'message': <error message>,
                'code': 40001,
            },
        ]
    Note:
        The list may contains one or more errors,
        here we only display the first error for api client.
    '''
    json_errors = json.loads(errors.as_json())
    error_list = []
    for key, errors in json_errors.items():
        new_error = {
            'code': 'form_error',
            'field': key,
            'message': errors[0]['message']
        }
        error_list.append(new_error)

    response = {
        'errors': error_list
    }
    return JsonResponse(response, status=httplib.BAD_REQUEST)


def error_json_response(code, message):
    response = {
        'errors': [
            {
                'code': str(code),
                'message': str(message),
            }
        ]
    }
    return JsonResponse(response, status=httplib.NOT_ACCEPTABLE)


def getUrlList(str):
    urls = []
    if str:
        urls = str.split(',')
        if '' in urls:
            urls.remove('')
    return urls
