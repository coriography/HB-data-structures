"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    # retrieve file
    cohort_data_file = open(filename)
    # loop through each line of file
    for line in cohort_data_file:
      # trim last two characters of each line
      line = line[:-1]
      # split/tokenize
      line_list = line.split("|")
      # unpack line
      f_name, l_name, house, professor, cohort_date = line_list
      # return set of house names
      # set constructor takes list of names
      if house != '':
        houses.add(house)
    
    # print(houses)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # retrieve file
    cohort_data_file = open(filename)

    # loop though each line of the file
    for line in cohort_data_file:    
    # trim last two characters of each line
      line = line[:-1]
      # split/tokenize by | character
      line_list = line.split("|")
      # unpack line by assigning each item in line_list to a variable
      f_name, l_name, house, professor, date = line_list
      # if cohort argument is empty, return all names
      # else return empty list
      if cohort == "All":
        # add all students to list
        students.add(f"{f_name} {l_name}")
      else:
      # if cohort variable is not provided, use default, and return all names
      # check if line contains cohort element
        if date != "": 
      # if cohort name in specified line contains the cohort, then add names to students list
          if date == cohort:
            students.add(f"{f_name} {l_name}")
            
      # if cohort variable is not a cohort provided, return empty list
        else: 
          break

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
