# upkeep-py

This package aims to help with easy Rest API calls to a user's onupkeep.com account.\
It will include all of the API calls from the documentation found [here](https://developers.onupkeep.com/)

#### -- Project Status: [On-Going]

### Required Packages:
* requests:
    * to make API calls
* base64:
    * simple password encryption
* ciso8601:
    * fast unix time conversion

## Quick Start:
```python
[1]: from upkeep import upkeep

# instantiate and login to return session_key
[2]: u = upkeep('user@onupkeep.com', 'password')

    {
      "success": true,
      "result": {
        "sessionToken": "r:4a25eddbf5aj42jk323f1472724hc43f",
        "expiresAt": "2018-12-31T00:00:00.000Z"
      }
    }

# create a user by passing in credentials
[4]: u.users.create_user('newuser@onupkeep.com', 'ADMIN', 'trickyPass',
                         firstName='Marty', lastName='McFly',
                         phoneNumber='800-123-4567'
                        )

     {
       "success": true,
       "results": [
         {
           "id": "fjQXLsOvG7",
           "accountType": "ADMIN",
           "email": "newuser@onupkeep.com",
           "firstName": "Marty",
           "lastName": "McFly",
           "phoneNumber": "800-123-4567"
           "dateOfLastLogin": "2018-05-22T03:05:27.262Z",
           "createdAt": "2017-12-06T19:23:09.162Z",
           "updatedAt": "2017-12-08T18:41:44.335Z"
         }
       ]
     }
        

# return all users in your organization
[3]: u.users.get_all_users()

    {
      "success": true,
      "result": {
        "id": "fjQXLsOvG7",
        "accountType": "ADMIN",
        "email": "newuser@onupkeep.com",
        "firstName": "Marty",
        "lastName": "McFly",
        "phoneNumber": "800-123-4567",
        "createdAt": "2017-12-06T19:23:09.162Z",
        "updatedAt": "2017-12-08T18:41:44.335Z"
      }
    }

```


## Contact
* Feel free to contact me if any questions, or comments on the project - [hello@dancorley.com]

