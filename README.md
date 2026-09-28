💬 CustomerSupportAgent
AI Customer Support with Persistent Memory using Hindsight

CustomerSupportAgent is an AI-powered customer support agent designed to remember previous customer interactions and use that information when the customer returns.

The main idea is simple:

The customer should not have to repeat their story every time.

🎯 Problem

In many customer-support systems, every new conversation can feel like starting from zero. Customers may have to repeatedly explain their issue, previous actions, or earlier conversations.

For example, a customer may initially report:

“My order was supposed to arrive yesterday, but it still hasn't been delivered.”

If the customer contacts support again later, a system without persistent memory may ask them to explain the problem again.

This can make the support experience repetitive and frustrating.

💡 Solution

CustomerSupportAgent uses Hindsight as a persistent memory layer for an AI customer-support agent.

The system can:

Remember previous customer conversations
Retrieve relevant information from earlier interactions
Use previous context when responding to new questions
Display the Hindsight memory used by the agent
Generate responses based on both the current message and remembered context

This allows customer support to continue with context instead of starting from zero.

🧠 Hindsight Integration

Hindsight is the central memory component of CustomerSupportAgent.

The project uses three important capabilities:

1. Retain

Customer conversations are stored in Hindsight memory.

Customer Message → Retain → Hindsight Memory

For example, the system can remember that a customer previously reported a delayed order.

2. Recall

When the customer contacts the support agent again, the system retrieves relevant information from previous conversations.

New Customer Message → Recall → Previous Customer Context

This allows the agent to access information that was provided earlier.

3. Reflect

The agent combines the current customer message with relevant remembered information to generate a context-aware response.

Previous Memory + Current Question → Reflect → AI Support Response

Together, Retain, Recall, and Reflect form the memory workflow of the application.

🔄 How It Works

Customer

↓

New Support Message

↓

CustomerSupportAgent

↓

Hindsight Memory

↓

Retain / Recall

↓

Previous Customer Context

↓

Reflect

↓

Context-Aware AI Response

↓

Customer

✨ Key Features
💬 Live Support Chat

Customers can enter their name and a new support message through the support interface.

The agent retrieves relevant previous memories before generating its response.

🧠 Persistent Customer Memory

Previous customer interactions can be stored in Hindsight and used in future conversations.

🔎 Memory Recall

The application retrieves relevant information about previous customer-support issues.

🤖 Context-Aware Responses

The AI support agent uses the current customer message together with remembered information to generate a response.

👀 Visible Hindsight Memory

The application displays the memory retrieved from Hindsight so that users can see how persistent memory contributes to the response.

🖥️ Application Sections
1. Status Dashboard

Displays the status of:

Hindsight Memory
Recall
AI Support
2. Live Support Chat

The main customer-facing support interface.

3. Save New Support Conversation

Allows a new customer interaction to be stored in Hindsight.

4. Customer Memory

Retrieves previous customer conversations from Hindsight.

5. AI Support Agent

Generates a response using the customer's current question and remembered context.

6. How CustomerSupportAgent Works

Explains the Retain → Recall → Reflect workflow.

🧪 Example
First Interaction

Customer:

“My order was supposed to arrive yesterday, but it still hasn't been delivered.”

The interaction is stored in Hindsight.

Later Interaction

Customer:

“My order is still not delivered. What do you remember about my issue?”

CustomerSupportAgent retrieves the relevant memory.

The application displays:

🧠 Hindsight Memory Used

The agent then generates a response using the remembered context.

The customer does not need to repeat the entire story.

🛠️ Technology Stack
Python
Streamlit
Hindsight
Hindsight Python Client
python-dotenv
🏗️ Architecture

Customer

↓

Streamlit Interface

↓

CustomerSupportAgent

↓

Hindsight Memory

Retain → Store customer information
Recall → Retrieve relevant context
Reflect → Generate a context-aware response

↓

Customer

📂 Project Structure

CustomerSupportAgent/

app.py
requirements.txt
README.md
.gitignore

The following files remain local and are not uploaded to GitHub:

.env
.venv/

The .env file contains the private Hindsight API key.

⚙️ How to Run Locally
1. Clone the repository

Replace YOUR-USERNAME with your GitHub username.

git clone https://github.com/YOUR-USERNAME/CustomerSupportAgent.git

Then:

cd CustomerSupportAgent

2. Create a virtual environment

python -m venv .venv

3. Activate the environment on Windows

.venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Add the Hindsight API key

Create a .env file in the project folder and add:

HINDSIGHT_API_KEY=your_api_key_here

Do not upload this file to GitHub.

6. Run the application

streamlit run app.py

The application will open in your browser.

🔐 Security

The Hindsight API key is stored in the .env file and excluded from GitHub using .gitignore.

The API key should never be committed to a public repository.

🚀 Future Improvements

The prototype can be extended with:

Customer profiles
Multiple conversation sessions
Conversation timestamps
Order-status integration
Support-ticket integration
Human-agent handoff
Customer sentiment analysis
Support analytics
Authentication
Database integration
🏆 Hackathon Context

Theme: AI Agents That Learn Using Hindsight

Project: CustomerSupportAgent

Use Case: Customer Support

Core Technology: Hindsight

The project demonstrates how persistent memory can be used in customer support so that an AI agent can remember relevant information from previous interactions and use that context in future conversations.

💬 Core Idea

CustomerSupportAgent remembers the customer's story, so the customer doesn't have to repeat it.