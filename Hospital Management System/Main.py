# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be run when the program starts.
    
    """

    # patients
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin' for the admin, password is '123' for tge admin
    doctors = [
        Doctor('John', 'Smith', 'Internal Med.'),
        Doctor('Jone', 'Smith', 'Pediatrics'),
        Doctor('Jone', 'Carlos', 'Cardiology')
    ]
    patients = [
        Patient('Sara', 'Smith', 20, '07012345678', 'B1 234'),
        Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB'),
        Patient('David', 'Smith', 15, '07123456789', 'C1 ABC')
    ]
    discharged_patients = []

    # trying to log in until the login details are correct
    while True:
        try:
            if admin.login():
                running = True  # Allowing the program to run
                break
            else:
                print('Incorrect username or password.')
        except Exception as e:
            print(f"Error during login: {e}")

    while running:
        # print the menu
        print('\nChoose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patients')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == '2':
            # vvew or discharge patients
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient (Y/N): ').lower()

                if op in ('yes', 'y'):
                    admin.discharge(patients, discharged_patients)

                elif op in ('no', 'n'):
                    break

                else:
                    print('Please answer with yes or no.')

        elif op == '3':
            # view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # ppdate admin details
            admin.update_details()

        elif op == '6':
            # quit
            print('Exiting the program. Goodbye!')
            running = False

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again.')

if __name__ == '__main__':
    main()

