---
title: "Learning Adversarial Search algorithms"
subtitle: "The Art of Unlosable Tic-Tac-Toe"
author: Eric Han
date: June 7, 2024
---

# Introduction

## Experience

<!-- Introduction: Start with a brief introduction of yourself, including your current position and academic background.
Key Achievements: Highlight significant accomplishments, such as degrees earned, research projects, publications, awards, and any notable contributions to your field.
Relevant Experience: Mention any previous teaching positions, industry experience, or relevant work that showcases your expertise. -->

My _Singaporean_ educational journey to CS, R&D:

* [2008] **Secondary School** --- Informal learning; scripting, games
    * Interest in Computing: why & how computers work
* [2010] **Pioneer JC** --- H2 Computing
    * Interest in research: A*STAR IHPC Quest 2009 (Bronze) - K-Means
* [2018] **B.Com. NUS** --- Com. Sci w Honors
    * A*STAR Scholarship - Internships working on R&D projects
* [2024] **PhD. NUS** --- AI/ML tackling scaling and robustness
    * First-author publications in AAAI, ICML.

Working experiences:

* [2018-2024] **Teaching Assistant/Graduate Tutor, NUS** --- Teach UG
* [B.Com.] **Research Intern, A\*STAR IHPC** --- ML Platform, Rec. Sys.

## Expertise

Support, teach (> 500 contact hours), grade, manage/mentor tutors for:

* AI/Machine Learning
    * **CS2109s** Introduction to AI and Machine Learning
    * **CS3243** Introduction to Artificial Intelligence
* Software Engineering
    * **CS3217** Software Engineering on Modern Application Platforms
    * **CS3203** Software Engineering Project
    * **CS2030/CS2030S** Programming Methodology II

Skilled with Linux (also administration), Windows, macOS:

* **Programming Languages** --- Python, C++, Java, Mojo...
* **Databases** --- Firebase, SQL...
* **Typesetting / Presentation Tools** --- LaTex, Markdown (This slides!)...
* **Tools/Platforms** --- Git, Mlflow, Plotly, Slurm, GCP...

## Teaching Philosophy

Effective learning is driven by an *innate desire* to learn the subject rather than *need*:

1. **Creating a relaxed and safe environment** --- Informal, casual, personal.
1. **Engaging students to facilitate learning in and after class** --- Telegram, buddy
1. **Creating equal opportunities for all students to learn** --- Reaching out

### Teaching Excellence (Tutorials/Recitation)

```{=latex}
\begin{table}[!h]
  \centering
  \begin{tabular}{>{\bfseries}r|cccccccccccccc}
    \toprule
     & \thead{2109} & \thead{2109} & \thead{3243} & \thead{3243} & \thead{3217} & \thead{3203} & \thead{3203} & \thead{3203} & \thead{3203} & \thead{3203}\\
    \midrule
     Score & 4.8 & 4.6 & 4.8 & 4.5 & 3.8 & 4.6 & 4.4 & 4.8 & 4.1 & 3.3 \\
     Resp. & 36 & 13 & 25 & 39 & 6 & 13 & 16 & 18 & 20 & 3 \\
     Nom. & 47\% & 30\% & 32\% & 31\% & 0\% & 61\% & 31\% & 61\% & 10\% & 33\% \\
    \bottomrule
  \end{tabular}
\end{table}
```

## Plans

For the teaching position, I am interested to

- Focus on improving teaching quality
- Curriculum development/improvement
- Casual research
    - Mentor for Undergraduate Research / FYP
- Involved in consultancy/policy

# Mini-Lecture

## Recap on environment properties

* **Fully / Partially Observable**: Can the agent see?
* **Single / Multi-Agent**: How many agents?
* **Deterministic / Stochastic**: Is there randomness in transition?
* **Episodic / Sequential**: Is there dependence on previous action?
* **Static / Dynamic**: Can the environment change while the agent is thinking?
* **Discrete / Continuous**: Discretized or varying continuously?

## Recap on formulation

**Un/Informed Search (Path)**:

