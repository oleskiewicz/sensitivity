N?=100
Y?=0
E:=./dat/params.txt

F:=./cmd/ishigami.py

./dat/inds.txt: ./dat/outputs.txt
	python3 -m SALib.analyze.sobol \
		--parallel \
		-p $(E) \
		-Y $< \
		-c $(Y) > $@

./dat/outputs.txt: ./dat/inputs.txt $(F)
	$(F) :::: ./dat/inputs.txt > $@

./dat/inputs.txt: $(E)
	python3 -m SALib.sample.saltelli \
		-p $(E) \
		-o $@ \
		-n $(N)
