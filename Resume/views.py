from django.shortcuts import render
import plotly.graph_objects as go


# Create your views here.
def about_me(request):
    info = {
        'favicon': 'https://raw.githubusercontent.com/wadeChriestenson/Resume/main/assets/img/resume-100x100.png',
        'name': 'Wade Chriestenson',
        'hello': 'Hello World!!!',
        'email': 'wade@wadeprojects.io',
        'emailLink': 'mailto:wade@wadeprojects.io',
        'emailPic': 'https://raw.githubusercontent.com/wadeChriestenson/Resume/main/assets/img/email.png',
        'gitHub': 'https://github.com/wadeChriestenson',
        'gitHubPic': 'https://raw.githubusercontent.com/wadeChriestenson/Resume/main/assets/img/github.png',
        'linkedin': 'https://www.linkedin.com/in/wadechriestenson/',
        'linkedinPic': 'https://raw.githubusercontent.com/wadeChriestenson/Resume/main/assets/img/linkedin.png',
        'phoneNum': 'tel:620-869-5907',
        'phone': '620 869-5907',
        'phonePic': 'https://raw.githubusercontent.com/wadeChriestenson/Resume/main/assets/img/phone.png',
    }
    theWhy = {
        '1': 'Critical Thinking - I Must',
        '2': 'Problem Solving - Out of Necessity',
        '3': 'Self Taught - with a Keyboard',
        '4': 'Intermediate Googler',
        '5': 'Team Focused',
        '6': 'I find the Solution'
    }
    work1 = {
        'companyName': 'Vision Plastics',
        'dates': 'Dec 2020 to Present',
        'task1': 'Create or update standard work for assembly department using the corporate ERP.',
        'task2': 'Setup machine per MESI documents(sonic welders, CNC, drill presses, heat stakers, etc..)',
        'task3': 'Problem Solve and Trouble shot defects caused by operators or machinery in assembly.',
        'task4': 'Practice and implement lean throughout the assembly department(5s, one piece flow, standard work.)',
    }
    work2 = {
        'companyName': 'Pioneer Truck Weld',
        'dates': 'Sep 2020 to Dec 2020',
        'task1': 'Brake Press Operator- Run and maintain presses. ',
        'task2': 'Form parts to prints and assure all parts meet quality standard. ',
        'task3': 'Plasma Table- Cut flat metal parts to desired measurements. ',
        'task4': 'Hoist and store metal to location. ',
        'task5': 'Sheer Operator- cut and square flat parts to desired prints and organize parts per value stream.',
    }
    work3 = {
        'companyName': 'ATI',
        'dates': 'Aug 2018 to July 2020',
        'task1': 'Blend Specialist- Blend titanium parts to specified work instruction.',
        'task2': 'Pneumatic hand tools- Work and understand all basic pneumatic forms of Dremel’s,',
        'task3': 'ninety-degree grinders, orbital sanders, and three-inch grinders.',
        'task4': 'Quality- Read and follow quality roadmaps per part, first pass yields all time.',
        'task5': 'Maintained- Clean, stock, sweep and follow daily, weekly, and monthly cleaning charts.',
    }
    work4 = {
        'companyName': 'Excel Industries',
        'dates': 'May 2013 to July 2018',
        'task1': 'Fabrication experience- Roller, Folding Table, Triumph Laser, ATC Amada Brake Press, and Amada Brake Press. Creation of Standards, Safety, and Preventive Maintenance in Fabrication.',
        'task2': 'Weld Experience- Tack Jig Welder, Robot Welder, and grinder. Checking quality of welds to prints. Creation of standards, safety, and preventive maintenance in weld cells.',
        'task3': 'Assembly- Follow prints to build specific units. Read and follow standards. Adhere to all safety rules and regulations.',
        'task4': 'Lead- Delegating task to floor employees. Communication with all departments to create units per schedule. Safety and Quality Audits in cells per value stream.',
    }

    T_labels = ['HTML', 'CSS', 'JavaScript', 'JQuery', 'Python', 'Django', 'SQLite', 'Plotly', 'Pandas']
    T_values = [2, 2, 1.5, 1, 2, 1.25, 1.5, 1.75, 1.25]

    T_plot = go.Figure([go.Bar(x=T_labels, y=T_values)])
    T_plot.update_layout(title='Tech Skills',
                         paper_bgcolor='rgba(0,0,0,0)',
                         plot_bgcolor='rgba(0,0,0,0)',
                         yaxis=dict(
                             title='Years',
                             titlefont_size=16,
                             tickfont_size=14,
                         ),
                         xaxis=dict(
                             title='Skills',
                             titlefont_size=16,
                             tickfont_size=14,
                         ))
    T_skills = T_plot.to_html()

    M_labels = ['Lean', 'SixSigma', '5S', 'Document Control', 'One Piece Flow', 'Fabrication', 'Prints']
    M_values = [9, 4, 8, 3, 8.5, 10, 5.5]

    M_plot = go.Figure([go.Bar(x=M_labels, y=M_values)])
    M_plot.update_layout(title='Manufacturing Skills',
                         paper_bgcolor='rgba(0,0,0,0)',
                         plot_bgcolor='rgba(0,0,0,0)',
                         yaxis=dict(
                             title='Years',
                             titlefont_size=16,
                             tickfont_size=14,
                         ),
                         xaxis=dict(
                             title='Skills',
                             titlefont_size=16,
                             tickfont_size=14,
                         ))
    M_skills = M_plot.to_html()

    S_labels = ['Leadership', 'Team Player', 'Problem Solving', 'Critical Thinking', 'Communication', 'Self-Motivated']
    S_values = [2, 3, 5, 6, 7, 10, 9]

    S_plot = go.Figure([go.Pie(labels=S_labels, values=S_values)])
    S_plot.update_layout(title='Soft Skills',
                         paper_bgcolor='rgba(0,0,0,0)',
                         plot_bgcolor='rgba(0,0,0,0)',
                         yaxis=dict(
                             title='Years',
                             titlefont_size=16,
                             tickfont_size=14,
                         ),
                         xaxis=dict(
                             title='Skills',
                             titlefont_size=16,
                             tickfont_size=14,
                         ))
    S_skills = S_plot.to_html()
    interest = {
        '1': ''
    }

    return render(request, 'about-me.html', {
        'info': info,
        "theWhy": theWhy,
        'work1': work1,
        'work2': work2,
        'work3': work3,
        'work4': work4,
        'T_skills': T_skills,
        'M_skills': M_skills,
        'S_skills': S_skills
    })
