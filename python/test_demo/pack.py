import os
import subprocess
import unittest


class CompilerTest(unittest.TestCase):
    project_path = "C:/Users/dsg/DevEcoStudioProjects/MyApplication"
    pages = 'entry/build/default/intermediates/assets/default/ets/pages'
    node_modules_path = 'entry/build/default/intermediates/assets/default/node_modules'

    @classmethod
    def setUpClass(cls) -> None:
        subprocess.check_output("npm run build", shell=True, cwd=cls.project_path)

    def setUp(self) -> None:
        os.chdir(path=self.project_path)
        print(os.getcwd())
        if "node_modelus" in os.listdir():
            subprocess.run("npm install")

    @classmethod
    def tearDownClass(cls) -> None:
        subprocess.run("npm run clean", shell=True, cwd=cls.project_path)
        print("clean over!")

    def tearDown(self) -> None:
        print("END")

    def test_compile_pages(self):
        page_path = os.path.join(self.project_path, self.pages)
        file_list = []
        for root, dirs, files in os.walk(page_path):
            for file in files:
                if file.endswith((".js", ".abc")):
                    file_list.append(file)
        self.assertIn("index.abc", file_list, msg='pages compiler fail')

    def test_compile_nodeModules(self):
        modules_path = os.path.join(self.project_path, self.node_modules_path)
        file_list = []
        for root, dirs, files in os.walk(modules_path):
            for file in files:
                if file.endswith((".js", ".abc")):
                    file_list.append(file)
        self.assertIn("index.abc", file_list, msg='node_modules compiler fail')


if __name__ == "__main__":
    unittest.main()
