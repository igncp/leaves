get-500-csv:
  cmd.run:
    - name: 'curl -O http://www.briandunning.com/sample-data/us-500.zip; unzip us-500.zip; rm us-500.zip'
    - user: vagrant
    - cwd: /data/CSVs
    - creates: /data/CSVs/us-500.csv
    - require:
      - file: /data/CSVs

get-bitcoin-values:
  cmd.run:
    - name: 'wget https://www.quandl.com/api/v1/datasets/BCHAIN/TOTBC.csv; mv TOTBC.csv bitcoin-values.csv'
    - user: vagrant
    - cwd: /data/CSVs
    - creates: /data/CSVs/bitcoin-values.csv
    - require:
      - file: /data/CSVs