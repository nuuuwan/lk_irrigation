# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_23:19:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 23:19:34 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 23:15:43 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.000 |  |
| 2026-09-24 23:12:04 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-09-24 23:11:09 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-24 23:09:13 | Kithulgala (Kelani Ganga) | 2.99 | 🟢 Normal | -0.235 |  |
| 2026-09-24 23:08:28 | Baddegama (Gin Ganga) | 4.55 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 23:06:57 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:06:03 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-24 23:05:26 | Urawa (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.043 |  |
| 2026-09-24 23:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.80 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-24 23:05:15 | Glencourse (Kelani Ganga) | 14.55 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-24 23:04:17 | Rathnapura (Kalu Ganga) | 6.42 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-09-24 23:04:14 | Holombuwa (Kelani Ganga) | 1.96 | 🟢 Normal | -0.134 |  |
| 2026-09-24 23:04:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:04:13 | Deraniyagala (Kelani Ganga) | 3.14 | 🟢 Normal | -0.417 |  |
| 2026-09-24 23:04:09 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-09-24 23:03:51 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 23:03:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:02:50 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 23:02:44 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-24 23:02:35 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 23:02:34 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-09-24 23:02:29 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -1.065 |  |
| 2026-09-24 23:02:14 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-09-24 23:02:14 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 23:02:09 | Hanwella (Kelani Ganga) | 5.81 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 23:01:53 | Thawalama (Gin Ganga) | 4.96 | 🟡 Alert | -0.132 |  |
| 2026-09-24 23:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:01:05 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:00:57 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 23:00:51 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:00:37 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:00:34 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 23:08:28 | Baddegama (Gin Ganga) | 4.55 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 23:12:04 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-09-24 23:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.80 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-24 23:11:09 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | -0.031 |  |
| 2026-09-24 23:04:17 | Rathnapura (Kalu Ganga) | 6.42 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-09-24 23:02:34 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-09-24 23:15:43 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.000 |  |
| 2026-09-24 23:01:53 | Thawalama (Gin Ganga) | 4.96 | 🟡 Alert | -0.132 |  |
| 2026-09-24 23:05:15 | Glencourse (Kelani Ganga) | 14.55 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-24 23:06:03 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-24 23:02:35 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 23:19:34 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 23:02:09 | Hanwella (Kelani Ganga) | 5.81 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 23:02:44 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-24 23:03:51 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 23:02:50 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 23:02:14 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 23:00:57 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 21:07:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:00:34 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:00:37 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:03:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:05:28 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:04:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:00:51 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:01:05 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:06:57 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:04:09 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-09-24 23:02:14 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-09-24 23:05:26 | Urawa (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.043 |  |
| 2026-09-24 22:07:04 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.097 |  |
| 2026-09-24 23:04:14 | Holombuwa (Kelani Ganga) | 1.96 | 🟢 Normal | -0.134 |  |
| 2026-09-24 23:09:13 | Kithulgala (Kelani Ganga) | 2.99 | 🟢 Normal | -0.235 |  |
| 2026-09-24 23:04:13 | Deraniyagala (Kelani Ganga) | 3.14 | 🟢 Normal | -0.417 |  |
| 2026-09-24 23:02:29 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -1.065 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)