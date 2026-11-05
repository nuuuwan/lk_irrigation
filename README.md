# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_07:13:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,299 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 07:13:29 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-05 07:12:19 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | -0.057 |  |
| 2026-11-05 07:08:49 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-05 07:08:13 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.074 |  |
| 2026-11-05 07:06:54 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:06:50 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.055 |  |
| 2026-11-05 07:05:47 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | -0.028 |  |
| 2026-11-05 07:05:41 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.029 |  |
| 2026-11-05 07:05:35 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.039 |  |
| 2026-11-05 07:04:50 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:04:49 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:04:38 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.039 |  |
| 2026-11-05 07:04:27 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 07:04:11 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.058 |  |
| 2026-11-05 07:04:11 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-11-05 07:03:35 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 07:03:33 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 07:03:30 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 07:03:29 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-05 07:03:16 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-11-05 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-05 07:03:08 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-11-05 07:03:07 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:02:59 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-11-05 07:02:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:02:42 | Thanamalwila (Kirindi Oya) | 2.30 | 🟢 Normal | -0.072 |  |
| 2026-11-05 07:02:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:01:45 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:01:45 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.148 |  |
| 2026-11-05 07:01:40 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.149 |  |
| 2026-11-05 07:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-05 07:01:36 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-05 07:01:36 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-05 07:01:31 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.122 |  |
| 2026-11-05 07:01:13 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-05 07:01:06 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 07:00:20 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.043 |  |
| 2026-11-05 07:00:12 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 07:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-05 07:02:59 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-11-05 07:13:29 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-05 07:00:12 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-05 07:03:35 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-05 07:01:06 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 07:04:27 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 07:01:36 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-05 07:08:49 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-05 07:03:07 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:02:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:03:29 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:02:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:04:50 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:18:36 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:06:54 | Kuda Oya (Kirindi Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 07:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-05 07:03:30 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 07:01:36 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-05 06:07:02 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-05 07:03:08 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-11-05 07:01:13 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-05 07:03:16 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-11-05 07:05:47 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | -0.028 |  |
| 2026-11-05 07:05:41 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.029 |  |
| 2026-11-05 07:04:11 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-11-05 07:03:33 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 07:05:35 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.039 |  |
| 2026-11-05 07:04:38 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.039 |  |
| 2026-11-05 07:00:20 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.043 |  |
| 2026-11-05 07:06:50 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.055 |  |
| 2026-11-05 07:12:19 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | -0.057 |  |
| 2026-11-05 07:04:11 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.058 |  |
| 2026-11-05 07:02:42 | Thanamalwila (Kirindi Oya) | 2.30 | 🟢 Normal | -0.072 |  |
| 2026-11-05 07:08:13 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.074 |  |
| 2026-11-05 07:01:31 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.122 |  |
| 2026-11-05 07:01:45 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.148 |  |
| 2026-11-05 07:01:40 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)