# Care Every Home

**Care Every Home** is an online platform designed to help communities access medical equipment through rental and donation services, guided by the principle that **"Every home deserves equal access to healthcare."**

This initiative allows users to rent high-quality medical equipment at affordable prices and offers a way for those with unused equipment to donate it to help others. The system encourages user feedback and suggestions to improve the service for the benefit of the community—especially the elderly, individuals with chronic illnesses, and families in need. The project's overarching goal is to build a sustainable and accessible healthcare support network for everyone.

---

##  Introduction

**Care Every Home** was developed by a team of university students to address the need for accessible medical equipment services. Built using the Django Framework, the platform is optimized for desktop and mobile use and aims to promote community involvement.

The project was inspired by real challenges faced by individuals who lack access to medical equipment due to financial or geographic limitations. Care Every Home serves as a centralized system for offering and receiving healthcare support.

---

##  User Stories

###  Renting Medical Equipment

* As a user in need of medical equipment,
* I want a system where I can choose from a list of available devices,
* So that I can rent, pay, and receive the equipment conveniently.

###  Donating Medical Equipment

* As a user with unused medical devices,
* I want a feature to donate equipment,
* So that I can help improve access to healthcare in my community.

###  Providing Feedback

* As a past renter or donor,
* I want to leave feedback on my experience,
* So that the service can continuously improve.

###  Responding to Donation Requests

* As a user who has medical equipment to donate,  
* I want to view a list of specific donation requests from people in need,  
* So that I can choose to respond and send equipment to help someone directly.

---

##  How to Use the Platform

### 1. Sign Up

1. Go to the "Log in" or "Sign Up" page.
2. Fill in your details and confirm via email.
3. Log in to access services.

### 2. Rent Equipment

1. Go to "Products" and choose a device.
2. Click "Rent Now" and select duration.
3. Enter shipping details and confirm.

### 3. Donate Equipment

1. Go to "Profile" > "Donate".
2. Enter item details and upload photos.
3. Submit and await contact for pickup.

### 4. Return Equipment & Payment

1. Go to "Profile" > "Rentals".
2. Select the item to return.
3. Make payment and confirm return.

### 5. Shipping Cost Calculation

1. Enter your address when renting.
2. System calculates and displays shipping.
3. Review total and proceed to payment.

### 6. Submit Feedback

1. Go to "Product Detail" or "Profile".
2. Click "Post Review", write feedback.
3. Submit the review.

### 7. Respond to Donation Requests

1. Go to "Browse Requests" under the "Donate" section.
2. Review requests submitted by users.
3. Click "Donate" next to the request you want to fulfill.
4. Fill in donation details and confirm.
5. Requester will be notified and status updated in your donation dashboard.

+--------------------+
| User in Need       |
| requests donation  |
+--------------------+
          ↓
+--------------------+
| Donater views      |
| "Browse Requests"  |
+--------------------+
          ↓
+--------------------+
| Selects a request  |
+--------------------+
          ↓
+-----------------------------+
| Fills in donation details   |
+-----------------------------+
          ↓
+--------------------+
| System notifies    |
| the requester      |
+--------------------+

---

##  Features

* Rent affordable, high-quality medical equipment
* Donate unused devices to support others
* Mobile and desktop-friendly interface
* Transparent shipping cost based on location
* Ratings and reviews for service improvement
* Admin panel for tracking and managing inventory
* Multiple user roles: normal user and shopkeeper
* Real-time tracking system (planned)
* Community-centered design

---

##  Why This Project?

Care Every Home emerged from the observation that many people lack access to necessary healthcare tools while others have them sitting unused. This platform connects these groups, promoting sustainability and generosity.

It also serves as a practical application of software engineering principles, especially in UI/UX, database management, and web development. Django was chosen for its scalability, security, and clean structure. The project also supports skill development in teamwork, communication, and agile methodologies.

---

##  Future Development

Planned improvements include:

* Real-time delivery tracking
* Direct chat between users and staff
* QR code and bank transfer payment options
* Mobile app
* Admin analytics dashboard
* Smart matching of donations to local needs
* Multi-language support
* Two-factor authentication
* Equipment usage history by user

---

##  Technologies Used

* **Backend:** Python 3.10, Django Framework
* **Database:** SQLite (dev), PostgreSQL (prod)
* **Frontend:** HTML5, CSS3, JavaScript
* **Styling:** Bootstrap 5 / Tailwind CSS
* **Version Control:** Git, GitHub
* **Deployment:** Docker (planned), Heroku (planned)

**GitHub Repository:** [Care Every Home on GitHub](https://github.com/ChadapaNgamchuen/dsi202_2025)

---

##  Project Installation & Usage

### Step-by-step Setup

1. **Clone the Repository**

```bash
git clone https://github.com/ChadapaNgamchuen/dsi202_2025
cd care-every-home
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set Up the Database**

```bash
python manage.py migrate
```

4. **Create a Superuser (Optional)**

```bash
python manage.py createsuperuser
```

5. **Run the Development Server**

```bash
python manage.py runserver
```

Once running, visit `http://127.0.0.1:8000/` in your browser to use the platform locally.
youtube:https://youtu.be/QGGe0VhAvho
---
"
