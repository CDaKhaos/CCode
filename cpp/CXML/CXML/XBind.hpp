#pragma once

#include "XBDef.hpp"
#include "XBMemberHolder.hpp"

namespace SINUX
{
    // 绑定基类
	template<class T>
	class XBind
	{
	public:
		virtual bool fromXml(TiXmlElement const & elem, T * data, SerializeParams const &) const = 0;
		virtual bool intoXml(TiXmlElement * elem, T const & data, SerializeParams const &) const = 0;
	};

	template<class T>
    bool BindToXml(TiXmlElement * elemOut, T const & dataIn)
	{
		XBind<T> const * binding = GetXBind(dataIn, Identity<T>());
		SerializeParams params;
		return binding->intoXml(elemOut, dataIn, params);
	}

	template<class T>
    bool BindFromXml(TiXmlElement const & elemIn, T * dataOut)
	{
		XBind<T> const * binding = GetXBind(*dataOut, Identity<T>());
		SerializeParams params;
		return binding->fromXml(elemIn, dataOut, params);
	}


    // 成员绑定
	template<class T>
	class XBindMember : public XBind<T>
	{
	public:
        bool empty() const  { return m_vMembers.empty(); }

        // 添加成员
        IMemberHolder<T> * AddMember(Tag tag, IMemberHolder<T> * pMbHd)
		{
            pMbHd->m_flags = MemberSerializeFlagsNone;
            pMbHd->m_tag = tag;
            m_vMembers.push_back(pMbHd);
            return pMbHd;
		}

        // 解析
		virtual bool fromXml(TiXmlElement const & elem, T * data, SerializeParams const & params) const
		{
			TiXmlElement const * child = elem.FirstChildElement();
            for (size_t i = 0; i < m_vMembers.size(); i++)
			{
                IMemberHolder<T> * pMbHd = m_vMembers[i];
				bool error = false;

				bool ret;
                if (pMbHd->isAttributeMember())
				{
                    ret = pMbHd->fromXml(elem, data);
				}
                else
                {
                    if (!child)
                    {
						return false;
					}
                    ret = pMbHd->fromXml(*child, data);
				}
				error = !ret;
                if (pMbHd->isAttributeMember())
                {
				}
                else if (!error)
                {
					child = child->NextSiblingElement();
				}

				if (error) 
				{
                    if (pMbHd->isAttributeMember())
                    {
						// no problem
						continue;
					}
                    else
                    {
						// error
						return false;
					}
				}
			}
			return true;
		}

        // 生成
		virtual bool intoXml(TiXmlElement * elem, T const & data, SerializeParams const &) const
		{
            for (size_t i = 0; i < m_vMembers.size(); i++)
            {
                IMemberHolder<T> * pMbHd = m_vMembers[i];
                pMbHd->intoXml(elem, &data);
			}
			return true;
		}

    private:
        std::vector<IMemberHolder<T> *> m_vMembers;
	};


	template<class T>
	class XBindGeneric : public XBind<T>
	{
	public:
		virtual bool fromXml(TiXmlElement const & elem, T * data, SerializeParams const &) const
		{
            TiXmlNode * pNode = elem.FirstChild();
			if (pNode == NULL)
			{
				ConvertFromString("", data);
				return true;
			}
            assert(pNode != NULL);
            if (pNode == NULL)
                return false;
            TiXmlText * pNodeData = pNode->ToText();
            assert(pNodeData != NULL);
            if (pNodeData == NULL)
                return false;
            ConvertFromString(pNodeData->Value(), data);
			return true;
		}

		virtual bool intoXml(TiXmlElement * elem, T const & data, SerializeParams const &) const
		{
			TiXmlText textData(ConvertToString(data));
			elem->InsertEndChild(textData);
			return true;
		}
	};

	template<class T, class VecT>
	class XBindStlContainer : public XBind<VecT>
	{
	public:

        char const * m_szSubTag;
        bool m_bUseSubTag;
        char const * m_szAttributeName;
		XBindStlContainer(bool useSubTag, char const * st = NULL, char const * sizeAttributeName = NULL)
            :m_szSubTag(st), m_bUseSubTag(useSubTag), m_szAttributeName(sizeAttributeName)
		{
		}

		virtual bool fromXml(TiXmlElement const & elem, VecT * data, SerializeParams const & params) const
		{
			data->clear();
			TiXmlElement const * child;
			child = elem.FirstChildElement();
            if (m_szAttributeName)
			{
				int sz = 0;
                ConvertFromString(elem.Attribute(m_szAttributeName), &sz);
				if (sz) 
				{
					//data->reserve(sz);
				}
			}
			while (child) 
			{
				T * value = new T();
				XBind<T> const * binding = GetXBind(*value, Identity<T>());
				bool ret = binding->fromXml(*child, value, params);
				data->push_back(*value);
				if (!ret) 
				{
					return false;
				}
				child = child->NextSiblingElement();
			}
			return true;
		}

		virtual bool intoXml(TiXmlElement * elem, VecT const & data, SerializeParams const & params) const
		{
            if (m_szAttributeName)
			{
                //elem->SetAttribute(m_szAttributeName, ConvertToString(data.size()));
				elem->SetAttribute(m_szAttributeName, ConvertToString((int)data.size())); //x64编译通过 cyx
			}
			for (typename VecT::const_iterator i = data.begin(); i != data.end(); i++) 
			{
				T const & value = *i;
				XBind<T> const * binding = GetXBind(value, Identity<T>());
				char const * tag;
                if (m_bUseSubTag)
				{
                    tag = m_szSubTag;
				}
				else 
				{
					tag = elem->Value();
				}
				TiXmlElement child(tag);
				if (!binding->intoXml(&child, value, params)) 
				{
					return false;
				}
				elem->InsertEndChild(child);
			}
			return true;
		}
	};

	template<class T, class VecT>
	class XBindStlContainerPtr : public XBind<VecT>
	{
	public:

        char const * m_szSubTag;
        bool m_bUseSubTag;
        char const * m_szAttributeName;
		XBindStlContainerPtr(bool useSubTag, char const * st = NULL, char const * sizeAttributeName = NULL)
            :m_szSubTag(st), m_bUseSubTag(useSubTag), m_szAttributeName(sizeAttributeName)
		{
		}

		virtual bool fromXml(TiXmlElement const & elem, VecT * data, SerializeParams const & params) const
		{
			data->clear();
			TiXmlElement const * child;
			child = elem.FirstChildElement();
            if (m_szAttributeName) {
				int sz = 0;
                ConvertFromString(elem.Attribute(m_szAttributeName), &sz);
				if (sz) {
					//data->reserve(sz);
				}
			}
			while (child) {
				T * value = new T();
				if (!value->create()) {
					return false;
				}
				XBind<T> const * binding = GetXBind(*value, Identity<T>());
				bool ret = binding->fromXml(*child, value, params);
				data->push_back(value);
				if (!ret) {
					return false;
				}
				child = child->NextSiblingElement();
			}
			return true;
		}

		virtual bool intoXml(TiXmlElement * elem, VecT const & data, SerializeParams const & params) const
		{
            if (m_szAttributeName) {
                elem->SetAttribute(m_szAttributeName, ConvertToString(data.size()));
			}
			for (typename VecT::const_iterator i = data.begin(); i != data.end(); i++) {
				T const * value = *i;
				if (!value) {
					continue;
				}
				XBind<T> const * binding = GetXBind(*value, Identity<T>());
				char const * tag;
                if (m_bUseSubTag) {
                    tag = m_szSubTag;
				}
				else {
					tag = elem->Value();
				}
				TiXmlElement child(tag);
				if (!binding->intoXml(&child, *value, params)) {
					return false;
				}
				elem->InsertEndChild(child);
			}
			return true;
		}
	};