* State space
* Initial state
* Final state
* Action
* Transition

**Local Search (Goal)**:

* Inital state
* Transition
* Heuristic/Stopping criteria

## Adversarial Search

**Motivation**: How can we win?

Ingredients needed to formulate a problem:

* **Inital state**: Starting configuration (representation)
* **Players**: Decision-makers within the game (2 players)
* **Actions**: Potential moves that the player can make
* **Transition**: Result of a move from a state
* **Terminal/Leaf test**: Checks if the game is over
* **Utility**: Reward for a terminal state and player

## Tic-tac-toe

2P childhood game where $(P_{O},P_{X})$ players take turns drawing their symbols on a 3x3 grid.
The winner is the first player to get 3 of his/her symbol in a row, col. or diag.

 . . . 

$$
\begin{aligned}
\ttt{}{}{}{}{}{}{}{}{}&\xrightarrow{P_{X}}
\ttt{}{X}{}{}{}{}{}{}{}\xrightarrow{P_{O}}
\ttt{O}{X}{}{}{}{}{}{}{}\xrightarrow{P_{X}}
\ttt{O}{X}{}{}{X}{}{}{}{}\xrightarrow{P_{O}}
\ttt{O}{X}{}{}{X}{}{}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{}{X}{X}{}{}{O}{}\\
&\xrightarrow{P_{O}}\ttt{O}{X}{}{X}{X}{O}{}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{X}{X}{X}{O}{}{O}{}\xrightarrow{P_{O}}
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}\xrightarrow{P_{O}}\emptyset
\end{aligned}
$$

 . . . 

\begin{tcolorbox}[title=Recap --- Environment Properties]
  Fully Observable, 2 Agent, Deterministic, Squential, Static, Discrete
\end{tcolorbox}

## Modeling Tic-tac-toe [Discussion]
$$\ttt{}{}{}{}{}{}{}{}{}\xrightarrow{P_{X}}
\ttt{}{X}{}{}{}{}{}{}{}\xrightarrow{P_{O}}
\ttt{O}{X}{}{}{}{}{}{}{}\xrightarrow{P_{X}}
\cdots
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}$$

2P childhood game where $(P_{O},P_{X})$ players take turns drawing their symbols on a 3x3 grid.
The winner is the first player to get 3 of his/her symbol in a row, col. or diag.

* **Inital state**: 
* **Players**: 
* **Actions**: 
* **Transition**: 
* **Terminal/Leaf test**: 
* **Utility**: 

## Modeling Tic-tac-toe
$$S_0=\ttt{0}{1}{2}{3}{4}{5}{6}{7}{8}\xrightarrow{a_0=(1,X)}
\ttt{}{X}{}{}{}{}{}{}{}\xrightarrow{\cdots}
\cdots
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}\xrightarrow{a_8=(8,X)}
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X} = S_9$$

* **Inital state**: $S_0$, 1D array of $9$ elements: $O,X,\emptyset$
* **Players**: $P_X$-max, $P_O$-min
* **$i$-th Actions**: $a_i=(c_i,y): c_i\in[0,8]$ where $S_i[c_i]=\emptyset$, symbol $y\in{X,O}$
* **Transition**: $T(S_i, a_i)=S_{i+1}$, where $S_{i+1}[j]=\begin{cases}
  y & \text{if } j = c_i \\
  S_{i}[j]& \text{otherwise}
\end{cases}$
* **Terminal/Leaf test**: Row, col. or diag having same symbols or no moves
* **Utility**: $U(S_i, p)$ is $0$ if draw, $1$ if $p$ wins, $-1$ if $p$ loses

## Modeling Tic-tac-toe

* **Inital state**: $S_0$, 1D array of $9$ elements: $O,X,\emptyset$
* **Players**: $P_X$-max, $P_O$-min
* **$i$-th Actions**: $a_i=(c_i,y): c_i\in[0,8]$ where $S_i[c_i]=\emptyset$, symbol $y\in{X,O}$
* **Transition**: $T(S_i, a_i)=S_{i+1}$, where $S_{i+1}[j]=\begin{cases}
  y & \text{if } j = c_i \\
  S_{i}[j]& \text{otherwise}
