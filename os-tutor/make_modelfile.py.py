import glob, os

ggufs = glob.glob("*.gguf")
print("Found:", ggufs)
assert ggufs, "No .gguf file in this folder!"

content = '''FROM ./%s

TEMPLATE """{{- if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{- range .Messages }}<|im_start|>{{ .Role }}
{{ .Content }}<|im_end|>
{{ end }}<|im_start|>assistant
<think>

</think>

"""

SYSTEM "You are an OS and shell tutor. Explain step by step and be accurate."

PARAMETER temperature 0.7
PARAMETER top_p 0.8
PARAMETER top_k 20
PARAMETER stop "<|im_end|>"
''' % ggufs[0]

with open("Modelfile", "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print(open("Modelfile", encoding="utf-8").read()[:200])