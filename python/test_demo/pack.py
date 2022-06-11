import os
import subprocess
import sys
import unittest


def check_env() -> bool:
    all_env = os.environ.get("PATH")
    git_status, git_version = subprocess.getstatusoutput('git --version')
    node_status, node_version = subprocess.getstatusoutput('node -v')
    npm_status, npm_version = subprocess.getstatusoutput('npm -v')
    if "git" in all_env.lower() or git_status == 0:
        print("Git ready.")
    else:
        return False
    if "nodejs" in all_env.lower() or node_status == 0:
        print("nodejs ready.")
    if "npm" in all_env.lower() or npm_status == 0:
        print("npm ready.")

    return True


class CompilerTest(unittest.TestCase):
    project_path = "C:/Users/dsg/DevEcoStudioProjects/MyApplication"
    pages = 'entry/build/default/intermediates/assets/default/ets/pages'
    node_modules_path = 'entry/build/default/intermediates/assets/default/node_modules'

    @classmethod
    def setUpClass(cls) -> None:
        if not check_env():
            sys.exit(1)
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
