import unittest
from app import app
import json
 
 
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
 
    def test_verify_approveCreditRequest(self):
        payload = json.dumps({"requiredAmount":5000,"taxId":2,"businessName":"Jhon"})
        response = self.app.post('/api/v1/credit', headers={"Content-Type": "application/json"}, data=payload)                
        obj = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(obj["result"], "Approved")
 
    def test_verify_undecidedCreditRequest(self):
        payload = json.dumps({"requiredAmount":50000,"taxId":2,"businessName":"Jhon"})
        response = self.app.post('/api/v1/credit', headers={"Content-Type": "application/json"}, data=payload)                
        obj = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(obj["result"], "Undecided")

    def test_verify_declinedCreditRequest(self):
        payload = json.dumps({"requiredAmount":99000,"taxId":2,"businessName":"Jhon"})
        response = self.app.post('/api/v1/credit', headers={"Content-Type": "application/json"}, data=payload)                
        obj = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(obj["result"], "Declined")
 
if __name__ == '__main__':
    unittest.main()