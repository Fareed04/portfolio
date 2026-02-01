from django.shortcuts import render

def home(request):
    # This dictionary mimics the state we had in React.
    # In the future, you can replace this with database queries like Project.objects.all()
    context = {
        'profile': {
            'name': 'Fareed Ologundudu',
            'roles': ["Data Analyst", "Python Developer", "ML Enthusiast", "Chess Strategist"],
            'about': "Transforming complex datasets into clear, actionable business strategies. Expert in Python, SQL, and Machine Learning pipelines.",
            'email': 'ologundudu.fareed@example.com',
            'linkedin': 'https://linkedin.com/in/fareedologundudu',
            'github': '#',
            'chess_elo': 1306,
        },
        'skills': {
            "Core Analysis": [
                {"name": "Python", "level": 90},
                {"name": "SQL", "level": 85},
                {"name": "Data Cleaning", "level": 95},
                {"name": "EDA", "level": 85}
            ],
            "Frameworks & DB": [
                {"name": "Django", "level": 75},
                {"name": "PostgreSQL", "level": 80},
                {"name": "Pandas/NumPy", "level": 90},
                {"name": "Scikit-Learn", "level": 70}
            ],
            "Visualization": [
                {"name": "Matplotlib", "level": 80},
                {"name": "Seaborn", "level": 80},
                {"name": "Tableau", "level": 65},
                {"name": "Plotly", "level": 75}
            ]
        },
        'projects': [
            {
                'title': "Customer Churn Prediction",
                'category': "Machine Learning",
                'description': "Built a predictive model to identify customers at risk of leaving. Utilized Random Forest and Logistic Regression.",
                'tags': ["Python", "Scikit-Learn", "Pandas", "Matplotlib"],
                'stats': "87% Accuracy",
                'link': "#",
                'github': "#",
                'bg': "from-blue-500/10 to-cyan-500/10"
            },
            {
                'title': "E-Commerce Sales Dashboard",
                'category': "Data Analysis",
                'description': "Interactive dashboard visualizing sales trends, regional performance, and top-selling categories using real-world transactional data.",
                'tags': ["SQL", "Tableau", "Excel"],
                'stats': "$2M+ Revenue Analyzed",
                'link': "#",
                'github': "#",
                'bg': "from-purple-500/10 to-pink-500/10"
            },
            {
                'title': "Housing Price Regression",
                'category': "Machine Learning",
                'description': "Developed a regression model to predict housing prices based on features like location, square footage, and year built.",
                'tags': ["Python", "XGBoost", "Seaborn"],
                'stats': "RMSE: 0.13",
                'link': "#",
                'github': "#",
                'bg': "from-orange-500/10 to-red-500/10"
            },
            {
                'title': "Web Scraper & API Integration",
                'category': "Engineering",
                'description': "Automated data collection pipeline using Python requests and BeautifulSoup to aggregate market data into PostgreSQL.",
                'tags': ["Python", "PostgreSQL", "Django"],
                'stats': "10k+ Records/Day",
                'link': "#",
                'github': "#",
                'bg': "from-emerald-500/10 to-green-500/10"
            }
        ]
    }
    return render(request, 'home/home.html', context)