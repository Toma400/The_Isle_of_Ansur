#this file will be used each time game loads the save
#it will have two purposes: checking for NUID abscence and comparing save version
#if save version is different, instructions for it will be here 
#for example, if version 1.0->1.1 added one variable
#instructions here will guide Python code how to make 1.0 save add missing elements
#if change is drastic (1.0->4.0), code will need to adapt for each change
#therefore it can go slowly: 1.0->1.1->1.5->2.0->3.0->3.5->4.0
#this will be easier than doing any possible "if" variant for any possible combination of update (1.0->4.0, 1.1->4.0, etc)
#instead, it will be just 1.0->1.1, 1.1->1.5, 1.5->2.0
#the only importance is to make it loop itself, is version from save is not current in-game
#so it will not stop after first iteration, but will iterate updates until save_system = game_system