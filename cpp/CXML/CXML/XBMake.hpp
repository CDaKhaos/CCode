#pragma once

#include "XBind.hpp"

namespace SINUX
{
	// 生成XML文件
	template<class T>
	void MakeXml(const std::string& sPath, T const & t, const std::string& sRoot = "ROOT")
	{
		TiXmlDocument doc;
		TiXmlDeclaration* decl = new TiXmlDeclaration("1.0", "UTF-8", "");
		doc.LinkEndChild(decl);

		TiXmlElement* pEle = new TiXmlElement(sRoot);
		BindToXml(pEle, t);
		doc.LinkEndChild(pEle);

		FILE *fp = NULL;
		fopen_s(&fp, sPath.c_str(), "w");
		doc.Print(fp, 0);
		fclose(fp);

		// 释放上面new的所有指针
		doc.Clear();
	}

	template<class T>
    bool ParseXml(const std::string& sPath, T & t, const std::string& sRoot = "ROOT")
	{
		TiXmlDocument doc(sPath.c_str());
		if (!doc.LoadFile())
		{
			return false;
		}

		TiXmlElement* pEle = NULL;
		pEle = doc.FirstChildElement();

		BindFromXml(*pEle, &t);

        doc.Clear();

		return true;
	}

}
