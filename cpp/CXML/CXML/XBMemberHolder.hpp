#pragma once

#include "XBMemberValuePolicy.hpp"
#include "XBind.hpp"

#define LINUX

namespace SINUX
{
	int cc_strcmp(char const* _String1, char const* _String2)
	{
#ifdef LINUX
		return strcmp(_String1, _String2);
#else
		return cc_strcmp(_String1, _String2)
#endif
	}

	template<class T>
	class IMemberHolder
	{
	public:
        MemberSerializeFlags m_flags;
        Tag m_tag;
        SerializeParams m_params;

        void setFlags(MemberSerializeFlags f)
        {
            m_flags = f;
		}

        SerializeParams const & params()
        {
            m_params._tag = m_tag;
            return m_params;
		}

        virtual char const * tag(int which = 0) { return m_tag._tag[which]; }

		virtual bool fromXml(TiXmlElement const &, T *) = 0;
		virtual bool intoXml(TiXmlElement *, T const *) = 0;
		virtual bool isAttributeMember() = 0;
	};

    template<class T>   class XBind;        // forward declaration

    template<class T, class MT>
    class FromXmlChildElement : public IMemberHolder<T>
    {
    public:
        IMemberValuePolicy<T, MT> * _mvPolicy;
        FromXmlChildElement(IMemberValuePolicy<T, MT> * mvPolicy)
        {
            _mvPolicy = mvPolicy;
        }

        virtual bool fromXml(TiXmlElement const & elem, T * thisPtr)
        {
            if (!cc_strcmp(elem.Value(), IMemberHolder<T>::tag()))
            {
                MT mv;
                XBind<MT> const * binding = GetXBind(mv, Identity<MT>());
                if (binding->fromXml(elem, &mv, IMemberHolder<T>::params())) 
				{
                    _mvPolicy->setMemberValue(thisPtr, mv);
                    return true;
                }
                else 
				{
                    return false;
                }
            }
            else 
			{
                return false;
            }
        }

        virtual bool intoXml(TiXmlElement * elem, T const * thisPtr)
        {
            MT const & mv = _mvPolicy->getMemberValue(thisPtr);
            TiXmlElement child(IMemberHolder<T>::tag());
            XBind<MT> const * binding = GetXBind(mv, Identity<MT>());
            if (binding->intoXml(&child, mv, IMemberHolder<T>::params()))
            {
                elem->InsertEndChild(child);
                return true;
            }
            else
            {
                return false;
            }
        }

        virtual bool isAttributeMember() { return false; }
    };


    template<class T, class MT, class FromXmlPolicy, class MemberValuePolicy> class MemberHolder;    // forward declaration

