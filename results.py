# Starts node with the correct working directory
import os

print "IMPORTANT! Use Ctrl-C to flush data back to disk upon exit."
os.system("nodejs viewer/server.js")
print "\nGoodbye!"