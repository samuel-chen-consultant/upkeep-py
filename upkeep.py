import requests
from base64 import b64encode, b64decode

class upkeep:
    '''
    a python package to make calls to the upkeep API, as defined on their doc page:
    https://developers.onupkeep.com/
    '''
    def __init__(self, email, _pass):
        
        self.email = email
        self._pass = self.encode(_pass)
        self.url = 'https://api.onupkeep.com/api/v2/'
        self.loggedin = 0
        self.token = self.login()
        
        # functions to create API calls
        self.get = self.get
        self.post = self.post
        self.patch =self.patch
        
        # create sub-functions
        self.users = self.users(self)


    def encode(self, _pass):
        _pass = _pass.encode("utf-8")
        _pass = b64encode(_pass)
        return _pass

    def login(self):
        if self.loggedin == 1:
            return "you're already logged in silly!"
        else:
            url = self.url + 'auth'
            _pass = b64decode(self._pass)
            _pass = _pass.decode("utf-8")
            data = {'email': self.email,
                    'password': _pass}
            
            # uncomment when credentials are given
            # r = requests.post(url, data=data)
            # if r.status_code != requests.codes.ok:
            #     print('''something went wrong.
            #     please check your credentials and try again''')
            #     return None
            # r = r.json()['result']['sessionToken']
            self.loggedin = 1
            
        return data
    
    def logout(self):
        
        url = self.url + 'auth'
        data = {'Session-Token': self.token}
        r = requests.delete(url, data=data)
        print("you've successfully been logged out")
        self.loggedin = 0
    
    
    def get(self, epoint=None, **kwargs):
        '''helper function for the various subclasses'''
        
        url = self.url + epoint
        params = kwargs
        headers = {'Session-Token': self.token}
#         # uncomment when credentials are given
#         requests.get(url, params, headers = headers)
        
        return url, params
    
    def post(self, epoint=None, **kwargs):
        '''helper function for the various subclasses'''
        
        url = self.url + epoint
        data = kwargs
        headers = {'Session-Token': self.token}
        
#         # uncomment when credentials are given
#         requests.post(url = url, data = data)
        
        return url, data
    
    def patch(self, epoint=None, **kwargs):
        '''helper function for the various subclasses'''
        
        url = self.url + epoint
        data = kwargs
        headers = {'Session-Token': self.token}
        
#         # uncomment when credentials are given
#         requests.patch(url, data, headers = headers)

        return url, data
    
    
    class users:
        '''
        used to query within users endpoint.
        docs - https://developers.onupkeep.com/#users
        '''

        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'users/'
            
        def create_user(self, email, accountType, password, **kwargs):
            '''
            This endpoint creates a new user:
            https://developers.onupkeep.com/#create-a-user
            '''
            
            r = self.upkeep.post(self.epoint, **kwargs)
            return r
        
        def get_all_users(self,):
            pass
        
        def get_user(self,):
            pass
        
        def update_user(self,):
            pass