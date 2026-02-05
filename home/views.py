from django.shortcuts import render
from django.http import Http404

# Global data source with IDs and Filter Categories added for functionality
PROJECTS_DATA = [
    {
        'id': 1,
        'title': "Bank Customer Churn Prediction",
        'category': "Deep Learning",
        'filter_category': "Predictive Modeling", # Added for button mapping
        'description': "Developed a deep learning pipeline using Artificial Neural Networks (ANN) to forecast customer attrition with 87% accuracy. Integrated a real-time Streamlit dashboard to transform model probabilities into actionable retention strategies.",
        'long_description': "This project involved building a robust deep learning pipeline using TensorFlow and Keras to tackle the challenge of bank customer churn. Beyond just prediction, I integrated a real-time Streamlit dashboard that translates complex model probabilities into actionable retention strategies for account managers. The model successfully handles class imbalance and provides clear insights into the drivers of attrition.",
        'tags': ["TensorFlow", "Keras", "Python", "Deep Learning", "Streamlit", "Scikit-Learn"],
        'stats': "87% Accuracy",
        'link': "https://github.com/Fareed04/Customer-Churn-Prediction-using-ANN",
        'github': "https://github.com/Fareed04/Customer-Churn-Prediction-using-ANN",
        'bg': "from-blue-600/20 to-indigo-600/20"
    },
    {
        'id': 2,
        'title': "Medical Appointment No-Show Analysis",
        'category': "Data Analytics & ML",
        'filter_category': "Predictive Modeling",
        'description': "Analyzed 110,000+ medical records to identify drivers of patient absenteeism. Developed a cost-sensitive Logistic Regression model that achieved 86% recall, effectively solving the 'accuracy trap' in imbalanced healthcare data.",
        'long_description': "In this end-to-end analytics project, I examined over 110,000 records to understand why patients miss appointments. I navigated the 'accuracy trap' inherent in imbalanced healthcare data by focusing on recall metrics. The resulting Logistic Regression model achieved 86% recall for no-shows, allowing healthcare providers to implement targeted reminder systems and optimize scheduling.",
        'tags': ["Python", "EDA", "Scikit-Learn", "Feature Engineering", "Predictive Modeling", "Seaborn"],
        'stats': "86% No-Show Recall",
        'link': "https://github.com/Fareed04/medical-appointment-no-shows-analysis",
        'github': "https://github.com/Fareed04/medical-appointment-no-shows-analysis",
        'bg': "from-teal-500/10 to-emerald-500/10"  
    },
    {
        'id': 3,
        'title': "E-Commerce Logistics Analysis",
        'category': "Data Analytics & SQL",
        'filter_category': "Business Analytics",
        'description': "Analyzed 100,000+ Olist e-commerce records using SQL and Python to identify logistical bottlenecks. Discovered a 'Double Loss' pattern where late deliveries increased freight costs by 12% while slashing customer satisfaction scores by 40%.",
        'long_description': "Using the Olist e-commerce dataset, I performed deep-dive SQL queries and Python-based visualization to uncover a 'Double Loss' pattern. This pattern showed that late deliveries didn't just hurt satisfaction—they directly increased freight costs by 12%. My analysis provided a roadmap for logistics optimization that balances cost and speed.",
        'tags': ["SQL", "Python", "Pandas", "Matplotlib", "Logistics Analysis", "Business Intelligence"],
        'stats': "12% Cost Reduction Potential",
        'link': "https://github.com/Fareed04/logistics-performance-analysis/blob/main/README.md",
        'github': "https://github.com/Fareed04/logistics-performance-analysis/blob/main/README.md",
        'bg': "from-orange-500/10 to-amber-500/10"
    },
    {
        'id': 4,
        'title': "Sales Performance Intelligence",
        'category': "Financial Analytics",
        'filter_category': "Business Analytics",
        'description': "Evaluated $2.2M in multi-year transaction data to decode revenue drivers. Performed a deep-dive 'Volume vs. Value' analysis to explain historical sales fluctuations and identified high-margin technology assets as the primary growth engine.",
        'long_description': "This project focused on financial analytics for a high-volume retail client. By processing $2.2M in transaction data, I isolated the key variables affecting quarterly revenue. The 'Volume vs. Value' analysis revealed that while transaction volume was stable, the shift towards lower-margin products was eroding profits. The insights led to a strategic pivot towards high-margin technology assets.",
        'tags': ["Python", "Pandas", "Trend Analysis", "Financial Modeling", "Matplotlib", "Business Intelligence"],
        'stats': "$2.2M Revenue Analyzed",
        'link': "https://github.com/Fareed04/sales-performance-analysis",
        'github': "https://github.com/Fareed04/sales-performance-analysis",
        'bg': "from-green-500/10 to-emerald-500/10"
    },
    {
        'id': 5,
        'title': "Chess.com Personal Analytics",
        'category': "Personal Growth / API Analysis",
        'filter_category': "Exploratory Analysis",
        'description': "Engineered a data pipeline using the Chess.com API to extract and analyze 2,000+ personal games. Developed custom visualizations to identify high-win-rate openings (75% with Englund Gambit) and pinpoint tactical weaknesses in specific variations.",
        'long_description': "Combining my passion for chess with data engineering, I built a custom pipeline to extract game data from the Chess.com API. I cleaned and structured data from over 2,000 games to perform granular analysis on opening repertoires. The analysis highlighted a 75% win rate with the Englund Gambit but revealed mid-game tactical weaknesses in closed positions.",
        'tags': ["Python", "APIs", "Data Visualization", "Pandas", "Seaborn", "Exploratory Data Analysis"],
        'stats': "2,000+ Games Analyzed",
        'link': "https://github.com/Fareed04/Chess-data-analysis",
        'github': "https://github.com/Fareed04/Chess-data-analysis",
        'bg': "from-slate-700/10 to-gray-500/10"
    },
    {
        'id': 6,
        'title': "Healthcare Speech Translator",
        'category': "Applied AI",
        'filter_category': "Python Development",
        'description': "Developed a real-time translation platform using a Django backend to manage speech-to-text processing. Engineered a low-latency bridge between Python-based translation logic and browser Web Speech APIs to facilitate multilingual patient care.",
        'long_description': "To bridge communication gaps in healthcare settings, I built a full-stack Django application that provides real-time speech translation. The system uses Web Speech APIs for capture and a Python backend for processing and logging. It was designed with low latency in mind to ensure smooth doctor-patient interactions.",
        'tags': ["Python", "Django", "JavaScript", "NLP", "Speech-to-Text", "REST API"],
        'stats': "Real-Time Processing",
        'link': "https://healthcaretranslation-ruddy.vercel.app", 
        'github': "https://github.com/Fareed04/healthcare_translation_project", 
        'bg': "from-red-600/10 to-rose-600/10"
    },
]

