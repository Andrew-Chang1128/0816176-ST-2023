/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Constants.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/LLVMContext.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constants.h"

#include <vector>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace llvm;
using namespace std;
char LabPass::ID = 0;

bool LabPass::doInitialization(Module &M) {
  return true;
}


static Constant* getI8StrVal(Module &M, char const *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();

  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
    GlobalValue::InternalLinkage, strConstant, name);

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = { zero, zero };
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
    gvStr, indices, true);

  return strVal;
}
static FunctionCallee printfPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  PointerType *printfArgTy = PointerType::getUnqual(Type::getInt8Ty(ctx));

  // FunctionType *printfType = FunctionType::get(
  //   Type::getInt32Ty(ctx),
  //   { Type::getInt8PtrTy(ctx) },
  //   true);
  FunctionType *printfTy = FunctionType::get(
    Type::getInt32Ty(ctx),
    printfArgTy,
    true);

  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfTy);

  return printfCallee;
}

static GlobalVariable* createNullGV (Module &M, Twine const &name) {
  LLVMContext &ctx = M.getContext ();
  Constant *nullConstant = Constant::getNullValue (IntegerType::getInt32Ty (ctx));
  // insert global var in module
  GlobalVariable *nullGV = new GlobalVariable(
    M, nullConstant->getType(),
    false,
    GlobalValue::InternalLinkage, 
    nullConstant, 
    name
  );

  return nullGV;
}
static FunctionCallee exitPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  FunctionType *exitType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt32Ty(ctx) },
    false);

  FunctionCallee exitCallee = M.getOrInsertFunction("exit", exitType);

  return exitCallee;
}

static Constant* getInt8StrPtr (Module &M, const char *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();
  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *strGV = new GlobalVariable(
    M, strConstant->getType(),
    true,
    GlobalValue::InternalLinkage,
    strConstant,
    name
  );

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = {zero, zero};
  Constant *strPtr = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
                     strGV, indices, true);
  return strPtr;
}
bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";
  LLVMContext &ctx = M.getContext();
  // FunctionCallee exitCallee = exitPrototype(M);
  FunctionCallee printfCallee = printfPrototype(M);  

  Constant *stackBofMsg = getI8StrVal(M, "!!!STACK BOF!!!\n", "stackBofMsg");
  
  GlobalVariable* depthGV = createNullGV(M, "intDepth");

  for (auto &F : M) {
    if (F.empty()) {
      continue;
    }
    IRBuilder<> BuilderEntry(&*F.getEntryBlock().getFirstInsertionPt());

    Value *ld1 = BuilderEntry.CreateLoad(BuilderEntry.getInt32Ty(), depthGV, depthGV->getName());
    Value *add = BuilderEntry.CreateAdd(ld1, BuilderEntry.getInt32(1));
    BuilderEntry.CreateStore(add, depthGV);
    
    BuilderEntry.CreateCall(
      printfCallee, {
        getInt8StrPtr(M, "%*s", "strIndent"),
        ld1,
        getInt8StrPtr(M, "", "strSpaces")
      }
    );

    BuilderEntry.CreateCall(
      printfCallee, {
        getInt8StrPtr(M, "%s: %p\n", "strAddr"),
        BuilderEntry.CreateGlobalStringPtr(F.getName()),&F
      }
    );

    IRBuilder<> BuilderEnd (&*(--F.back ().end()));


    Value *ld2 = BuilderEnd.CreateLoad(BuilderEnd.getInt32Ty(), depthGV, depthGV->getName()) ;
    Value *sub = BuilderEnd.CreateSub(ld2, BuilderEnd.getInt32(1));
    BuilderEnd.CreateStore(sub, depthGV);
    // GlobalVariable *gv = M.getGlobalVariable("depth");
    // LLVMContext& context = F.getContext();
    // Value* func_getbitcast = ConstantExpr::getBitCast(&F, Type::getInt8PtrTy(context));
    // // errs() <<F.getName() <<": "<< func_getbitcast << " depth: " <<depth <<"\n";
    // // std::string str;
    // // llvm::raw_string_ostream rso(str);
    // // func_getbitcast->print(rso);
    // BasicBlock &Bstart = F.front();
    // BasicBlock &Bend = F.back(); //the last BB of the function (should contain return instruction)
    // // Split "ret" from original basic block (the last BB of the function, Bend)
    // Instruction &ret = *(++Bend.rend()); //only the return instruction
    // BasicBlock *Bret = Bend.splitBasicBlock(&ret, "ret"); //Bret is the last BB that doesn't contain return (the BB "above" "return")

    // //at every instruction (every function call), create an IRBuilder that print the function name
    // Instruction &Istart = Bstart.front();
    // IRBuilder<> BuilderStart(&Istart);
    // string str = F.getName().str() + " \n";
    // const char* cstr = str.c_str();
    // Constant *stackBofMsg = getI8StrVal(M,cstr , "stackBofMsg");
    // BuilderStart.CreateCall(printfCallee, { stackBofMsg });
    // depth++;

   
    
  }



  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);
