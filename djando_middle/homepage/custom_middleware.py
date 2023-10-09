
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        response = self.get_response(request)
        self.count += 1
        if self.count == 3:
            self.count = 0
            resp_arr = response.content.decode().replace('<body>', '').replace('</body>', '').split(' ')
            resp = ' '.join([str(x[::-1]) for x in resp_arr])
            print(resp_arr, resp)
            response.content = resp.encode()
        print(response.content.decode(), self.count)
        return response