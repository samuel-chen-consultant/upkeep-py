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
        self.patch = self.patch
        
        # create sub-functions (un-comment as creating)
        self.users = self.users(self)
        self.customers = self.customers(self)
        self.vendors = self.vendors(self)
        self.teams = self.teams(self)
        self.assets = self.assets(self)
        self.locations = self.locations(self)
        self.parts = self.parts(self)
        self.requests = self.requests(self)
        self.work_orders = self.work_orders(self)
        self.prev_maint = self.prev_maint(self)
        self.work_order_sched = self.work_order_sched(self)
        self.meters = self.meters(self)
        self.purchase_order = self.purchase_order(self)
        self.p_order_category = self.p_order_category(self)
        self.reporting = self.reporting(self)
        


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
        # Do I need this???
        if not self.loggedin:
            raise ()
    
    def logout(self):
        '''
        helper function to remove a session token
        should be used after each session
        '''
        url = self.url + 'auth'
        data = {'Session-Token': self.token}
        r = requests.delete(url, data = data)
        print("you've successfully been logged out")
        self.loggedin = 0
    
    
    def get(self, url, **kwargs):
        '''helper function for the various subclasses'''
        
        params = kwargs
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
            
            r = self.upkeep.patch(url, **kwargs)
            
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
        used to query within teams endpoint.
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
            
            r = self.upkeep.patch(url, **kwargs)
            
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
        
    class assets:
        '''
        used to query within assets endpoint.
        https://developers.onupkeep.com/#assets
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'assets/'
            

        def create_asset(self, name, **kwargs):
            '''
            This endpoint creates a new asset.
            https://developers.onupkeep.com/#create-an-asset
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, name = name, **kwargs)
            
            return r

        def get_all_teams(self, **kwargs):
            '''
            This endpoint retrieves all assets for your account.
            https://developers.onupkeep.com/#get-all-assets
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_asset(self, _assetid):
            '''
            This endpoint retrieves a specific asset.
            https://developers.onupkeep.com/#get-a-specific-asset
            '''
            url = self.upkeep.url + self.epoint + str(_assetid)
            
            r = self.upkeep.get(url)
            
            return r
        
        def update_asset(self, _assetid, **kwargs):
            '''
            This endpoint updates a specific asset.
            https://developers.onupkeep.com/#update-a-specific-asset
            '''
            url = self.upkeep.url + self.epoint + str(_assetid)
            
            r = self.upkeep.patch(url)
            
            return r
        
        def delete_team(self, _assetid):
            '''
            This endpoint deletes a specific team.
            https://developers.onupkeep.com/#delete-a-specific-asset
            '''
            url = self.upkeep.url + self.epoint + str(_assetid)
            
            r = self.upkeep.delete(url)
            
            return r
        
        def user_to_asset(self, _assetid, _uid):
            '''
            This endpoint adds users for a specific asset.
            https://developers.onupkeep.com/#add-user-to-a-specific-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/users/' + str(_uid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def user_from_asset(self, _assetid, _uid,):
            '''
            This endpoint removes users for a specific asset.
            https://developers.onupkeep.com/#removes-user-from-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/users/' + str(_uid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
        def team_to_asset(self, _assetid, _teamid):
            '''
            This endpoint adds teams to a specific asset.
            https://developers.onupkeep.com/#assign-team-to-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/teams/' + str(_teamid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def team_from_asset(self, _assetid, _teamid):
            '''
            This endpoint removes users for a specific asset.
            https://developers.onupkeep.com/#removes-team-from-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/teams/' + str(_teamid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
        def cust_to_asset(self, _assetid, _custid):
            '''
            This endpoint adds customers to a specific asset.
            https://developers.onupkeep.com/#assign-customer-to-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/customers/' + str(_custid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def cust_from_asset(self, _assetid, _custid):
            '''
            This endpoint removes customers for a specific asset.
            https://developers.onupkeep.com/#removes-customer-from-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/customers/' + str(_custid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
        def vend_to_asset(self, _assetid, _vendid):
            '''
            This endpoint adds vendors to a specific asset.
            https://developers.onupkeep.com/#assign-vendor-to-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/vendors/' + str(_vendid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def vend_from_asset(self, _assetid, _vendid):
            '''
            This endpoint removes customers for a specific asset.
            https://developers.onupkeep.com/#remove-assigned-vendor-from-an-asset
            '''
            url = self.upkeep.url + self.epoint
            q = str(_assetid) + '/customers/' + str(_vendid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
    class locations:
        '''
        used to query within locations endpoint.
        https://developers.onupkeep.com/#locations
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'locations/'
        
        def create_location(self, name, **kwargs):
            '''
            This endpoint creates a new team.
            https://developers.onupkeep.com/#create-a-location
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, name = name, **kwargs)
            
            return r
        
        def get_all_locations(self, **kwargs):
            '''
            This endpoint retrieves all locations for your account.
            https://developers.onupkeep.com/#get-all-locations
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_location(self, _locid, **kwargs):
            '''
            This endpoint retrieves a specific team.
            https://developers.onupkeep.com/#get-a-specific-location
            '''
            url = self.upkeep.url + self.epoint + str(_locid)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
       
        def update_location(self, _locid, **kwargs):
            '''
            This endpoint updates a specific team.
            https://developers.onupkeep.com/#update-a-specific-location
            '''
            url = self.upkeep.url + self.epoint + str(_locid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def delete_location(self, _locid):
            '''
            This endpoint deletes a specific team.
            https://developers.onupkeep.com/#delete-a-specific-location
            '''
            url = self.upkeep.url + self.epoint + str(_locid)
            
            r = self.upkeep.delete(url)
            
            return r
        
        
        def user_to_location(self, _locid, _uid):
            '''
            This endpoint adds users to a specific location.
            https://developers.onupkeep.com/#add-user-to-a-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/users/' + str(_uid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def user_from_location(self, _locid, _userid):
            '''
            This endpoint removes a customer from a specific location.
            https://developers.onupkeep.com/#remove-assigned-user-from-an-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/customers/' + str(_userid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
        def team_to_location(self, _locid, _teamid):
            '''
            This endpoint adds a team to a specific location.
            https://developers.onupkeep.com/#add-team-to-a-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/users/' + str(_teamid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def team_from_location(self, _locid, _teamid):
            '''
            This endpoint removes a team for a specific location.
            https://developers.onupkeep.com/#remove-assigned-team-from-an-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/customers/' + str(_teamid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
        def cust_to_location(self, _locid, _custid):
            '''
            This endpoint adds a user to a specific location.
            https://developers.onupkeep.com/#add-customer-to-a-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/users/' + str(_custid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def cust_from_location(self, _locid, _custid):
            '''
            This endpoint removes a customer for a specific location.
            https://developers.onupkeep.com/#remove-assigned-customer-from-a-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/customers/' + str(_custid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
        def vend_to_location(self, _locid, _vendid):
            '''
            This endpoint adds a vendor to a specific location.
            https://developers.onupkeep.com/#add-vendor-to-a-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/users/' + str(_vendid)
            
            r = self.upkeep.post(url + q)
            
            return r
        
        def vend_from_location(self, _locid, _vendid):
            '''
            This endpoint removes a customer for a specific location.
            https://developers.onupkeep.com/#remove-assigned-vendor-from-a-location
            '''
            url = self.upkeep.url + self.epoint
            q = str(_locid) + '/customers/' + str(_vendid)
            
            r = self.upkeep.delete(url + q)
            
            return r
        
    class parts:
        '''
        used to query within parts endpoint.
        https://developers.onupkeep.com/#parts
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'parts/'
            

        def create_part(self, name, **kwargs):
            '''
            This endpoint creates a new part.
            https://developers.onupkeep.com/#create-a-part
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, name = name, **kwargs)
            
            return r
        
        def get_all_parts(self, **kwargs):
            '''
            This endpoint retrieves all parts for your account.
            https://developers.onupkeep.com/#get-all-locations
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_part(self, _partid, **kwargs):
            '''
            This endpoint retrieves a specific part.
            https://developers.onupkeep.com/#get-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_partid)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
       
        def update_part(self, _partid, **kwargs):
            '''
            This endpoint updates a specific part.
            https://developers.onupkeep.com/#update-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_locid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def delete_part(self, _partid):
            '''
            This endpoint deletes a specific part.
            https://developers.onupkeep.com/#delete-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_partid)
            
            r = self.upkeep.delete(url)
            
            return r
        
    class requests:
        '''
        used to query within requests endpoint.
        https://developers.onupkeep.com/#requests
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'requests/'
        
        def create_request(self, title, **kwargs):
            '''
            This endpoint creates a new request.
            https://developers.onupkeep.com/#create-a-request
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, title = title, **kwargs)
            
            return r
        
        def get_all_requests(self, **kwargs):
            '''
            This endpoint retrieves all parts for your account.
            https://developers.onupkeep.com/#get-all-locations
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_request(self, _reqid, **kwargs):
            '''
            This endpoint retrieves a specific part.
            https://developers.onupkeep.com/#get-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_reqid)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
       
        def cancel_request(self, _reqid, **kwargs):
            '''
            This endpoint cancels a specific request, triggering and email to creator.
            https://developers.onupkeep.com/#cancel-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_reqid) + '/cancel'
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def delete_request(self, _reqid):
            '''
            This endpoint deletes a specific request.
            https://developers.onupkeep.com/#delete-a-specific-request
            '''
            url = self.upkeep.url + self.epoint + str(_reqid)
            
            r = self.upkeep.delete(url)
            
            return r
        
    class work_orders:
        '''
        used to query within work orders endpoint.
        docs - https://developers.onupkeep.com/#work-orders
        '''
        
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'work-orders/'
            
        def create_work_order(self, title, **kwargs):
            '''
            This endpoint creates a new work order.
            
            If connected to Zapier, data will be sent for work order trigger.
            
            If a user is assigned, and email will be sent to them, else email to admins.
            https://developers.onupkeep.com/#create-a-work-order
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, title = title, **kwargs)
            
            return r
        
        def get_all_work_orders(self, **kwargs):
            '''
            This endpoint retrieves all work orders for your account.
            https://developers.onupkeep.com/#get-all-work-orders
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_work_order(self, _workid, **kwargs):
            '''
            This endpoint retrieves a specific work order.
            https://developers.onupkeep.com/#get-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_workid)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
       
        def upate_work_order(self, _workid, **kwargs):
            '''
            This endpoint updates a specific work order.
            
            If connected to Zapier, data will be sent for status change trigger.
            
            https://developers.onupkeep.com/#update-a-specific-work-order
            '''
            url = self.upkeep.url + self.epoint + str(_workid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def upate_work_order_message(self, _workid, message):
            '''
            This endpoint updates a specific work order.
            https://developers.onupkeep.com/#update-work-order-messages
            '''
            url = self.upkeep.url + self.epoint + str(_workid) + '/update-messages/'
            
            r = self.upkeep.post(url, text = message)
            
            return r
        
        def delete_work_order(self, _workid):
            '''
            This endpoint deletes a specific request.
            https://developers.onupkeep.com/#delete-a-specific-work-order
            '''
            url = self.upkeep.url + self.epoint + str(_workid)
            
            r = self.upkeep.delete(url)
            
            return r
        
    class prev_maint:
        '''
        used to query within preventative maintenance endpoint.
        docs - https://developers.onupkeep.com/#work-orders
        '''
        
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'preventative-maintenance/'
            
        def create_order(self, title, schedule, **kwargs):
            '''
            This endpoint creates a new work order.
            
            If connected to Zapier, data will be sent for work order trigger.
            
            If a user is assigned, and email will be sent to them, else email to admins.
            https://developers.onupkeep.com/#create-a-preventative-maintenance-work-order
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, title = title, recurringSchedule = schedule, **kwargs)
            
            return r
        
        def get_all_orders(self, **kwargs):
            '''
            This endpoint retrieves all work orders for your account.
            * only retrieves root work order, read more in docs
            https://developers.onupkeep.com/#get-all-preventative-maintenance-work-orders
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_order(self, _previd, **kwargs):
            '''
            This endpoint retrieves a specific preventative maintenance order.
            https://developers.onupkeep.com/#get-a-preventative-maintenance-work-order
            '''
            url = self.upkeep.url + self.epoint + str(_previd)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
       
        def upate_order(self, _previd, **kwargs):
            '''
            This endpoint updates a specific work order.d
            https://developers.onupkeep.com/#update-a-specific-preventative-maintenance-work-order
            '''
            url = self.upkeep.url + self.epoint + str(_workid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def delete_order(self, _previd):
            '''
            This endpoint deletes a specific request.
            https://developers.onupkeep.com/#delete-a-specific-work-order
            '''
            url = self.upkeep.url + self.epoint + str(_previd)
            
            r = self.upkeep.delete(url)
            
            return r
        
        
    class work_order_sched:
        '''
        used to query within work order schedule endpoint.
        docs - https://developers.onupkeep.com/#work-order-schedule
        '''
        
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'work-order-schedule'
            
        def get_schedule(self, **kwargs):
            '''
            This endpoint retrieves the schedule of all preventative maintenance work orders for your account.
            https://developers.onupkeep.com/#get-the-schedule-of-preventative-maintenance-work-orders
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
    class meters:
        '''
        used to query within meters endpoint.
        docs - https://developers.onupkeep.com/#meters
        '''

        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'meters/'
        
        def create_meter(self, name, units, frequency, **kwargs):
            '''
            This endpoint creates a new meter.
            https://developers.onupkeep.com/#meters
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, title = title, units = units,
                                 frequency = frequency, **kwargs)
            return r
        
        def get_all_meters(self, **kwargs):
            '''
            This endpoint retrieves all meters for your account.
            https://developers.onupkeep.com/#get-all-meters
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_work_order(self, _workid, **kwargs):
            '''
            This endpoint retrieves a specific work order.
            https://developers.onupkeep.com/#get-a-specific-part
            '''
            url = self.upkeep.url + self.epoint + str(_workid)
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
       
        def get_meter(self, _meterid, **kwargs):
            '''
            This endpoint updates a specific work order.
            https://developers.onupkeep.com/#get-a-specific-meter
            '''
            url = self.upkeep.url + self.epoint + str(_meterid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def update_meter(self, _meterid, name, units, frequency, **kwargs):
            '''
            This endpoint updates a specific meter.
            https://developers.onupkeep.com/#update-a-specific-meter
            '''
            url = self.upkeep.url + self.epoint + str(_meterid)
            
            r = self.upkeep.patch(url, name = name, units = units,
                                  frequency = frequency, **kwargs)
            
            return r
        
        def delete_meter(self, _meterid):
            '''
            This endpoint deletes a specific meter.
            https://developers.onupkeep.com/#delete-a-specific-meter
            '''
            url = self.upkeep.url + self.epoint + str(_meterid)
            
            r = self.upkeep.delete(url)
            
            return r
        
        def reading_to_meter(self, _meterid, value):
            '''
            This endpoint adds a reading to a meter
            https://developers.onupkeep.com/#add-a-reading-to-a-meter
            '''
            url = self.upkeep.url + self.epoint + str(_meterid) + '/readings'
            
            r = self.upkeep.post(url, value = value)
            
            return r
        
        def get_all_readings_meter(self, _meterid, **kwargs):
            '''
            This endpoint retrieves all readings for a meter.
            https://developers.onupkeep.com/#get-all-readings-for-a-meter
            '''
            url = self.upkeep.url + self.epoint + str(_meterid) + '/readings'
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def create_meter_notification(self, _meterid, title, value,
                                      frequency, **kwargs):
            '''
            This endpoint creates a new meter notification for particular meter.
            https://developers.onupkeep.com/#create-a-meter-notification
            '''
            
            url = self.upkeep.url + self.epoint + str(_meterid) + '/notifications'
            
            r = self.upkeep.post(url, title = title, triggerValue = value, 
                                 triggerFrequency = frequency, **kwargs)
            
            return r
        
        def get_all_meter_notifications(self, _meterid, **kwargs):
            '''
            This endpoint retrieves all notifications for particular meter.
            https://developers.onupkeep.com/#get-all-meter-notifications
            '''
            
            url = self.upkeep.url + self.epoint + str(_meterid) + '/notifications'
            
            r = self.upkeep.get(url, **kwargs)
            
        def get_meter_notification(self, _meterid, _notifid, **kwargs):
            '''
            This endpoint retrieves all notifications for particular meter.
            https://developers.onupkeep.com/#get-all-meter-notifications
            '''
            
            url = self.upkeep.url + self.epoint + str(_meterid)
            q = '/notifications' + _notifid
            
            r = self.upkeep.get(url + q, **kwargs)
            
            return r
        
        def update_meter_notification(self, _meterid, _notifid, **kwargs):
            '''
            This endpoint updates a specific meter notification.
            https://developers.onupkeep.com/#update-a-specific-meter-notification
            '''
            
            url = self.upkeep.url + self.epoint + str(_meterid)
            q = '/notifications' + _notifid
            
            r = self.upkeep.patch(url + q, **kwargs)
            
            return r
        
        def del_meter_notification(self, _meterid, _notifid):
            '''
            This endpoint deletes a specific meter notification.
            https://developers.onupkeep.com/#delete-a-specific-meter-notification
            '''
            url = self.upkeep.url + self.epoint + str(_meterid)
            q = '/notifications' + _notifid
            
            r = self.upkeep.delete(url + q, **kwargs)
            
            return r
        
    class purchase_order:
        '''
        used to query within purchase order endpoint.
        docs - https://developers.onupkeep.com/#purchase-orders
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'purchase-orders/'
            
        def create_order(self, title, **kwargs):
            '''
            This endpoint creates a new purchase order.
            https://developers.onupkeep.com/#purchase-orders
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, title = title, **kwargs)
            
            return r
        
        def get_all_orders(self, **kwargs):
            '''
            This endpoint retrieves all Purchase Orders for your account.
            https://developers.onupkeep.com/#get-all-purchase-orders
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        def get_order(self, _orderid, **kwargs):
            '''
            This endpoint retrieves a specific Purchase Order.
            https://developers.onupkeep.com/#get-a-specific-purchase-order
            '''
            url = self.upkeep.url + self.epoint + str(_orderid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def update_order(self, _orderid, **kwargs):
            '''
            This endpoint updates a specific meter.
            https://developers.onupkeep.com/#update-a-specific-meter
            '''
            url = self.upkeep.url + self.epoint + str(_orderid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def patrially_fulfill_order(self, _orderid, **kwargs):
            '''
            This API call partially fulfills a Purchase Order.
            https://developers.onupkeep.com/#partially-fulfill-a-purchase-order
            '''
            url = self.upkeep.url + self.epoint + str(_orderid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def del_order(self, _orderid):
            '''
            This endpoint deletes a specific Purchase Order.
            https://developers.onupkeep.com/#delete-a-specific-purchase-order
            '''
            url = self.upkeep.url + self.epoint + str(_orderid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def add_message(self, _orderid, message):
            '''
            This endpoint adds update message for particular Purchase Order.
            https://developers.onupkeep.com/#add-text-message-to-purchase-order
            '''
            url = self.upkeep.url + self.epoint
            q = str(_orderid) + '/update-messages'
            
            r = self.upkeep.patch(url, text = message, **kwargs)
            
            return r
        
    class p_order_category:
        '''
        used to query within purchase order category endpoint.
        docs - https://developers.onupkeep.com/#purchase-order-category
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            self.epoint = 'purchase-order-categories/'
            
        def create_category(self, name, **kwargs):
            '''
            This endpoint creates a new purchase order category.
            https://developers.onupkeep.com/#purchase-orders
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.post(url, name = name)
            
            return r
        
        def get_all_categories(self, **kwargs):
            '''
            This endpoint retrieves all purchase order categories for your account.
            https://developers.onupkeep.com/#get-all-purchase-orders-categories
            '''
            url = self.upkeep.url + self.epoint
            
            r = self.upkeep.get(url)
            
            return r
        
        def get_category(self, _catid, **kwargs):
            '''
            This endpoint retrieves a specific Purchase Order Category.
            https://developers.onupkeep.com/#get-all-purchase-orders-categories
            '''
            url = self.upkeep.url + self.epoint + str(_catid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def update_category(self, _catid, **kwargs):
            '''
            This endpoint updates a specific meter.
            https://developers.onupkeep.com/#update-a-specific-meter
            '''
            url = self.upkeep.url + self.epoint + str(_catid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
        def del_category(self, _catid):
            '''
            This endpoint deletes a specific Purchase Order Category.
            https://developers.onupkeep.com/#delete-a-specific-purchase-order-category
            '''
            url = self.upkeep.url + self.epoint + str(_catid)
            
            r = self.upkeep.patch(url, **kwargs)
            
            return r
        
    class reporting:
        '''
        IN BETA
        
        Public api for for fetching various aggregate counts eg Work Orders open, In progress, Avg time to complete etc. User can group by different entities and apply various filters. By default data is fetched for Work Orders created within last month
        
        https://developers.onupkeep.com/#get-work-order-aggregate-counts
        '''
        def __init__(self, upkeep):
            self.upkeep = upkeep
            
        def get_agg_counts(self, **kwargs):
            
            url = 'https://analytics-api.onupkeep.com/v2/work-orders/dashboard'
            
            r = self.upkeep.get(url, **kwargs)
            
            return r
        
        
        
# if you've made it this far, thanks for taking the time to peruse my work. 
# let's chat - hello@dancorley.com
            