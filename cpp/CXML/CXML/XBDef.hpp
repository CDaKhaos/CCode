#pragma once

//#define LINUX

#if _MSC_VER >=1600 //(1600 is VS2010)
#pragma execution_character_set("utf-8")
#endif

#include "tinyxml.h"

#include <vector>
#include <list>
#include <complex>
#include <sstream>

namespace SINUX
{
	template< class T >
	void cc_sprintf(char* const buffer, char const* const _format, const T& value, size_t iBufSize = 2048)
	{
#ifdef LINUX
		sprintf(buffer, _format, value);
#else
		sprintf_s(buffer, iBufSize, _format, value);
#endif
	}

	// 为了调用时，不用带模板参数，定义空类
	class IdentityBase
	{
	public:
	};

	template< class T >
	class Identity : public IdentityBase
	{
	public:
		typedef T type;

	};

    // 序列化类型
    enum MemberSerializeFlags
	{
		MemberSerializeFlagsNone = 0,
        MemberOptional = 1,
	};

    // XML的标签
	class Tag
	{
	public:
		// support up to 3 tags
		char const * _tag[3];


		Tag(char const * tagOne = NULL) 
		{
			_tag[0] = tagOne;
			_tag[1] = NULL;
			_tag[2] = NULL;
		}
		Tag(char const * tagOne, char const * tagTwo) 
		{
			_tag[0] = tagOne;
			_tag[1] = tagTwo;
			_tag[2] = NULL;
		}
		Tag(char const * tagOne, char const * tagTwo, char const * tagThree) 
		{
			_tag[0] = tagOne;
			_tag[1] = tagTwo;
			_tag[2] = tagThree;
		}
	};

	struct SerializeParams {
		Tag _tag;
	};

	// 新类型，在此处添加
    static void	ConvertFromString(char const * strIn, const char * * dataOut)
	{
		*dataOut = strIn;
	}

    static char const *	ConvertToString(double const & d)
	{
		static char buffer[2048];
        cc_sprintf(buffer, "%0.10f", d);
		return buffer;
	}


    static char const * ConvertToString(float const & f)
	{
		return ConvertToString((double)f);
	}

    static char const *	ConvertToString(int const & d)
	{
        static char buffer[2048];

        cc_sprintf(buffer, "%d", d);

		return buffer;
	}

    static char const *	ConvertToString(unsigned long long const & d)
	{
		static char buffer[2048];
        cc_sprintf(buffer, "%llu", d);
		return buffer;
	}

    static char const *	ConvertToString(char const * const & s)
	{
		return s;
	}

	static char const *	ConvertToString(char unsigned const * const & s)
	{
		return (char const *)s;
	}

    static char const *	ConvertToString(std::string const & s)
	{
		return s.c_str();
	}

	// 新类型，在此处添加
	// unsigned char *

	static void	ConvertFromString(char const * strIn, unsigned char ** dataOut)
	{
		*dataOut = (unsigned char *)strIn;
	}

	static void	ConvertFromString(char const * strIn, char ** dataOut)
	{
		*dataOut = (char *)strIn;
	}

    static void	ConvertFromString(char const * strIn, std::string * dataOut)
	{
		*dataOut = strIn;
	}

    static void	ConvertFromString(char const * strIn, int * dataOut)
	{
		*dataOut = atoi(strIn);
	}

    static void	ConvertFromString(char const * strIn, unsigned int * dataOut) //cyx
	{
		*dataOut = (unsigned int)atoi(strIn);
	}

	static void	ConvertFromString(char const * strIn, unsigned long long * dataOut)
	{
		*dataOut = (unsigned long long)atoll(strIn);
	}

    static void	ConvertFromString(char const * strIn, unsigned char * dataOut)
    {
        *dataOut = (unsigned int)atoi(strIn);
    }

    static void	ConvertFromString(char const * strIn, double * dataOut)
	{
		*dataOut = atof(strIn);
	}

    static void	ConvertFromString(char const * strIn, float * dataOut)
	{
		*dataOut = (float)atof(strIn);
	}

	static void	ConvertFromString(char const * strIn, bool * dataOut) //cyx
	{
		*dataOut = (unsigned int)atoi(strIn);
	}
}

