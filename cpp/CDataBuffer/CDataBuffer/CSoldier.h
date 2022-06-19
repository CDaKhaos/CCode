#pragma once

#include "CBaseActor.h"

class CSoldier : public CBaseActor
{
public:
	CSoldier() { m_type = emSoldier;  }
	virtual ~CSoldier() {}

public:
	virtual void Serial(CSunShine::CDataBuffer& dBuf)
	{
		CBaseActor::Serial(dBuf);
		dBuf << m_nLive;
		dBuf << m_b;

	}
	virtual void DSerial(CSunShine::CDataBuffer& dBuf)
	{
		CBaseActor::DSerial(dBuf);
		dBuf >> m_nLive;
		dBuf >> m_b;
	}
public:
	int m_nLive;
	int m_b;
};

