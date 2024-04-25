import encryption_tool

tool = encryption_tool.EncryptionTool()
tool.set_key()
source = open(tool.path, 'r')
text = source.read()
if tool.output is not None:
    output = open(tool.output, 'a')
else:
    output = open(tool.path, 'w')
tool.work(text, output)
source.close()
output.close()
