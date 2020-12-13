input = """48
171
156
51
26
6
80
62
65
82
130
97
49
31
142
83
75
20
154
119
56
114
92
33
140
74
118
1
96
44
128
134
121
64
158
27
17
101
59
12
89
88
145
167
11
3
39
43
105
16
170
63
111
2
108
21
146
77
45
52
32
127
147
76
58
37
86
129
57
133
120
163
138
161
139
71
9
141
168
164
124
157
95
25
38
69
87
155
135
15
102
70
34
42
24
50
68
169
10
55
117
30
81
151
100
162
148"""

adapters = sorted([int(x) for x in input.split("\n")])

def part1():
    output = 0
    count1 = 0
    count3 = 1

    for adapter in adapters:
        assert adapter - output <= 3
        if adapter - output == 1:
            count1 += 1
        if adapter - output == 3:
            count3 += 1
        output += adapter - output
    print(count1 * count3)

adapters = sorted([int(x) for x in input.split("\n")])
adapters.insert(0, 0)
adapters.append(adapters[-1]+3)
accumulator = []

for i in range(0, len(adapters)):
    connections = 0
    adapter = adapters[i]
    if len(adapters) > i+3:
        if adapters[i+3] - adapter <= 3:
            connections += 1
    if len(adapters) > i+2:
        if adapters[i+2] - adapter <= 3:
            connections += 1
    if len(adapters) > i+1:
        if adapters[i+1] - adapter <= 3:
            connections += 1
    if connections > 0:
        accumulator.append(connections)

reversed = accumulator[::-1]
branches = 1
branch_acc = []
for i in range(0, len(accumulator)):
    current = reversed[i]
    if current == 1:
        branch_acc.append(branches)
    elif current == 2:
        branches = branch_acc[i-1] + branch_acc[i-2]
        branch_acc.append(branches)
    elif current == 3:
        branches = branch_acc[i-1] + branch_acc[i-2] + branch_acc[i-3]
        branch_acc.append(branches)
print(branches)