\end{cases}$
* **Terminal/Leaf test**: \fbox{Row, col. or diag having same symbols or no moves}
* **Utility**: $U(S_i, p)$ is $0$ if draw, $1$ if $p$ wins, $-1$ if $p$ loses

\begin{tcolorbox}[title=FAQ: Can I describe and not write math?]
  Yes, but it must be \textbf{clear}; ie. Able to translate into code without additional assumptions; you should (at min) describe how the state is represented.
\end{tcolorbox}

## Modeling Tic-tac-toe in Python

* **Inital state**: $S_0$, 1D array of $9$ elements: $O,X,\emptyset$
* **$i$-th Actions**: $a_i=(c_i,y): c_i\in[0,8]$ where $S_i[c_i]=\emptyset$, symbol $y\in{X,O}$

~~~python
X,O,E = 'X','O','.'
SYMBOLS = {X,O}
WINNING_POS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
class TicTacToe(object):
  def __init__(self, Si=[ E ] * 9):
    self.Si = Si
    self.winner = E
  def actions(self):
    e_cis = [ ci for ci, Si_ci in enumerate(self.Si) if Si_ci == E ]
    return [ (ci, y) for y in SYMBOLS for ci in e_cis ]
~~~

Full code here: [http://eric-han.com]()

## Zero-sum game

Zero-sum game is a game where one player gain is equals to another's loss, where the total utility of the game is the same/constant (ie. no improvement). 

### Tic-tac-toe is zero-sum

* If $P_X$ wins $P_O$ loses: $\sum U = 1 - 1=0$
* If $P_O$ wins $P_X$ loses: $\sum U = 1 - 1=0$
* If $P_O,P_X$ draws: $\sum U = 0 + 0=0$

So, for Tic-tac-toe: $U(S_i, X) = -U(S_i, O)$

**Intuition**: For nerds like me, if you played enough, you notice you keep getting draws.

\begin{tcolorbox}[title=Question]
  Can we come up with an algorithm to play Tic-tac-toe?
\end{tcolorbox}

## Tic-tac-toe gametree

![Gametree (R&N 3rd Ed) --- Inital, Players, Actions, Transition, Terminal, Utility](rn_gametree.png){width=70%}

## Minimax algorithm

**Intuition**: Simulate the game until the end with an imaginary optimal opponent.

$$
\begin{aligned}
\ttt{}{}{}{}{}{}{}{}{}&\xrightarrow{P_{X}}
\ttt{}{X}{}{}{}{}{}{}{}\xrightarrow{P_{O}}
\ttt{O}{X}{}{}{}{}{}{}{}\xrightarrow{P_{X}}
\ttt{O}{X}{}{}{X}{}{}{}{}\xrightarrow{P_{O}}
\ttt{O}{X}{}{}{X}{}{}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{}{X}{X}{}{}{O}{}\\
&\xrightarrow{P_{O}}\boxed{\ttt{O}{X}{}{X}{X}{O}{}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{X}{X}{X}{O}{}{O}{}\xrightarrow{P_{O}}
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}\xrightarrow{P_{X}}
\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}\xrightarrow{P_{O}}\emptyset}
\end{aligned}
$$

I am player $P_X$, trying to find the best move at $\ttt{O}{X}{}{X}{X}{O}{}{O}{}$

## Minimax algorithm

**Intuition**: Simulate the game until the end with an imaginary opponent.

