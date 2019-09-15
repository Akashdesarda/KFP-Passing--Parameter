from kfp import dsl

class SendMsg(dsl.ContainerOp):
    
    def __init__(self, name, send_msg):
        super(SendMsg, self).__init__(
            name = name, 
            image = 'gcr.io/athenas-owl-dev/vi-container-hub/test-experiments/comp1@sha256:4e4584ffa4a2f50bab5dd5a0170a5118a79671f9eae03c18398ed06fdddf468a',
            command=['python', 'msg.py'], 
            arguments=[
                '--msg', send_msg,
            ],
            file_outputs = {'output':'output.txt'}
        )
        
class GetMsg(dsl.ContainerOp):
    
    def __init__(self, name, get_msg):
        super(GetMsg, self).__init__(
            name = name,
            image = 'gcr.io/athenas-owl-dev/vi-container-hub/test-experiments/comp2@sha256:b6faf16e3d7fd741531ecb8ae963dc060d032af6e860dc90aa553a1e903bf948',
            command=['python', 'msg.py'],
            arguments=[
                '--msg', get_msg
            ]
        )
        
@dsl.pipeline(
    name='Passing Parameter',
    description='Passing parameter between two container'
)
def passing_parameter(
    send_msg = dsl.PipelineParam('send msg', value='akash')
):
    send_msg_op = SendMsg('Send Msg', send_msg)
    get_msg_op = GetMsg('Receive msg', send_msg_op.output)
    
if __name__== '__main__':
    import kfp.compiler as compiler
    compiler.Compiler().compile(passing_parameter, __file__ + '.tar.gz')