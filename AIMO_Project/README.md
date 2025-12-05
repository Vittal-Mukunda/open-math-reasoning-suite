🧠 AIMO Project – Local Mathematical Olympiad Evaluation SystemA complete environment for loading, solving, submitting, and scoring AI-generated mathematical reasoning tasks.⭐ OverviewThis repository simulates an AI Mathematical Olympiad (AIMO) competition environment. It provides a local evaluation sandbox identical in structure to official competitions, allowing you to:📥 Load Olympiad-style math problems.🏃 Run a baseline or custom solver.📝 Submit answers to an internal evaluator.📊 Score your model’s performance exactly like a real AI competition.📄 Generate an automatic submission.csv.📁 Repository StructureThe project is organized to separate the evaluation logic from the problem datasets and solver implementations.PlaintextAIMO_Project/
│
├── README.md              # Project Documentation
├── requirements.txt       # Python Dependencies
│
├── api/                   # Simulation of the Competition API
│   ├── __init__.py
│   └── client.py          # The AIMOClient class
│
├── evaluator/             # Internal Scoring Logic
│   ├── __init__.py
│   ├── scoring.py         # Scoring rules and CSV generation
│   └── loader.py          # Problem dataset loader
│
├── problems/              # Data Storage
│   └── sample_problems.json
│
├── baselines/             # Example Solvers
│   └── simple_baseline.py
│
├── utils/                 # (Optional) Helper functions
│   └── helpers.py
│
├── submission.csv         # Output file (Generated after running)
└── test_runner.py         # Main execution script
🔍 Component Details1. The API (api/)A simulated interface that mirrors how official AIMO competition servers interact with models.FunctionDescriptionget_next()Fetches the next problem object from the queue.submit(id, answer)Stores the prediction for the specific problem ID.reset()Clears the current state (useful for restarting runs).2. The Evaluator (evaluator/)loader.py: Loads problems from JSON, ensuring fields like id, latex, and answer exist.scoring.py: Compares predictions with ground truth, calculates the final score, and writes the results to submission.csv.3. Problem Format (problems/)Problems are stored in sample_problems.json following this strict schema:JSON{
  "id": "p4",
  "latex": "What is 10 + 10?",
  "answer": 20
}
🛠 Installation & SetupPrerequisitesPython 3.8 or higherStep 1: Verify PythonPowerShellpython --version
Step 2: Clone & NavigateNavigate to the project directory (update the path to match your local machine).PowerShellcd C:\Users\Vittal\OneDrive\Desktop\Math_Olympiad\open-math-reasoning-suite\AIMO_Project
Step 3: Install DependenciesPowerShellpip install -r requirements.txt
▶️ Usage GuideRunning the EvaluationTo run the full simulation—which loads problems, runs the solver, and grades the results—execute the test runner:PowerShellpython test_runner.py
Expected Output:Console log showing progress.Final Score summary.Generation of submission.csv in the root folder.Adding Custom ProblemsYou can extend the dataset by editing problems/sample_problems.json.Example:JSON[
  ...
  {
    "id": "p7",
    "latex": "Find the value of 3^3.",
    "answer": 27
  }
]
🤖 Adding Your Own SolverTo create a custom solver, add a new script in the baselines/ directory (e.g., my_solver.py).Template Code:Pythonfrom api.client import AIMOClient

def run():
    # Initialize the simulated API client
    client = AIMOClient()
    
    # Get the first problem
    problem = client.get_next()

    while problem is not None:
        print(f"Solving problem {problem['id']}...")
        
        # -----------------------------------------------
        # YOUR LOGIC GOES HERE
        # Example: answer = my_llm.generate(problem['latex'])
        # -----------------------------------------------
        
        # Placeholder logic
        answer = 0 

        # Submit the answer
        client.submit(problem["id"], answer)
        
        # Fetch next problem
        problem = client.get_next()
[!IMPORTANT]After creating your solver, remember to update test_runner.py to import and execute your new run() function instead of the baseline.🤝 ContributionContributions are welcome! If you'd like to improve the scoring logic or add new baseline models:Fork the repository.Create a feature branch (git checkout -b feature/NewSolver).Commit your changes.Push to the branch and open a Pull Request
