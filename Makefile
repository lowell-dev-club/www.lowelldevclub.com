init:
	pip3 install -r requirements.txt

clean:
	pystarter clean

run: clean
	gunicorn run:app --preload --timeout 10 --max-requests 300