# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_01:33:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 01:33:05 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:32:32 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.027 |  |
| 2026-09-23 01:21:43 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 01:15:55 | Peradeniya (Mahaweli Ganga) | 3.94 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-23 01:15:23 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-23 01:12:28 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-23 01:08:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-23 01:07:48 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | -0.029 |  |
| 2026-09-23 01:05:12 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-23 01:05:06 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-09-23 01:05:03 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:04:35 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.104 |  |
| 2026-09-23 01:04:26 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-23 01:04:21 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:04:16 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-23 01:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:04:05 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-23 01:03:15 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:02 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-09-23 01:02:57 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:33 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-23 01:02:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 01:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | -0.041 |  |
| 2026-09-23 01:01:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:01:48 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.022 |  |
| 2026-09-23 01:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:22 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.010 |  |
| 2026-09-23 01:01:09 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-23 01:00:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:00:30 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 01:12:28 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-23 01:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | -0.041 |  |
| 2026-09-23 01:01:22 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.010 |  |
| 2026-09-23 01:00:30 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |
| 2026-09-23 01:15:55 | Peradeniya (Mahaweli Ganga) | 3.94 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-23 01:04:05 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-23 01:15:23 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-23 01:08:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-23 01:05:12 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-23 01:21:43 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 01:04:26 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-23 00:10:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-23 01:02:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:00:31 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:00:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 00:04:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:33:05 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:03:15 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:57 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:04:21 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:02:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-23 01:01:55 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:04:07 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:05:03 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 01:05:06 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-09-22 22:07:34 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.012 |  |
| 2026-09-23 01:01:48 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.022 |  |
| 2026-09-23 01:32:32 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.027 |  |
| 2026-09-23 01:07:48 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | -0.029 |  |
| 2026-09-23 01:02:33 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-23 00:02:34 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.051 |  |
| 2026-09-23 01:03:02 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-09-23 01:04:35 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)