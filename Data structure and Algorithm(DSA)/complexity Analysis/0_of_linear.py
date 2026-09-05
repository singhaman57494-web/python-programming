#          --0(n)

def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
        
    return False

papers = ["Anita", "bharat", "karan", "diya", "esha" ]
search_name = "bharat"

result = find_paper(papers, search_name)

if result:
    print("paper found")
else:
    print("paper not found")