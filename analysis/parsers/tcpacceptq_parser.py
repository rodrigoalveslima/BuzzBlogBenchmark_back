# Copyright (C) 2022 Georgia Tech Center for Experimental Research in Computer Systems

import argparse
import re

import pandas as pd

# Constants
COLUMNS = ["timestamp", "acceptq_len_avg", "acceptq_len_max", "acceptq_lat_avg", "acceptq_lat_max"]
TCPACCEPTQ_LOG_PATTERN = r"^([0-9\.\-\:]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$"


class TcpacceptqParser:

  @classmethod
  def df(cls, logfile):
    data = [cls.extract_values_from_log(log) for log in logfile]
    return pd.DataFrame(data=[d for d in data if d], columns=COLUMNS)

  @staticmethod
  def extract_values_from_log(log):
    match = re.match(TCPACCEPTQ_LOG_PATTERN, log.strip())
    if not match:
      return None
    timestamp, acceptq_len_avg, acceptq_len_max, acceptq_lat_avg, acceptq_lat_max = match.groups()
    return (timestamp, acceptq_len_avg, acceptq_len_max, acceptq_lat_avg, acceptq_lat_max)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Generate CSV file")
  parser.add_argument("--log_filepath", required=True, action="store", type=str, help="Path to log file (input)")
  parser.add_argument("--csv_filepath", required=True, action="store", type=str, help="Path to CSV file (output)")
  args = parser.parse_args()
  with open(args.log_filepath) as logfile:
    TcpacceptqParser.df(logfile).to_csv(args.csv_filepath, index=False)
