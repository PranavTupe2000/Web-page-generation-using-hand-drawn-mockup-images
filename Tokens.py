form = """<form> 
    {{ main }} 
</form>"""

text = """{{ text }}
{{ main }}"""

HR = """<hr>
{{ main }}"""

textbox = """<div class="mb-3">
  <label class="form-label">{{ text }}</label>
  <input type="text" class="form-control" >
</div>
{{ main }}"""

select = """<select class="form-select mb-3" aria-label="Default select example">
  <option >{{ text }}</option>
</select>
{{ main }}"""

button = """<button type="submit" class="btn btn-{{ theme }}"> {{ text }} </button>
{{ main }}"""

image = """<img src="{{ text }}">
{{ main }}"""

video = """<video controls>  
  <source src="{{ text }}" type="video/mp4">    
</video>
{{ main }}"""

paragraph = """<p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero accusamus qui aspernatur? Ea, nam praesentium! Voluptates, impedit possimus sint iste sed tenetur. Velit delectus obcaecati quisquam nobis, minus quibusdam eligendi. </p>
{{ main }}"""

checkbox = """<div class="form-check">
  <input class="form-check-input" type="checkbox" value="">
  <label class="form-check-label" >
    {{ text }}
  </label>
</div>
{{ main }}"""

radio = """<div class="form-check">
  <input class="form-check-input" type="radio" >
  <label class="form-check-label" >
    {{ text }}
  </label>
</div>
{{ main }}"""

header = """<nav class="navbar navbar-dark bg-{{ theme }}">
  <div class="container-fluid">
    <span class="navbar-brand mb-0 h1">{{ text }}</span>
  </div>
</nav>
<br>
{{ main }}"""

container="""<div class="container">
        {{ main }}
  </div>"""

row ="""<div class="row">
    {{ main }}
  </div>
  {{ next }}"""

col ="""<div class="col">
    {{ main }}
  </div>
  {{ next }}"""

tokens = {
    "form": form,
    "Text": text,
    "HR": HR,
    "Textbox": textbox,
    "Select": select,
    "Button": button,
    "Image": image,
    "Video": video,
    "Paragraph": paragraph,
    "Checkbox": checkbox,
    "Radio": radio,
    "header": header,
    "container": container,
    "row": row,
    "col": col
}