def home(request):
    context = {
        'profile': {
            'name': 'Fareed Ologundudu',
            'roles': [
                "Python Data Analyst",
                "Operations & Business Analyst"
            ],
            'about': (
                "I help teams identify and fix operational inefficiencies by analyzing messy, real-world data "
                "and translating it into decisions managers can act on immediately. "
                "Experienced in Python-driven analysis, SQL, and end-to-end analytics workflows."
            ),
            'email': 'ologundudufareed@gmail.com',
            'linkedin': 'https://linkedin.com/in/fareed-ologundudu-129506249',
            'github': 'https://github.com/Fareed04'
        },
        'skills': {
            "Core Analytics": [
                {"name": "Python", "level": 90},
                {"name": "SQL", "level": 85},
                {"name": "Data Cleaning & Validation", "level": 95},
                {"name": "Exploratory Data Analysis (EDA)", "level": 85}
            ],
            "Data & Backend": [
                {"name": "Pandas / NumPy", "level": 90},
                {"name": "PostgreSQL", "level": 80},
                {"name": "Django / APIs", "level": 75},
                {"name": "Scikit-Learn (Applied)", "level": 70}
            ],
            "Reporting & Visualization": [
                {"name": "Matplotlib", "level": 80},
                {"name": "Seaborn", "level": 80},
                {"name": "Plotly", "level": 75},
                {"name": "Tableau", "level": 65}
            ]
        },
        'projects': PROJECTS_DATA
    }
    return render(request, 'home/home.html', context)

def project_detail(request, project_id):
    project = next((item for item in PROJECTS_DATA if item["id"] == project_id), None)
    
    if not project:
        raise Http404("Project not found")
        
    return render(request, 'home/project_detail.html', {'project': project})