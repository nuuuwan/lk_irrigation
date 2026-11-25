# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_08:05:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,150 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 08:05:06 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 08:04:57 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-11-25 08:04:51 | Siyambalanduwa (Heda Oya) | 1.36 | 🟢 Normal | -0.108 |  |
| 2026-11-25 08:04:21 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.048 |  |
| 2026-11-25 08:04:03 | Giriulla (Maha Oya) | 2.69 | 🟢 Normal | -0.137 |  |
| 2026-11-25 08:03:55 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-11-25 08:03:32 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.201 |  |
| 2026-11-25 08:03:32 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.042 |  |
| 2026-11-25 08:03:24 | Moraketiya (Walawe Ganga) | 2.85 | 🟢 Normal | -0.051 |  |
| 2026-11-25 08:03:18 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-25 08:03:12 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.108 |  |
| 2026-11-25 08:02:52 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.104 |  |
| 2026-11-25 08:02:42 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 08:02:30 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-11-25 08:02:24 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.054 |  |
| 2026-11-25 08:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.026 |  |
| 2026-11-25 08:02:02 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | -0.095 |  |
| 2026-11-25 08:01:55 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-11-25 08:01:48 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 08:01:47 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.003 |  |
| 2026-11-25 08:01:40 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.028 |  |
| 2026-11-25 08:01:25 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 08:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 08:01:16 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.146 |  |
| 2026-11-25 08:00:56 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.080 |  |
| 2026-11-25 08:00:47 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.080 |  |
| 2026-11-25 08:00:40 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 08:00:02 | Magura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.140 |  |
| 2026-11-25 07:40:40 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.146 |  |
| 2026-11-25 07:40:02 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.091 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 08:03:12 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | -0.108 |  |
| 2026-11-25 07:08:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-25 07:16:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-25 07:00:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-25 07:40:02 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-25 08:01:25 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 08:05:06 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 08:02:42 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 08:01:48 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:01:32 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 08:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:10:04 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 08:00:40 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 08:01:47 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.003 |  |
| 2026-11-25 08:01:55 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-11-25 08:03:55 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-11-25 07:18:07 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-11-25 08:03:18 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 08:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.026 |  |
| 2026-11-25 08:01:40 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.028 |  |
| 2026-11-25 08:02:30 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-11-25 08:03:32 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.042 |  |
| 2026-11-25 07:22:58 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.047 |  |
| 2026-11-25 08:04:21 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.048 |  |
| 2026-11-25 08:04:57 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-11-25 08:03:24 | Moraketiya (Walawe Ganga) | 2.85 | 🟢 Normal | -0.051 |  |
| 2026-11-25 08:02:24 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.054 |  |
| 2026-11-25 08:00:47 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.080 |  |
| 2026-11-25 08:00:56 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.080 |  |
| 2026-11-25 07:07:42 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.092 |  |
| 2026-11-25 08:02:02 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | -0.095 |  |
| 2026-11-25 08:02:52 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.104 |  |
| 2026-11-25 08:04:51 | Siyambalanduwa (Heda Oya) | 1.36 | 🟢 Normal | -0.108 |  |
| 2026-11-25 08:04:03 | Giriulla (Maha Oya) | 2.69 | 🟢 Normal | -0.137 |  |
| 2026-11-25 08:00:02 | Magura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.140 |  |
| 2026-11-25 08:01:16 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.146 |  |
| 2026-11-25 07:07:41 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.163 |  |
| 2026-11-25 08:03:32 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)