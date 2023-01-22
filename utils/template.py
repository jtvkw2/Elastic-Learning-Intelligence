import urllib.parse

def load_css() -> str:
    """ Return all css styles. """
    common_tag_css = """
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: .15rem .40rem;
                position: relative;
                text-decoration: none;
                font-size: 95%;
                border-radius: 5px;
                margin-right: .5rem;
                margin-top: .4rem;
                margin-bottom: .5rem;
    """
    return f"""
        <style>
            #tags {{
                {common_tag_css}
                color: rgb(88, 88, 88);
                border-width: 0px;
                background-color: rgb(240, 242, 246);
            }}
            #tags:hover {{
                color: black;
                box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
            }}
            #active-tag {{
                {common_tag_css}
                color: rgb(246, 51, 102);
                border-width: 1px;
                border-style: solid;
                border-color: rgb(246, 51, 102);
            }}
            #active-tag:hover {{
                color: black;
                border-color: black;
                background-color: rgb(240, 242, 246);
                box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
            }}
        </style>
    """


def no_result_html() -> str:
    """ """
    return """
        <div style="color:grey;font-size:95%;margin-top:0.5em;">
            No results were found.
        </div><br>
    """


def number_of_results(total_hits: int, duration: float) -> str:
    """ HTML scripts to display number of results and time taken. """
    return f"""
        <div style="color:grey;font-size:95%;">
            {total_hits} results ({duration:.2f} seconds)
        </div><br>
    """


def pagination(total_pages: int, search: str, current_page: int,
               tags: str) -> str:
    """ Create and return html for pagination. """
    # search words and tags
    params = f'?search={urllib.parse.quote(search)}'
    if tags is not None:
        params += f'&tags={tags}'

    # avoid invalid page number (<=0)
    if (current_page - 5) > 0:
        start_from = current_page - 5
    else:
        start_from = 1

    hrefs = []
    if current_page != 1:
        hrefs.append(f'<a href="{params}&page={1}">&lt&ltFirst</a>')
        hrefs.append(f'<a href="{params}&page={current_page - 1}">&ltPrevious</a>')

    for i in range(start_from, min(total_pages + 1, start_from + 10)):
        if i == current_page:
            hrefs.append(f'{current_page}')
        else:
            hrefs.append(f'<a href="{params}&page={i}">{i}</a>')

    if current_page != total_pages:
        hrefs.append(f'<a href="{params}&page={current_page + 1}">Next&gt</a>')

    return '<div>' + '&emsp;'.join(hrefs) + '</div>'


def search_result(i: int, url: str, title: str, highlights: str,
                  author: str, length: str, **kwargs) -> str:
    """ HTML scripts to display search results. """
    return f"""
        <div style="font-size:120%;">
            {i + 1}.
            <a href="{url}">
                {title}
            </a>
        </div>
        <div style="font-size:95%;">
            <div style="color:grey;font-size:95%;">
                {url[:90] + '...' if len(url) > 100 else url}
            </div>
            <div style="float:left;font-style:italic;">
                {author} ·&nbsp;
            </div>
            <div style="color:grey;float:left;">
                {length} ...
            </div>
            {highlights}
        </div>
    """


def tag_boxes(search: str, tags: list, active_tag: str) -> str:
    """ HTML scripts to render tag boxes. """
    html = ''
    search = urllib.parse.quote(search)
    for tag in tags:
        if tag != active_tag:
            html += f"""
            <a id="tags" href="?search={search}&tags={tag}">
                {tag.replace('-', ' ')}
            </a>
            """
        else:
            html += f"""
            <a id="active-tag" href="?search={search}">
                {tag.replace('-', ' ')}
            </a>
            """

    html += '<br><br>'
    return html