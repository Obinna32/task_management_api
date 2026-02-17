from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """
    Custom exception handler to ensure all error responses 
    follow the same { 'error': 'message', 'status_code': 400 } format.
    """
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            'error': response.data.get('detail', 'An error occurred'),
            'status_code': response.status_code
        }
        response.data = custom_data

    return response