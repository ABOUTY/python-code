# ucsbcs154lab9
# All Rights Reserved
# Copyright (c) 2023 Jonathan Balkind
# Distribution Prohibited
import pyrtl

# metadata managed by this module, don't modify names/ports or make async!


# Uncomment to run the Sample Test
# You may want to recomment before submitting as it could interfere with the autograder
if __name__ == "__main__":
    TestOneInstructionFullFlow()
    print("Pass TestOneInstructionFullFlow")

    TestRobNotReady()
    print("Pass ROB Not Ready After a Fill ")