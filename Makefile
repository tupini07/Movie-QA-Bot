help: 
	@echo This is a utility to run multiple kinds of commands. 
	@echo
	@echo To run the bot use the following command:
	@echo -e "\t run-bot" -- run bot on the command line:"
	@echo -e "\t run-voice -- run bot over voice"
	@echo

	@echo -e  "Other availbale commands are: \n"

	@echo -e "Training: "
	@echo -e "\t train-nlu -- train nlu module"
	@echo -e "\t train-nlu-aggregated -- train nlu module on aggregation of train and test data"
	@echo -e "\t train-dialogue -- train dialogue part"
	@echo -e "\t train-online -- start bot in interactive training mode"
	@echo -e "\t train-online-with-nlu -- start bot in interactive training mode using the NLU interpreter"
	@echo

	@echo -e "Data Utilities: "
	@echo -e "\t convert-data - converts NLSPARQL data to rasa format"
	@echo -e "\t analyze-data - Print various information on the dataset"
	@echo

	@echo -e "Evaluation: "
	@echo -e "\t evaluate-nlu -- only evaluate nlu against test data"
	@echo -e "\t evaluate-nlu-crossval -- do a crossvalidation on aggregated dataset"
	@echo -e "\t evaluate-dialogue -- only evaluate dialogue against test data"
	@echo -e "\t train-and-evaluate -- train nlu and dialogue and evaluate both"
	@echo


run-bot:
	@echo --- Running bot on command line
	@python bot.py run

run-voice:
	@echo --- Running bot with voice
	@python bot.py run-voice


convert-data:
	@echo --- Converting NLSPARQL data to rasa format and saving in data/ folder
	@echo Converting train NLSPARQL.train.data
	@cd data/scripts; python convert_to_rasa.py ../NLSPARQL/NLSPARQL.train.data ../NLSPARQL/NLSPARQL.train.utt.labels.txt ../train_rasa.json
	@echo 
	@echo Converting test NLSPARQL.test.data
	@cd data/scripts; python convert_to_rasa.py ../NLSPARQL/NLSPARQL.test.data ../NLSPARQL/NLSPARQL.test.utt.labels.txt ../test_rasa.json
	@echo 
	@echo Agregating training and testing into aggregated.py
	@cd data/scripts; python agregate_jsons.py ../aggregated.json ../test_rasa.json ../train_rasa.json
	@echo 


analyze-data: convert-data
	@echo --- Analyzing data
	@cd data/scripts; python analyze_data.py


train-and-evaluate: train-nlu ; train-dialogue ; evaluate-nlu ; evaluate-dialogue
	

train-nlu: convert-data
	@echo --- Training NLU
	@python bot.py train-nlu

train-nlu-aggregated: convert-data
	@echo --- Training NLU module on the aggregated data training + testing
	@python bot.py train-nlu-agg

train-dialogue:
	@echo --- Training Dialogue
	@python bot.py train-dialogue

train-online:
	@echo --- Starting Bot in online training mode
	@python bot.py train-online

train-online-with-nlu:
	@echo --- Starting Bot in online training mode using the NLU interpreter
	@python bot.py train-online-wnlu


evaluate-nlu: train-nlu
	@echo --- Evaluating NLU
	@python -m rasa_nlu.evaluate -d data/test_rasa.json -m models/nlu/default/current/

evaluate-nlu-crossval: convert-data
	@echo --- Evaluating NLU with crossvalidation
	@echo Warning! This will take a very long time, so go grab a cup of coffee
	@python -m rasa_nlu.evaluate \
							--data data/aggregated.json \
							--config nlu_model_config.yml \
							--mode crossvalidation \
							--folds 5 \
							--verbose

evaluate-dialogue: train-dialogue
	@echo --- Evaluating Dialogue
	@python -m rasa_core.evaluate -s data/test_st.md -d models/dialogue/ -v


