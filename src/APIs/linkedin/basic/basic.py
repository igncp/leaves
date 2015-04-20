import os, sys
inserted_path = '/../linkedin_helpers'
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + inserted_path))
import linkedin_helpers


def main():
  application = linkedin_helpers.authenticate()
  profile = application.get_profile()
  message = "The account's owner name is {} {}".format(profile['firstName'], profile['lastName'])
  print message

if __name__ == "__main__":
  main()
