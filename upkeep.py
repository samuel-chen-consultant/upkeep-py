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
        
        # create sub-functions (un-comment as creating)
        self.users = self.users(self)
        self.customers = self.customers(self)
        self.vendors = self.vendors(self)
        self.teams = self.teams(self)
#         self.assets = self.assets(self)
#         self.locations = self.locations(self)
#         self.parts = self.parts(self)
#         self.requests = self.requests(self)
#         self.worders = self.worders(self)
#         self.prev_main = self.prev_main(self)
#         self.wo_sched = self.wo_sched(self)
#         self.meters = self.meters(self)
#         self.pur_ord = self.pur_ord(self)
#         self.pur_ord_cat = self.pur_ord_cat(self)
#         self.report = self.report(self)
        


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

    def login_check(self):
        if not self.loggedin:
            raise()
    
    def logout(self):
        
        url = self.url + 'auth'
        data = {'Session-Token': self.token}
        r = requests.delete(url, data=data)
        print("you've successfully been logged out")
        self.loggedin = 0
    
    
    def get(self, url, **kwargs):
        '''helper function for the various subclasses'''
        
        if kwargs: 
            params = kwargs
        else: 
            params = None
        headers = {'Session-Token': self.token}
#         # uncomment when credentials are given
#         requests.get(url, params, headers = headers)
        
        return url, params
    
    def post(self, url, **kwargs):
        '''helper function for the various subclasses'''
        
        data = kwargs
        headers = {'Session-Token': self.token}
        
#         # uncomment when credentials are given
#         requests.post(url = url, data = data)
        
        return url, data
    
    def patch(self, url, **kwargs):
        '''helper function for the various subclasses'''
        
        data = kwargs
        headers = {'Session-Token': self.token}
        
#         # uncomment when credentials are given
#         requests.patch(url, data, headers = headers)

        return url, data

    def delete(self, url, **kwargs):
        '''helper function for the various subclasses'''
        data = kwargs
        headers = {'Session-Token': self.token}
#         # uncomment when credentials are given
#         requests.delete(url, headers = headers)
    
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
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, email = email, accountType = accountType,
                                 password = password, **kwargs)
            return r
        
        def get_all_users(self, **kwargs):
            '''
            This endpoint retrieves all users for your account.
            https://developers.onupkeep.com/#get-all-users
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_user(self, _id):
            '''
            This endpoint retrieves a specific user.
            https://developers.onupkeep.com/#get-a-specific-user
            '''
            
            url = self.upkeep.url + self.epoint + str(_id)
            
            r = self.upkeep.get(url)
            
            return r
        
        def update_user(self, _id):
            '''
            This endpoint updates a specific user.
            https://developers.onupkeep.com/#update-a-specific-user
            '''
            url = self.upkeep.url + self.epoint + _id
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
    
    class customers:
        '''
        used to query within customers endpoint.
        https://developers.onupkeep.com/#customers
        '''

        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'customers/'
            
        def create_customer(self, name, **kwargs):
            '''
            This endpoint creates a new customer.
            https://developers.onupkeep.com/#create-a-customer
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, name=name, **kwargs)
            
            return r
        
        def get_all_customers(self, **kwargs):
            '''
            This endpoint retrieves all customers for your account.
            https://developers.onupkeep.com/#get-all-customers
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_customer(self, _id):
            '''
            This endpoint retrieves a specific customer.
            https://developers.onupkeep.com/#get-a-specific-customer
            '''
            url = self.upkeep.url + self.epoint + str(_id)
            
            r = self.upkeep.get(url)
            
            return r
        
        def update_customer(self, _id, **kwargs):
            '''
            This endpoint updates a specific customer.
            https://developers.onupkeep.com/#update-a-specific-customer
            '''
            url = self.upkeep.url + self.epoint + str(_id)
            
            r = self.upkeep.patch(url)
            
            return r
        
        
    class vendors:
        '''
        used to query within vendors endpoint.
        https://developers.onupkeep.com/#vendors
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'vendors/'
            
        def create_vendor(self, businessName, **kwargs):
            '''
            This endpoint creates a new vendor.
            https://developers.onupkeep.com/#create-a-vendor
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, businessName = businessName, **kwargs)
            
            return r
        
        def get_all_vendors(self, **kwargs):
            '''
            This endpoint retrieves all vendors for your account.
            https://developers.onupkeep.com/#get-all-vendors
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_vendor(self, _id):
            '''
            This endpoint retrieves a specific vendor.
            https://developers.onupkeep.com/#get-a-specific-vendor
            '''
            url = self.upkeep.url + self.epoint + str(id)
            
            r = self.upkeep.get(url)
            
            return r
        
        def update_vendor(self, _id, **kwargs):
            '''
            This endpoint creates a new vendor.
            https://developers.onupkeep.com/#create-a-vendor
            '''
            url = self.upkeep.url + self.epoint + _id
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
    
    class teams:
        '''
        used to query within tesms endpoint.
        https://developers.onupkeep.com/#teams
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'teams/'
            
        def create_team(self, name, description, **kwargs):
            '''
            This endpoint creates a new team.
            https://developers.onupkeep.com/#create-a-team
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, name = name,
                                 description = description, **kwargs)
            return r
        
        def get_all_teams(self, **kwargs):
            '''
            This endpoint retrieves all teams for your account.
            https://developers.onupkeep.com/#get-all-teams
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r

        def get_team(self, _teamid):
            '''
            This endpoint retrieves a specific team.
            https://developers.onupkeep.com/#get-a-specific-team
            '''
            url = self.upkeep.url + self.epoint + str(_teamid)
            
            r = self.upkeep.get(url)
            
            return r
        
        def update_team(self, _teamid, **kwargs):
            '''
            This endpoint updates a specific team.
            https://developers.onupkeep.com/#update-a-specific-team
            '''
            url = self.upkeep.url + self.epoint + str(_teamid)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def delete_team(self, _teamid):
            '''
            This endpoint deletes a specific team.
            https://developers.onupkeep.com/#delete-a-specific-team
            '''
            url = self.upkeep.url + self.epoint + str(_teamid)
            
            r = self.upkeep.delete(url)
            
            return r
        
        def get_team_users(self, _teamid):
            '''
            This endpoint retrieves all users for a specific team.
            https://developers.onupkeep.com/#get-all-users-for-a-specific-team
            '''
            url = self.upkeep.url + self.epoint + str(_teamid) + '/users'
            
            r = self.upkeep.get(url)
            
            return r
        
        def user_to_team(self, _teamid, _uid):
            '''
            This endpoint adds users for a specific team.
            https://developers.onupkeep.com/#add-user-to-a-specific-team
            '''
            url = self.upkeep.url + self.epoint
            q = str(_teamid) + '/users/' + str(_uid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def user_from_team(self, _teamid, _uid,):
            '''
            This endpoint removes users for a specific team.
            https://developers.onupkeep.com/#removes-user-from-a-specific-team
            '''
            url = self.upkeep.url + self.epoint
            q = str(_teamid) + '/users/' + str(_uid)
            
            r = self.upkeep.delete(url + q)
            
            return r