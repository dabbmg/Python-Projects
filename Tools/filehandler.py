"""
Intended for command line use
-Mathew Dabb
"""
import json
import pickle
import os

class FileHandler:


    def readObjectFromFile(self, directory):
        obj = None
        dirStr = str(directory)
        try:
            if os.stat(dirStr).st_size == 0:
                print("\n---\nFile at directory: '%s' is empty." % dirStr)
            else:
                with open(dirStr, 'r') as f:
                    obj = json.loads(f.read())
        except FileNotFoundError:
            print("\nFile does not exist at directory '%s'" % dirStr)
        except:
            print("\nSomething went wrong reading object from file '%s'" % dirStr)
        return obj


    def writeObjectToFile(self, object, directory):
        dirStr = str(directory)
        try:
            with open(dirStr, 'w') as f:
                f.write("")
            with open(dirStr, 'w') as f:
                pickle.dump(object, f, -1)
        except:
            print("Something went wrong writing to file '%s'" + dirStr)

    

    def makeDirectory(self, parent_dir, directory):
        dirStr = str(directory)
        try:
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            print("\nDirectory '%s' created." % dirStr)
        except FileExistsError:
            print("\nFolder '%s' already exists." % dirStr)
        except FileNotFoundError:
            print("\nFolder path '%s' is invalid." % dirStr)
