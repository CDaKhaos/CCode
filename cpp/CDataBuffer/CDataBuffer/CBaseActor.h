#pragma once
#include "CBaseUnit.h"
#include "CDataDefine.h"

class CBaseActor :public CBaseUnit
{
public:
	CBaseActor() { m_type = emActorUnkonw; }
	virtual ~CBaseActor() {}

public:
	virtual void Serial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf << m_sID;
		dBuf << m_pos;
		dBuf << m_type;
		dBuf << m_att;
	}
	virtual void DSerial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf >> m_sID;
		dBuf >> m_pos;
		dBuf >> m_type;
		dBuf >> m_att;
	}

protected:
	string	m_sID;		// ID
	Pos		m_pos;		// 位置
	ActorType m_type;	// 单兵类型
	AttType m_att;		// 阵营信息
};

