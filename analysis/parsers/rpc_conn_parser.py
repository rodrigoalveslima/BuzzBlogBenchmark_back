# Copyright (C) 2022 Georgia Tech Center for Experimental Research in Computer Systems

import argparse
import re

import pandas as pd

# Constants
COLUMNS = ["timestamp", "lservice", "rservice", "backlog", "latency"]
RPC_CONN_LOG_PATTERN = r"^\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]+)\] pid=([^\s]+) tid=([^\s]+) ls=([^\s]+) rs=([^\s]+) bl=([^\s]+) lat=([^\s]+)$"


class RPCConnParser:

  @classmethod
  def df(cls, logfile):
    data = [cls.extract_values_from_log(log) for log in logfile]
    return pd.DataFrame(data=[d for d in data if d], columns=COLUMNS)

  @staticmethod
  def extract_values_from_log(log):
    match = re.match(RPC_CONN_LOG_PATTERN, log)
    if not match:
      return None
    timestamp, _, _, lservice, rservice, backlog, latency = match.groups()
    return (timestamp, lservice, rservice, backlog, latency)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Generate CSV file")
  parser.add_argument("--log_filepath", required=True, action="store", type=str, help="Path to log file (input)")
  parser.add_argument("--csv_filepath", required=True, action="store", type=str, help="Path to CSV file (output)")
  args = parser.parse_args()
  with open(args.log_filepath) as logfile:
    RPCConnParser.df(logfile).to_csv(args.csv_filepath, index=False)
