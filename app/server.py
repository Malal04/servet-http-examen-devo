from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message = """
            <html>
            <head>
                <title>Accueil</title>
                <link rel="stylesheet" href="/styles.css">
            </head>
            <body>
                <h1>Bienvenue sur mon site Docker !</h1>
                <p>Ceci est une page d'accueil.</p>
                <a href="/about">À propos</a>
            </body>
            </html>
            """
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/about":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message = """
            <html>
            <head>
                <title>À propos</title>
                <link rel="stylesheet" href="/styles.css">
            </head>
            <body>
                <h1>À propos de ce site</h1>
                <p>Ce site est hébergé avec Docker.</p>
                <a href="/">Retour à l'accueil</a>
            </body>
            </html>
            """
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/styles.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            css = """
            body { font-family: Arial, sans-serif; text-align: center; }
            h1 { color: #007bff; }
            a { text-decoration: none; color: #007bff; font-size: 20px; }
            """
            self.wfile.write(css.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message = "<html><body><h1>404 - Page non trouvée</h1></body></html>"
            self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
