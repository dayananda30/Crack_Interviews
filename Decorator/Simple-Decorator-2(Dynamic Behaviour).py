'''
Run CICD only during night time

'''
from datetime import datetime

def not_during_the_day(func):
    def wrapper():
        if 7 >= datetime.now().hour > 22:
            func()     # Run the CICD
        else:
            print("CICD will not trigger During Day Time")
            pass  # Don't run the CICD

    return wrapper

def run_cicd():
    print("Triggering Test Suites for nightly run")


if __name__ == '__main__':
    run_cicd = not_during_the_day(run_cicd)
    run_cicd()



