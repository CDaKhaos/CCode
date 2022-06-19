#pragma once
#include "CBaseActor.h"
class CUav : public CBaseActor
{
public:
	CUav() { m_type = emUav; }
	virtual ~CUav() {}

public:
	virtual void Serial(CSunShine::CDataBuffer& dBuf)
	{
		CBaseActor::Serial(dBuf);
		dBuf << A;
	}
	virtual void DSerial(CSunShine::CDataBuffer& dBuf)
	{
		CBaseActor::DSerial(dBuf);
		dBuf >> A;
	}
public:
	string A;

};

