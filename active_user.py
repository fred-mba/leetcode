#!/usr/bin/python3

users = {'Hans': 'active', 'Elenore': 'inactive', 'Sasha': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(f'{active_users}')
