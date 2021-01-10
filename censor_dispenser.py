# These are the emails you will be censoring. The open() function
# is opening the text file that the emails are contained in and the
# .read() method is allowing us to save their contexts to the following
# variables.
import re
import sys

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation",
                     "learning algorithm", "her", "herself", "Helena"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed",
                  "out of control", "help", "unhappy", "bad", "upset", "awful",
                  "broken", "damage", "damaging", "dismal", "distressed", "concerning",
                  "horrible", "horribly", "questionable"]


def main():
    with open("email_one.txt", "r") as email:
        email = email.read()
        print(censor1(email))
    with open("email_two.txt", "r") as email:
        email = email.read()
        print(censor2(email, proprietary_terms))
    with open("email_three.txt", "r") as email:
        email = email.read()
        print(censor3(email, proprietary_terms, negative_words))
    with open("email_four.txt", "r") as email:
        email = email.read()
        print(censor4(email, proprietary_terms, negative_words))
    sys.exit(0)


def censor1(email):
    p = re.compile("learning algorithms", flags=re.IGNORECASE)
    tmp = re.findall(p, email)
    if len(tmp) > 0:
        email = re.sub(p, "*" * len(tmp[0]), email)
    return email


def censor2(email, lst):
    email = scrub(email, lst)
    return email


def censor3(email, lst, lst1):
    email = scrub(email, lst)
    email = scrub(email, lst1)
    return email


def censor4(email, lst, lst1):
    email = scrub(email, lst)
    email = scrub(email, lst1)
    p = re.compile(r"(?:[*])(\s\w+)")
    tmp = re.findall(p, email)
    if len(tmp) > 0:
        email = re.sub(p, "*" * len(tmp[0]), email)
    return email


def scrub(email, lst):
    for i in range(len(lst)):
        p = re.compile(rf"\b({lst[i]}s*)\b", flags=re.IGNORECASE)
        tmp = re.findall(p, email)
        if len(tmp) > 0:
            email = re.sub(p, "*" * len(tmp[0]), email)
    return email


main()
