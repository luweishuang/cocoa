PYTHONPATH=. python ../scripts/generate_dataset.py \
    --schema-path data/bookhatball-schema.json \
    --scenarios-path data/toy-scenarios.json \
    --train-examples-paths data/toy-transcripts.json \
    --train-max-examples 1 --test-max-examples 0 --max-turns 14 \
    --agents rulebased rulebased \
    --random-seed 8
    # --price-tracker price-tracker.pkl