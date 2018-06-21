N?=100               # number of re-samplings
Y?=0
E:=./dat/params.txt  # experiment file
F:=./cmd/ishigami.py # model

./dat/inds.txt: ./dat/outputs.txt
	python3 -m SALib.analyze.sobol \
		--parallel \
		-p $(E) \
		-Y $< \
		-c $(Y) > $@

./dat/outputs.txt: ./dat/inputs.txt $(F)
	$(F) :::: $< > $@

./dat/inputs.txt: $(E)
	python3 -m SALib.sample.saltelli \
		-p $(E) \
		-o $@ \
		-n $(N)
