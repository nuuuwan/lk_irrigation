# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_10:03:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,103 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 10:03:51 | Giriulla (Maha Oya) | 2.86 | 🟢 Normal | -0.089 |  |
| 2026-11-08 10:03:27 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 10:02:34 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | -0.120 |  |
| 2026-11-08 10:02:19 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-08 10:02:11 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.064 |  |
| 2026-11-08 10:02:04 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:02:00 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 10:02:00 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 10:01:54 | Moragaswewa (Deduru Oya) | 2.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-08 10:01:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-11-08 10:01:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:38 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-08 10:01:32 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-11-08 10:01:22 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:16 | Pitabeddara (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.107 |  |
| 2026-11-08 10:01:05 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:00:55 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 09:04:21 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.039 |  |
| 2026-11-08 09:13:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-11-08 09:05:40 | Dunamale (Aththanagalu Oya) | 3.67 | 🟡 Alert | -0.030 |  |
| 2026-11-08 09:11:13 | Magura (Kalu Ganga) | 4.12 | 🟡 Alert | -0.084 |  |
| 2026-11-08 09:04:22 | Moraketiya (Walawe Ganga) | 3.27 | 🟡 Alert | -0.102 |  |
| 2026-11-08 09:01:59 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 10:01:54 | Moragaswewa (Deduru Oya) | 2.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-08 09:16:50 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-08 10:02:00 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 10:03:27 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 09:08:08 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 09:00:41 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 10:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:00:55 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 09:04:57 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:22 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:02:04 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:05 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-08 09:05:22 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-11-08 09:02:59 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-08 10:02:19 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-08 10:02:00 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 10:01:32 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-11-08 09:08:06 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-11-08 09:03:47 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-11-08 10:01:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-11-08 10:01:38 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-08 09:08:23 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.045 |  |
| 2026-11-08 09:02:08 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-11-08 09:02:20 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.051 |  |
| 2026-11-08 09:03:37 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.051 |  |
| 2026-11-08 09:05:14 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.057 |  |
| 2026-11-08 10:02:11 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.064 |  |
| 2026-11-08 10:03:51 | Giriulla (Maha Oya) | 2.86 | 🟢 Normal | -0.089 |  |
| 2026-11-08 10:01:16 | Pitabeddara (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.107 |  |
| 2026-11-08 09:04:33 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.118 |  |
| 2026-11-08 10:02:34 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | -0.120 |  |
| 2026-11-08 09:05:55 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)