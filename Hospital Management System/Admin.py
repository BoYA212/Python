from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """
        Print a list.
        Args:
            a_list (list): A list of printable items.
        """
        for index, item in enumerate(a_list):
            print(f'{index + 1:3}|{item}')

    def login(self):
        """
        A method that handles login.
        Raises:
            Exception: Raised when the username and password don't match the registered data.
        Returns:
            string: The username.
        """
        print("-----Login-----")

        # Get the details of the admin
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # Check if the username and password match the registered ones
        if username == self.__username and password == self.__password:
            print("Login successful.")
            return username
        else:
            raise Exception("Invalid username or password.")

    def find_index(self, index, items):
        """
        Check if an index is valid within a list.
        Args:
            index (int): The index to check.
            items (list): The list to check against.
        Returns:
            bool: True if valid, False otherwise.
        """
        return 0 <= index < len(items)

    def get_doctor_details(self):
        """
        Get the details needed to add a doctor.
        Returns:
            tuple: First name, surname, and speciality of the doctor in that order.
        """
        first_name = input("Enter the doctor's first name: ")
        surname = input("Enter the doctor's surname: ")
        speciality = input("Enter the doctor's speciality: ")
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that handles registering, viewing, updating, and deleting doctors.
        Args:
            doctors (list<Doctor>): The list of all doctors.
        """
        print("-----Doctor Management-----")

        # Menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Input: ")

        if op == '1':
            print("-----Register-----")
            first_name, surname, speciality = self.get_doctor_details()

            # Check if the name is already registered
            if any(doctor.get_first_name() == first_name and doctor.get_surname() == surname for doctor in doctors):
                print('Name already exists.')
            else:
                doctors.append(Doctor(first_name, surname, speciality))
                print('Doctor registered.')

        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        elif op == '3':
            print("-----Update Doctor's Details-----")
            self.view(doctors)
            try:
                index = int(input('Enter the ID of the doctor: ')) - 1
                if self.find_index(index, doctors):
                    doctor = doctors[index]

                    print('Choose the field to update:')
                    print(' 1 - First name')
                    print(' 2 - Surname')
                    print(' 3 - Speciality')

                    field = input('Input: ')

                    if field == '1':
                        new_first_name = input('Enter the new first name: ')
                        doctor.set_first_name(new_first_name)
                    elif field == '2':
                        new_surname = input('Enter the new surname: ')
                        doctor.set_surname(new_surname)
                    elif field == '3':
                        new_speciality = input('Enter the new speciality: ')
                        doctor.set_speciality(new_speciality)
                    else:
                        print('Invalid field selection.')
                else:
                    print("Doctor not found.")
            except ValueError:
                print('Invalid input.')

        elif op == '4':
            print("-----Delete Doctor-----")
            self.view(doctors)
            try:
                index = int(input('Enter the ID of the doctor to delete: ')) - 1
                if self.find_index(index, doctors):
                    doctors.pop(index)
                    print('Doctor deleted.')
                else:
                    print("Doctor not found.")
            except ValueError:
                print('Invalid input.')

        else:
            print('Invalid operation chosen. Check your input!')

    def view_patient(self, patients):
        """
        Print a list of patients.
        Args:
            patients (list<Patient>): List of all active patients.
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient.
        Args:
            patients (list<Patient>): The list of all active patients.
            doctors (list<Doctor>): The list of all doctors.
        """
        print("-----Assign-----")
        self.view_patient(patients)

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if not self.find_index(patient_index, patients):
                print('Patient not found.')
                return

            print("-----Doctors-----")
            self.view(doctors)
            doctor_index = int(input('Please enter the doctor ID: ')) - 1

            if self.find_index(doctor_index, doctors):
                patient = patients[patient_index]
                doctor = doctors[doctor_index]

                patient.link(doctor.full_name())
                doctor.add_patient(patient.full_name())

                print('The patient is now assigned to the doctor.')
            else:
                print('Doctor not found.')

        except ValueError:
            print('Invalid input.')

    def discharge(self, patients, discharged_patients):
        """
        allow the admin to discharge a patient when treatment is done.
        Args:
            patients (list<Patient>): The list of all active patients.
            discharged_patients (list<Patient>): The list of all discharged patients.
        """
        print("-----Discharge Patient-----")
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if self.find_index(patient_index, patients):
                discharged_patients.append(patients.pop(patient_index))
                print('Patient discharged.')
            else:
                print('Patient not found.')
        except ValueError:
            print('Invalid input.')

    def view_discharge(self, discharged_patients):
        """
        prints the list of all discharged patients.
        Args:
            discharged_patients (list<Patient>): The list of all discharged patients.
        """
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details(self):
        """
        allows the user to update and change username, password, and address.
        """
        print('Choose the field to update:')
        print(' 1 - Username')
        print(' 2 - Password')
        print(' 3 - Address')

        try:
            op = int(input('Input: '))

            if op == 1:
                self.__username = input('Enter the new username: ')
                print('Username updated.')

            elif op == 2:
                password = input('Enter the new password: ')
                if password == input('Re-enter the new password: '):
                    self.__password = password
                    print('Password updated.')
                else:
                    print('Passwords do not match.')

            elif op == 3:
                self.__address = input('Enter the new address: ')
                print('Address updated.')

            else:
                print('Invalid selection.')

        except ValueError:
            print('Invalid input.')

