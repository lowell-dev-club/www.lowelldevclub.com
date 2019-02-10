from lowelldevclub import app

# run app
app.run(
    host='0.0.0.0', # host to view from outside the network
    port=5000, # assign to port 5000
    debug=True # Have debug pages show when there is an error
)
