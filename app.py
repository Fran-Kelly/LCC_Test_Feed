import os
from crawler import fetch_new_reports
from summariser import summarise_report
from rss import generate_rss

def run():
    reports = fetch_new_reports()
    summaries = []
    for report in reports:
        summary = summarise_report(report['title'], report['url'], report['content'])
        summaries.append({
            'title': report['title'],
            'link': report['url'],
            'summary': summary,
            'date': report['date']
        })
    generate_rss(summaries)

def serve():
    import http.server, socketserver
    PORT = 8080
    os.chdir("public")
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run()
    else:
        serve()
