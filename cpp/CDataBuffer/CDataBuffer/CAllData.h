#pragma once
#include "CUav.h"
#include "CSoldier.h"


class CAllData : public CBaseUnit
{
public:
	CAllData()
	{
		m_pSendBuf = nullptr;

	}
	CAllData(char* pBuf, size_t iLen)
	{
		m_pSendBuf = nullptr;
		RecvBuf(pBuf, iLen);
	}
	virtual ~CAllData() 
	{
		delete[] m_pSendBuf;
		m_pSendBuf = nullptr;
	}

public:
	virtual void Serial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf << m_vUav;
		dBuf << m_vSoldier;
	}
	virtual void DSerial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf >> m_vUav;
		dBuf >> m_vSoldier;
	}

	char* GetSendBuf(size_t& iLen)
	{
		if (m_pSendBuf != nullptr)
		{
			delete[] m_pSendBuf;
			m_pSendBuf = nullptr;
		}
		CSunShine::CDataBuffer dBuf;
		Serial(dBuf);
		m_pSendBuf = dBuf.GetCharBuf(iLen);

		return m_pSendBuf;
	}

	void RecvBuf(char* pBuf, size_t iLen)
	{
		CSunShine::CDataBuffer dBuf(pBuf, iLen);
		DSerial(dBuf);
	}
public:
	vector<CUav> m_vUav;
	vector<CSoldier> m_vSoldier;

private:
	char* m_pSendBuf;
};

