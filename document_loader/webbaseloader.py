from langchain_community.document_loaders import WebBaseLoader
# WebBaseLoader work goog on html base content so well not on heavy javascript 
#in which user intercation is too much 
#for that there are other loaders

loader=WebBaseLoader("https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=159651196451&hvpone=&hvptwo=&hvadid=675114638367&hvpos=&hvnetw=g&hvrand=1360470235745867303&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9076954&hvtargid=kwd-10573980&hydadcr=2246_13468515")
docs=loader.load()
print(docs)