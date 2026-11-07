# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_12:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 12:12:18 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:12:11 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:11:24 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:09:56 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:09:45 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-07 12:08:01 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.036 |  |
| 2026-11-07 12:07:44 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.201 |  |
| 2026-11-07 12:06:58 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.099 |  |
| 2026-11-07 12:06:55 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.009 |  |
| 2026-11-07 12:05:42 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-07 12:05:33 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:05:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.123 |  |
| 2026-11-07 12:04:28 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.029 |  |
| 2026-11-07 12:03:59 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 12:03:52 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-07 12:03:35 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:03:11 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:05 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.150 |  |
| 2026-11-07 12:03:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-07 12:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:02:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:02:38 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:02:37 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:37 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.090 |  |
| 2026-11-07 12:02:31 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-07 12:02:27 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:05 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:02 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 12:01:50 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.142 |  |
| 2026-11-07 12:01:50 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.033 |  |
| 2026-11-07 12:01:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:36 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.103 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 11:11:14 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | -0.018 |  |
| 2026-11-07 12:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.029 |  |
| 2026-11-07 12:03:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-07 12:05:42 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-07 12:03:59 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 12:02:31 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-07 12:02:02 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 12:05:33 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:11:24 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:27 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:03:35 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 11:05:29 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:02:37 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:09:56 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:12:18 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 12:06:55 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.009 |  |
| 2026-11-07 12:04:28 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-07 11:03:30 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:36 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:03:11 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-07 12:09:45 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-07 12:03:52 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-07 12:01:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-07 12:02:38 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:17 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-11-07 12:01:50 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.033 |  |
| 2026-11-07 12:08:01 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.036 |  |
| 2026-11-07 12:12:11 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:02:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.054 |  |
| 2026-11-07 12:02:37 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.090 |  |
| 2026-11-07 12:06:58 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.099 |  |
| 2026-11-07 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.103 |  |
| 2026-11-07 12:05:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.123 |  |
| 2026-11-07 12:01:50 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.142 |  |
| 2026-11-07 12:03:05 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.150 |  |
| 2026-11-07 12:07:44 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)