\begin{figure}
\scalebox{0.6}{
\begin{forest}
[$\ttt{O}{X}{}{X}{X}{O}{}{O}{}$
[$\ttt{O}{X}{X}{X}{X}{O}{}{O}{}$,edge label={node[midway,left,font=\scriptsize]{(2,X)}}
[$\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}$,edge label={node[midway,left,font=\scriptsize]{(6,O)}}
[$\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
]
[$\ttt{O}{X}{X}{X}{X}{O}{}{O}{O}$,edge label={node[midway,left,font=\scriptsize]{(8,O)}}
[$\ttt{O}{X}{X}{X}{X}{O}{X}{O}{O}$,edge label={node[midway,left,font=\scriptsize]{(6,X)}}]
]
]
[$\ttt{O}{X}{}{X}{X}{O}{X}{O}{}$,edge label={node[midway,left,font=\scriptsize]{(6,X)}}
[$\ttt{O}{X}{O}{X}{X}{O}{X}{O}{}$,edge label={node[midway,left,font=\scriptsize]{(2,O)}}
[$\ttt{O}{X}{O}{X}{X}{O}{X}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
]
[$\ttt{O}{X}{}{X}{X}{O}{X}{O}{O}$,edge label={node[midway,left,font=\scriptsize]{(8,O)}}
[$\ttt{O}{X}{X}{X}{X}{O}{X}{O}{O}$,edge label={node[midway,left,font=\scriptsize]{(2,X)}}]
]
]
[$\ttt{O}{X}{}{X}{X}{O}{}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(8,X)}}
[$\ttt{O}{X}{O}{X}{X}{O}{}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(2,O)}}
[$\ttt{O}{X}{O}{X}{X}{O}{X}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(6,X)}}]
]
[$\ttt{O}{X}{}{X}{X}{O}{O}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(6,O)}}
[$\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(2,X)}}]
]
]
]
\end{forest}
}
\end{figure}

We can fill in the utility values for the leaf nodes!

## Minimax algorithm

**Utility for X**: $U(S_i, X)$ is $0$ if draw, $1$ if $X$ wins, $-1$ if $X$ loses

\begin{figure}
\scalebox{0.6}{
\begin{forest}
[{$\ttt{O}{X}{}{X}{X}{O}{}{O}{}$},edge label={node[midway,left,font=\scriptsize]{()}}
[{$\ttt{O}{X}{X}{X}{X}{O}{}{O}{}$},edge label={node[midway,left,font=\scriptsize]{(2,X)}}
[{$\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}$},edge label={node[midway,left,font=\scriptsize]{(6,O)}}
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
]
[{$\ttt{O}{X}{X}{X}{X}{O}{}{O}{O}$},edge label={node[midway,left,font=\scriptsize]{(8,O)}}
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{X}{O}{O}\right)=1$},edge label={node[midway,left,font=\scriptsize]{(6,X)}}]
]
]
[{$\ttt{O}{X}{}{X}{X}{O}{X}{O}{}$},edge label={node[midway,left,font=\scriptsize]{(6,X)}}
[{$\ttt{O}{X}{O}{X}{X}{O}{X}{O}{}$},edge label={node[midway,left,font=\scriptsize]{(2,O)}}
[{$U\left(\ttt{O}{X}{O}{X}{X}{O}{X}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
]
[{$\ttt{O}{X}{}{X}{X}{O}{X}{O}{O}$},edge label={node[midway,left,font=\scriptsize]{(8,O)}}
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{X}{O}{O}\right)=1$},edge label={node[midway,left,font=\scriptsize]{(2,X)}}]
]
]
[{$\ttt{O}{X}{}{X}{X}{O}{}{O}{X}$},edge label={node[midway,left,font=\scriptsize]{(8,X)}}
[{$\ttt{O}{X}{O}{X}{X}{O}{}{O}{X}$},edge label={node[midway,left,font=\scriptsize]{(2,O)}}
[{$U\left(\ttt{O}{X}{O}{X}{X}{O}{X}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(6,X)}}]
]
[{$\ttt{O}{X}{}{X}{X}{O}{O}{O}{X}$},edge label={node[midway,left,font=\scriptsize]{(6,O)}}
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(2,X)}}]
]
]
]
\end{forest}
}
\end{figure}

We know we want the best action later, so we choose the best action (max) there!

## Minimax algorithm

For the best action chosen, we inherit its corresponding value!

