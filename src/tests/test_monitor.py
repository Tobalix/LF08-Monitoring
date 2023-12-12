import unittest
import os
import shutil
import tempfile
import time
from src.python_version.monitor import cpu_log, ram_log  # Replace 'your_module' with the actual module name

class TestLoggingFunctions(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_cpu_log(self):
        log_file_path = os.path.join(self.temp_dir, 'test_CPU.log')
        cpu_log(log_file_path)
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            log_contents = log_file.read()
            self.assertIn('CPU:', log_contents)
            # Assuming psutil.cpu_percent() always returns a value >= 80 in your test
            self.assertIn('WARNING', log_contents)

    def test_ram_log(self):
        log_file_path = os.path.join(self.temp_dir, 'test_RAM.log')
        ram_log(log_file_path)
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            log_contents = log_file.read()
            self.assertIn('RAM:', log_contents)
            # Assuming psutil.virtual_memory().percent always returns a value >= 80 in your test
            self.assertIn('WARNING', log_contents)

if __name__ == '__main__':
    unittest.main()
