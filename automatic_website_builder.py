import os
import webbrowser


print('write your browser:')
mystring=input(">>")
mypic = input("photo url>>")
picnumber=int(input("picture number>>"))

#embedlink=input("youtube video embed link>>")

with open('myfile.html','w') as f:
    f.write('<html>\n')
    f.write("""<head>
            
                    
                
            </head>""")
    
    f.write('<body bgcolor="yellow">\n')
    f.write('<p>\n\n\t')
    f.write("""<style>
                    h1 {
                        text-align: center;
                    }
                </style>
            \n\n""")
    
    f.write('<h1>')

with open('myfile.html', 'a') as f:
    f.write(mystring)
    
    

with open('myfile.html','a') as f:
    f.write('\n</h1>')
    f.write('\n<hr>')
    
    f.write('\n<h1><marquee behavior="scroll" direction="left" scrollamount="3">')
    f.write(mystring)
    f.write("\n</marquee>")
            
    f.write("""\n<marquee behavior="scroll" direction="left" scrollamount="10">""")
    f.write(mystring)
    f.write("\n</marquee>")
    
    f.write('\n<marquee behavior="scroll" direction="left" scrollamount="17">')
    f.write(mystring)
    f.write("\n</marquee></h1>\n\n")
    
    
    for i in range(picnumber):
        f.write(f'<h2>photo no {i+1}</h2>')
           
        
        f.write("""
                    <div style="text-align: center;">
                            <img src="
    
                """)
        f.write(mypic)
        
        f.write("""
                 " alt="Sky" style="width: 350px;">
                """)
    
   
    
    f.write('\n</p>')
    f.write('\n</body>')
    f.write('\n</html>')

filename = 'file:///'+os.getcwd()+'/' + 'myfile.html'

##for opening into webbrowser
webbrowser.open_new_tab(filename)
