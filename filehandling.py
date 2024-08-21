# FILE HANDLING

# open() function takes two parameters; filename, and mode.

# four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist 

#Read File
def read_file(filename):
    try:
        with open(filename) as a:
            print(a.read())
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("Error : ",e)
    finally:
        print("read function ends")
filename = "demofile.txt"
# read_file(filename)
    
#Write File
def write_file(filename,content):
    try:
        with open(filename,"w") as b :
            b.write(content)
        print("file is successfully overwritten")
    except TypeError:
        print("content is missing")
    except Exception as e:
        print("Error : ",e )
    finally:
        print("write function ends")
filename = "defile.txt"
content = "this file is written and created newly "
# write_file(filename,content)

#Append File
def append_file(filename , content):
    try:
        with open(filename,"a") as c:
            c.write(content)
    except AttributeError:
        print("object has no attribute 'append'")
    except Exception as e:
        print("Error : ",e)
    finally:
        print("append function ends")
filename = "defile.txt"
content = "\nappend"        
# append_file(filename, content)

#Delete File

def delete_file(filename):
    import os 
    try:
        os.remove(filename)
        print("file successfully deleted")
    except FileNotFoundError:
        print("The system cannot find the file")
    except IOError:
        print("Error: could not delete file " )
    finally:
        print("delete function ends")
filename = "hello.txt"
# delete_file(filename)

def create_file(filename):
    try :
        with open(filename,"x") as d:
            d.write("new file created")
        print("file succesfully created ")
    except IOError:
        print("Error: could not create file  ")
    except FileExistsError:
        print("Error : File already exits")
    except Exception as e:
        print("Error : ",e)
    finally:
        print("create function ends!!!")
filename = "hello.txt"
create_file(filename)

# write_file("demofile.txt","write")
# read_file("demofile.txt")
# append_file("defile.txt","\nappend")
# delete_file("defile.txt")
