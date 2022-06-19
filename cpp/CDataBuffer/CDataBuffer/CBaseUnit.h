#pragma once

#include "CDataBuffer.h"

class CBaseUnit
{
public:
	CBaseUnit() {}
	virtual ~CBaseUnit() {}

public:
	virtual void Serial(CSunShine::CDataBuffer& dBuf) = 0;
	virtual void DSerial(CSunShine::CDataBuffer& dBuf) = 0;
};

class Pos : public CBaseUnit
{
public:
	Pos() { x = y = z = 0; }
	virtual ~Pos() {}

public:
	virtual void Serial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf << x;
		dBuf << y;
		dBuf << z;
	}
	virtual void DSerial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf >> x;
		dBuf >> y;
		dBuf >> z;
	}

public:
	float x;
	float y;
	float z;
};


