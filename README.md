# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_01:03:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 01:03:12 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-07 01:02:44 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.070 |  |
| 2026-11-07 01:02:44 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-11-07 01:02:36 | Giriulla (Maha Oya) | 3.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 01:02:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-07 01:02:24 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:23 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-07 01:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.103 |  |
| 2026-11-07 01:00:35 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:00:35 | Glencourse (Kelani Ganga) | 12.54 | 🟢 Normal | 0.458 | 🔺 Rising |
| 2026-11-07 01:00:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 00:04:59 | Holombuwa (Kelani Ganga) | 3.92 | 🟠 Minor Flood | -0.512 |  |
| 2026-11-07 00:03:18 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.122 | 🔺 Rising |
| 2026-11-07 01:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-07 01:00:35 | Glencourse (Kelani Ganga) | 12.54 | 🟢 Normal | 0.458 | 🔺 Rising |
| 2026-11-07 00:07:21 | Peradeniya (Mahaweli Ganga) | 4.16 | 🟢 Normal | 0.377 | 🔺 Rising |
| 2026-11-07 00:02:38 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-07 01:03:12 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 00:02:21 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-07 00:04:24 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-07 00:09:21 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-07 00:12:49 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 01:02:36 | Giriulla (Maha Oya) | 3.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 00:06:51 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-07 00:03:36 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 00:08:14 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-07 00:04:49 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-07 00:02:16 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:33 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:24 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:13 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:00:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:11:57 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:03:31 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:10:54 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:23 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 00:03:48 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:00:35 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-07 00:09:34 | Rathnapura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.019 |  |
| 2026-11-07 00:04:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-11-07 01:02:44 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-11-07 01:02:44 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.070 |  |
| 2026-11-07 01:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)