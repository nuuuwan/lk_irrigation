# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_04:28:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,416 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 04:28:35 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.122 |  |
| 2026-10-13 04:23:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:18:51 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:16:49 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.043 |  |
| 2026-10-13 04:13:57 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:09:53 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-10-13 04:08:02 | Urawa (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.137 |  |
| 2026-10-13 04:08:00 | Pitabeddara (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-13 04:07:17 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:05:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:04:50 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-10-13 04:04:29 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-13 04:03:45 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-10-13 04:03:42 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:03:30 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-10-13 04:03:23 | Panadugama (Nilwala Ganga) | 6.27 | 🟠 Minor Flood | 0.122 | 🔺 Rising |
| 2026-10-13 04:02:59 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:02:36 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:02:17 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-10-13 04:02:02 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-10-13 04:01:50 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.052 |  |
| 2026-10-13 04:01:39 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:01:15 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-13 04:01:09 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:00:52 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-10-13 04:00:52 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-13 04:00:37 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.037 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 04:03:23 | Panadugama (Nilwala Ganga) | 6.27 | 🟠 Minor Flood | 0.122 | 🔺 Rising |
| 2026-10-13 03:10:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | 0.027 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-13 03:05:18 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-13 04:08:00 | Pitabeddara (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-13 04:01:50 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 04:00:37 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-13 04:00:52 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-13 04:04:29 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:02:36 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:23:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:01:39 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:13:57 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:11:10 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:02:59 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:18:51 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:03:42 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:05:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:01:09 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:07:54 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:28:15 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:07:45 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.005 |  |
| 2026-10-13 03:02:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.005 |  |
| 2026-10-13 03:06:27 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-10-13 04:02:17 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-10-13 04:03:30 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-10-13 04:01:15 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-13 04:02:02 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-10-13 04:09:53 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-10-13 04:03:45 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-10-13 04:04:50 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-10-13 04:16:49 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.043 |  |
| 2026-10-13 04:00:52 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-10-13 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.052 |  |
| 2026-10-13 04:28:35 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.122 |  |
| 2026-10-13 04:08:02 | Urawa (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)