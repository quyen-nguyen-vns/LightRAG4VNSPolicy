qa_data = [
    {
        "question": "What is the document’s most recent update date and effective date?",
        "expected_answer": "Updated: 25/11/2024; Effective: 25/11/2024",
        "where_in_doc": "Cover header, Page 1",
    },
    {
        "question": "How does the policy define Personal Data?",
        "expected_answer": "Information and data about individuals (symbols, letters, numbers, images, sounds, etc.) associated with a specific person or enabling identification, including basic and sensitive personal data.",
        "where_in_doc": "Personal Data definition, Page 1",
    },
    {
        "question": "List 5 example items considered Personal Data in this policy.",
        "expected_answer": "ID/citizen identification/passport; full name; date of birth; gender; residence; (also email, phone number, marital status, education, work experience, etc.)",
        "where_in_doc": "Examples of Personal Data, Page 1",
    },
    {
        "question": "What must you confirm about any referee information you add to your profile?",
        "expected_answer": "You confirm you have read and agreed that employers may contact the referee, and that you have consent/approval to provide the referee’s details.",
        "where_in_doc": "Referee information note, Page 1",
    },
    {
        "question": "Give three purposes for which VNS may process Personal Data without prior notice or consent.",
        "expected_answer": "Compliance and risk (e.g., AML/anti-corruption/conflict checks/accounting); surveys/research/quality assessment; dispute resolution and database management.",
        "where_in_doc": "Processing purposes, Page 1",
    },
    {
        "question": "What right do you have if your Personal Data is outdated or inaccurate?",
        "expected_answer": "You may request VNS to update, correct, or adjust the information, and VNS may process your data for that adjustment without prior notice or consent.",
        "where_in_doc": "Adjust Personal Data, Page 1",
    },
    {
        "question": "Name two ways VNS collects Personal Data.",
        "expected_answer": "Directly from you (e.g., forms/requests/contacts) and indirectly via websites/apps/social media usage.",
        "where_in_doc": "How data is collected, Page 2–3",
    },
    {
        "question": "Provide three technical data points VNS may collect when you use its websites or apps.",
        "expected_answer": "IP address; browser type/version; time zone settings; (also OS/platform, plugin types, device info, etc.)",
        "where_in_doc": "Technical information list, Page 2–3",
    },
    {
        "question": "State three purposes for which your personal information may be used.",
        "expected_answer": "Managing/performing requests and contracts (including renewals/claims/fees); communicating with you (management info, technical support); designing or improving products/services.",
        "where_in_doc": "Purposes list, Page 3",
    },
    {
        "question": "What security measures does VNS mention for protecting Personal Data?",
        "expected_answer": "Restricting direct data access within VNS systems and encrypting sensitive data during transmission; deletion/destruction when no longer needed.",
        "where_in_doc": "Retention and safeguards, Page 4",
    },
    {
        "question": "Who may your Personal Data be disclosed to? Give three categories.",
        "expected_answer": "VNS agents/contractors/third-party service providers (e.g., IT, cloud, customer centers); any member company of VNS; government or regulatory authorities as required by law.",
        "where_in_doc": "Disclosure recipients, Page 4",
    },
    {
        "question": "Where may your information be processed or stored geographically?",
        "expected_answer": "In Vietnam or any country where VNS or its third-party contractors are based or provide services.",
        "where_in_doc": "Cross-border transfer, Page 4",
    },
    {
        "question": "What is the contact email for requests about accessing or correcting Personal Data?",
        "expected_answer": "career@vnsilicon.net",
        "where_in_doc": "Contact for requests, Page 4",
    },
    {
        "question": "May VNS use your data for direct marketing? Under what condition?",
        "expected_answer": "Yes, if permitted by law; where required, only after obtaining your consent. You can later withdraw consent.",
        "where_in_doc": "Direct marketing section, Page 4–5",
    },
    {
        "question": "How can you opt out of direct marketing after consenting?",
        "expected_answer": "Notify VNS in writing to the address in the “Right to Access Personal Data” section or email career@vnsilicon.net.",
        "where_in_doc": "Direct marketing opt-out, Page 5",
    },
    {
        "question": "What kinds of information can data processing tools (cookies) collect for analytics?",
        "expected_answer": "IP, domain, browser/software type/configuration, language, location, OS, referrer, pages/content viewed, access time.",
        "where_in_doc": "Use of Data Processing Tools, Page 5",
    },
    {
        "question": "What happens if you block the site’s data processing tools (cookies)?",
        "expected_answer": "You won’t fully enjoy all benefits; some functions may not work correctly.",
        "where_in_doc": "Cookie preferences impact, Page 5",
    },
    {
        "question": "Does the policy permit automated processing of personal data?",
        "expected_answer": "Yes, VNS may apply automated personal data processing methods through algorithms.",
        "where_in_doc": "Automated processing note, Page 5",
    },
    {
        "question": "Are external websites linked from VNS covered by this Policy?",
        "expected_answer": "No; you should check the privacy policies of those external sites.",
        "where_in_doc": "External Links, Page 5",
    },
    {
        "question": "Can VNS change this Policy without prior notice, and when do changes take effect?",
        "expected_answer": "Yes; changes may be made at any time without notice and take effect immediately upon being updated on the website/app/tool.",
        "where_in_doc": "Amendments to Privacy Policy, Page 5–6",
    },
    # --- From Onboarding Document ---
    {
        "question": "What is VNS’s mission?",
        "expected_answer": "To become the premier innovation and technology solutions center driving digital transformation, empowering businesses and talent through cutting-edge solutions.",
        "where_in_doc": "Onboarding – Mission & Vision :contentReference[oaicite:0]{index=0}",
    },
    {
        "question": "What are the core values of VNS?",
        "expected_answer": "Innovation, Client Focus, Excellence, Integrity, Employee-centric, Growth Mindset, Empowerment, Recognition & Rewards, Diversity & Inclusion, Entrepreneurial Spirit.",
        "where_in_doc": "Onboarding – Values & Culture :contentReference[oaicite:1]{index=1}",
    },
    {
        "question": "When was VNS licensed and when did the first office open?",
        "expected_answer": "Licensed on 15 Nov 2024; first office opened on 25 Dec 2024 with 8 members.",
        "where_in_doc": "Onboarding – VNS Journey :contentReference[oaicite:2]{index=2}",
    },
    {
        "question": "What industries does VNS serve?",
        "expected_answer": "Financial services, retail & e-commerce, agriculture, manufacturing, logistics & transportation, and government services.",
        "where_in_doc": "Onboarding – Client sectors :contentReference[oaicite:3]{index=3}",
    },
    {
        "question": "Who are the top executives of VNS?",
        "expected_answer": "CEO: Tai Pham; Managing Director: Jessica Quach; Technical Director: Kevin Le.",
        "where_in_doc": "Onboarding – Organization Structure :contentReference[oaicite:4]{index=4}",
    },
    {
        "question": "What are some key benefits and rewards offered by VNS?",
        "expected_answer": "Competitive salary, 13th-month bonus, annual performance bonus, loyalty bonuses (1M at 3 years, 1.5M at 5 years, 2M at 10 years), allowances, healthcare premium, extra leave days, training, company trips, TET gift, and welcome kit.",
        "where_in_doc": "Onboarding – Compensation & Benefits :contentReference[oaicite:5]{index=5}",
    },
    {
        "question": "What are the official working hours at VNS?",
        "expected_answer": "Monday to Friday, 8 hours/day. Morning: 09:00–12:00, Afternoon: 13:00–18:00.",
        "where_in_doc": "Onboarding – Internal Policy :contentReference[oaicite:6]{index=6}",
    },
    {
        "question": "What does the first-day onboarding schedule include?",
        "expected_answer": "10:00–10:15: Office tour/photos; 10:15–11:30: IT equipment setup; 11:30–12:00: Team introductions; 12:00–13:00: Lunch break; 13:00–17:00: Team catch-up; 17:00–18:00: HRBP check-in.",
        "where_in_doc": "Onboarding – Next Schedule :contentReference[oaicite:7]{index=7}",
    },
]
