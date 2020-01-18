init:
	pip3 install -r requirements.txt

clean:
	pystarter clean

update:
	pip install --upgrade wtforms wheel urllib3 six setuptools requests pytest py pluggy pip more-itertools mistune MarkupSafe idna gunicorn chardet certifi attrs atomicwrites pystarter

run: clean
	gunicorn run:app --preload --timeout 10 --max-requests 300