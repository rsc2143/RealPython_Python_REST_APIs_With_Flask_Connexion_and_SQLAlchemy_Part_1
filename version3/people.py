from datetime import datetime
from flask import (
    make_response,
    abort
)

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:       json string of all people
    """
    # Create the list of people from our data
    return [PEOPLE(key) for key in sorted(PEOPLE.keys())]

def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with the information for that person searched by the last name

    :param lname: last name of person to find
    :return:      person matching last name
    """
    # Does the person exist in peopl
    if(lname in PEOPLE):
        person = PEOPLE.get(lname)

    # otherwise, report person as not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
    return person

def create(person):
    """
    This function creates a new person in the people structure
    based on the passed data for that person

    :param person: person to create in people structure
    :return:       201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname" = lname,
            "fname" = fname,
            "timestamp" = get_timestamp()
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )
    #Otherwise, they exist and thats an error
    else:
        abort(
            406, "Person with last name {lname} already exits".format(lname=lname)
        )

def update(lname, person):
    """
    This function updates an existing person in the people structure

    :param lname:  Last name of person to update
    :param person: person to create in people structure
    :return:       updated person structure
    """

    # Does this person exist in people structure
    if lname in PEOPLE[lname]:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = person.get("timestamp")

        return PEOPLE[lname]

    # otherwise its an error
    else:
        abort(
            404, "Person with last name {lname} not found".fotmat(lname=lname)
        )

def delete(lname):
    """
    This function deletes an existing person in the people structure

    :param lname:  Last name of person to be deleted
    :return:       200 on successful delete, 404 on not found
    """
    # Does the person exist in people structure
    if lname in PEOPLE[lname]:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname)
        )
    # otherwise its an error
    else:
        abort(
        404, "Person with last name {lname} not found".format(lname=lname)
        )
