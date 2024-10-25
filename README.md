# CareerCompass: AI-Powered Career Guidance

CareerCompass is an innovative AI-powered chatbot designed to revolutionize career advice. By leveraging advanced technologies and comprehensive data sources, it provides personalized guidance for job seekers, professionals, and career counselors alike.

## Key Features

- **Interview Preparation**: Offers tailored tips and strategies for successful interviews.
- **Knowledge Integration**: Incorporates insights from career-related articles and reputable advice books.

## Technologies

- Gemini Model
- LangChain
- Streamlit
- FAISS Vector Database

## How It Works

1. Generates and stores vector embeddings of various literatures using Gemini and FAISS.
2. Retrieves relevant information based on user queries.
3. Creates personalized responses using prompt templates and Gemini.
4. Displays interactive conversations through a Streamlit dashboard.

## Applications

- **Educational Institutions**: Guide students in career path decisions.
- **Remote Career Counseling**: Provide advice in areas with limited access to traditional counseling.
- **Continuous Learning Platforms**: Offer career guidance based on newly acquired skills.

## Benefits

- Accessible, personalized career guidance
- Data-driven insights for informed decision-making
- Up-to-date advice incorporating the latest industry trends
- Scalable solution for various professional development needs

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/utkarshgupta2009/career-advisor-chatbot
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file in the project root and add:
   ```
   SERPAPI_API_KEY=your_serpapi_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```
4. Run the application:
   ```
   streamlit run app.py
   ```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

CareerCompass empowers individuals to navigate their professional journeys with confidence, backed by AI-driven insights and comprehensive career resources. 