"""教师表建议纳入清单；其余来源保留为注释，默认不调度。"""
APPROVED_SOURCES = (
    'j-db72c3c601',  # Environmental Chemistry Letters
    'j-b2a795c62c',  # Science China Earth Sciences
    'j-637d3c6893',  # Environment International
    'j-3d69adb6cc',  # Environmental Modelling & Software
    'j-e3cffa92a3',  # Environmental Research
    'j-cc0520cd13',  # Journal of Hazardous Materials
    'j-f18c5c6d80',  # Journal of Hydrology
    'j-c7fe39938d',  # Water Research
    'j-76f25ed87e',  # Journal of Cleaner Production
    'j-ef70b31a3b',  # The Lancet Planetary Health
    'j-454594cd31',  # One Earth
    'j-d4f2c6db6c',  # Sustainable Cities and Society
    'commsenv',  # Communications Earth & Environment
    'nclimate',  # Nature Climate Change
    'natecolevol',  # Nature Ecology & Evolution
    'ngeo',  # Nature Geoscience
    'natrevearthenviron',  # Nature Reviews Earth & Environment
    'natsustain',  # Nature Sustainability
    'natwater',  # Nature Water
    'npjcleanwater',  # npj Clean Water
    'npjclimatsci',  # npj Climate and Atmospheric Science
    'npjurbansustain',  # npj Urban Sustainability
    'nature-jes',  # Journal of Exposure Science & Environmental Epidemiology
    'j-66226e45c5',  # Trends in Ecology & Evolution
    'j-93b6de779b',  # Acta Ecologica Sinica
    'j-d5153e140b',  # Eco-Environment & Health
    'j-3c29fd056f',  # Ecological Indicators
    'j-7eb046a640',  # Environmental Science and Ecotechnology
    'j-3e89b0beb9',  # Food Hydrocolloids
    'j-953779b30d',  # Journal of Remote Sensing
    'j-f72cff72c6',  # International Journal of Applied Earth Observation and Geoinformation
    'j-4b102d66fb',  # ISPRS Journal of Photogrammetry and Remote Sensing
    'j-ef7cd14dbc',  # Remote Sensing of Environment
    'j-16256b0ce3',  # Earth-Science Reviews
    'j-96be195ee8',  # International Journal of Mining Science and Technology
    'j-0d7b7f9cca',  # Science China Technological Sciences
    'j-b9e88c9085',  # Additive Manufacturing
    'j-8143dc670f',  # Advanced Engineering Informatics
    'j-da866ae444',  # Automation in Construction
    'j-3fe12bcc6e',  # Building and Environment
    'j-20e3868bcd',  # Energy and Buildings
    'j-c3975648f8',  # Engineering Structures
    'j-ba9e12f1c9',  # International Journal of Heat and Mass Transfer
    'j-0b805d1731',  # International Journal of Machine Tools and Manufacture
    'j-c788b13dcd',  # International Journal of Mechanical Sciences
    'j-3b179d0686',  # Mechanical Systems and Signal Processing
    'j-7db6bc49fe',  # Reliability Engineering & System Safety
    'commschem',  # Communications Chemistry
    'natcatal',  # Nature Catalysis
    'nchembio',  # Nature Chemical Biology
    'natchemeng',  # Nature Chemical Engineering
    'nchem',  # Nature Chemistry
    'nmat',  # Nature Materials
    'nnano',  # Nature Nanotechnology
    'natrevchem',  # Nature Reviews Chemistry
    'natrevmats',  # Nature Reviews Materials
    'natsynth',  # Nature Synthesis
    'npj2dmaterials',  # npj 2D Materials and Applications
    'npjmatdeg',  # npj Materials Degradation
    'npjquantmats',  # npj Quantum Materials
    'nature-micronano',  # Microsystems & Nanoengineering
    'nature-am',  # NPG Asia Materials
    'j-73ae0ea805',  # Chem
    'j-0a94e1dd0b',  # Matter
    'j-f7041871ab',  # Trends in Chemistry
    'j-92e8a1607c',  # Advanced Fiber Materials
    'j-29c654efbc',  # Journal of Cheminformatics
    'j-291c5f64e2',  # Nano Convergence
    'j-c68f7da396',  # Nano-Micro Letters
    'j-93f2940543',  # Advanced Composites and Hybrid Materials
    'j-dbedd658b3',  # Science China Chemistry
    'j-b52070b429',  # Science China Materials
    'j-e85da65425',  # Acta Materialia
    'j-2c17c1a9f2',  # Acta Physico-Chimica Sinica
    'j-9dfd99facf',  # Advances in Colloid and Interface Science
    'j-9560448126',  # Advances in Nutrition
    'j-472852446c',  # Analytica Chimica Acta
    'j-2360cc9d11',  # Applied Catalysis B Environment and Energy
    'j-5a340b6bed',  # Biotechnology Advances
    'j-a7e6c8a427',  # Carbohydrate Polymers
    'j-6097563751',  # Carbon
    'j-8eff360546',  # Chemical Engineering Journal
    'j-9969e777ad',  # Chemometrics and Intelligent Laboratory Systems
    'j-54bd8c62a1',  # Cleaner Materials
    'j-91c9cf8d92',  # Composites Part B Engineering
    'j-f339346c60',  # Composites Science and Technology
    'j-04135a0409',  # Coordination Chemistry Reviews
    'j-131412d3fe',  # Current Opinion in Green and Sustainable Chemistry
    'j-81110b91e0',  # Current Opinion in Solid State and Materials Science
    'j-6cf9b89ec2',  # Journal of Catalysis
    'j-b906b6f81f',  # Journal of Materials Science & Technology
    'j-eb06e3a648',  # Materials & Design
    'j-7bfd1ffaaf',  # Materials Science and Engineering R Reports
    'j-18fb82c92b',  # Materials Today
    'j-2e7e0743f5',  # Materials Today Bio
    'j-ff99d89b8c',  # Metabolism
    'j-a7c952f88e',  # Molecular Aspects of Medicine
    'j-31764e1eab',  # Physics of Life Reviews
    'j-9ff3577364',  # Progress in Materials Science
    'j-825e995b88',  # Progress in Polymer Science
    'j-9623b4b6db',  # Redox Biology
    'j-bb97940e03',  # Scripta Materialia
    'j-6a2242b280',  # TrAC Trends in Analytical Chemistry
    'j-c94b3260f2',  # Trends in Environmental Analytical Chemistry
    'j-fe57259a51',  # Sensors and Actuators B Chemical
    'iros',  # IEEE/RSJ International Conference on Intelligent Robots and Systems
    'rss',  # Robotics: Science and Systems
    'j-f4a8fc84bb',  # Science Robotics
    'j-d67ff4907c',  # Cyborg and Bionic Systems
    'j-0fe19b9e20',  # Robotics and Autonomous Systems
    'j-0cde8a3b99',  # Robotics and Computer-Integrated Manufacturing
    'recomb',  # Annual International Conference on Research inComputational Molecular Biology
    'bibm',  # IEEE International Conference on Bioinformatics and Biomedicine
    'rtss',  # IEEE Real-Time Systems Symposium
    'ismb',  # International conference on Intelligent Systems for Molecular Biology
    'miccai',  # International Conference on Medical Image Computing and Computer-Assisted Intervention
    'www',  # The Web Conference
    'j-9232dae3d1',  # Review of Managerial Science
    'j-8931ee1083',  # Energy Economics
    'j-d08002909e',  # Journal of Business Research
    'j-916f94530c',  # Journal of Retailing and Consumer Services
    'j-b1526e25bf',  # PhotoniX
    'j-6244b75b55',  # Satellite Navigation
    'j-82b1ddfc1d',  # Annual Reviews in Control
    'j-eb0b362d81',  # Energy Strategy Reviews
    'j-23d3f85df7',  # eTransportation
    'j-ed2487e684',  # International Journal of Plasticity
    'j-49d979c142',  # Journal of Manufacturing Systems
    'j-da9329943d',  # Progress in Aerospace Sciences
    'j-4c36329d0f',  # Progress in Energy and Combustion Science
    'j-9ca36fbb5a',  # Technovation
    'j-35715e1db8',  # Journal of Parallel and Distributed Computing
    'mlsys',  # Conference on Machine Learning and Systems
    'atc',  # ACM SIGOPS Annual Technical Conference (formerly USENIX ATC)
    'ppopp',  # ACM SIGPLAN Symposium on Principles & Practice of Parallel Programming
    'socc',  # ACM Symposium on Cloud Computing
    'spaa',  # ACM Symposium on Parallelism in Algorithms and Architectures
    'fpga',  # ACM/SIGDA International Symposium on Field-Programmable Gate Arrays
    'date',  # Design, Automation & Test in Europe
    'eurosys',  # European Conference on Computer Systems
    'icdcs',  # IEEE International Conference on Distributed Computing Systems
    'ipdps',  # IEEE International Parallel & Distributed Processing Symposium
    'iscas',  # IEEE International Symposium on Circuits and Systems
    'hpca',  # IEEE International Symposium on High Performance Computer Architecture
    'micro',  # IEEE/ACM International Symposium on Microarchitecture
    'sc',  # International Conference for High Performance Computing, Networking, Storage, and Analysis
    'asplos',  # International Conference on Architectural Support for Programming Languages and Operating Systems
    'iccd',  # International Conference on Computer Design
    'icpp',  # International Conference on Parallel Processing
    'ics',  # International Conference on Supercomputing
    'isca',  # International Symposium on Computer Architecture
    'cgo',  # The International Symposium on Code Generation and Optimization
    'soda',  # ACM-SIAM Symposium on Discrete Algorithms
    'focs',  # IEEE Annual Symposium on Foundations of Computer Science
    'hscc',  # International Conference on Hybrid Systems: Computation and Control
    'mm',  # ACM International Conference on Multimedia
    'sca',  # ACM SIGGRAPH/Eurographics Symposium on Computer Animation
    'siggraph',  # ACM Special Interest Group on Computer Graphics
    'dcc',  # Data Compression Conference
    'vr',  # IEEE Conference on Virtual Reality and 3D User Interfaces
    'icassp',  # IEEE International Conference on Acoustics,Speech and Signal Processing
    'icme',  # IEEE International Conference on Multimedia& Expo
    'vis',  # IEEE Visualization Conference
    'j-fa04e01c10',  # Data Mining and Knowledge Discovery
    'j-44c6c7fac3',  # Knowledge and Information Systems
    'j-6c204bdd6e',  # Knowledge-Based Systems
    'recsys',  # ACM Conference on Recommender Systems
    'cikm',  # ACM International Conference on Information and Knowledge Management
    'kdd',  # ACM SIGKDD Conference on Knowledge Discovery and Data Mining
    'sigmod',  # ACM SIGMOD Conference
    'pods',  # ACM SIGMOD-SIGACT-SIGAI Symposium on Principles of Database Systems
    'cidr',  # Conference on Innovative DataSystems Research
    'ecml-pkdd',  # European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases
    'icdm',  # IEEE International Conference on Data Mining
    'sigir',  # International ACM SIGIR Conference on Research and Development in Information Retrieval
    'vldb',  # International Conference on Very Large Data Bases
    'sdm',  # SIAM International Conference on Data Mining
    'j-0d21a65b81',  # Information Processing & Management
    'j-7352d41a27',  # Artificial Intelligence Review
    'j-fe8a45e725',  # International Journal of Computer Vision
    'j-f97db96938',  # Machine Learning
    'j-4add517d26',  # Artificial Intelligence
    'j-729522c31f',  # Computer Vision and Image Understanding
    'j-f6416922ec',  # Information Fusion
    'j-3991fd2dc7',  # Neural Networks
    'j-f26b06f4ee',  # Neurocomputing
    'j-704f11b185',  # Pattern Recognition
    'j-70da0b6ba3',  # Applied Soft Computing
    'j-5d396d92fa',  # Engineering Applications of Artificial Intelligence
    'j-a6cfe198b1',  # Expert Systems with Applications
    'natcomputsci',  # Nature Computational Science
    'natmachintell',  # Nature Machine Intelligence
    'npjcompumats',  # npj Computational Materials
    'npjscilearn',  # npj Science of Learning
    'sdata',  # Scientific Data
    'j-12453ccb88',  # Business & Information Systems Engineering
    'j-8d1b1806d8',  # Computer Science Review
    'j-938b2d3492',  # Intelligent Computing
    'nenergy',  # Nature Energy
    'j-972e72b183',  # Joule
    'j-5be82edc26',  # Advances in Applied Energy
    'j-3488061829',  # Applied Energy
    'j-437bcb1511',  # Energy
    'j-b4ac12ae95',  # Energy Conversion and Management
    'j-1eb350782d',  # Energy Reviews
    'j-a11637a2e7',  # Energy Storage Materials
    'j-71ce7eb9b9',  # EnergyChem
    'j-d49438c2b7',  # Green Energy and Resources
    'j-bfcb6ab02b',  # Journal of Energy Chemistry
    'j-f72e35bac7',  # Nano Energy
    'j-32e580f9bf',  # Renewable and Sustainable Energy Reviews
    'j-4a8bd2ddf7',  # Renewable Energy
    'natfood',  # Nature Food
    'nplants',  # Nature Plants
    'npjscifood',  # npj Science of Food
    'nature-bmt',  # Bone Marrow Transplantation
    'j-530a5c55b0',  # Food Engineering Reviews
    'j-c8af77652d',  # Food Chemistry
    'j-ad9089e1ea',  # Soil Biology and Biochemistry
    'j-999aedec01',  # Trends in Food Science & Technology
    'j-800d438108',  # Plant Phenomics
    'j-a51bff429f',  # Trends in Plant Science
    'j-0d5068779d',  # Molecular Plant
    'j-a8a43dcc50',  # Plant Communications
    'j-0675aa8262',  # Precision Agriculture
    'j-dad8818884',  # Agricultural and Forest Meteorology
    'j-e625b131f8',  # Agricultural Systems
    'j-6c033988ef',  # Computers and Electronics in Agriculture
    'ubicomp',  # ACM International Joint Conference on Pervasive and Ubiquitous Computing
    'uist',  # ACM Symposium on User Interface Software and Technology
    'percom',  # IEEE International Conference on Pervasive Computing and Communications
    'icwsm',  # The International AAAI Conference on Web and Social Media
    'j-d562500035',  # Trends in Cognitive Sciences
    'j-f1c866e24e',  # Research Policy
    'j-430f217ee3',  # Social Science Research
    'j-8d28ded9e4',  # Technological Forecasting and Social Change
    'j-7735fd308f',  # Cities
    'j-74e31d8040',  # Landscape and Urban Planning
    'j-b1a799447f',  # The Lancet Global Health
    'j-89420e930d',  # The Lancet Public Health
    'j-5ee808df0e',  # Social Science & Medicine
    'j-8a3cfd2781',  # Transportation Research Part B Methodological
    'j-8340ff7e98',  # Transportation Research Part C Emerging Technologies
    'j-7a7c416cc3',  # Transportation Research Part D Transport and Environment
    'j-69b4b3aecf',  # Transportation Research Part E Logistics and Transportation Review
    'j-40e322ab64',  # Computers & Education
    'j-e578c05fa9',  # Computers and Education Artificial Intelligence
    'j-d2017db5cc',  # Learning and Instruction
    'j-b7e8dbde6c',  # Journal of Econometrics
    'j-61f337f3c1',  # Journal of Financial Economics
    'j-e947fc6e14',  # Decision Support Systems
    'j-12a98c9199',  # European Journal of Operational Research
    'j-5af9c05b93',  # Scientometrics
    'j-3ecf0afce7',  # Journal of Informetrics
    'natcities',  # Nature Cities
    'nathumbehav',  # Nature Human Behaviour
    'nrpsychol',  # Nature Reviews Psychology
    'nature-palcomms',  # Humanities and Social Sciences Communications
    'nature-mp',  # Molecular Psychiatry
    'nature-npp',  # Neuropsychopharmacology
    'nature-tp',  # Translational Psychiatry
    'j-611ac32c1d',  # Computers in Human Behavior
    'j-b72a164df5',  # Educational Psychology Review
    'j-41efefd652',  # International Journal of Educational Technology in Higher Education
    'j-f28cf1469d',  # Smart Learning Environments
    'j-4a7ca851fa',  # Clinical Psychology Review
    'j-649bd697db',  # Computers and Education Open
    'j-0b0e305642',  # Environmental Impact Assessment Review
    'j-d3cadb2414',  # International Journal of Information Management
    'j-16f3c7d6d3',  # Technology in Society
    'j-e0bd6ccaed',  # Tourism Management
    'eccb',  # European Conference on Computational Biology
    'commsbio',  # Communications Biology
    'nataging',  # Nature Aging
    'natbiomedeng',  # Nature Biomedical Engineering
    'nbt',  # Nature Biotechnology
    'natcancer',  # Nature Cancer
    'natcardiovascres',  # Nature Cardiovascular Research
    'ncb',  # Nature Cell Biology
    'ng',  # Nature Genetics
    'ni',  # Nature Immunology
    'nm',  # Nature Medicine
    'natmetab',  # Nature Metabolism
    'nmeth',  # Nature Methods
    'nmicrobiol',  # Nature Microbiology
    'neuro',  # Nature Neuroscience
    'nprot',  # Nature Protocols
    'natrevbioeng',  # Nature Reviews Bioengineering
    'nrc',  # Nature Reviews Cancer
    'nrcardio',  # Nature Reviews Cardiology
    'nrclinonc',  # Nature Reviews Clinical Oncology
    'nrd',  # Nature Reviews Drug Discovery
    'natrevelectreng',  # Nature Reviews Electrical Engineering
    'nrendo',  # Nature Reviews Endocrinology
    'nrgastro',  # Nature Reviews Gastroenterology & Hepatology
    'nrg',  # Nature Reviews Genetics
    'nri',  # Nature Reviews Immunology
    'nrmp',  # Nature Reviews Methods Primers
    'nrmicro',  # Nature Reviews Microbiology
    'nrm',  # Nature Reviews Molecular Cell Biology
    'nrneurol',  # Nature Reviews Neurology
    'nrn',  # Nature Reviews Neuroscience
    'nrrheum',  # Nature Reviews Rheumatology
    'nrurol',  # Nature Reviews Urology
    'nsmb',  # Nature Structural & Molecular Biology
    'npjamd',  # npj Aging
    'npjamar',  # npj Antimicrobials and Resistance
    'npjbiofilms',  # npj Biofilms and Microbiomes
    'npjbcancer',  # npj Breast Cancer
    'npjdigitalmed',  # npj Digital Medicine
    'npjgenmed',  # npj Genomic Medicine
    'npjmgrav',  # npj Microgravity
    'npjparkd',  # npj Parkinson’s Disease
    'npjprecisiononcology',  # npj Precision Oncology
    'npjpcrm',  # npj Primary Care Respiratory Medicine
    'npjregenmed',  # npj Regenerative Medicine
    'npjsba',  # npj Systems Biology and Applications
    'npjvaccines',  # npj Vaccines
    'nature-aps',  # Acta Pharmacologica Sinica
    'nature-bcj',  # Blood Cancer Journal
    'nature-bjc',  # British Journal of Cancer
    'nature-cddiscovery',  # Cell Death Discovery
    'nature-celldisc',  # Cell Discovery
    'nature-cr',  # Cell Research
    'nature-ejhg',  # European Journal of Human Genetics
    'nature-eye',  # Eye
    'nature-gene',  # Genes & Immunity
    'nature-hr',  # Hypertension Research
    'nature-ijo',  # International Journal of Obesity
    'nature-laban',  # Lab Animal
    'nature-leu',  # Leukemia
    'nature-nutd',  # Nutrition and Diabetes
    'nature-onc',  # Oncogene
    'nature-oncsis',  # Oncogenesis
    'nature-pr',  # Pediatric Research
    'nature-pcan',  # Prostate Cancer and Prostatic Diseases
    'nature-npjschz',  # Schizophrenia
    'j-3d73a601f6',  # Science Immunology
    'j-691bf1ca1e',  # Science Translational Medicine
    'j-7a8d9ea925',  # Biomaterials Research
    'j-552f37b41b',  # Cancer Communications
    'j-74426cc4c1',  # Health Data Science
    'j-1e4b0859b5',  # Cancer Cell
    'j-4607bc7c42',  # Cell
    'j-0b75c492f7',  # Cell Chemical Biology
    'j-283615fb03',  # Cell Host & Microbe
    'j-dbcb0fcd74',  # Cell Metabolism
    'j-0a4425f44b',  # Cell Reports
    'j-f1684575f9',  # Cell Reports Medicine
    'j-ff38927ce9',  # Cell Stem Cell
    'j-495a105a04',  # Cell Systems
    'j-7cc3932475',  # Current Biology
    'j-f544c7a60d',  # Developmental Cell
    'j-56868b5aa5',  # Immunity
    'j-97a3b8d4d3',  # Med
    'j-937d0240eb',  # Molecular Cell
    'j-39f29a2f07',  # Neuron
    'j-9482c5d5bf',  # Structure
    'j-d2025a16cb',  # Trends in Biochemical Sciences
    'j-069630e73d',  # Trends in Biotechnology
    'j-1afb4654c3',  # Trends in Cancer
    'j-d24b8c2ea3',  # Trends in Cell Biology
    'j-216eba8f80',  # Trends in Endocrinology and Metabolism
    'j-5514e73d4c',  # Trends in Genetics
    'j-7c4dcf6bad',  # Trends in Immunology
    'j-f457cf101a',  # Trends in Microbiology
    'j-72172ba21c',  # Trends in Molecular Medicine
    'j-1a2d106b4b',  # Trends in Neurosciences
    'j-ec40580ce8',  # Trends in Parasitology
    'j-5a06230a87',  # Trends in Pharmacological Sciences
    'j-32e2cb1c9f',  # Molecular Therapy
    'j-4bf1b752f6',  # Molecular Therapy — Nucleic Acids
    'j-9f4e581a9f',  # Stem Cell Reports
    'j-2ec03844e7',  # The American Journal of Human Genetics
    'j-8f443c7880',  # EBioMedicine
    'j-8838d520aa',  # EClinicalMedicine
    'j-010bbc0bbc',  # The Lancet
    'j-6a81ab0750',  # The Lancet Child & Adolescent Health
    'j-df77234eb6',  # The Lancet Diabetes & Endocrinology
    'j-c6e14b9150',  # The Lancet Digital Health
    'j-967ed653cf',  # The Lancet Gastroenterology & Hepatology
    'j-b65bc153a0',  # The Lancet Haematology
    'j-1c0b582639',  # The Lancet Healthy Longevity
    'j-c93d27d7ce',  # The Lancet Infectious Diseases
    'j-483eb48696',  # The Lancet Microbe
    'j-af35c70bf5',  # The Lancet Neurology
    'j-d921a7e606',  # The Lancet Oncology
    'j-77bb843c9f',  # The Lancet Psychiatry
    'j-c702b0c2a4',  # The Lancet Regional Health - Europe
    'j-cef98d1da3',  # The Lancet Regional Health - Western Pacific
    'j-71921095d2',  # The Lancet Respiratory Medicine
    'j-dcadebb589',  # The Lancet Rheumatology
    'j-d94e323c3b',  # Alzheimer’s Research & Therapy
    'j-d058311f73',  # Biochar
    'j-4fb8bd2886',  # BioData Mining
    'j-736c22a224',  # BMC Biology
    'j-614c0898b2',  # BMC Medicine
    'j-a2f9b41c54',  # Carbon Neutrality
    'j-b5cbe6c7c8',  # Genome Biology
    'j-128792d050',  # Genome Medicine
    'j-3dee3825e5',  # Intensive Care Medicine
    'j-1dc21a94b1',  # Journal of Hematology & Oncology
    'j-9378816e2c',  # Journal of Nanobiotechnology
    'j-570c36674b',  # Microbiome
    'j-652a538c84',  # Molecular Biomedicine
    'j-e040f3f32c',  # Molecular Cancer
    'j-9596fa43cd',  # Molecular Neurodegeneration
    'j-dd56888193',  # Science China Life Sciences
    'j-6d145c9546',  # Advanced Drug Delivery Reviews
    'j-00a21d67da',  # Ageing Research Reviews
    'j-35fc948b7d',  # Annals of Oncology
    'j-e2a94b05b4',  # Annals of the Rheumatic Diseases
    'j-90e902bc57',  # Artificial Intelligence in Medicine
    'j-d006c8a763',  # Biomaterials
    'j-24652e28b9',  # Blood
    'j-e64dff0f80',  # Cancer Genetics
    'j-ca8fb4629a',  # Cancer Letters
    'j-55a37271d8',  # Cement and Concrete Composites
    'j-a9b953b30a',  # Cement and Concrete Research
    'j-a847fdc23a',  # Chinese Herbal Medicines
    'j-c554736351',  # Clinical Gastroenterology and Hepatology
    'j-8ec1c3871b',  # Computational Biology and Chemistry
    'j-24982684ad',  # Computer Methods and Programs in Biomedicine
    'j-40f01ce1e2',  # Diagnostic and Interventional Imaging
    'j-d491873aa5',  # Drug Discovery Today
    'j-41d825854c',  # European Urology
    'j-aba2a5c1d5',  # Gastroenterology
    'j-7dead2abe6',  # International Journal of Medical Informatics
    'j-5e43722961',  # JACC CardioOncology
    'j-06b16d0494',  # JACC Cardiovascular Interventions
    'j-896c5ba968',  # JACC Heart Failure
    'j-fd8b491e89',  # Journal of Advanced Research
    'j-becc8fcc40',  # Journal of Allergy and Clinical Immunology
    'j-e9725f8b7d',  # Journal of Controlled Release
    'j-c34b87cb15',  # Journal of Hepatology
    'j-165d67ba72',  # Journal of Pharmaceutical Analysis
    'j-0f6b15d93b',  # Journal of the American Academy of Dermatology
    'j-a6cf8cddc8',  # Journal of the American College of Cardiology
    'j-a1e0f9b090',  # Journal of the National Cancer Center
    'j-37b23398b2',  # Journal of Thoracic Oncology
    'j-156db6914b',  # Kidney International
    'j-e828addd7d',  # Medical Image Analysis
    'j-9d1d0d3a73',  # Ophthalmology
    'j-e2678b0db0',  # Pharmacological Research
    'j-6f25cc9655',  # Pharmacological Reviews
    'j-7448014cd8',  # Pharmacology & Therapeutics
    'j-d6f749bf6c',  # Phytomedicine
    'j-c2843d80b8',  # Seminars in Cancer Biology
    'j-0cb9ab9944',  # The Lancet HIV
    'embc',  # Annual International Conference of the IEEE Engineering in Medicine and Biology Society
    'isbi',  # IEEE International Symposium on Biomedical Imaging
    'j-bdffac0a5c',  # Biosensors and Bioelectronics
    'j-b55e43c0c4',  # Cell Reports Physical Science
    'natastron',  # Nature Astronomy
    'nphys',  # Nature Physics
    'natrevphys',  # Nature Reviews Physics
    'npjqi',  # npj Quantum Information
    'j-4fc3d65983',  # Archives of Computational Methods in Engineering
    'j-b86929fb5a',  # Computational Mechanics
    'j-e39bc45340',  # Engineering With Computers
    'j-7cb47416fb',  # Biochimica et Biophysica Acta (BBA) - Reviews on Cancer
    'j-1ba458f82d',  # Computer Methods in Applied Mechanics and Engineering
    'j-5641775722',  # Computer Physics Communications
    'j-57011f11e4',  # Computers & Structures
    'j-ce9a52b1f6',  # Journal of Computational Physics
    'j-01c665c7a1',  # Space Science & Technology
    'j-7b7ab0eaeb',  # Science China Physics Mechanics and Astronomy
    'j-29686b6ead',  # Aerospace Science and Technology
    'aaai',  # AAAI Conference on Artificial Intelligence
    'acl',  # Annual Meeting of the Association for Computational Linguistics
    'emnlp',  # Conference on Empirical Methods in Natural Language Processing
    'neurips',  # Conference on Neural Information Processing Systems
    'ecai',  # European Conference on Artificial Intelligence
    'eccv',  # European Conference on Computer Vision
    'icra',  # IEEE International Conference on Robotics and Automation
    'cvpr',  # IEEE/CVF Computer Vision and Pattern Recognition Conference
    'wacv',  # IEEE/CVF Winter Conference on Applications of Computer Vision
    'icaps',  # International Conference on Automated Planning and Scheduling
    'coling',  # International Conference on Computational Linguistics
    'iccv',  # International Conference on Computer Vision
    'iclr',  # International Conference on Learning Representations
    'icml',  # International Conference on Machine Learning
    'kr',  # International Conference on Principles of Knowledge Representation and Reasoning
    'ijcai',  # International Joint Conference on Artificial Intelligence
    'aamas',  # International Joint Conference on Autonomous Agents and Multi-agent Systems
    'naacl',  # North American Chapter of the Associationfor Computational Linguistics
    'ppsn',  # Parallel Problem Solving from Nature
    'commsphys',  # Communications Physics
    'j-d0ed63ed81',  # eLight
    'j-30dbcd1836',  # Physics Reports
    'j-2afeaa0078',  # Progress in Particle and Nuclear Physics
    'j-31f1ddbac1',  # Surface Science Reports
    'sensys',  # ACM/IEEE International Conference on Embedded Artificial Intelligence and Sensing Systems
    'infocom',  # IEEE International Conference on Computer Communications
    'icnp',  # IEEE International Conference on Network Protocols
    'secon',  # IEEE International Conference on Sensing, Communication, and Networking
    'iwqos',  # IEEE/ACM International Workshop on Quality of Service
    'mobihoc',  # International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing
    'nsdi',  # Symposium on Network System Design and Implementation
    'acsac',  # Annual Computer Security Applications Conference
    'srds',  # IEEE International Symposium on Reliable Distributed Systems
    'sp',  # IEEE Symposium on Security and Privacy
    'dsn',  # International Conference on Dependable Systems and Networks
    'ndss',  # Network and Distributed System Security Symposium
    'usenix-security',  # USENIX Security Symposium
    'pldi',  # ACM SIGPLAN Conference on Programming Language Design and Implementation
    'lctes',  # ACM SIGPLAN/SIGBED International Conference on Languages, Compilers andTools for Embedded Systems
    'models',  # ACM/IEEE International Conference on Model Driven Engineering Languages and Systems
    'icpc',  # IEEE International Conference on Program Comprehension
    'saner',  # IEEE International Conference on Software Analysis, Evolution,and Reengineering
    'issre',  # IEEE International Symposium on Software Reliability Engineering
    'ase',  # International Conference on Automated Software Engineering
    'cc',  # International Conference on Compiler Construction
    'icse',  # International Conference on Software Engineering
    'icsme',  # International Conference on Software Maintenance and Evolution
    'issta',  # International Symposium on Software Testing and Analysis
    'osdi',  # USENIX Symposium on Operating Systems Design and Implementation
    'globecom',  # IEEE Global Communications Conference
    'icc',  # IEEE International Conference on Communications
    'wcnc',  # IEEE Wireless Communications and Networking Conference
    'natelectron',  # Nature Electronics
    'nphoton',  # Nature Photonics
    'npjflexelectron',  # npj Flexible Electronics
    'j-7c6e5692e3',  # Frontiers of Computer Science
    'j-21982a54fe',  # Science China Information Sciences
    'j-2912789b57',  # Ad Hoc Networks
    'j-f7cc482a48',  # Advanced Sensor and Energy Materials
    'j-1990fab752',  # Agriculture Communications
    'j-a93c728c29',  # Computer Networks
    'j-ed923e2572',  # Information Sciences
    'ipmi',  # International Conference on Information Processing in Medical Imaging
    'j-be601df25e',  # Research
    'j-4143d04801',  # Engineering
    'j-2787efe2f4',  # Science Bulletin
    'nature',  # Nature
    'ncomms',  # Nature Communications
    'srep',  # Scientific Reports
    'j-d2d0663714',  # Science
    'j-5b29afb433',  # Science Advances
    'j-b6525f43da',  # iScience
    'j-9c7c2ba906',  # The Innovation
)

