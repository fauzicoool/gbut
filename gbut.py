from rich.console import Console
from bs4 import BeautifulSoup

from typer import Typer

import os, time, requests

cli=Typer()
cons=Console()
tasks = [f"task {n}" for n in range(1, 11)]

def search(keywords:str):
    data_title=[]
    res=requests.get(f"https://otakudesu.cloud/?s={keywords}&post_type=anime")
    soup = BeautifulSoup(res.text, "html.parser")
    ul=soup.find("ul",class_="chivsrc")
    lists=ul.find_all("li")
    for li in lists:
        title1=li.find("h2")
        title2=title1.find("a").text
        data_title.append(title2)
    return data_title

@cli.command(name="s-nime", help="what are you doing bro!..")
def sanime():
    searchInput=cons.input("[bold red]Search Anime: ")
    if searchInput == "exit":
        cons.clear()
    else:
        cons.clear()
        with cons.status("[bold green]Searching anime...") as status:
            search_data = search(searchInput)
            for i in range(5):
                time.sleep(1)
            cons.print("[bold blue]Result: ")
            for i in range(len(search_data)):
                cons.print(f"[bold][{i+1}] {search_data[i]}")


@cli.command(name="about")
def about():
    cons.print("[bold red]Alert!")

if __name__ == '__main__':
    cli()