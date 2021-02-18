string  = '<a href="http://tube.agaysex.com/ass/" target="_blank">ass</a>'

while "<" in string or ">" in string:    
    start = string.find("<")
    end = string.find(">")
    string = string.replace(string[start:end+1],"")

print(string)
