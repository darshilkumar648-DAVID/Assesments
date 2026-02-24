# ------- QUE 1 ------- #

class ClinicAppointment:
    def __init__(self):
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm", "4pm"]
        self.appointments = []
        self.max_per_slot = 3

    ### Book Appointment ###

    def book_appointment(self):
        print("\n--- Book Your Appointment Here ---")

        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        if 0 >= age <= 140:
            print("❌ Invalid Age.")
            return
        mobile = input("Enter Mobile Number: ")
        if len(mobile) != 10:
            print("❌ Invalid Mobile Number. Must be 10 digits.")
            return
        doctor = input("Enter Preferred Doctor Name: ")

        print("\nAvailable Time Slots Are:")
        for i in range(len(self.time_slots)):
            print(i + 1, self.time_slots[i])

        choice = int(input("Select Slot Number You Want: "))
        if choice < 1 or choice > len(self.time_slots):
            print("❌ Invalid Slot Number.")
            return
        
        slot = self.time_slots[choice - 1]

        # Check slot availability #
        count = 0
        for app in self.appointments:
            if app["Doctor"] == doctor and app["Slot"] == slot:
                count = count + 1

        if count < self.max_per_slot:
            appointment = {
                "Name": name,
                "Age": age,
                "Mobile": mobile,
                "Doctor": doctor,
                "Slot": slot
            }
            self.appointments.append(appointment)
            print("✅ Your Appointment Booked Successfully!")
        else:
            print("❌ Your Selected Slot",slot,"is Full For This Doctor. Please Select Another Slot Or Choose Another Doctor.")

    ### View Appointment ###

    def view_appointment(self):
        print("\n--- View Your Appointment Here ---")
        mobile = input("Enter Your Mobile Number: ")

        found = False
        for app in self.appointments:
            if app["Mobile"] == mobile:
                print("\nAppointment Details:")
                print("Name:", app["Name"])
                print("Age:", app["Age"])
                print("Doctor:", app["Doctor"])
                print("Time Slot:", app["Slot"])
                found = True

        if found == False:
            print("❌ No Such Appointment Found.")

    ### Cancel Appointment ###

    def cancel_appointment(self):
        print("\n--- Cancel Your Appointment Here ---")
        mobile = input("Enter mobile number: ")

        found = False
        for app in self.appointments:
            if app["Mobile"] == mobile:
                print("\n--- Appointment Found ---")
                print("Name:", app["Name"])
                print("Age:", app["Age"])
                print("Doctor:", app["Doctor"])
                print("Time Slot:", app["Slot"])
                confirm = input("Do you really want to cancel? (yes/no): ")
                if confirm == "yes":
                    self.appointments.remove(app)
                    print("✅ Appointment Cancelled Successfully!")
                else:
                    print("❌ Cancellation Aborted.")
                found = True
                return
            if found == False:
                print("❌ No Such Appointment Found to Cancel.")
                self.appointments.remove(app)
                print("✅ Appointment Cancelled Successfully!")
                return

        print("❌ No Such Appointment Found to Cancel.")

    ### Main Menu ###

    def menu(self):
        while True:
            print("\n===== Clinic Appointment System =====")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Doctor Wise Appointment")
            print("5. Show Available Slots")
            print("6. Exit")

            choice = input("Enter [1,2,3,4] No. As per Your Requirement: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointment()
            elif choice == "3":
                self.cancel_appointment()
            elif choice == "4":
                self.doctor_wise_appointments()
            elif choice == "5":
                self.show_available_slots()
            elif choice == "6":
                print("Bye bye!")
                break
            else:
                print("❌Sorry You Entered Invalid Number. Please Try again.")

    def doctor_wise_appointments(self):
        doctor = input("Enter Doctor Name: ")
        found = False

        print("\n--- Appointments for Doctor", doctor, "---")

        for app in self.appointments:
            if app["Doctor"] == doctor:
                print("-----------------------")
                print("Name:", app["Name"])
                print("Mobile:", app["Mobile"])
                print("Slot:", app["Slot"])
                found = True
        if found == False:
            print("No appointments for this doctor.")

    def show_available_slots(self):
        doctor = input("Enter Doctor Name: ")

        print("\n--- Available Slots for", doctor, "---")

        for slot in self.time_slots:
            count = 0
            for app in self.appointments:
                if app["Doctor"] == doctor and app["Slot"] == slot:
                    count = count + 1
            if count < self.max_per_slot:
                print(slot, "→ Available")
            else:
                print(slot, "→ FULL")

clinic = ClinicAppointment()
clinic.menu()


# ------- QUE 2 ------- #

class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 101 

    ### New Admission ###
    def new_admission(self):
        name = input("Enter Student Name: ")
        age = int(input("Enter Age (5-18): "))
        student_class = int(input("Enter Class (1-12): "))
        mobile = input("Enter Guardian Mobile Number: ")

        # Age Validation 
        if age < 5 or age > 18:
            print("❌ Invalid Age! Age must be between 5 and 18.")
            return

        # Class Validation
        if student_class < 1 or student_class > 12:
            print("❌ Invalid Class! Class must be between 1 and 12.")
            return

        # Mobile Validation
        if not mobile.isdigit() or len(mobile) != 10:
            print("❌ Invalid Mobile Number! Must be exactly 10 digits And Also Not Any Alphabet.")
            return

        # Assign Student ID
        student_id = self.next_id
        self.next_id += 1

        # Save Record
        self.students[student_id] = {
            "Name": name,
            "Age": age,
            "Class": student_class,
            "Mobile": mobile
        }

        print(f"✅ Admission Successful! Student ID = {student_id}")

    ### View Student Details ###
    def view_student(self):
        student_id = int(input("Enter Student ID: "))
        student = self.students.get(student_id)

        if student:
            print("\n--- Student Details ---")
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("❌ Student ID Not Found!")

    ### Update Student Info ###
    def update_student(self):
        student_id = int(input("Enter Student ID to Update: "))

        if student_id not in self.students:
            print("❌ Student ID Not Found!")
            return

        print("1. Update Mobile Number")
        print("2. Update Class")
        choice = int(input("Choose Option: "))

        if choice == 1:
            new_mobile = input("Enter New Mobile Number: ")
            if not new_mobile.isdigit() or len(new_mobile) != 10:
                print("❌ Invalid Mobile Number!")
            else:
                self.students[student_id]["Mobile"] = new_mobile
                print("✅ Mobile Number Updated!")

        elif choice == 2:
            new_class = int(input("Enter New Class (1-12): "))
            if new_class < 1 or new_class > 12:
                print("❌ Invalid Class!")
            else:
                self.students[student_id]["Class"] = new_class
                print("✅ Class Updated!")

        else:
            print("❌ Invalid Choice!")

    ### Remove Student Record ###
    def remove_student(self):
        student_id = int(input("Enter Student ID to Remove: "))

        if student_id in self.students:
            del self.students[student_id]
            print("✅ Student Record Removed!")
        else:
            print("❌ Student ID Not Found!")

    ### Main Menu ###
    def menu(self):
        while True:
            print("\n===== School Management System =====")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")

            choice = int(input("Enter Number[1,2,3,4,5] Of Your Choice: "))

            if choice == 1:
                self.new_admission()
            elif choice == 2:
                self.view_student()
            elif choice == 3:
                self.update_student()
            elif choice == 4:
                self.remove_student()
            elif choice == 5:
                print("👋 Exiting System...")
                break
            else:
                print("❌ Invalid Choice!")

school = SchoolManagement()
school.menu()


# ------- QUE 3 ------- #

import uuid

class BusReservation:
    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            1: {"route": "Mumbai to Pune", "price": 500, "seats": 40},
            2: {"route": "Delhi to Jaipur", "price": 600, "seats": 40},
            3: {"route": "Bangalore to Chennai", "price": 700, "seats": 40},
            4: {"route": "Hyderabad to Goa", "price": 800, "seats": 40}
        }
        
        # Store tickets
        self.tickets = {}

        # Seat tracking per route
        self.booked_seats = {route_id: [] for route_id in self.routes}

    def show_routes(self):
        print("\nAvailable Routes:")
        for route_id, info in self.routes.items():
            print(f"{route_id}. {info['route']} - ₹{info['price']} "
                  f"(Available Seats: {40 - len(self.booked_seats[route_id])})")

    def book_ticket(self):
        self.show_routes()
        
        try:
            route_choice = int(input("\nEnter route number: "))
            if route_choice not in self.routes:
                print("Invalid route selection.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        if len(self.booked_seats[route_choice]) >= 40:
            print("Sorry! No seats available on this route.")
            return
        
        name = input("Enter passenger name: ")
        age = input("Enter passenger age: ")
        mobile = input("Enter mobile number: ")
        
        # Assign seat
        seat_number = len(self.booked_seats[route_choice]) + 1
        self.booked_seats[route_choice].append(seat_number)
        
        # Generate ticket ID
        ticket_id = str(uuid.uuid4())[:8]
        
        ticket_info = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": self.routes[route_choice]["route"],
            "price": self.routes[route_choice]["price"],
            "seat": seat_number
        }
        
        self.tickets[ticket_id] = ticket_info
        
        print("\nTicket Booked Successfully!")
        print(f"Ticket ID: {ticket_id}")
        print(f"Seat Number: {seat_number}")

    def view_ticket(self):
        ticket_id = input("Enter Ticket ID: ")
        ticket = self.tickets.get(ticket_id)
        
        if ticket:
            print("\nTicket Details:")
            for key, value in ticket.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Ticket not found.")

    def cancel_ticket(self):
        ticket_id = input("Enter Ticket ID to cancel: ")
        
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            
            # Find route id
            for route_id, info in self.routes.items():
                if info["route"] == ticket["route"]:
                    self.booked_seats[route_id].remove(ticket["seat"])
                    break
            
            del self.tickets[ticket_id]
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found.")


### Menu Driven Program ###

def main():
    system = BusReservation()
    
    while True:
        print("\n===== Bus Reservation System =====")
        print("1. Show Available Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")
        
        choice = input("Enter [1,2,3,4,5] Number Of Your Choice: ")
        
        if choice == "1":
            system.show_routes()
        elif choice == "2":
            system.book_ticket()
        elif choice == "3":
            system.view_ticket()
        elif choice == "4":
            system.cancel_ticket()
        elif choice == "5":
            print("Thank You For Using The System.")
            break
        else:
            print("Invalid Choice. Try Again.")


if __name__ == "__main__":
    main()