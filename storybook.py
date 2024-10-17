import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets['key'])

def story_gebn(prompt):
  system_prompt = """You are the world renowned author for young adults fiction short stories. Given a concept, generate a short story revelant to the themes of the concept with a twist ending."""

  response = client.chat.completions.create (
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": prompt}
    ],
    temperature=0.6,
    max_tokens=600
  )
  return response.choices[0].message.content

def art_gen(prompt):
      response = client.images.generate(
          model = "dall-e-2",
          prompt = prompt, 
          size = "1024x1024",
          n = 1
      )
      return response.data[0].url

def design_gen(prompt):
  system_prompt = """
  You will be given a short story. Generate a prompt for the cover art that is sultable for the story. The prompt is for dall-e-2
  """

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": prompt}
      ],

      temperature = 1.3,
      max_tokens = 2000
  )
  return response.choices[0].message.content

prompt = st.text_input("Enter a prompt")
if st.button("Generate"):
    story = story_gebn(prompt)
    design = design_gen(story)
    art = art_gen(design)
   
    st.caption(design)
    st.divider()
    st.caption(story)
    st.divider()
    st.image(art)