#pragma once

#include "XBind.hpp"

namespace SINUX
{
	// 生成XML文件
	template<class T>
	void MakeXml(const std::string& sPath, T const & t, const std::string& sRoot = "ROOT")
	{
		XMLDocument doc;
		//XMLDeclaration* decl = new XMLDeclaration("1.0", "UTF-8", "");
		XMLDeclaration* decl = doc.NewDeclaration("xml version=\"1.0\" encoding=\"UTF-8\"");//cyx 20220725

		doc.LinkEndChild(decl);

        //XMLElement* pEle = new XMLElement(sRoot.c_str());
		XMLElement* pEle = doc.NewElement(sRoot.c_str()); //cyx 20220725
		BindToXml(pEle, t);
		doc.LinkEndChild(pEle);

		FILE *fp = NULL;
		cc_fopen(&fp, sPath.c_str(), "w");
		XMLPrinter printer(fp);
		doc.Print(&printer);  //cyx 20220725
		//doc.Print(fp, 0);
		fclose(fp);

		// 释放上面new的所有指针
		doc.Clear();
	}

	template<class T>
    bool ParseXml(const std::string& sPath, T & t, const std::string& sRoot = "ROOT")
	{
		//XMLDocument doc(sPath.c_str());
		XMLDocument doc; //cyx 20220725
		if (doc.LoadFile(sPath.c_str())) 
		{
			return false;
		}

		XMLElement* pEle = NULL;
		pEle = doc.FirstChildElement();

		BindFromXml(*pEle, &t);

        doc.Clear();

		return true;
	}

}
