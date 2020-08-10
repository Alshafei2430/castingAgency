import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


username = "shafei"
password = "012"

wrong_token = "ndfgdkgkjfj"
assistant_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh2TWZuU3RNTnZaUC1ob2xCTUpDLSJ9.eyJpc3MiOiJodHRwczovL2Rldi0xMnRoeHI2aS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNzE4MWQ3MTQ2OGMwMDEzMDAwMzA1IiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1OTQzMzE3NTgsImV4cCI6MTU5NDQxODE1OCwiYXpwIjoiaEtLOUhFWmdWVExkd2JqWm83OHpJTHVVSXFpZ0o5VUoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWUiLCJnZXQ6bW92aWVzIl19.c5rwb7e1fX7An5Kua159vUQnJfAic0rpl4VgqqzRN98IXA0VeNVYIGZnmYb4aK5s2Gdl9DIV-sE_VSaRx6MGqkwe8IfxDR7H5XNmNUqJrJF7l24OI7UkZsklc0y1HHWXdIwVgeRoNLhYqE1zuqO_Y5kUuS-xxEBHQrn35ve9uAM6K87GSB94HrJaJzQF2FEDAOXux-4gpAYy8iyou3gEB-5MCCCqtXtyjO8uJxyqL3a9NoycOBGwNhhBBnpME6RcW_H6yyOy-ND9jGI5gGsENukb2YzkUdABjv6OStdopUHEWIgj47w8jYN53d2GWw4Y2Q5foImLWu04SOj5AnMAcA"
director_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh2TWZuU3RNTnZaUC1ob2xCTUpDLSJ9.eyJpc3MiOiJodHRwczovL2Rldi0xMnRoeHI2aS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNzE5MzNmZDMwZTIwMDEzNjY0YzFhIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1OTQzMzE1NzcsImV4cCI6MTU5NDQxNzk3NywiYXpwIjoiaEtLOUhFWmdWVExkd2JqWm83OHpJTHVVSXFpZ0o5VUoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWUiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.HzRhfPebLQcOSR1nH6BkQ99c_o4wlFwLMED3YEXrJyRhpZFKSQYb92XVe8ZjwwgsG3LabfF9YV5ekF_fUnn0-zKSvpvzkGLT_iDcDH978t82TXniImKBHWJb9i1iCGL1DnLAs7pYrLjnoJsMnC1AP-XdwmbC0vA_0sS6LnVB_PLEGlFErQNwQdB7poVyFItjVUEJDjqLCvDWyc5fFgCuPfl8AI-67YlkDOcPp6tjDa1yXbSi1C9OuuueK6tzt2kmC5NrfJm36PqHE4aJEhqOWJQW5_LlM5-cEhMfvA1hGAsJ98OMMPO3Zsy6sL6VTTIRquiq_rnhCN2exv9aygEJhA"
e_p_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilh2TWZuU3RNTnZaUC1ob2xCTUpDLSJ9.eyJpc3MiOiJodHRwczovL2Rldi0xMnRoeHI2aS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwNzExZWVmZDMwZTIwMDEzNjY0YmViIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1OTQzMzE5NjQsImV4cCI6MTU5NDQxODM2NCwiYXpwIjoiaEtLOUhFWmdWVExkd2JqWm83OHpJTHVVSXFpZ0o5VUoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWUiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.p7ElWIYSzmbMzM-P0GfnxVM8gTcHd5xvdHdpI-xLbnTi1duF1MCfEpLvaSGJbvivwOhs4HdQrzoZgIpzwFLDuLnk89pF_SEfqLZoN5IbfS2u_yH1QeIYClAznWT2v4c65esINiLK2j7DgZf2GnovzYhZX5tctPPxLF-cfgE7vsgB7k7e5-azFmnItZO-4jzGyqo_fpRa8zr885G98rQqXv33Zf5AN2gxig6O0h0_-7Zlw9pGkBmY7ZMCBRijYX5WtffcPczCETL46K1PpPdHfPtGo8KJCv_dlPDrsDXbPnNM5L3BT2WfBmFQ3CpIgBXaNckqrW-ew2NFtx_VV2kleA"



class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency"
        self.database_path = "postgresql://{}:{}@{}/{}".format(username, password, 'localhost:5433', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_movies(self): #done
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_405_method_not_allowed(self): #done
        res = self.client().post('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')


    def test_get_actors(self): #done
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_405_not_allowed(self): #done
        res = self.client().post('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')


    def test_401_authError(self): #done
        res = self.client().get('/actors/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')
    

    def test_401_authError(self): #done
        res = self.client().get('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')


    def test_create_actor(self):
        res = self.client().post('/actors/create',
            json={
                "name": "fathy",
                "age": 17,
                "gender": "male"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {director_token}')
            ]    
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_401_authError(self): #done
        res = self.client().post('/actors/create',
            json={
                "name": "fathy",
                "age": 17,
                "gender": "male"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {assistant_token}')
            ]    
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_create_movie(self):
        res = self.client().post('/movies/create',
            json={
                "title": "iron man",
                "release_date": "2025-5-19"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {e_p_token}')
            ]    
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_401_authError(self): #done
        res = self.client().post('/movies/create',
            json={
                "title": "iron man",
                "release_date": "2025-5-19"
            },
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {director_token}')
            ]    
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')


    def test_delete_actor(self): #done
        res = self.client().delete('/actors/3',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {e_p_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_404_resource_not_found(self): #done
        res = self.client().delete('/actors/1000',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {e_p_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_delete_movie(self): #done
        res = self.client().delete('/movies/3',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {e_p_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_resource_not_found(self): #done
        res = self.client().delete('/movies/1000',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {e_p_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')


    def test_404_creation_not_allowed(self): #done
        res = self.client().get('/movies/create/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_edit_actor(self): #done
        res = self.client().patch('/actors/1',
            json={"name": "hani"},
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {director_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_401_unauthorized(self): #done
        res = self.client().patch('/actors/1',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {wrong_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')


    def test_edit_movie(self): #done
        res = self.client().patch('/movies/2',
            json={"title": "show time"},
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {e_p_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_401_unauthorized(self): #done
        res = self.client().patch('/movies/1',
            headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {wrong_token}')
            ]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unauthorized')
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()