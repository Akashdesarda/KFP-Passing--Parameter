#%%
import kfp
from kfp import dsl

def SendMsg(
    send_msg: str = 'akash'
):
    return dsl.ContainerOp(
        name = 'Print msg', 
        image = 'docker.io/akashdesarda/comp1:latest', 
        command = ['python', 'msg.py'],
        arguments=[
            '--msg', send_msg
        ],
        file_outputs={
            'output': '/output.txt',
        }
    )
    
def GetMsg(
    get_msg: str
):
    return dsl.ContainerOp(
        name = 'Read msg from 1st component',
        image = 'docker.io/akashdesarda/comp2:latest',
        command = ['python', 'msg.py'],
        arguments=[
            '--msg', get_msg
        ]
    )
    
@dsl.pipeline(
    name = 'Pass parameter',
    description = 'Passing para')
def  passing_parameter(send_msg):
    comp1 = SendMsg(send_msg)
    comp2 = GetMsg(comp1.output)


if __name__ == '__main__':
  import kfp.compiler as compiler
  compiler.Compiler().compile(passing_parameter, __file__ + '.tar.gz')