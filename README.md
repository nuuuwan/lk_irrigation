# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_16:06:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 16:06:40 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:05:55 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-09-15 16:05:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.113 |  |
| 2026-09-15 16:04:28 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 16:03:40 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-09-15 16:03:36 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:03:27 | Hanwella (Kelani Ganga) | 2.49 | 🟢 Normal | -0.100 |  |
| 2026-09-15 16:03:27 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.116 |  |
| 2026-09-15 16:03:22 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:03:15 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:03:08 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:03:02 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-09-15 16:02:58 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-09-15 16:02:56 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:02:51 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 16:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:02:44 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | -0.040 |  |
| 2026-09-15 16:02:35 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 16:02:19 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:02:14 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:02:04 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:13 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:04 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 16:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 15:04:10 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.108 |  |
| 2026-09-15 16:05:55 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-09-15 15:09:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-15 15:06:49 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-15 16:02:51 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 16:01:04 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 16:02:35 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 16:04:28 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 15:03:59 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:03:08 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:09:10 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:02:04 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:06:40 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:03:22 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:02:19 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:03:36 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:13 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:02:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:01:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:01:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-15 15:08:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-09-15 16:03:15 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:02:14 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:02:56 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:03:02 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-09-15 16:03:40 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-09-15 16:02:58 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-09-15 15:07:21 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.029 |  |
| 2026-09-15 15:07:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-09-15 16:02:44 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | -0.040 |  |
| 2026-09-15 16:03:27 | Hanwella (Kelani Ganga) | 2.49 | 🟢 Normal | -0.100 |  |
| 2026-09-15 16:05:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.113 |  |
| 2026-09-15 16:03:27 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.116 |  |
| 2026-09-15 15:04:40 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.132 |  |
| 2026-09-15 15:02:43 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.134 |  |
| 2026-09-15 15:02:59 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)