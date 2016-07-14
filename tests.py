import os
import app
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

    #setup
    def setUp(self):
        self.app = app.app.test_client()

    def testPOSTandDBUpdate(self):
        rv = self.app.post('/tx', data=dict(owner="Testivus",model="Skynet"),follow_redirects=True)
        unittest.TestCase.assertEqual(self,str(rv),'<Response streamed [200 OK]>','POST Failed')

    def testGET(self):
        rv = self.app.get('/api/return/person/Testivus')
        unittest.TestCase.assertEqual(self,rv.status_code,200)

        rv = self.app.get('/api/return/asset/Skynet')
        unittest.TestCase.assertEqual(self,rv.status_code,200)

    def testDBPersistence(self):
        rv = self.app.get('/api/return/person/Testivus')
        datastring = rv.get_data(as_text=True)
        unittest.TestCase.assertIn(self,'Testivus',datastring)

        rv = self.app.get('/api/return/asset/Skynet')
        datastring = rv.get_data(as_text=True)
        unittest.TestCase.assertIn(self,'Skynet',datastring)









#test runner
suite = unittest.TestLoader().loadTestsFromTestCase(AppTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
