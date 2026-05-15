from Login.login import do_login
import dotenv
if __name__ == "__main__":
    path = dotenv.find_dotenv()
    envs = dict(dotenv.dotenv_values()).items()
    file = open(path, "w")
    print(envs)
    result = ""
    for key, value in envs:
        result += "{}={}\n".format(key, value)
    print(result)
    file.write(result)
    file.close()
