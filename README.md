# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_05:04:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,478 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 05:04:59 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-23 05:04:51 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.030 |  |
| 2026-10-23 05:04:17 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-23 05:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:04:02 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.079 |  |
| 2026-10-23 05:03:55 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:03:48 | Glencourse (Kelani Ganga) | 11.97 | 🟢 Normal | -0.088 |  |
| 2026-10-23 05:03:15 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:03:15 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.050 |  |
| 2026-10-23 05:03:03 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-23 05:02:52 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:02:46 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:02:46 | Moragaswewa (Deduru Oya) | 5.05 | 🟡 Alert | -0.247 |  |
| 2026-10-23 05:02:36 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.040 |  |
| 2026-10-23 05:02:07 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:01:56 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.099 |  |
| 2026-10-23 05:01:43 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.170 |  |
| 2026-10-23 05:01:40 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 05:01:26 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:01:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:00:46 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 05:00:21 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 05:00:21 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:38:24 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 05:02:46 | Moragaswewa (Deduru Oya) | 5.05 | 🟡 Alert | -0.247 |  |
| 2026-10-23 04:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.413 | 🔺 Rising |
| 2026-10-23 05:03:03 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-23 04:15:35 | Holombuwa (Kelani Ganga) | 1.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 04:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 05:01:40 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 05:04:59 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-23 04:08:26 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-23 04:38:24 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-23 05:00:21 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 05:00:46 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 05:01:26 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:02:46 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:01:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:00:21 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:00:24 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:02:07 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-23 05:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:03:55 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:02:52 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:06:14 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.010 |  |
| 2026-10-23 05:03:15 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:03:02 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:07:30 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-10-23 05:04:17 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-23 05:04:51 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.030 |  |
| 2026-10-23 04:15:01 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.035 |  |
| 2026-10-23 05:02:36 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.040 |  |
| 2026-10-23 05:03:15 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.050 |  |
| 2026-10-23 04:03:20 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | -0.052 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-23 05:04:02 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.079 |  |
| 2026-10-23 04:09:41 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.087 |  |
| 2026-10-23 05:03:48 | Glencourse (Kelani Ganga) | 11.97 | 🟢 Normal | -0.088 |  |
| 2026-10-23 04:01:05 | Rathnapura (Kalu Ganga) | 4.41 | 🟢 Normal | -0.088 |  |
| 2026-10-23 05:01:56 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.099 |  |
| 2026-10-23 05:01:43 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)