	template<class T, class MT>
	IMemberHolder<T> * Member(MT T::*mp)
	{
		typedef FromXmlChildElement<T, MT> XmlPolicy;
		typedef MemberPtrHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._memberPtr = mp;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * Member(MT & (T::*mp)())
	{
		typedef FromXmlChildElement<T, MT> XmlPolicy;
		typedef MemberRefFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._memberRefFunc = mp;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * Member(MT(T::*getter)(), void (T::*setter)(MT))
	{
		typedef FromXmlChildElement<T, MT> XmlPolicy;
		typedef MemberFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * Member(MT(T::*getter)()const, void (T::*setter)(MT))
	{
		typedef FromXmlChildElement<T, MT> XmlPolicy;
		typedef MemberFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = (MT(T::*)())getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * Member(
		MT const & (T::*getter)(),
		void (T::*setter)(MT const &))
	{
		typedef FromXmlChildElement<T, MT> XmlPolicy;
		typedef MemberFuncHolderConstRef<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

    template<class T, class MT> class FromXmlAttribute; // forward declaration
	// BEGIN ATTRIBUTE MAKERS
	template<class T, class MT>
	IMemberHolder<T> * MemberAttribute(MT T::*mp)
	{
		typedef FromXmlAttribute<T, MT> XmlPolicy;
		typedef MemberPtrHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._memberPtr = mp;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * MemberAttribute(MT(T::*getter)(), void (T::*setter)(MT))
	{
		typedef FromXmlAttribute<T, MT> XmlPolicy;
		typedef MemberFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * MemberAttribute(MT(T::*getter)() const, void (T::*setter)(MT))
	{
		typedef FromXmlAttribute<T, MT> XmlPolicy;
		typedef MemberFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = (MT(T::*)())getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * MemberAttribute(
		MT const & (T::*getter)(),
		void (T::*setter)(MT const &))
	{
		typedef FromXmlAttribute<T, MT> XmlPolicy;
		typedef MemberFuncHolderConstRef<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}
	// END ATTRIBUTE MAKERS

	// BEGIN PEER MAKERS
    template<class T, class MT>   class FromXmlElement; // forward declaration
	template<class T, class MT>
	IMemberHolder<T> * MemberPeer(MT T::*mp)
	{
		typedef FromXmlElement<T, MT> XmlPolicy;
		typedef MemberPtrHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._memberPtr = mp;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * MemberPeer(MT(T::*getter)(), void (T::*setter)(MT))
	{
		typedef FromXmlElement<T, MT> XmlPolicy;
		typedef MemberFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * MemberPeer(
		MT const & (T::*getter)(),
		void (T::*setter)(MT const &))
	{
		typedef FromXmlElement<T, MT> XmlPolicy;
		typedef MemberFuncHolderConstRef<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy._getter = getter;
        pMph->m_mvPolicy._setter = setter;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	IMemberHolder<T> * MemberPeer(MT & (T::*mp)())
	{
		typedef FromXmlElement<T, MT> XmlPolicy;
		typedef MemberRefFuncHolder<T, MT> MemberValuePolicy;
		typedef MemberHolder<T, MT, XmlPolicy, MemberValuePolicy> MH_Type;
        MH_Type * pMph = new MH_Type();
        pMph->m_mvPolicy.memberRefFunc_ = mp;
        return &pMph->m_xmlPolicy;
	}

	template<class T, class MT>
	class FromXmlElement : public IMemberHolder<T>
	{
	public:
        IMemberValuePolicy<T, MT> * m_mvPolicy;
		FromXmlElement(IMemberValuePolicy<T, MT> * mvPolicy)
		{
            m_mvPolicy = mvPolicy;
		}

		virtual bool fromXml(TiXmlElement const & elem, T * thisPtr)
		{
            MT & mv = const_cast<MT &>(m_mvPolicy->getMemberValue(thisPtr));
			XBind<MT> const * binding = GetXBind(mv, Identity<MT>());
            if (binding->fromXml(elem, &mv, IMemberHolder<T>::params())) {
                m_mvPolicy->setMemberValue(thisPtr, mv);
				return true;
			}
			else {
				return false;
			}
		}

		virtual bool intoXml(TiXmlElement * elem, T const * thisPtr)
		{
            MT const & mv = m_mvPolicy->getMemberValue(thisPtr);
			XBind<MT> const * binding = GetXBind(mv, Identity<MT>());
			std::string oldValue = elem->Value();
            elem->SetValue(IMemberHolder<T>::tag());
            bool ret = binding->intoXml(elem, mv, IMemberHolder<T>::params());
			elem->SetValue(oldValue);
			return ret;
		}

		virtual bool isAttributeMember() { return true; }
	};



	template<class T, class MT>
	class FromXmlAttribute : public IMemberHolder<T>
	{
	public:
        IMemberValuePolicy<T, MT> * m_mvPolicy;
		FromXmlAttribute(IMemberValuePolicy<T, MT> * mvPolicy)
		{
            m_mvPolicy = mvPolicy;
		}

		virtual bool fromXml(TiXmlElement const & elem, T * thisPtr)
		{
			MT mv;
            const char * attributeValue = elem.Attribute(IMemberHolder<T>::tag());
			if (attributeValue && *attributeValue) {
				ConvertFromString(attributeValue, &mv);
                m_mvPolicy->setMemberValue(thisPtr, mv);
				return true;
			}
			else {
				return false;
			}
		}

		virtual bool intoXml(TiXmlElement * elem, T const * thisPtr)
		{
            MT const & mv = m_mvPolicy->getMemberValue(thisPtr);
			char const * attributeValue = ConvertToString(mv);
            elem->SetAttribute(IMemberHolder<T>::tag(), attributeValue);
			return true;
		}

		virtual bool isAttributeMember() { return true; }
	};

	template<class T, class MT, class FromXmlPolicy, class MemberValuePolicy>
	class MemberHolder
	{
	public:
        FromXmlPolicy m_xmlPolicy;
        MemberValuePolicy m_mvPolicy;

		MemberHolder()
            : m_xmlPolicy((IMemberValuePolicy<T, MT> *)&m_mvPolicy)
		{
		}
	};
}

