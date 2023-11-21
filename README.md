# PyGPT
A custom GPT to Python port that doesn't need an API key!

This project uses the g4f library for Python to create a GPT-3.5 wrapper that you can use for your Python AI projects!

<h1>How To Customize</h1>
<li>
  <ul>At the beginning, write the following lines of code: 
    <li>
      <ul><code>g4f.debug.logging = False</code>: This code turns off logging</ul>
      <ul><code>g4f.version_check = False</code>: This code turns off checking the version of g4f</ul>
    </li>
  </ul>
  <ul>Remove the for loop: <code>for _ in range(max_prompts):</code>. This code is just for testing</ul>
</li>
