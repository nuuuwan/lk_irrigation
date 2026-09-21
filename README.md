# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_05:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 05:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:19 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.122 |  |
| 2026-09-22 05:03:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.119 |  |
| 2026-09-22 05:02:53 | Siyambalanduwa (Heda Oya) | 0.00 | 🟢 Normal | -0.157 |  |
| 2026-09-22 05:02:45 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:02:16 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | -0.102 |  |
| 2026-09-22 05:02:15 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-22 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-09-22 05:01:44 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:31 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.005 |  |
| 2026-09-22 05:01:22 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-22 05:01:21 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:00:59 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.000 |  |
| 2026-09-22 05:00:51 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.045 |  |
| 2026-09-22 05:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:00:34 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.000 |  |
| 2026-09-22 05:00:10 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.081 |  |
| 2026-09-22 04:36:09 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.013 |  |
| 2026-09-22 04:34:05 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 04:19:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 04:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.19 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 04:09:24 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-22 05:00:59 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.000 |  |
| 2026-09-22 04:34:05 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 04:08:44 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | -0.036 |  |
| 2026-09-22 04:11:46 | Holombuwa (Kelani Ganga) | 2.24 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-22 04:06:03 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-22 05:01:22 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-22 04:08:15 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 05:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:02:45 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:07:14 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:02:58 | Ellagawa (Kalu Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:21 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:44 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:01:31 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.005 |  |
| 2026-09-22 04:03:16 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-09-22 03:06:19 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-09-22 04:36:09 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.013 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-22 05:01:51 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-09-22 04:08:11 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.027 |  |
| 2026-09-22 05:02:15 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-22 05:00:51 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.045 |  |
| 2026-09-22 04:00:32 | Peradeniya (Mahaweli Ganga) | 4.32 | 🟢 Normal | -0.061 |  |
| 2026-09-22 03:09:15 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.074 |  |
| 2026-09-22 05:00:10 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.081 |  |
| 2026-09-22 05:02:16 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | -0.102 |  |
| 2026-09-22 04:03:58 | Glencourse (Kelani Ganga) | 12.32 | 🟢 Normal | -0.119 |  |
| 2026-09-22 05:03:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.119 |  |
| 2026-09-22 05:03:19 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.122 |  |
| 2026-09-22 05:02:53 | Siyambalanduwa (Heda Oya) | 0.00 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)