import xmlrunner
import unittest
import docker
import requests
import time, sys

def bring_up_cnt(img_name = None, port = 8080, client = None):

    return client.containers.run(
        img_name + ":latest",
        remove=True,
        detach=True,
        ports={str(port)+"/tcp": port}
    )

def send_request(url):
    try:
        return requests.get(url).status_code
    except requests.ConnectionError as e:
        print("Connection error: {}".format(e))
        raise
    

class TestMicroServiceHTTPaccess(unittest.TestCase):

    ports = {
        "ms_a": 5000,
        "ms_b": 5001,
        "ms_c": 5002
    }

    ms_app = None

    url = "http://localhost"

    def setUp(self):

        self.dc_client = docker.from_env()
        self.cnt = bring_up_cnt(self.ms_app, self.ports[self.ms_app], self.dc_client)
        time.sleep(5)

        self.url += ''.join([":", str(self.ports[self.ms_app]), "/"])
        self._testMethodName

    def test_srv_access(self):
        self.assertEqual(send_request(self.url), 200, self.ms_app)

    def tearDown(self):
        self.cnt.remove(force=True)
        self.dc_client.close()


if __name__ == "__main__":
    ms_app = sys.argv.pop()
    TestMicroServiceHTTPaccess.ms_app = ms_app
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports', outsuffix=ms_app),
        failfast=False, 
        buffer=False, 
        catchbreak=False
    )