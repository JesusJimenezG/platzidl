#!/usr/bin/env python
import sys, os, re, getpass, io
from subprocess import Popen, PIPE, STDOUT

# IMPORTANT SETTINGS TO PREVENT SPAM BLOCKING OF YOUR ACCOUNT/IP AT PLATZILSIGHT #
SLEEP_INTERVAL =  10 #                                                          #
SLEEP_OFFSET = 5    #               Change this at your own risk.              #
RATE_LIMIT = "1M"    #                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DLPATH, USERNAME, PASSWORD = "", "", ""

PLATZIURL = "https://platzi.com/clases/"


def _get_usr_pw():
    """Requesting credentials from the user
    
    Raises:
        ValueError: User enters an empty password too many times
    """
    global USERNAME
    global PASSWORD

    print("Ingresa tus credenciales de Platzi")
    for i in range(3):
        u0 = input("Username: ")
        if u0 == "":
            print("Username cannot be empty, enter username again")
            continue
        else:
            USERNAME = u0
        
        print("Password (will no be displayed)")
        p0 = getpass.getpass(': ')
        if p0 != "":
            PASSWORD = p0
            break
        else:
            print('Password cannot be empty, enter password again')
    else:
        raise ValueError('Username or password was not given.')


def _cli_request(command, logpath):
    """Invokes an OS command line request
    
    Arguments:
        command {str} -- Full command string
        logpath {str} -- Path to stdout/stderror log file
    
    """
    os.chdir(os.path.dirname(logpath))
    print("Logging stdout/stderror to:\n" + logpath + "\n")

    with Popen(command, shell=True, stdout=PIPE, stderr=STDOUT) as process, \
        open(file=logpath, mode='at') as logfile:
            for line in io.TextIOWrapper(process.stdout, newline=''):
                sys.stdout.write(line)
                logfile.write(line)
                logfile.flush()

def _get_youtube_dl_cli_command(course, sleep_interval=SLEEP_INTERVAL, sleep_offset=SLEEP_OFFSET, rate_limit=RATE_LIMIT):
    """Putting together youtube-dl CLI command used to invoke the download requests.
    
    Arguments:
        course {str} -- Course identifier
    
    Keyword Arguments:
        sleep_interval {int} -- Minimum sleep time between video downloads (default: {150})
        sleep_offset {int} -- Randomize sleep time up to minimum sleep time plus this value (default: {50})
        rate_limit {str} -- Download speed limit (use "K" or "M" ) (default: {"1M"})
    
    Returns:
        str -- youtue-dl CLI command
    """
    # Quote and space char
    # # # # # # # # # # # #
    qu = '"';  sp = ' '   # 
    # Download parameters #

    platziurl = PLATZIURL
    username = qu + USERNAME + qu
    password = qu + PASSWORD + qu
    filename_template = qu + "%(playlist_index)s-%(chapter_number)s-%(title)s-%(resolution)s.%(ext)s" + qu
    minsleep = sleep_interval
    
    # CMD Tool # # # # # #
    tool = "youtube-dl"  #
    # Flags - useful settings when invoking download request
    usr =  "--username" + sp + username
    pw =  "--password" + sp + password
    minsl =  "--sleep-interval" + sp + str(minsleep)
    maxsl =  "--max-sleep-interval" + sp + str(minsleep + sleep_offset)
    lrate = "--limit-rate" + sp + rate_limit
    fn =  "-o" + sp + filename_template
    vrb =   "--verbose"
    curl = qu + platziurl + course + qu

    # Join command
    cli_components = [tool, usr, pw, minsl, maxsl, lrate, fn, vrb, curl]
    command = sp.join(cli_components)

    return command


def _platzidl(course):
    """Handling the video downloading requests for a single course
    
    Arguments:
        course {str} -- Course identifier
    
    Returns:
        str -- youtue-dl CLI command
    """
    # OS parameters - Creates course path and sets current course directory
    course_sinbarra = course.replace("/", '-')
    coursepath = os.path.join(DLPATH,course_sinbarra)
    if not os.path.exists(coursepath):
        os.mkdir(coursepath)
    os.chdir(coursepath)

    command = _get_youtube_dl_cli_command(course)
    
    # Execute command and log stdout/stderror
    logile = course_sinbarra + ".log"
    logpath = os.path.join(coursepath,logile)
    _cli_request(command, logpath)


def download_courses(courses):
    """Dowloading all courses listed in courselist.txt
    
    Arguments:
        courses {[type]} -- List of course ID
    
    """
    for course in courses:
        _platzidl(course)


def get_courses(scriptpath):
    """Parsing courselist.txt
    
    Arguments:
        scriptpath {str} -- Absolute path to script directory
    
    Returns:
        [str] -- List of course identifiers exposed by courselist.txt
    """
    # courses textfile prelocated inside script directory
    filelist = "courselist.txt"
    
    # Loops the list's lines and stores it as a python list
    filepath = os.path.join(scriptpath,filelist)
    courses = []
    try:
        with open(filepath, 'r+') as file:
            for line in file.readlines():
                if re.search(r'\S', line):
                    courses.append(line.strip())
        return courses
    except FileNotFoundError:
        print("There is no courselist.txt in script path. Terminating script ...")


def main():
    """Main execution
    Using command line to store username and password, loops
    through the course IDs and invoking download requests.
    """
    global DLPATH
    global USERNAME
    global PASSWORD
    if len(sys.argv) > 2:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]
    else:
        _get_usr_pw()

    # Script's absolute directory path
    scriptpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    
    # Download directory path
    dldirname = "Courses"
    DLPATH = os.path.join(scriptpath,dldirname)
    if not os.path.exists(DLPATH):
        os.mkdir(DLPATH)

    # Looping through the courses determined by get_courses() invoking download requests
    courses = get_courses(scriptpath)
    if courses:
        download_courses(courses)


if __name__ == "__main__":
    main()
