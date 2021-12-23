% List of guessing vocab and letter

vocab(['Software','Security','Enginnering','Programmer','Algorithm','Data','Network','Logic']).
letter(['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z'])

hangman:-
    getVocab(answer),
    !,
    write('Welcome to hangman game'),
    nl,
    name(answer,answerList),
    makeBlanks(answerList,blankList),
    getGuess(answerList,blankList).

% Randomly return a vocab from the list
getVocab(answer):-
    vocab(L),
    length(L,X),
    R is random(X),
    N is R+1,
    getNth(L,N,Ans).

% This part is let AI guess the letter

askGuess(answerList,blankList):-
    name(blankName,blankList),
    write(blankName),
    nl,
    write('Is it:'),
    random_member(X,letter)
    nl,
    processGuess(answerList,blankList,guessName).

processGuess(answerList,blankList,guessName):-
    member(guessName,answerList),
    !,
    write('Correct!!'),
    nl,
    substitute(answerList,blankList,guessName,newBlanks),
    checkWin(answerList,newBlanks).

% Check to see the vocab is guessed. If so, write 'You win'

checkWin(answerList,newBlanks):-
    name(answer,answerList),
    name(blankName,blankList),
    blankName = answer,
    !,
    write('You win').

checkWin(answerList,blankList):-
    !,
    getGuess(answerList,blankList).

% getNth(L,N,Ans) should be true when Ans is the Nth element of the list L. N will always be at least 1.
getNth([H|T],1,H).

getNth([H|T],N,Ans):-
    N1 is N-1,
    getNth(T,N1,Ans1),
    Ans=Ans1.

% makeBlanks(ansCode,blankCode) should take an answer phrase, which is a list
% of character codes that represent the answer phrase, and return a list
% where all codes but the '_' turn into the code for '*'.  The underscores
% need to remain to show where the words start and end.
makeBlanks(ansCode,blankCode):-
    maplist(answer_blank,ansCode,blankCode).

answer_blank(Ans,Blank):-
    Ans == 0'_ -> Blank = Ans ; Blank = 0'* .

% substitute(AnsList, BlankList, GuessName, NewBlanks) Takes character code lists AnsList and BlankList, 
% and GuessName, which is the character code for the guessed letter.  The NewBlanks should again be a 
% character code list, which puts all the guesses into the display word and keeps the *'s and _'s otherwise.


% This part is let user answer the AI