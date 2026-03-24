from langchain.text_splitter import CharacterTextSplitter

text ='''
In a quiet corner of the city, where the noise fades into a gentle hum, there stood a small café that seemed 
untouched by time. People came not just for the coffee, but for the feeling it gave—a sense of calm, of belonging.
The walls were filled with stories, written not in words but in laughter, in shared glances, and in silent moments 
between strangers. Outside, life rushed by in a blur, but inside, every second felt slower, softer, almost meaningful.
It was a place where thoughts settled, dreams took shape, and even the most restless minds found a little peace.'''

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)