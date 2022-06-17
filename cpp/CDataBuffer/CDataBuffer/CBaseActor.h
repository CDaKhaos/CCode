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
	Pos		m_pos;		// λ��
	ActorType m_type;	// ��������
	AttType m_att;		// ��Ӫ��Ϣ
};

