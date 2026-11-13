# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_03:03:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,212 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 03:03:12 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 03:03:09 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:02:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-11-14 03:02:48 | Baddegama (Gin Ganga) | 3.83 | 🟡 Alert | -0.020 |  |
| 2026-11-14 03:02:47 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.013 |  |
| 2026-11-14 03:02:46 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-11-14 03:02:35 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.041 |  |
| 2026-11-14 03:02:21 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:11 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:09 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:34 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-11-14 03:01:12 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:00:16 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-14 03:00:16 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:41:09 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.024 |  |
| 2026-11-14 02:40:05 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 02:35:14 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-14 02:33:19 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.041 |  |
| 2026-11-14 02:20:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.097 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 02:40:05 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 03:02:48 | Baddegama (Gin Ganga) | 3.83 | 🟡 Alert | -0.020 |  |
| 2026-11-14 01:06:42 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.020 |  |
| 2026-11-14 02:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | -0.057 |  |
| 2026-11-14 02:20:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-14 03:00:16 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 02:03:41 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:12 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:01:54 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:02:09 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:46 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:11:32 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 01:02:16 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 03:03:09 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:06:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:14:27 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-11-14 01:31:10 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.007 |  |
| 2026-11-14 03:03:12 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:03:38 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:01:17 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-14 03:00:16 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-14 03:02:47 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.013 |  |
| 2026-11-14 03:02:21 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-14 03:02:11 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-11-14 02:41:09 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.024 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 00:01:56 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-11-14 01:02:42 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-11-14 02:04:32 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.039 |  |
| 2026-11-14 03:02:46 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-11-14 03:02:35 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.041 |  |
| 2026-11-14 02:05:33 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.047 |  |
| 2026-11-14 03:01:34 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-11-14 03:02:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-11-14 01:38:19 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)