# 以下来源未被本次建议纳入，保留记录；不加入 APPROVED_SOURCES。
# 'spj-ultrafastscience',  # 补充候选：Ultrafast Science
# 'j-6e5458755a',  # 补充候选：The Science of The Total Environment
# 'j-5844f85801',  # 补充候选：GEOSCIENTIFIC MODEL DEVELOPMENT
# 'j-c6e762ffed',  # 补充候选：Journal of Advances in Modeling Earth Systems
# 'j-c2f6213a4a',  # 补充候选：Cell Reports Sustainability
# 'commssustain',  # 补充候选：Communications Sustainability
# 'npjclimataction',  # 补充候选：npj Climate Action
# 'npjmatsustain',  # 补充候选：npj Materials Sustainability
# 'npjnathazards',  # 补充候选：npj Natural Hazards
# 'npjoceansustain',  # 补充候选：npj Ocean Sustainability
# 'npjsustainagric',  # 补充候选：npj Sustainable Agriculture
# 'npjsustainmobil',  # 补充候选：npj Sustainable Mobility and Transport
# 'j-497cf31d67',  # 补充候选：Ecological Modelling
# 'natprogsuschem',  # 暂缓：Nature Progress Sustainable Chemistry
# 'nrbd',  # 暂缓：Nature Reviews Biodiversity
# 'npjbiodivers',  # 暂缓：npj Biodiversity
# 'npjforests',  # 暂缓：npj Forests
# 'npjgeoinform',  # 暂缓：npj Geoinformatics
# 'npjhydrosph',  # 暂缓：npj Hydrosphere
# 'npjsoilecol',  # 暂缓：npj Soil Ecology
# 'j-665fe8ec0f',  # 暂缓：Current Forestry Reports
# 'j-851b57d116',  # 暂缓：Reviews in Environmental Science and Bio/Technology
# 'j-1686531bfd',  # 补充候选：IEEE Transactions on Geoscience and Remote Sensing
# 'j-a6696dab7e',  # 暂缓：Current Climate Change Reports
# 'spj-olar',  # 补充候选：Ocean-Land-Atmosphere Research
# 'commsmat',  # 补充候选：Communications Materials
# 'npjmetamat',  # 补充候选：npj Metamaterials
# 'nature-pj',  # 补充候选：Polymer Journal
# 'j-a3d114c36b',  # 补充候选：Chem Catalysis
# 'j-dce56550fe',  # 补充候选：Nano Research
# 'j-c310c924e1',  # 补充候选：Chemical Engineering Research and Design
# 'j-c2fd137b24',  # 补充候选：Chemical Engineering Science
# 'j-3ceb99ac46',  # 补充候选：Computational Materials Science
# 'j-8bf921d704',  # 补充候选：Computers & Chemical Engineering
# 'j-301985dec6',  # 补充候选：ACS Central Science
# 'j-a4d6e94493',  # 补充候选：ACS Nano
# 'j-57fdf66acb',  # 补充候选：Advanced Functional Materials
# 'j-e9df882b6e',  # 补充候选：Advanced Materials
# 'j-68483fd883',  # 补充候选：Angewandte Chemie International Edition
# 'j-f2809cf9cd',  # 补充候选：Chemical Reviews
# 'j-d48594a04d',  # 补充候选：Chemical Science
# 'j-b3bd439b46',  # 补充候选：Chemical Society Reviews
# 'j-a6648ce51f',  # 补充候选：Chemistry of Materials
# 'j-9f6d0b4963',  # 补充候选：Digital Discovery
# 'j-c3bb7ec73a',  # 补充候选：Journal of Chemical Information and Modeling
# 'j-69bc6ac864',  # 补充候选：Journal of Chemical Theory and Computation
# 'j-239c7d332f',  # 补充候选：Journal of the American Chemical Society
# 'npjbiocatal',  # 暂缓：npj Biocatalysis
# 'npjphotocatal',  # 暂缓：npj Photocatalysis
# 'j-30ce503fad',  # 暂缓：Electrochemical Energy Reviews
# 'j-cf36dbf511',  # 暂缓：Chinese Journal of Catalysis
# 'j-136b68687f',  # 暂缓：Journal of Photochemistry and Photobiology C Photochemistry Reviews
# 'j-5f7da8f493',  # 暂缓：Progress in Lipid Research
# 'npjrobot',  # 补充候选：npj Robotics
# 'j-a22fc94b94',  # 补充候选：IEEE Robotics and Automation Letters
# 'j-a66eea4387',  # 补充候选：IEEE Transactions on Robotics
# 'corl',  # 暂缓：Conference on Robot Learning
# 'cogsci',  # 暂缓：Annual Meeting of the Cognitive Science Society
# 'wine',  # 暂缓：Conference on Web and Internet Economics
# 'emsoft',  # 暂缓：International Conference on Embedded Software
# 'j-331477104b',  # 暂缓：JOURNAL OF INNOVATION & KNOWLEDGE
# 'l4dc',  # 暂缓：Learning for Dynamics and Control
# 'commseng',  # 补充候选：Communications Engineering
# 'gecco',  # 暂缓：Genetic and Evolutionary Computation Conference
# 'j-a9e96933ba',  # 暂缓：GREEN ENERGY AND INTELLIGENT TRANSPORTATION
# 'j-2d54e9e9d0',  # 暂缓：JOURNAL OF INDUSTRIAL INFORMATION INTEGRATION
# 'ijcnn',  # 补充候选：International Joint Conference on Neural Networks
# 'acml',  # 暂缓：Asian Conference on Machine Learning
# 'icann',  # 暂缓：International Conference on Artificial Neural Networks
# 'msml',  # 暂缓：Mathematical and Scientific Machine Learning
# 'j-a1003cddd1',  # 补充候选：Future Generation Computer Systems
# 'podc',  # 暂缓：ACM Symposium on Principles of Distributed Computing
# 'dac',  # 暂缓：Design Automation Conference
# 'euro-par',  # 暂缓：European Conference on Parallel and Distributed Computing
# 'hot-chips',  # 暂缓：Hot Chips: A Symposium on High Performance Chips
# 'cluster',  # 暂缓：IEEE International Conference on Cluster Computing
# 'rtas',  # 暂缓：IEEE Real-Time and Embedded Technology and ApplicationsSymposium
# 'iccad',  # 暂缓：International Conference on Computer-Aided Design
# 'codes-isss',  # 暂缓：International Conference on Hardware/Software Co-design and System Synthesis
# 'hipeac',  # 暂缓：International Conference on High Performance and Embedded Architectures and Compilers
# 'sigmetrics',  # 暂缓：International Conference on Measurement and Modeling of Computer Systems
# 'pact',  # 暂缓：International Conference on Parallel Architectures and Compilation Techniques
# 'vee',  # 暂缓：International Conference on Virtual Execution Environments
# 'performance',  # 暂缓：International Symposium on Computer Performance, Modeling, Measurements and Evaluation
# 'itc',  # 暂缓：International Test Conference
# 'lisa',  # 暂缓：Large Installation System Administration Conference
# 'msst',  # 暂缓：Mass Storage Systems and Technologies
# 'hpdc',  # 暂缓：The International ACM Symposium on High-Performance Parallel and Distributed Computing
# 'fast',  # 暂缓：USENIX Conference on File and Storage Technologies
# 'stoc',  # 暂缓：ACM Symposium on the Theory of Computing
# 'lics',  # 暂缓：ACM/IEEE Symposium on Logic in Computer Science
# 'cade',  # 暂缓：Conference on Automated Deduction
# 'ccc',  # 暂缓：Conference on Computational Complexity
# 'esa',  # 暂缓：European Symposium on Algorithms
# 'fmcad',  # 暂缓：Formal Methods in Computer-Aided Design
# 'icalp',  # 暂缓：International Colloquium on Automata, Languages and Programming
# 'cocoon',  # 暂缓：International Computing and Combinatorics Conference
# 'cav',  # 暂缓：International Conference on Computer Aided Verification
# 'concur',  # 暂缓：International Conference on Concurrency Theory
# 'sat',  # 暂缓：International Conference on Theory and Applications of Satisfiability Testing
# 'socg',  # 暂缓：International Symposium on Computational Geometry
# 'automl',  # 暂缓：International Conference on Automated Machine Learning
# 'i3d',  # 暂缓：ACM SIGGRAPH Symposium onInteractive 3D Graphics and Games
# 'icmr',  # 暂缓：ACM SIGMM International Conference on Multimedia Retrieval
# 'eurographics',  # 暂缓：Annual Conference of the European Association for Computer Graphics
# 'interspeech',  # 暂缓：Conference of the International Speech Communication Association
# 'eurovis',  # 暂缓：Eurographics Conference on Visualization
# 'sgp',  # 暂缓：Eurographics Symposium on Geometry Processing
# 'egsr',  # 暂缓：Eurographics Symposium on Rendering
# 'ismar',  # 暂缓：International Symposium on Mixed and Augmented Reality
# 'pg',  # 暂缓：Pacific Conference on Computer Graphics and Applications
# 'spm',  # 暂缓：Symposium on Solid and Physical Modeling
# 'j-eea156e193',  # 补充候选：GigaScience
# 'j-68da5d732a',  # 补充候选：Cell Reports Methods
# 'j-4d34f7a2b0',  # 补充候选：Patterns
# 'j-d21769e19b',  # 补充候选：ACM Transactions on Knowledge Discovery from Data
# 'j-cc1fc20e2d',  # 补充候选：IEEE Transactions on Knowledge and Data Engineering
# 'wsdm',  # 暂缓：ACM International Conference on Web Search and Data Mining
# 'icde',  # 暂缓：IEEE International Conference on Data Engineering
# 'dasfaa',  # 暂缓：International Conference on Database Systems for Advanced Applications
# 'icdt',  # 暂缓：International Conference on Database Theory
# 'edbt',  # 暂缓：International Conference on Extending DatabaseTechnology
# 'iswc',  # 暂缓：International Semantic Web Conference
# 'wise',  # 暂缓：Web Information Systems Engineering Conference
# 'log',  # 暂缓：Learning on Graphs Conference
# 'clear',  # 暂缓：Conference on Causal Learning and Reasoning
# 'colm',  # 暂缓：Conference on Language Modeling
# 'j-b21279a93a',  # 补充候选：Quantitative Science Studies
# 'nesy',  # 暂缓：International Conference on Neurosymbolic Learning and Reasoning
# 'j-949f7bec3f',  # 补充候选：ACM Computing Surveys
# 'j-3c70509180',  # 补充候选：IEEE Transactions on Evolutionary Computation
# 'j-f583f91ba0',  # 补充候选：IEEE Transactions on Neural Networks and Learning Systems
# 'j-3450721b9d',  # 补充候选：IEEE Transactions on Pattern Analysis and Machine Intelligence
# 'j-680c2237d5',  # 补充候选：Journal of Machine Learning Research
# 'j-2e4f8bd724',  # 补充候选：Applied Intelligence
# 'j-5912944ab3',  # 补充候选：Neural Computing and Applications
# 'npjai',  # 补充候选：npj Artificial Intelligence
# 'npjunconvcomput',  # 补充候选：npj Unconventional Computing
# 'nrcomput',  # 不纳入：Nature Reviews Computing
# 'commsaicomp',  # 补充候选：Communications AI & Computing
# 'j-37f5e0cab9',  # 补充候选：Transactions on Machine Learning Research
# 'npjcleanenergy',  # 补充候选：npj Clean Energy
# 'npjenergymats',  # 补充候选：npj Energy Materials
# 'j-fe93cecc28',  # 补充候选：Energy and AI
# 'j-8ecdcf78fa',  # 补充候选：Energy & Environmental Science
# 'npjelectsysres',  # 暂缓：npj Energy Systems and Resilience
# 'j-4509d0b256',  # 暂缓：Energy Material Advances
# 'npjsciplants',  # 暂缓：npj Science of Plants
# 'cscw',  # 暂缓：ACM Conference on Computer Supported Cooperative Work and Social Computing
# 'chi',  # 暂缓：ACM Conference on Human Factors in Computing Systems
# 'iui',  # 暂缓：ACM International Conference on Intelligent User Interfaces
# 'iss',  # 暂缓：ACM International Conference on Interactive Surfaces and Spaces
# 'mobilehci',  # 暂缓：ACM International Conference on Mobile Human-Computer Interaction
# 'group',  # 暂缓：ACM International Conference on Supporting Group Work
# 'ecscw',  # 暂缓：European Conference on Computer Supported Cooperative Work
# 'ic2s2',  # 暂缓：International Conference on Computational Social Science
# 'j-2db3853929',  # 补充候选：Omega
# 'commspsychol',  # 补充候选：Communications Psychology
# 'nature-dpn',  # 补充候选：NPP—Digital Psychiatry and Neuroscience
# 'npjenvsocsci',  # 暂缓：npj Environmental Social Sciences
# 'spj-ehs',  # 补充候选：Ecosystem Health and Sustainability
# 'commshealth',  # 补充候选：Communications Health
# 'commsmed',  # 补充候选：Communications Medicine
# 'naturehealth',  # 补充候选：Nature Health
# 'natmentalhealth',  # 补充候选：Nature Mental Health
# 'npjadvmanuf',  # 补充候选：npj Advanced Manufacturing
# 'npjbts',  # 补充候选：npj Biological Timing and Sleep
# 'npjbiomedinnov',  # 补充候选：npj Biomedical Innovations
# 'npjbiosensing',  # 补充候选：npj Biosensing
# 'npjcardiohealth',  # 补充候选：npj Cardiovascular Health
# 'npjcleanair',  # 补充候选：npj Clean Air
# 'npjcomplex',  # 补充候选：npj Complexity
# 'npjdementia',  # 补充候选：npj Dementia
# 'npjdigipubhealth',  # 补充候选：npj Digital Public Health
# 'npjdrugdiscov',  # 补充候选：npj Drug Discovery
# 'npjemergcontam',  # 补充候选：npj Emerging Contaminants
# 'npjhealthsyst',  # 补充候选：npj Health Systems
# 'npjheritagesci',  # 补充候选：npj Heritage Science
# 'npjimaging',  # 补充候选：npj Imaging
# 'npjmentalhealth',  # 补充候选：npj Mental Health Research
# 'npjmetabhealth',  # 补充候选：npj Metabolic Health and Disease
# 'npjsoftmat',  # 补充候选：npj Soft Matter
# 'npjspintronics',  # 补充候选：npj Spintronics
# 'npjviruses',  # 补充候选：npj Viruses
# 'nature-bdjopen',  # 补充候选：BDJ Open
# 'nature-bjcreports',  # 补充候选：BJC Reports
# 'nature-bdj',  # 补充候选：British Dental Journal
# 'nature-ejcn',  # 补充候选：European Journal of Clinical Nutrition
# 'nature-ebd',  # 补充候选：Evidence-Based Dentistry
# 'nature-eyeopen',  # 补充候选：Eye Open
# 'nature-hdy',  # 补充候选：Heredity
# 'nature-hgv',  # 补充候选：Human Genome Variation
# 'nature-ijir',  # 补充候选：International Journal of Impotence Research
# 'nature-jhg',  # 补充候选：Journal of Human Genetics
# 'nature-jp',  # 补充候选：Journal of Perinatology
# 'nature-sc',  # 补充候选：Spinal Cord
# 'nature-ismej',  # 补充候选：The ISME Journal
# 'nature-tpj',  # 补充候选：The Pharmacogenomics Journal
# 'j-4d6ad57450',  # 补充候选：BioDesign Research
# 'j-4268ecb123',  # 补充候选：Computational and Structural Biotechnology Journal
# 'j-0525f40568',  # 补充候选：Cell Biomaterials
# 'j-88c0f6266b',  # 补充候选：Cell Genomics
# 'j-3af9c228f4',  # 补充候选：Biophysical Journal
# 'j-b07ab475f0',  # 补充候选：Human Genetics and Genomics Advances
# 'j-67e951c2e5',  # 补充候选：Molecular Therapy — Methods & Clinical Development
# 'j-43ec917d32',  # 补充候选：The Lancet Regional Health - Americas
# 'j-4a28339855',  # 补充候选：The Lancet Regional Health - Southeast Asia
# 'j-7b7eedfada',  # 补充候选：Computers in Biology and Medicine
# 'j-7cd0deae63',  # 补充候选：Journal of Biomedical Informatics
# 'j-ed1b6b5acc',  # 补充候选：Bioinformatics
# 'j-be3892c033',  # 补充候选：BMJ
# 'j-29a8fd9812',  # 补充候选：Briefings in Bioinformatics
# 'j-a2a4c86493',  # 补充候选：IEEE Journal of Biomedical and Health Informatics
# 'j-59177541f9',  # 补充候选：IEEE Transactions on Biomedical Engineering
# 'j-a5410147da',  # 补充候选：IEEE Transactions on Medical Imaging
# 'j-a479480dc4',  # 补充候选：JAMA
# 'j-fc68afbde2',  # 补充候选：NEJM AI
# 'j-aa4951a524',  # 补充候选：Nucleic Acids Research
# 'j-d921d2ae3e',  # 补充候选：PLoS Biology
# 'j-81fef52ed0',  # 补充候选：PLoS Computational Biology
# 'j-66e46642fc',  # 补充候选：PLoS Genetics
# 'j-f5eb35c2ed',  # 补充候选：PLoS Medicine
# 'j-d9b5ac56cb',  # 补充候选：Radiology Artificial Intelligence
# 'j-bc46f9e3a8',  # 补充候选：The New England Journal of Medicine
# 'acm-bcb',  # 暂缓：ACM Conference on Bioinformatics, Computational Biology, and Health Informatics
# 'chil',  # 暂缓：Conference on Health, Inference, and Learning
# 'ml4h',  # 暂缓：Machine Learning for Health
# 'mlhc',  # 暂缓：Machine Learning for Healthcare Conference
# 'mlcb',  # 暂缓：Machine Learning in Computational Biology
# 'midl',  # 暂缓：Medical Imaging with Deep Learning
# 'psb',  # 暂缓：Pacific Symposium on Biocomputing
# 'natprogbrainhealth',  # 暂缓：Nature Progress Brain Health
# 'natprogoncology',  # 暂缓：Nature Progress Oncology
# 'nrct',  # 暂缓：Nature Reviews Clean Technology
# 'nrdp',  # 暂缓：Nature Reviews Disease Primers
# 'nrneph',  # 暂缓：Nature Reviews Nephrology
# 'npjautoimmun',  # 暂缓：npj Autoimmunity
# 'npjdigisurg',  # 暂缓：npj Digital Surgery
# 'npjentomology',  # 暂缓：npj Entomology
# 'npjexercisemed',  # 暂缓：npj Exercise Medicine and Health
# 'npjextremeeco',  # 暂缓：npj Extreme Ecosystems
# 'npjfungalsci',  # 暂缓：npj Fungal Science
# 'npjgutliver',  # 暂缓：npj Gut and Liver
# 'npjnephrology',  # 暂缓：npj Nephrology
# 'npjpain',  # 暂缓：npj Pain
# 'npjpalaeo',  # 暂缓：npj Palaeoecosystems
# 'npjparasitology',  # 暂缓：npj Parasitology
# 'npjstructbiol',  # 暂缓：npj Structural Biology
# 'npjtoxicol',  # 暂缓：npj Toxicology
# 'npjvetsci',  # 暂缓：npj Veterinary Sciences
# 'npjwomenshealth',  # 暂缓：npj Women's Health
# 'nature-boneres',  # 暂缓：Bone Research
# 'nature-cgt',  # 暂缓：Cancer Gene Therapy
# 'nature-cdd',  # 暂缓：Cell Death and Differentiation
# 'nature-cddis',  # 暂缓：Cell Death and Disease
# 'nature-cmi',  # 暂缓：Cellular and Molecular Immunology
# 'nature-emm',  # 暂缓：Experimental & Molecular Medicine
# 'nature-gt',  # 暂缓：Gene Therapy
# 'nature-ijos',  # 暂缓：International Journal of Oral Science
# 'nature-jhh',  # 暂缓：Journal of Human Hypertension
# 'nature-lsa',  # 暂缓：LIGHT-SCIENCE & APPLICATIONS
# 'nature-mi',  # 暂缓：Mucosal Immunology
# 'nature-sigtrans',  # 暂缓：SIGNAL TRANSDUCTION AND TARGETED THERAPY
# 'nature-ja',  # 暂缓：The Journal of Antibiotics
# 'j-0f9af82bfb',  # 暂缓：Science Signaling
# 'j-744a74032c',  # 暂缓：BME Frontiers
# 'j-14206a3533',  # 暂缓：Angiogenesis
# 'j-4cafd90e4b',  # 暂缓：Biological Research
# 'j-729ebff637',  # 暂缓：Cancer and Metastasis Reviews
# 'j-f3f8479ad0',  # 暂缓：Current Obesity Reports
# 'j-a737560684',  # 暂缓：Fungal Diversity
# 'j-f13260538a',  # 暂缓：Seminars in Immunopathology
# 'j-15b33dc45b',  # 暂缓：Cytokine & Growth Factor Reviews
# 'j-26e867c25f',  # 暂缓：JACC Cardiovascular Imaging
# 'j-7bda0e0eda',  # 暂缓：Progress in Retinal and Eye Research
# 'j-cdad3c6aec',  # 暂缓：Seminars in Immunology
# 'npjbiolphysmech',  # 补充候选：npj Biological Physics and Mechanics
# 'npjspaceexplor',  # 补充候选：npj Space Exploration
# 'j-006b8c5903',  # 补充候选：Newton
# 'j-0cff477bcb',  # 补充候选：Journal of Computational Science
# 'j-697a8c3ea6',  # 补充候选：Machine Learning Science and Technology
# 'j-6134caba4b',  # 补充候选：Physical Review Letters
# 'j-c1df51cc17',  # 补充候选：Physical Review Research
# 'j-b17d143a2d',  # 补充候选：Physical Review X
# 'j-3d890ee256',  # 补充候选：SIAM Journal on Mathematics of Data Science
# 'j-4b079da7ee',  # 补充候选：SIAM Journal on Scientific Computing
# 'npjstructeng',  # 暂缓：npj Structural Engineering
# 'npjthermscieng',  # 暂缓：npj Thermal Science and Engineering
# 'j-f50657d29a',  # 暂缓：Living Reviews in Solar Physics
# 'j-957d6a1aa2',  # 暂缓：The Astronomy and Astrophysics Review
# 'j-2df580d5e1',  # 暂缓：New Astronomy Reviews
# 'natmecheng',  # 不纳入：Nature Mechanical Engineering
# 'colt',  # 暂缓：Annual Conference on Computational Learning Theory
# 'uai',  # 暂缓：Conference on Uncertainty in ArtificialIntelligence
# 'iccbr',  # 暂缓：International Conference on Case-Based Reasoning
# 'aistats',  # 暂缓：International Conference on Artificial Intelligence and Statistics
# 'j-5bea5723be',  # 暂缓：Living Reviews in Relativity
# 'sigcomm',  # 暂缓：ACM International Conference on Applications, Technologies, Architectures, and Protocols for Computer Communication
# 'conext',  # 暂缓：ACM International Conference on emerging Networking EXperiments and Technologies
# 'mobicom',  # 暂缓：ACM International Conference on Mobile Computing and Networking
# 'mobisys',  # 暂缓：ACM International Conference on Mobile Systems, Applications, and Services
# 'imc',  # 暂缓：ACM Internet Measurement Conference
# 'ipsn',  # 暂缓：International Conference on Information Processing in Sensor Networks
# 'nossdav',  # 暂缓：International Workshop on Network and Operating System Support for Digital Audio and Video
# 'ccs',  # 暂缓：ACM Conference on Computer and Communications Security
# 'asiacrypt',  # 暂缓：Annual International Conference on the Theory and Application of Cryptology and Information Security
# 'esorics',  # 暂缓：European Symposium on Research in Computer Security
# 'fse-crypto',  # 暂缓：Fast Software Encryption
# 'csfw',  # 暂缓：IEEE Computer Security Foundations Symposium
# 'ches',  # 暂缓：International Conference on Cryptographic Hardware and Embedded Systems
# 'eurocrypt',  # 暂缓：International Conference on the Theory and Applications of Cryptographic Techniques
# 'crypto',  # 暂缓：International Cryptology Conference
# 'raid',  # 暂缓：International Symposium on Research in Attacks, Intrusions and Defenses
# 'pkc',  # 暂缓：International Workshop on Practice and Theory in Public Key Cryptography
# 'tcc',  # 暂缓：Theory of Cryptography Conference
# 'fse',  # 暂缓：ACM International Conference on the Foundations of Software Engineering
# 'icfp',  # 暂缓：ACM SIGPLAN International Conference on Function Programming
# 'popl',  # 暂缓：ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
# 'sosp',  # 暂缓：ACM Symposium on Operating Systems Principles
# 'oopsla',  # 暂缓：Conference on Object-Oriented Programming Systems, Languages,and Applications
# 'ecoop',  # 暂缓：European Conference on Object-Oriented Programming
# 'etaps',  # 暂缓：European Joint Conferences on Theory and Practice of Software
# 'icws',  # 暂缓：IEEE International Conference on Web Services
# 're',  # 暂缓：IEEE International Requirements Engineering Conference
# 'caise',  # 暂缓：International Conference on Advanced Information Systems Engineering
# 'cp',  # 暂缓：International Conference on Principles and Practice of Constraint Programming
# 'icsoc',  # 暂缓：International Conference on Service Oriented Computing
# 'vmcai',  # 暂缓：International Conference on Verification,Model Checking, and Abstract Interpretation
# 'middleware',  # 暂缓：International Middleware Conference
# 'sas',  # 暂缓：International Static Analysis Symposium
# 'esem',  # 暂缓：International Symposium on Empirical Software Engineering and Measurement
# 'fm',  # 暂缓：International Symposium on Formal Methods
# 'hotos',  # 暂缓：USENIX Workshop on Hot Topics in Operating Systems
# 'j-a5a74a6df0',  # 补充候选：Device
# 'natsensors',  # 补充候选：Nature Sensors
# 'npjacoustics',  # 补充候选：npj Acoustics
# 'npjnanophoton',  # 补充候选：npj Nanophotonics
# 'npjwireltech',  # 补充候选：npj Wireless Technology
# 'nature-ismecomms',  # 补充候选：ISME Communications
# 'j-945993e932',  # 补充候选：Frontiers of Information Technology & Electronic Engineering
# 'j-988beb915d',  # 补充候选：Computer Communications
# 'j-edbd772c3e',  # 补充候选：ICT Express
# 'j-45e5b14725',  # 补充候选：IEEE Communications Surveys & Tutorials
# 'j-c2d07012e9',  # 补充候选：IEEE Internet of Things Journal
# 'j-2171d9d29e',  # 补充候选：IEEE Journal on Selected Areas in Communications
# 'j-6b255f4362',  # 补充候选：IEEE Transactions on Communications
# 'j-01ff6b321b',  # 补充候选：IEEE Transactions on Signal Processing
# 'j-6f4955aab1',  # 补充候选：IEEE Transactions on Wireless Communications
# 'natprogoptphoton',  # 暂缓：Nature Progress Optics & Photonics
# 'npjintgrelect',  # 暂缓：npj Integrated Electronics
# 'npjpowerelect',  # 暂缓：npj Power Electronics
# 'npjselfpowelect',  # 暂缓：npj Self-Powered Electronics
# 'j-36fac3e093',  # 暂缓：Advanced Devices & Instrumentation
# 'j-423e2dd439',  # 暂缓：DIGITAL COMMUNICATIONS AND NETWORKS
# 'j-8d0ae5771c',  # 暂缓：INTERNET OF THINGS
# 'scirev',  # 补充候选：Scientific Reviews
# 'j-485a04fef4',  # 补充候选：Nexus
# 'j-1291b1ecf4',  # 补充候选：National Science Review
# 'j-4ac86cfc4b',  # 补充候选：PNAS Nexus
# 'j-5206bf3cc0',  # 补充候选：Proceedings of the National Academy of Sciences
