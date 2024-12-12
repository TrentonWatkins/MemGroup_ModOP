import subprocess
import time

import priProc


def run_portCom():
    """Run the portCom.py script."""
    print("Running portCom.py...")
    subprocess.run(["python", "portCom.py"], check=True)



if __name__ == "__main__":
    try:
        # Run the scripts in the specified order
        memory_heap1 = []
        priProc.addMemBlock(memory_heap1, "emptyBlock")
        priProc.addMemBlock(memory_heap1, "emptyBlock")
        priProc.addMemBlock(memory_heap1, "emptyBlock")
        priProc.addMemBlock(memory_heap1, "emptyBlock")
        priProc.addMemBlock(memory_heap1, "emptyBlock")
        run_portCom()
    except Exception as e:
        print(f"An error occurred while running the scripts: {e}")




