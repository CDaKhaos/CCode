#pragma once

namespace SINUX
{
	template<class T, class MT>
	class IMemberValuePolicy
	{
	public:
		virtual MT const & getMemberValue(T const * thisPtr) = 0;
		virtual void setMemberValue(T * thisPtr, MT const & mv) = 0;
	};


	template<class T, class MT>
	class MemberFuncHolder : public IMemberValuePolicy<T, MT>
	{
	public:
        MT(T::*_getter)();
        void (T::*_setter)(MT);

		virtual MT const & getMemberValue(T const * thisPtr) 
		{
			static MT mv;
            mv = (const_cast<T*>(thisPtr)->*_getter)();
			return mv;
		}

		virtual void setMemberValue(T * thisPtr, MT const & mv) 
		{
            (thisPtr->*_setter)(mv);
		}

	};

	template<class T, class MT>
	class MemberFuncHolderConstRef : public IMemberValuePolicy<T, MT>
	{
	public:
        MT const & (T::*_getter)();
        void (T::*_setter)(MT const &);

		virtual MT const & getMemberValue(T const * thisPtr) 
		{
            return (thisPtr->*_getter)();
		}

		virtual void setMemberValue(T * thisPtr, MT const & mv) 
		{
            (thisPtr->*_setter)(mv);
		}
	};

	template<class T, class MT>
	class MemberPtrHolder : public IMemberValuePolicy<T, MT>
	{
	public:
        MT T::*_memberPtr;  // 成员函数地址
        virtual MT const & getMemberValue(T const * thisPtr) { return thisPtr->*_memberPtr; }
        virtual void setMemberValue(T * thisPtr, MT const & mv)
        {
			// by casting away const here, we can support member pointers to arrays
            thisPtr->*_memberPtr = const_cast<MT &>(mv);
		}
	};


	template<class T, class MT>
	class MemberRefFuncHolder : public IMemberValuePolicy<T, MT>
	{
	public:
        MT & (T::*_memberRefFunc)();
        virtual MT const & getMemberValue(T const * thisPtr) { return (const_cast<T*>(thisPtr)->*_memberRefFunc)(); }
		virtual void setMemberValue(T * thisPtr, MT const & mv) 
		{
            (thisPtr->*_memberRefFunc)() = mv;
		}
	};

}


