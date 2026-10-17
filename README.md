# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_12:11:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 12:11:40 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.105 |  |
| 2026-10-17 12:09:41 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-10-17 12:08:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.005 |  |
| 2026-10-17 12:07:49 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.043 |  |
| 2026-10-17 12:07:12 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -0.047 |  |
| 2026-10-17 12:07:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-10-17 12:07:05 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-10-17 12:06:51 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-10-17 12:06:27 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.042 |  |
| 2026-10-17 12:05:50 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:05:26 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:05:02 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.058 |  |
| 2026-10-17 12:04:49 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.040 |  |
| 2026-10-17 12:04:43 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-17 12:03:46 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.124 |  |
| 2026-10-17 12:03:39 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.069 |  |
| 2026-10-17 12:03:30 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-17 12:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.75 | 🟡 Alert | -0.010 |  |
| 2026-10-17 12:03:12 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-17 12:03:10 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.055 |  |
| 2026-10-17 12:03:03 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-10-17 12:02:55 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.421 |  |
| 2026-10-17 12:02:54 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-10-17 12:02:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-10-17 12:02:28 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-10-17 12:02:22 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 12:02:15 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.137 |  |
| 2026-10-17 12:02:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:02:06 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.021 |  |
| 2026-10-17 12:01:58 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:01:55 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:01:50 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-17 12:01:49 | Thanthirimale (Malwathu Oya) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-17 12:01:41 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-17 12:00:51 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:00:44 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 12:00:44 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:00:36 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 12:00:44 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 12:03:10 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.055 |  |
| 2026-10-17 12:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.75 | 🟡 Alert | -0.010 |  |
| 2026-10-17 12:03:30 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-17 12:01:41 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 12:01:49 | Thanthirimale (Malwathu Oya) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-17 12:02:22 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 12:05:50 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:00:51 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:05:26 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:02:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:01:55 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:00:44 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 12:08:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.005 |  |
| 2026-10-17 12:09:41 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-10-17 12:06:51 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-10-17 12:03:12 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-17 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-17 12:07:05 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-10-17 12:03:03 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-10-17 12:02:54 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-10-17 12:04:43 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-17 12:02:06 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.021 |  |
| 2026-10-17 12:01:50 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-17 12:02:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-10-17 12:07:09 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-10-17 12:04:49 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.040 |  |
| 2026-10-17 12:02:28 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-10-17 12:06:27 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.042 |  |
| 2026-10-17 12:07:49 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.043 |  |
| 2026-10-17 12:07:12 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | -0.047 |  |
| 2026-10-17 12:00:36 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.050 |  |
| 2026-10-17 12:05:02 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.058 |  |
| 2026-10-17 12:03:39 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.069 |  |
| 2026-10-17 12:11:40 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.105 |  |
| 2026-10-17 12:03:46 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.124 |  |
| 2026-10-17 12:02:15 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.137 |  |
| 2026-10-17 12:02:55 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.421 |  |
| 2026-10-17 11:12:04 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)