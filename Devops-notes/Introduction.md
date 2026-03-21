SDLC - Software Development Life Cycle
    
    Software -> App (like your MERN project)
    Development -> Building it
    Life Cycle -> Full journey

    -> When we build a software project, we don't just randomly start 
       coding. There must be some organized way to build software.
       That organized way is called SDLC.

    -> SDLC means the full journey of building software from idea to
        final product.


SDLC Steps

1. Requirement -> What do users want?

2. Design -> How will we build it?

3. Development -> Writing code

4. Testing -> Checking for bugs

5. Deployment -> Making it live

6. Maintenance -> Fixing and updating


=> There are different ways companies follow SDLC process.

    -> Two popular approaches are:

    1. Waterfall (Traditional Method)
        -> In this method, we complete one step fully, then move to the 
        next step.

        Step 1 → Step 2 → Step 3 → Step 4

        problem: No going back easily.
            -> If client says after development:
                “I want change.”
                    It becomes difficult.

    
    2. Agile (Modern Flexible Method)
        -> Agile was introduced because software requirements change often, 
        and companies needed a more flexible way.

        -> Agile is a way to manage projects by breaking them into smaller
        parts. It focuses on working together and making constant improvements.

        -> Here we complete projects in sprint
            Sprint = small time period (like 2 weeks) where small features 
            are built.




Before Devops
    -> Earlier companies had two teams
    1. Developers -> write code
    2. Operations team -> Deploy & manage servers

    Developer didn’t know server.
    Server team didn’t know code.

    workflow
    Developers write code -> send zip file to ops team -> Ops team deploys it
     -> something breaks -> Ops blames Dev and Dev blames Ops.

    # It works on my machine. 

    Problems:
    Slow release, Miscommunication, Manual Deployment, No automation,
    Downtime, Very stressful release

* To solve these problems Devops was created.


DEVOPS = DEV + OPS

-> DevOps is a way of working where developers and operations work 
together and automate the process of building and deploying software.

Automation = Using tools/scripts so humans don’t manually repeat tasks.


DevOps Lifecycle:

    Plan -> Code -> Build -> Test -> Deploy -> Monitor -> Repeat

    Plan -> Decide features
    Code -> Write program
    Build -> Prepare app to run
    Test -> Check for bugs
    Deploy -> Put on server
    Monitor -> Watch if server is running fine

    Repeat -> Repeat continuously.




CI/CD (Continuous Integration / Continuous Deployment):

    -> CI/CD is a process used to automatically build, test, and deploy applications 
    whenever developers push code to a repository like GitHub.

    Example:
    When we pushed our MERN project to GitHub and Render automatically deployed it, 
    CI/CD was happening.


Continuous Integration (CI):

    Continuous -> Something that happens repeatedly.
    Integration -> Adding new code written by developers into the main project.

    Continuous Integration means:
    -> Whenever a developer pushes new code to the repository (like GitHub), the system 
    automatically:

        -> Downloads the new code
        -> Adds it to the existing project code
        -> Installs required dependencies
        -> Runs tests
        -> Checks for errors
        -> Builds the application

    This automatic process ensures that the new code works correctly with the existing project.

    => Continuous Integration is the process of automatically adding new code to the main project
     and checking that everything still works correctly.


    Why CI is needed:

        In team projects multiple developers work on the same codebase.
        If code is merged rarely, it can cause:

            -> Code conflicts
            -> Bugs
            -> Broken applications

        CI solves this by frequent integration and automated checks.

    Example:

    You pushed your code to GitHub
                ↓
    Render builds the application and installs dependencies

    This automatic build and check process is Continuous Integration.



Continuous Delivery / Continuous Deployment (CD):

    -> CD refers to the process of making the application ready for release or automatically 
    deploying it.

    There are two meanings of CD.

1. Continuous Delivery

    The system automatically:
    -> Builds the application
    -> Runs tests
    -> Prepares the application for deployment

    However, a human must manually approve deployment.

    Flow:

    Push Code
    ↓
    Build & Test
    ↓
    Ready to Deploy
    ↓
    Manual approval


2. Continuous Deployment

    -> After testing, the system automatically deploys the application without human approval.

    Flow:

    Push Code
    ↓
    Build & Test
    ↓
    Automatically deployed


Summary:

CI -> Automatically integrates and builds code
Continuous Delivery -> Code is ready for deployment but requires approval
Continuous Deployment -> Code is automatically deployed



Cloud Computing:

    -> Cloud computing means using remote servers over the internet instead of maintaining 
    physical servers locally.

    Applications run on servers provided by cloud companies.

        Example providers:
        -> Amazon Web Services (AWS)
        -> Microsoft Azure
        -> Google Cloud Platform (GCP)


On-Premises vs Cloud


   # On-Premises

    -> Servers are physically located inside a company’s building.

    Company responsibilities:
        -> Buy hardware
        -> Maintain servers
        -> Handle cooling and electricity
        -> Manage hardware failures

    Problems:
        -> Expensive
        -> Hard to scale
        -> Requires hardware maintenance



    # Cloud

    Servers are hosted in large data centers owned by cloud providers.
    Companies rent these servers instead of buying them.

    Advantages:
        -> No hardware maintenance
        -> Pay for what you use
        -> Easy scalability
        -> Global availability



Cloud Service Models

    -> IaaS, PaaS, and SaaS are service models that define how much responsibility the 
    cloud provider handles.


    IaaS (Infrastructure as a Service)

        Cloud provider gives virtual infrastructure such as:
            -> Servers
            -> Storage
            -> Networking

        The user manages:
            -> Operating system
            -> Runtime environment
            -> Applications
            -> Security

        Example: AWS EC2


    PaaS (Platform as a Service)

        Cloud provider provides a ready environment to run applications.

        The provider manages:
            -> Infrastructure
            -> Operating system
            -> Runtime environment

        The developer only manages:
            -> Application code

        Examples: Render, Heroku, Vercel


    SaaS (Software as a Service)

        Cloud provider delivers fully functional software through the internet.

        Users simply use the software without managing infrastructure or code.

        Examples: Gmail, Netflix, ChatGPT, Google Docs


    Service Model Comparison:


    Model	User Responsibility
    IaaS ->	Manage OS, runtime, and application
    PaaS ->	Manage only application code
    SaaS ->	No technical management required



Cloud Deployment Types

    Deployment types describe who can access the cloud infrastructure.

    Public Cloud
        -> Infrastructure is shared among multiple organizations, but each user’s data 
        remains isolated.

        Example: AWS public cloud

        Advantages:
            -> Lower cost
            -> Easy setup
            -> Highly scalable


    Private Cloud

        -> Cloud infrastructure is dedicated to a single organization.

        Advantages:
        -> Greater control
        -> Higher security

        Disadvantage:
        -> Higher cost

        Used by organizations like banks and government agencies.


    Hybrid Cloud

        -> Hybrid cloud is a combination of public and private cloud.

        Example:
        -> Sensitive data stored in private cloud
        -> Public services hosted on public cloud


    Deployment Type Comparison:

    Type	            Description
    Public Cloud  ->	Shared infrastructure used by multiple organizations
    Private Cloud ->	Dedicated infrastructure for one organization
    Hybrid Cloud  ->	Combination of public and private cloud
