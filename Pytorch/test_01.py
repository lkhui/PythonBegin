from __future__ import print_function
import torch
import MyData


# d = MyData(123123)
# print(d.data)

x = torch.zeros(2,3, dtype=torch.long)
y = torch.rand(3,3, dtype=torch.float)
z = torch.tensor([[1,2,3],
                  [1,2,3],
                  [1,2,3]])
print(z)