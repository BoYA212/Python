class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): The mobile number
            postcode (string): Postcode
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = "None"
        self.__symptoms = []

    def full_name(self):
        """the full name of the patient."""
        return f"{self.__first_name} {self.__surname}"

    def get_doctor(self):
        """the name of the linked doctor."""
        return self.__doctor

    def link(self, doctor):
        """give the patient a doctor.

        Args:
            doctor (string): The doctor's full name.
        """
        self.__doctor = doctor

    def add_symptom(self, symptom):
        """adds a symptom to the patient's list of symptoms.

        Args:
            symptom (string): A symptom description.
        """
        self.__symptoms.append(symptom)

    def print_symptoms(self):
        """prints all the symptoms of the patient."""
        if self.__symptoms:
            print("Symptoms:")
            for symptom in self.__symptoms:
                print(f"- {symptom}")
        else:
            print("No symptoms recorded.")

    def __str__(self):
        """a formatted string representation of the patient."""
        return f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}"

