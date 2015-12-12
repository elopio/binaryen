#!/usr/bin/env python

import os, sys, subprocess, difflib

print '[ processing and updating testcases... ]\n'

for asm in sorted(os.listdir('test')):
  if asm.endswith('.asm.js'):
    print '..', asm
    wasm = asm.replace('.asm.js', '.wast')
    actual, err = subprocess.Popen([os.path.join('bin', 'asm2wasm'), os.path.join('test', asm)], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    # verify output
    if not os.path.exists(os.path.join('test', wasm)):
      print actual
      raise Exception('output .wast file does not exist')
    open(os.path.join('test', wasm), 'w').write(actual)

for wasm in sorted(os.listdir('test')):
  if wasm.endswith('.wast'):
    print '..', wasm
    asm = wasm.replace('.wast', '.2asm.js')
    actual, err = subprocess.Popen([os.path.join('bin', 'wasm2asm'), os.path.join('test', wasm)], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    open(os.path.join('test', asm), 'w').write(actual)

for t in sorted(os.listdir('test')):
  if t.endswith('.wast') and not t.startswith('spec'):
    print '..', t
    t = os.path.join('test', t)
    actual, err = subprocess.Popen([os.path.join('bin', 'binaryen-shell'), t, '-print-before'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    actual = actual.replace('printing before:\n', '')

    open(t, 'w').write(actual)

for s in ['minimal.s', 'basics.s', 'call.s', 'cfg-stackify.s', 'comparisons_f32.s', 'comparisons_f64.s', 'comparisons_i32.s', 'comparisons_i64.s', 'conv.s']:
  print '..', s
  wasm = s.replace('.s', '.wast')
  full = os.path.join('test', 'dot_s', s)
  if not os.path.exists(full):
    full = os.path.join('test', 'experimental', 'prototype-wasmate', 'test', s)
  actual, err = subprocess.Popen([os.path.join('bin', 's2wasm'), full], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  assert err == '', 'bad err:' + err
  expected_file = os.path.join('test', 'dot_s', wasm)
  open(expected_file, 'w').write(actual)

print '\n[ success! ]'

