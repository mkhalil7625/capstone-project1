1. Write a more descriptive docstring at the start of the program. The docstring should describe the purpose and features of the program.
2. Create data structure(s) to store the questions and answers. Your data structure should make it easy to add a new topic+questions, and to add/remove questions for an existing topic. Your program should not require the same number of questions for any topic.  Data structure should be structured in a way that makes it easy for the program to access the data. 
3. Reduce repeated code. 
4. Use functions to group code into logical blocks
5. Enable user to enter answer in any case and program should decide it is correct. For example, if the answer is 'Chicago', then 'chicago', 'cHicAgo' and 'CHICAGO' are all correct.
6. Improve the user interface when the user selects the quiz topic. It's not clear what the user should enter here,
`topic = input('Would you like art, or space questions? ') `
If the user doesn't enter the exact string 'art' or the exact string 'space' then they must restart the program to try again.
Remember that the program should work if there are more available topics, and the user should be able to choose between all available topics.  
7. Ensure message that is printed if user gets all the answers correct is always printed even if questions are added or removed.  If another question was added, and the user answers all correctly, would the message on line 37 or line 70 be printed?
8. Comment code. You don't need to comment every line, but add comments to help explain the more complex parts of the program.