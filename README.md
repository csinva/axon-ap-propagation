# axon simulations
- tapering axon simulation code based on Johnson, Holmes, Brown, and Jung 2015

# setup
## run the code
- clone the repo
- compile the mod files (differs based on OS - see NEURON documentation)
- run main.hoc

# todo

# reference
## goals
1. maximize velocity
2. minimize energy
3. minimize noise variability

## constraints
- amount of protein membrane can sustain

### hypotheses
- node only gets to minimum needed
	- see brill et al ~1997
- Resting potential might be getting messed up
- Look at changing gbar
- Look at changing potassium conductances

## notes
- currently fires with noise
	- fires at very low voltage
- Johnson, Holmes, Brown, and Jung 2015
	- Goal: maximize conduction velocity but minimize metabolic costs
	- Myelination does this by decreasing capacitance
	- Increasing axon diameter does this by increasing ion flow
	- They assume fixed number of sodium channels and change morphology
	- 3 different taperings along the PARA
- other papers
	- base on Mcintyre, Richardson, and Grill 2001
	- empirical fits to blight, 1985 rat recording and david, 1995 rat recording

	
## done
- fixed surface area and looked at different diameters