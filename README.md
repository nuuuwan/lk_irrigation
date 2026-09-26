# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_09:08:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 09:08:37 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | -0.100 |  |
| 2026-09-26 09:08:00 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:07:41 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:06:58 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-26 09:06:20 | Glencourse (Kelani Ganga) | 13.25 | 🟢 Normal | -0.085 |  |
| 2026-09-26 09:06:07 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.088 |  |
| 2026-09-26 09:05:22 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:05:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 09:04:21 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:04:21 | Hanwella (Kelani Ganga) | 5.67 | 🟢 Normal | -0.049 |  |
| 2026-09-26 09:04:17 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:04:17 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.059 |  |
| 2026-09-26 09:04:08 | Pitabeddara (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-09-26 09:03:46 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:03:38 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-26 09:03:32 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:03:30 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:03:23 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:03:21 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | -0.011 |  |
| 2026-09-26 09:03:05 | Nawalapitiya (Mahaweli Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 09:02:39 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.215 |  |
| 2026-09-26 09:02:36 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 09:02:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:02:17 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-26 09:01:59 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-09-26 09:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:01:22 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-09-26 09:01:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:00:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:00:50 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.031 |  |
| 2026-09-26 09:00:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:00:18 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.061 |  |
| 2026-09-26 08:57:31 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:27:26 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 08:11:48 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 09:02:36 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 09:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 09:06:58 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-26 09:06:07 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.088 |  |
| 2026-09-26 08:04:53 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-26 09:03:38 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-26 09:02:17 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-26 09:03:05 | Nawalapitiya (Mahaweli Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 09:00:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:08 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:03:23 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:01:09 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:07:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:04:21 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:00:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:04:17 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:05:22 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:03:30 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:07:41 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:02:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:00:18 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 09:05:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:03:46 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:03:32 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:08:00 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:02:21 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-26 09:03:21 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | -0.011 |  |
| 2026-09-26 09:04:08 | Pitabeddara (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-09-26 09:00:50 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.031 |  |
| 2026-09-26 09:01:22 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-09-26 09:01:59 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-09-26 09:04:21 | Hanwella (Kelani Ganga) | 5.67 | 🟢 Normal | -0.049 |  |
| 2026-09-26 09:04:17 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.059 |  |
| 2026-09-26 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.061 |  |
| 2026-09-26 09:06:20 | Glencourse (Kelani Ganga) | 13.25 | 🟢 Normal | -0.085 |  |
| 2026-09-26 09:08:37 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | -0.100 |  |
| 2026-09-26 09:02:39 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)