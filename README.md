## Decryption:
The task is to create a function which can take a text input file,  
and return a decrypted message by processing the file according to  
the Decryption key as follows:  
The file will contain multiple lines in this format:  
```<integer><space><word><\n>```.  
The Decryption key is as follows:  
1. Sort each pair of ```<integer><space><word>``` based on the ascending order  
of the integers.
1. Make a pyramid structure of the integer values using the  
sorted pairs like this:  
1  
2 3  
4 5 6  
and so on.  
The corresponding words against the last integers in this pyramid  
represent the words which are supposed to be present in the encrypted  
message in order.  
1. Return the string containing these words in order without quotes  
or ```.``` or any leading/trailing spaces.  
Then the code runs a print statement on the function to print  
the message on the console when the project is run.  
For the sake of simplicity, the text file to be consumed as input  
has been put in the root directory of the project.  