AI-Powered Human Resource
Management System (HRMS)
Instructions
Candidate must submit all of the following. Incomplete submissions will not be
evaluated.
1. GitHub Repository
Public repo with clean commits, a proper README, and working code. No
single-commit dumps.
2. README.md
Must include: project overview, tech stack, setup instructions, feature list,
known limitations, and screenshots or GIFs.
3. Demo Video (Max. 5 minutes)
Recorded on YouTube (unlisted), or Google Drive. Must show the full
working app— every major feature — with the candidate narrating their
design decisions.

VIDEO — WHAT TO COVER (Maximum: 5 min)
• Introduction: What the project does and which problem it solves (30
sec)
• Walk through the UI — show every screen and flow (2 min)
• Demonstrate the AI in action with real inputs — show at least 3
different scenarios (1.5 min)
• Explain one key prompt design decision: why you wrote the prompt
the way you did (30 sec)
• State one limitation and how you'd fix it with more time (30 sec)

4. Submission Form
Fill the provided Microsoft Form with: Name, GitHub link, Video link, and a
100-word reflection on what you would improve with more time.

Project Objective

AI-Powered Human Resource Management System (HRMS) 1

Build a fully functional HRMS where AI is woven into core HR workflows — not
bolted on as an afterthought. From onboarding to performance reviews to
policy Q&A;, the system should make HR tasks faster, smarter, and less manual.
Note: Candidates are not restricted to use AI to write their code, but
understanding of the code and implemented features is required.
Area Suggestions

AI / LLM Integration

Candidates may use any LLM provider of
there choice.
Eg: Claude, Gemini, Ollama (local LLM

bonus), OpenAI (GPT-4 / GPT-4o / GPT-
4o-mini)

Backend Python (Django/FastAPI), SQLlite.
Frontend

React.js/Next.js, TailwindCSS, ShadCN UI
(optional)

🧩 Core Modules
Module 1 — Employee Records & Directory
A complete employee management module.
Functional Requirements
HR admin can:
Add, edit, and deactivate employee profiles
Upload and store employee documents (offer letter, ID proof, etc.)
Search employees by name, department, skill, or any field
View department org chart (visual tree)
Export employee list as CSV
Stored Fields

AI-Powered Human Resource Management System (HRMS) 2

Field group Fields
Profile data

name, designation, department, joining
date, manager, contact

AI Features
Auto-generate a professional employee bio from basic profile data
Detect duplicate or incomplete profiles and flag them

Module 2 — AI-Powered Recruitment & ATS
A built-in ATS (Applicant Tracking System) that HR can use during the hiring
process.
Functional Requirements
HR creates a job posting: role, JD, required skills, experience level
Candidates are added (name + resume PDF upload)
HR can move candidates through stages:
Applied → Screening → Interview → Offer → Hired / Rejected
Side-by-side comparison view of shortlisted candidates
Workflow Stages (Hiring Pipeline)
Step Stage
1 Applied
2 Screening
3 Interview
4 Offer
5 Hired / Rejected

AI-Powered Human Resource Management System (HRMS) 3

AI Features
AI scores each resume against the JD and gives a match % with
reasoning
AI highlights top 3 strengths and top 2 gaps per candidate
AI auto-generates 5 tailored interview questions per candidate

Module 3 — Leave & Attendance Management
Functional Requirements
Employee can apply for leave: type (sick, casual, earned, WFH), dates,
reason
Manager approves or rejects with a comment
Leave balance tracker per employee per leave type
Mark attendance: Present / WFH / Half Day / Absent
Calendar view of team leaves (who is out when)
Monthly attendance summary report per employee

AI Features
Flag unusual leave patterns (e.g. repeated Mondays/Fridays off)
Predict team capacity risk if multiple leave requests clash

Module 4 — AI Performance Review System
A structured performance review cycle with AI assistance for managers.
Functional Requirements
HR triggers a review cycle: sets period (e.g. Q2 2025), selects employees

AI-Powered Human Resource Management System (HRMS) 4

Employee fills a self-assessment form: achievements, challenges, goals for
next period
Manager fills manager review form: ratings on 5 key parameters (Quality,
Delivery, Communication, Initiative, Teamwork)
Final review can be exported as a PDF for the employee's record

AI Features
AI reads both forms and generates a balanced, professional review
summary in paragraph form
AI flags mismatches: where employee self-rating is very different from
manager rating
AI suggests 2–3 specific development actions based on the review data

Module 5 — AI Onboarding Assistant
A dedicated onboarding flow for new joiners, with an AI assistant (chatbot) to
answer their questions.
Functional Requirements
HR creates an onboarding checklist per role (e.g. Software Engineer,
Marketing Executive)
New joiner sees their personalised checklist with progress tracking
Checklist items can have due dates and assignees
HR can upload policy documents, handbooks, and guides
HR can see which questions were asked most — to improve documentation

AI Features
AI Chatbot: new joiner can ask any question about policies, tools, leave
rules, etc.
If chatbot cannot answer: it says 'Please contact HR at [email]'

AI-Powered Human Resource Management System (HRMS) 5

⚠️ Important Constraint

Chatbot answers from the uploaded documents only — no
hallucination

Module 6 — HR Analytics & Insights
Functional Requirements
Headcount by department (chart)
Attrition rate (if termination date is marked for any employee)
Average tenure per department
Open positions vs filled positions
Leave utilisation rate across the company

AI Features
AI-generated monthly HR summary: key highlights, risks, and
recommended actions

⭐ Bonus (up to 10 pts): AI-generated offer letter from a template /
Payroll summary module
