"""
Copyright 2020 Google LLC
Copyright 2020 PerfectVIPs Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

"""

from pygen_src.riscv_instr_pkg import imm_t
from pygen_src.isa.riscv_instr import riscv_instr
from pygen_src.isa.riscv_compressed_instr import riscv_compressed_instr
import logging

def DEFINE_INSTR(instr_n, instr_format, instr_category, instr_group, imm_tp=imm_t.IMM, g=globals()):
    class_name = "riscv_{}_instr".format(instr_n.name)

    def __init__(self):
        riscv_instr.__init__(self)
        self.instr_name = instr_n
        self.format = instr_format
        self.category = instr_category
        self.group = instr_group
        self.imm_type = imm_tp

        self.set_imm_len()
        self.set_rand_mode()
    NewClass = type(class_name, (riscv_instr,), {
        "__init__": __init__,
        "valid": riscv_instr.register(instr_n)
    })
    g[class_name] = NewClass


def DEFINE_C_INSTR(instr_n, instr_format, instr_category, instr_group, imm_tp=imm_t.IMM, g=globals()):
    class_name = "riscv_{}_instr".format(instr_n.name)
    logging.info("class name {}".format(class_name))
    def __init__(self):
        riscv_compressed_instr.__init__(self)
        riscv_compressed_instr.instr_name = instr_n
        riscv_compressed_instr.format = instr_format
        riscv_compressed_instr.category = instr_category
        riscv_compressed_instr.group = instr_group
        riscv_compressed_instr.imm_type = imm_tp
        riscv_compressed_instr.set_imm_len()
        riscv_compressed_instr.set_rand_mode()
    NewClass = type(class_name, (riscv_compressed_instr,), {
        "__init__": __init__,
        "valid": riscv_compressed_instr.register(instr_n)
    })
    g[class_name] = NewClass

'''
TODO
@vsc.constraint
def add_pseudo_instr(self, instr_n, instr_format, instr_category, instr_group):
        with vsc.if_then(self.pseudo_instr_name == instr_n):
            self.format == instr_format.name
            self.category == instr_category.name
            self.group == instr_group.name
'''
