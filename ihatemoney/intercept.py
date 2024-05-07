from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    # Check if the request URL is the one where we expect to manipulate the response
    if "api/projects/testproject5" in flow.request.pretty_url:
        # Decode the response
        data = flow.response.get_text()
        if '"logging_preference": 0' in data:
            # Replace the incorrect value with the correct one
            new_data = data.replace('"logging_preference": 0', '"logging_preference": 1')
            flow.response.set_text(new_data)

# Save this script in the same directory as your Flask application
