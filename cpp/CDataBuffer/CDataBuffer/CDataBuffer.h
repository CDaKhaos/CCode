#ifndef __CC_DATA_BUFFER_H__
#define __CC_DATA_BUFFER_H__

#pragma once

#include <assert.h>
#include <string>
#include <vector>
using namespace std;

#define LINUX

namespace CSunShine
{
    void cc_memcpy(void* pDes, const void* pSrc, size_t iLen)
    {
#ifdef LINUX
            memcpy(pDes, pSrc, iLen);
#else
			memcpy_s(pDes, iLen, pSrc, iLen);
#endif

    }

	class CDataBuffer
	{
	public:
		CDataBuffer()
		{
			Init();
		}
		CDataBuffer(char* pBuf, size_t iLen)
		{
			Init();
			AdaptBuffer(iLen);
            cc_memcpy(m_pBuffer, pBuf, iLen);
		}
		~CDataBuffer()
		{
			delete[] m_pBuffer;
			m_pBuffer = NULL;
			Init();
		}

		CDataBuffer(const CDataBuffer& other)
		{
			*this = other;
		}
		CDataBuffer& operator= (const CDataBuffer& other)
		{
			m_iBufferSize = other.m_iBufferSize;
			m_iGetBufOffset = other.m_iGetBufOffset;
			m_iSetBufOffset = other.m_iSetBufOffset;

			m_pBuffer = new char[m_iBufferSize];
            cc_memcpy(m_pBuffer, other.m_pBuffer, m_iBufferSize);
			return *this;
		}

		// 需要外部删除
		char* GetCharBuf(size_t& i)
		{
			i = m_iSetBufOffset;
			char* pBuf = new char[m_iSetBufOffset];
			cc_memcpy(pBuf, m_pBuffer, m_iSetBufOffset);
			return pBuf;
		}

		template<typename T>
		CDataBuffer& operator<< (const T& t)
		{
			int nSize = sizeof(T);
			AdaptBuffer(nSize);
			cc_memcpy(m_pBuffer+m_iSetBufOffset, &t, nSize);
			m_iSetBufOffset += nSize;

			return *this;
		}

		template<typename T>
		CDataBuffer& operator>> (T& t)
		{
			int nSize = sizeof(T);
			assert(m_iGetBufOffset + nSize <= m_iBufferSize);
			cc_memcpy(&t, m_pBuffer+m_iGetBufOffset, nSize);
			m_iGetBufOffset += nSize;

			return *this;
		}

		CDataBuffer& operator<< (const string& sValue)
		{
			size_t iSize = sValue.size()+1;
			AdaptBuffer(iSize);
			cc_memcpy(m_pBuffer+m_iSetBufOffset, sValue.c_str(), iSize);
			m_iSetBufOffset += iSize;

			return *this;
		}

		CDataBuffer& operator>> (string& sValue)
		{
			sValue = m_pBuffer+m_iGetBufOffset;
			m_iGetBufOffset += sValue.size() + 1;
			assert(m_iGetBufOffset <= m_iBufferSize);

			return *this;
		}

		template<typename T>
		CDataBuffer& operator<< (vector<T>& vValues)
		{
			size_t iSize = vValues.size();
			*this << iSize;
			typename vector<T>::iterator iter = vValues.begin();
			for (; iter != vValues.end(); ++iter)
			{
				*this << *iter;
			}

			return *this;
		}

		template<typename T>
		CDataBuffer& operator>> (vector<T>& vValues)
		{
			size_t iSize = 0;
			*this >> iSize;
			while (iSize--)
			{
				T t;
				*this >> t;
				vValues.push_back(t);
			}

			return *this;
		}

	private:
		void Init()
		{
			m_pBuffer = NULL;
			m_iBufferSize = 0;
			m_iSetBufOffset = 0;
			m_iGetBufOffset = 0;
		}
		void AdaptBuffer(const size_t nSize)
		{
			while (m_iBufferSize < m_iSetBufOffset+nSize)
			{
				m_iBufferSize += 512;
				char* pBuf = new char[m_iBufferSize];
				cc_memcpy(pBuf, m_pBuffer, m_iSetBufOffset);
				delete[] m_pBuffer;
				m_pBuffer = pBuf;
			}
		}
	private:
		char* m_pBuffer;
		size_t m_iBufferSize;
		size_t m_iSetBufOffset;
		size_t m_iGetBufOffset;
	};
}


#endif	// __CC_DATA_BUFFER_H__
