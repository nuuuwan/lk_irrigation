# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_15:05:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,365 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 15:05:58 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:05:46 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.086 |  |
| 2026-10-18 15:05:39 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.058 |  |
| 2026-10-18 15:05:12 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:05:00 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 15:04:13 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | -0.020 |  |
| 2026-10-18 15:04:00 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.028 |  |
| 2026-10-18 15:03:43 | Moragaswewa (Deduru Oya) | 2.10 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-18 15:03:38 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.053 |  |
| 2026-10-18 15:03:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:03:08 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-10-18 15:02:47 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.081 |  |
| 2026-10-18 15:02:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:02:38 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:02:27 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:02:15 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:02:14 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.051 |  |
| 2026-10-18 15:02:12 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:02:07 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -1.488 |  |
| 2026-10-18 15:02:05 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:01:53 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-18 15:01:44 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:37 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 15:01:29 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:01:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:22 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-18 15:01:20 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:10 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-18 15:00:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:00:16 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 15:00:06 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -1.488 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 15:05:00 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 14:18:44 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.008 |  |
| 2026-10-18 15:03:43 | Moragaswewa (Deduru Oya) | 2.10 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-18 15:01:22 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-18 15:01:53 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-18 14:10:01 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-18 15:01:37 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 15:00:16 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 15:01:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:44 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:05:58 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:02:12 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:02:27 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:02:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:03:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:10 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:14:05 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:01:20 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:05:12 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:01:29 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:02:38 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:02:15 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:00:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:02:05 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 14:00:31 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-10-18 14:05:33 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2026-10-18 15:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-18 14:05:10 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.013 |  |
| 2026-10-18 15:03:08 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-10-18 15:04:13 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | -0.020 |  |
| 2026-10-18 14:14:50 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.026 |  |
| 2026-10-18 15:04:00 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.028 |  |
| 2026-10-18 15:02:14 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.051 |  |
| 2026-10-18 15:03:38 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.053 |  |
| 2026-10-18 15:05:39 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.058 |  |
| 2026-10-18 15:02:47 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.081 |  |
| 2026-10-18 15:05:46 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.086 |  |
| 2026-10-18 14:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -0.161 |  |
| 2026-10-18 15:02:07 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -1.488 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)