    template<class T, class CpxT>
    class XBindComplex : public XBind<CpxT>
    {
    public:

        char const * m_szSubTag;
        bool m_bUseSubTag;
        char const * m_szAttributeName;
        XBindComplex(bool useSubTag, char const * st = NULL, char const * sizeAttributeName = NULL)
            :m_szSubTag(st), m_bUseSubTag(useSubTag), m_szAttributeName(sizeAttributeName)
        {
        }

        virtual bool fromXml(TiXmlElement const & elem, CpxT * data, SerializeParams const & params) const
        {
            TiXmlElement const * child;
            child = elem.FirstChildElement();
            if (m_szAttributeName)
            {
                int sz = 0;
                ConvertFromString(elem.Attribute(m_szAttributeName), &sz);
                if (sz)
                {
                    //data->reserve(sz);
                }
            }

            T * valueR = new T();
            XBind<T> const * bindingR = GetXBind(*valueR, Identity<T>());
            bool ret = bindingR->fromXml(*child, valueR, params);
            if (!ret)
            {
                return false;
            }
            data->real(*valueR);
            child = child->NextSiblingElement();

            T * valueI = new T();
            XBind<T> const * bindingI = GetXBind(*valueI, Identity<T>());
            ret = bindingI->fromXml(*child, valueI, params);
            if (!ret)
            {
                return false;
            }
            data->imag(*valueI);
            child = child->NextSiblingElement();

            return true;
        }

        virtual bool intoXml(TiXmlElement * elem, CpxT const & data, SerializeParams const & params) const
        {
//            if (m_szAttributeName)
//            {
//                elem->SetAttribute(m_szAttributeName, ConvertToString(data.size()));
//            }

            T const& valueR = data.real();
            XBind<T> const * bindingR = GetXBind(valueR, Identity<T>());
            TiXmlElement childR("real");
            if (!bindingR->intoXml(&childR, valueR, params))
            {
                return false;
            }
            elem->InsertEndChild(childR);

            T const& valueI = data.imag();
            XBind<T> const * bindingI = GetXBind(valueI, Identity<T>());
            TiXmlElement childI("imag");
            if (!bindingI->intoXml(&childI, valueI, params))
            {
                return false;
            }
            elem->InsertEndChild(childI);



            return true;
        }
    };


	template<class T>
	static XBind<T> const *
		GetXBind(T const &, IdentityBase)
	{
		static XBindGeneric<T> binding;
		return &binding;
	}


	static XBind<float> const *
		GetXBind(float const &, IdentityBase)
	{
		static XBindGeneric<float> binding;
		return &binding;
	}

	static XBind<double> const *
		GetXBind(double const &, IdentityBase)
	{
		static XBindGeneric<double> binding;
		return &binding;
	}

	static XBind<int> const *
		GetXBind(int const &, IdentityBase)
	{
		static XBindGeneric<int> binding;
		return &binding;
	}

	static XBind<char const *> const *
		GetXBind(char const * const &, IdentityBase)
	{
		static XBindGeneric<char const *> binding;
		return &binding;
	}

	static XBind<std::string> const *
		GetXBind(std::string const &, IdentityBase)
	{
		static XBindGeneric<std::string> binding;
		return &binding;
	}

	template<class T, class VecT>
	XBind<VecT> const *
		GetXBind(std::vector<T> const &, Identity<VecT>)
	{
		static XBindStlContainer<T, VecT> binding(false);
		return &binding;
	}

	template<class T, class VecT>
	XBind<VecT> const *
		GetXBind(std::list<T> const &, Identity<VecT>)
	{
		static XBindStlContainer<T, VecT> binding(false);
		return &binding;
	}

    template<class T, class CpxT>
    XBind<CpxT> const *
        GetXBind(std::complex<T> const &, Identity<CpxT>)
    {
        static XBindComplex<T, CpxT> binding(false);
        return &binding;
    }

}

