include exp/$(EXP).mk # include SA experiment

sa: dat/$(EXP)/si.txt
fig: fig/$(EXP)/grid.png fig/$(EXP)/si.png

dat/$(EXP)/si.txt: dat/$(EXP)/y.txt exp/$(EXP).mk
	python -m SALib.analyze.sobol \
		-p dat/$(EXP)/params.txt \
		-Y $< \
		-c $(Y) > $@

dat/$(EXP)/y.txt: dat/$(EXP)/x.txt $(F) exp/$(EXP).mk
	parallel --bar -k $(F) :::: $< > $@

dat/$(EXP)/x.txt: dat/$(EXP)/params.txt exp/$(EXP).mk
	python -m SALib.sample.saltelli \
		-s $(S) \
		-p dat/$(EXP)/params.txt \
		-n $(N) \
		-o $@

fig/$(EXP)/grid.png: src/plot-grid.py dat/$(EXP)/x.txt dat/$(EXP)/y.txt
	$< -d dat/$(EXP) -o $@

fig/$(EXP)/si.png: src/plot-si.py dat/$(EXP)/y.txt
	$< -d dat/$(EXP) -o $@
