from IPython.core.magic import register_cell_magic
from IPython.display import display, HTML

@register_cell_magic
def mermaid(line, cell):
    """Cell magic for rendering Mermaid diagrams in Jupyter notebooks.
    
    Usage:
        %%mermaid
        graph TD;
            A[Start] --> B{Is it working?};
            B -- Yes --> C[Great!];
            B -- No --> D[Fix it];
            D --> B;
    """
    graph = cell

    html = f"""
    <div class="mermaid">
    {graph}
    </div>

    <script>
      if (typeof mermaid === 'undefined') {{
        var script = document.createElement('script');
        script.src = "https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js";
        script.onload = () => mermaid.initialize({{ startOnLoad: true }});
        document.head.appendChild(script);
      }} else {{
        mermaid.init();
      }}
    </script>
    """

    display(HTML(html))

def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magic_function(mermaid, 'cell') 