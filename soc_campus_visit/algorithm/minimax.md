
---
title: "Learning Adversarial Search algorithms"
subtitle: "The Art of Unlosable Tic-Tac-Toe"
author: Eric Han
date: June 7, 2024
---
__function__ MINIMAX-DECISION(_state_) __returns__ _an action_  
&emsp;__return__ arg max<sub> _a_ &Element; ACTIONS(_s_)</sub> MIN\-VALUE(RESULT(_state_, _a_))  

__function__ MAX\-VALUE(_state_) __returns__ _a utility value_  
&emsp;__if__ TERMINAL\-TEST(_state_) __then return__ UTILITY(_state_)  
&emsp;_v_ &larr; &minus;&infin;  
&emsp;__for each__ _a_ __in__ ACTIONS(_state_) __do__  
&emsp;&emsp;&emsp;_v_ &larr; MAX(_v_, MIN\-VALUE(RESULT(_state_, _a_)))  
&emsp;__return__ _v_  

__function__ MIN\-VALUE(_state_) __returns__ _a utility value_  
&emsp;__if__ TERMINAL\-TEST(_state_) __then return__ UTILITY(_state_)  
&emsp;_v_ &larr; &infin;  
&emsp;__for each__ _a_ __in__ ACTIONS(_state_) __do__  
&emsp;&emsp;&emsp;_v_ &larr; MIN(_v_, MAX\-VALUE(RESULT(_state_, _a_)))  
&emsp;__return__ _v_  
