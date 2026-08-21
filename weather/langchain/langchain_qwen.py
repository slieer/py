import unittest
import os
from langchain_community.llms import Tongyi
from langchain_community.llms import VolcEngineMaasLLM
from langchain_community.llms import ChatGLM


os.environ["DASHSCOPE_API_KEY"] = ''

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here




if __name__ == '__main__':
    unittest.main()
