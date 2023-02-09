import os
import pandas as pd
import matplotlib.pyplot as plt

dir = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm'
table_dir = os.path.join(dir, 'table')

f = plt.figure()
f.set_figwidth(15)
f.set_figheight(10)
plt.xlabel('k', size=15, labelpad=15)
plt.ylabel('psnr', size=15, labelpad=15)

def draw_change(df, img_name): 
    # plt.plot( 'k', 'psnr', data=df, marker='.', markerfacecolor='blue')
    plt.plot( 'k', 'psnr', data=df, marker='.', label=img_name)
    # plt.legend(prop={'size': 20})
    # plt.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, prop={'size': 20})


for fname in os.listdir(table_dir): 
    img_name = fname.split('.')[0]
    df = pd.read_csv(os.path.join(table_dir, fname))
    draw_change(df, img_name)
    f.legend(prop={'size': 18})
    plt.savefig(os.path.join(dir, 'output.png'))