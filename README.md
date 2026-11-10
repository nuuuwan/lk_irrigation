# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_16:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 16:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-10 16:02:58 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.113 |  |
| 2026-11-10 16:02:55 | Hanwella (Kelani Ganga) | 4.96 | 🟢 Normal | -0.155 |  |
| 2026-11-10 16:02:53 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.060 |  |
| 2026-11-10 16:02:52 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-11-10 16:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 16:02:43 | Moraketiya (Walawe Ganga) | 3.02 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-10 16:02:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 16:01:45 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-10 16:01:04 | Thalgahagoda (Nilwala Ganga) | 1.67 | 🟡 Alert | 0.000 |  |
| 2026-11-10 16:00:35 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 15:05:15 | Baddegama (Gin Ganga) | 4.25 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 16:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 15:03:01 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-10 16:02:43 | Moraketiya (Walawe Ganga) | 3.02 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-10 16:01:04 | Thalgahagoda (Nilwala Ganga) | 1.67 | 🟡 Alert | 0.000 |  |
| 2026-11-10 15:03:00 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.031 |  |
| 2026-11-10 15:09:05 | Magura (Kalu Ganga) | 4.63 | 🟡 Alert | -0.051 |  |
| 2026-11-10 15:03:00 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-10 16:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-10 15:01:06 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 16:01:45 | Kuda Oya (Kirindi Oya) | 1.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-10 16:02:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 15:04:31 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 15:13:00 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-10 15:02:53 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46⌛ | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:02:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:04:35 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:03:29 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:01:07 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:06:21 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:05:06 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-11-10 15:02:16 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-11-10 16:02:52 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-11-10 15:01:39 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-11-10 15:06:31 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.023 |  |
| 2026-11-10 15:07:28 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.029 |  |
| 2026-11-10 15:01:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-11-10 15:02:23 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | -0.040 |  |
| 2026-11-10 15:08:17 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.040 |  |
| 2026-11-10 15:01:33 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.052 |  |
| 2026-11-10 16:02:53 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.060 |  |
| 2026-11-10 16:00:35 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.063 |  |
| 2026-11-10 16:02:58 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.113 |  |
| 2026-11-10 15:06:17 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.127 |  |
| 2026-11-10 15:08:21 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.127 |  |
| 2026-11-10 16:02:55 | Hanwella (Kelani Ganga) | 4.96 | 🟢 Normal | -0.155 |  |
| 2026-11-10 15:03:54 | Glencourse (Kelani Ganga) | 11.98 | 🟢 Normal | -0.178 |  |
| 2026-11-10 15:07:33 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | -0.813 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)