\begin{figure}
\scalebox{0.6}{
\begin{forest}
[{$\ttt{O}{X}{}{X}{X}{O}{}{O}{}$},edge label={node[midway,left,font=\scriptsize]{()}}
[{$\ttt{O}{X}{X}{X}{X}{O}{}{O}{}$},edge label={node[midway,left,font=\scriptsize]{(2,X)}}
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{O}{O}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(6,O)}}]
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{}{O}{O}\right)=1$},edge label={node[midway,left,font=\scriptsize]{(8,O)}}]
]
[{$\ttt{O}{X}{}{X}{X}{O}{X}{O}{}$},edge label={node[midway,left,font=\scriptsize]{(6,X)}}
[{$U\left(\ttt{O}{X}{O}{X}{X}{O}{X}{O}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(2,O)}}]
[{$U\left(\ttt{O}{X}{}{X}{X}{O}{X}{O}{O}\right)=1$},edge label={node[midway,left,font=\scriptsize]{(8,O)}}]
]
[{$\ttt{O}{X}{}{X}{X}{O}{}{O}{X}$},edge label={node[midway,left,font=\scriptsize]{(8,X)}}
[{$U\left(\ttt{O}{X}{O}{X}{X}{O}{}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(2,O)}}]
[{$U\left(\ttt{O}{X}{}{X}{X}{O}{O}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(6,O)}}]
]
]
\end{forest}
}
\end{figure}

We dont know how the $P_O$ will play this move, so

* Assume that $P_O$ wants to win and plays optimally like me.
* We imagine that $P_O$ chooses the best action (min) there!

## Minimax algorithm

**Intuition**: Simulate the game until the end with an imaginary *optimal* opponent.

\begin{figure}
\scalebox{1}{
\begin{forest}
[{$\ttt{O}{X}{}{X}{X}{O}{}{O}{}$},edge label={node[midway,left,font=\scriptsize]{()}}
[{$U\left(\ttt{O}{X}{X}{X}{X}{O}{}{O}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(2,X)}}]
[{$U\left(\ttt{O}{X}{}{X}{X}{O}{X}{O}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(6,X)}}]
[{$U\left(\ttt{O}{X}{}{X}{X}{O}{}{O}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
]
\end{forest}
}
\end{figure}

Now I can just pick the move that is the best (max value):

* All 3 moves would, at worse-case, end up in draws.

## Minimax algorithm

**Intuition**: Simulate the game until the end with an imaginary *optimal* opponent.

__function__ MINIMAX-DECISION(_state_) __returns__ _an action_  
        __return__ arg max<sub> _a_ $\in$ ACTIONS(_s_)</sub> MIN\-VALUE(RESULT(_state_, _a_))

## Minimax Tic-tac-toe example

\begin{figure}
\scalebox{.4}{
\begin{forest}
[{$\ttt{}{}{}{}{}{}{}{}{}$},edge label={node[midway,left,font=\scriptsize]{()}}
[{$U\left(\ttt{X}{}{}{}{}{}{}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(0,X)}}]
[{$U\left(\ttt{}{X}{}{}{}{}{}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(1,X)}}]
[{$U\left(\ttt{}{}{X}{}{}{}{}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(2,X)}}]
[{$U\left(\ttt{}{}{}{X}{}{}{}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(3,X)}}]
[{$U\left(\ttt{}{}{}{}{X}{}{}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(4,X)}}]
[{$U\left(\ttt{}{}{}{}{}{X}{}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(5,X)}}]
[{$U\left(\ttt{}{}{}{}{}{}{X}{}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(6,X)}}]
[{$U\left(\ttt{}{}{}{}{}{}{}{X}{}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(7,X)}}]
[{$U\left(\ttt{}{}{}{}{}{}{}{}{X}\right)=0$},edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
]
\end{forest}
}
\end{figure}

## Minimax analysis

Issues - Huge/Infinite Game Trees

## Alpha-Beta Pruning algorithm

Intuition

## Alpha-Beta Tic-tac-toe example

## Alpha-Beta analysis

## 2048 

## Modeling 2048

## Minimax 2048 example

## Minimax limitations

## Expectimax algorithm

## Expectimax example