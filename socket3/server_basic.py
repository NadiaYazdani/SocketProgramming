import os
import errno
import glob
import shutil
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher



def recursive_copy_files(source_path, destination_path, override=False):
#
#Recursively copies files from source  to destination directory.
#:param source_path: source directory
#:param destination_path: destination directory
#:param override if True all files will be overwritten otherwise skip if file exist
#:return: count of copied files
#

    files_count = 0

    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    items = glob.glob(source_path + '/*')

    for item in items:
        if os.path.isdir(item):
            path = os.path.join(destination_path, item.split('/')[-1])
            files_count += recursive_copy_files(source_path=item, destination_path=path, override=override)
        else:
            file = os.path.join(destination_path, item.split('/')[-1])
            if not os.path.exists(file) or override:
                #Copy file
                shutil.copyfile(item, file)
                files_count += 1
    return files_count

#Add method to create a file based on the data coming from the client
@dispatcher.add_method
def writefile(**kwargs):
    filename = "./" + kwargs["token"] + "/" + kwargs["filename"] 
    pathname="./" + kwargs["token"]
    #If the directory does not exist, then create it
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #print filename
    with open(filename, "w") as f: 
        f.write(kwargs["data"])
    recursive_copy_files(pathname, "./replica_test_1", override = True)
    return "Success"

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b
    #dispatcher["write-file"] = lambda a, filename: write_into_file(filename,a)

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    
    #recursive_copy_files("./x", "./replica_test_1", override = True)
    return Response(response.json, mimetype='application/json')
    
    

if __name__ == '__main__':
    run_simple('localhost', 4000, application)
    #recursive_copy_files("./x", "./replica_test_1", override = True)
    print ("hello")
