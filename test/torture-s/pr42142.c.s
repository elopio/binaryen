	.text
	.file	"pr42142.c"
	.section	.text.sort,"ax",@progbits
	.hidden	sort                    # -- Begin function sort
	.globl	sort
	.type	sort,@function
sort:                                   # @sort
	.param  	i32
	.result 	i32
# %bb.0:                                # %entry
	i32.const	$push2=, 2
	i32.const	$push0=, 1
	i32.const	$push8=, 1
	i32.lt_s	$push1=, $0, $pop8
	i32.select	$push3=, $pop2, $pop0, $pop1
	i32.const	$push6=, 0
	i32.const	$push4=, 10
	i32.lt_s	$push5=, $0, $pop4
	i32.select	$push7=, $pop3, $pop6, $pop5
                                        # fallthrough-return: $pop7
	.endfunc
.Lfunc_end0:
	.size	sort, .Lfunc_end0-sort
                                        # -- End function
	.section	.text.main,"ax",@progbits
	.hidden	main                    # -- Begin function main
	.globl	main
	.type	main,@function
main:                                   # @main
	.result 	i32
# %bb.0:                                # %entry
	block   	
	i32.const	$push0=, 5
	i32.call	$push1=, sort@FUNCTION, $pop0
	i32.const	$push2=, 1
	i32.ne  	$push3=, $pop1, $pop2
	br_if   	0, $pop3        # 0: down to label0
# %bb.1:                                # %if.end
	i32.const	$push4=, 0
	return  	$pop4
.LBB1_2:                                # %if.then
	end_block                       # label0:
	call    	abort@FUNCTION
	unreachable
	.endfunc
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
                                        # -- End function

	.ident	"clang version 7.0.0 (https://llvm.googlesource.com/clang.git 1f874ca3c3f27c2149b6b33ca4a5966b3577280d) (https://llvm.googlesource.com/llvm.git 2e4bd2aa729dd2c33cdca2b39c971c675e914001)"
	.functype	abort, void
