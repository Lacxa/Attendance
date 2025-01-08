from datetime import datetime

from kivymd.toast import toast


class Uzuri:

    def parent(self, ):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/attendance-scan-c7af7-firebase-adminsdk-wew0v-95d6141355.json")
            initialize_app(cred, {'databaseURL': 'https://attendance-scan-c7af7-default-rtdb.firebaseio.com/'})
            ref = db.reference('parents').child(self.year()).child(self.month()).child(self.date())
            data = ref.get()
            if data:
                print("data")

            else:
                print("hola! no data available")

        return data

    def selected_parent(self, year, month, date):
        print(year, month, date)
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/attendance-scan-c7af7-firebase-adminsdk-wew0v-95d6141355.json")
            initialize_app(cred, {'databaseURL': 'https://attendance-scan-c7af7-default-rtdb.firebaseio.com/'})
            ref = db.reference('parents').child(year).child(month).child(date)
            data = ref.get()
            if data:
                print("parent")

            else:
                print("hola! no data available")

        return data

    def guest(self, ):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/attendance-scan-c7af7-firebase-adminsdk-wew0v-95d6141355.json")
            initialize_app(cred, {'databaseURL': 'https://attendance-scan-c7af7-default-rtdb.firebaseio.com/'})
            ref = db.reference('visitor').child("guest visitor").child(self.year()).child(self.month()).child(self.date())
            data = ref.get()
            if data:
                print("data2")

            else:
                print("hola! No guest available")

        return data

    def selected_guest(self, year, month, date ):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/attendance-scan-c7af7-firebase-adminsdk-wew0v-95d6141355.json")
            initialize_app(cred, {'databaseURL': 'https://attendance-scan-c7af7-default-rtdb.firebaseio.com/'})
            ref = db.reference('visitor').child("guest visitor").child(year).child(month).child(date)
            data = ref.get()

            if data:
                print("guest")
            else:
                print("No guest available")

        return data


    def school(self, ):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/attendance-scan-c7af7-firebase-adminsdk-wew0v-95d6141355.json")
            initialize_app(cred, {'databaseURL': 'https://attendance-scan-c7af7-default-rtdb.firebaseio.com/'})
            ref = db.reference('visitor').child("school visit").child(self.year()).child(self.month()).child(self.date())
            data = ref.get()
            if data:
                print("data3")

            else:
                print("hola! No school available")

        return data


    def selected_school(self, year, month, date ):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            cred = credentials.Certificate("credentials/attendance-scan-c7af7-firebase-adminsdk-wew0v-95d6141355.json")
            initialize_app(cred, {'databaseURL': 'https://attendance-scan-c7af7-default-rtdb.firebaseio.com/'})
            ref = db.reference('visitor').child("school visit").child(year).child(month).child(date)
            data = ref.get()

            if data:
                print("school")
            else:
                print("No school available")

        return data


    def year(self):
        current_time = str(datetime.now())
        date, time = current_time.strip().split()
        y, m, d = date.strip().split("-")

        return y

    def month(self):
        # Get the current datetime
        current_time = datetime.now()
        # Extract the full month name starting with a capital letter
        month_name = current_time.strftime("%B")

        return month_name

    def date(self):
        current_time = datetime.now()
        # Extract the date portion
        date, _ = str(current_time).strip().split()
        y, m, d = date.strip().split("-")
        # Remove leading zero by converting to an integer
        day_without_leading_zero = str(int(d))

        return day_without_leading_zero


    def day_remain(self, exp_date):
        nowoy = datetime.now().date().year
        nowom = datetime.now().date().month

        now = f"{nowoy}-{nowom}"

        m1 = int(now.strip().split("-")[1])

        m2 = int(exp_date.strip().split("-")[1])

        y1 = int(now.strip().split("-")[0])

        y2 = int(exp_date.strip().split("-")[0])

        yd = (y2 - y1) * 365

        ytm1 = 30 * m1

        ytm2 = 30 * m2

        v = ytm2 - ytm1 + yd

#Transfer.fetch_history(Transfer(), "2023-01-01", "2023-01-31")
#Uzuri.parent(Uzuri() )
#Uzuri.vistor(Uzuri())



