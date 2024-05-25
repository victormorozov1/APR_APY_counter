import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-pc', '--percent', type=float)
parser.add_argument('-is', '--invested-sum', type=float)
parser.add_argument('-in', '--income', type=float)
parser.add_argument('-p', '--period')
args = parser.parse_args()

income_ratio = (args.percent / 100) if args.percent else (args.income / args.invested_sum)

data = re.match(re.compile(r'(?P<n>\d+)(?P<period_type>\w+)'), args.period).groupdict()
num = int(data['n'])
period_type = data['period_type'].lower()
num = num * {'d': 1, 'm': 30, 'y': 365}[period_type]

apr = 365 / num * income_ratio
apy = (income_ratio + 1) ** (365 / num) - 1

print(f'APR: {apr * 100}%\nAPY: {apy * 100}%')
if args.invested_sum:
    print(f'With APY={apy * 100}% you will receive {args.invested_sum * (apy + 1)} in a year')
