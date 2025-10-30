# 🎓 Analyse Student Performance

A comprehensive web-based application built with **Flask** and **MySQL** designed to help educational institutions track and analyze student academic performance. This application enables teachers and administrators to efficiently manage student records, track progress, and generate insightful performance analytics.

![Student Performance Dashboard](https://img.shields.io/badge/Status-Active-success)
![GitHub last commit](https://img.shields.io/github/last-commit/HutSreypov/Analyse_Student_Performance)
![GitHub license](https://img.shields.io/github/license/HutSreypov/Analyse_Student_Performance)

## 🚀 Key Features

- **📊 Student Management**
  - Add, edit, and view student records
  - Track academic performance across multiple subjects
  - Monitor attendance and participation

- **📈 Performance Analytics**
  - Visualize student progress with interactive charts
  - Generate performance reports by class or individual
  - Identify learning trends and areas for improvement

- **🔐 User Authentication**
  - Secure login/registration system
  - Role-based access control (Admin/Teacher/Student)
  - Password reset functionality

- **🔍 Advanced Search & Filter**
  - Search students by name, ID, or class
  - Filter results by subject, grade level, or date range
  - Export data to CSV/Excel

- **📱 Responsive Design**
  - Mobile-friendly interface
  - Clean, intuitive dashboard
  - Accessible on all devices

## 🧱 Project Structure

```
Analyse-Student-Performance/
│
├── app.py                    # Main Flask application
│
├── /models                  # Database models
│   ├── __init__.py
│   ├── user_model.py        # User authentication and management
│   └── score_model.py       # Student score management
│
├── /routes                  # Application routes
│   ├── __init__.py
│   ├── auth_routes.py       # Authentication routes
│   ├── score_routes.py      # Score management routes
│   └── student_routes.py    # Student management routes
│
├── /templates               # HTML templates (Jinja2)
│   ├── base.html            # Base template
│   ├── auth/                # Authentication templates
│   │   ├── login.html
│   │   └── register.html
│   └── dashboard/           # Dashboard templates
│       ├── index.html
│       ├── scores/          # Score management
│       │   ├── list.html
│       │   ├── add.html
│       │   └── edit.html
│       └── students/        # Student management
│           ├── list.html
│           └── profile.html
│
├── /static                 # Static files
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Main JavaScript file
│   └── img/                # Images and icons
│
├── /database
│   └── schema.sql          # Database schema and initial setup
│
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 🛠️ Technology Stack

| Category       | Technologies                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Frontend**   | HTML5, CSS3, JavaScript, Bootstrap 5, Chart.js                              |
| **Backend**    | Python 3.8+, Flask 2.0+                                                     |
| **Database**   | MySQL 8.0+                                                                 |
| **APIs**       | RESTful API endpoints                                                      |
| **Deployment** | Docker, Gunicorn, Nginx                                                    |
| **CI/CD**      | GitHub Actions                                                             |
| **Testing**    | pytest, unittest                                                           |

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/HutSreypov/Analyse_Student_Performance.git
   cd Analyse-Student-Performance
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   - Create a MySQL database
   - Update the database configuration in `config.py`
   - Import the database schema:
     ```bash
     mysql -u username -p database_name < database/schema.sql
     ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_URI=mysql+pymysql://username:password@localhost/db_name
   ```

6. **Run the application**
   ```bash
   flask run
   ```
   The application will be available at `http://localhost:5000`

## 🚀 Deployment

For production deployment, it's recommended to use Gunicorn with Nginx:

```bash
# Install Gunicorn
pip install gunicorn

# Run the application with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions or suggestions, please contact [Your Name] at [your-email@example.com] or open an issue on GitHub.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Chart.js](https://www.chartjs.org/)

---

<div align="center">
  Made with ❤️ by [Sreypov Hut] | © 2025 All Rights Reserved
</div>
