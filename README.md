# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_14:19:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,570 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 14:19:51 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | -0.034 |  |
| 2026-11-05 14:19:42 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:11:23 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.038 |  |
| 2026-11-05 14:10:27 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.018 |  |
| 2026-11-05 14:09:54 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.038 |  |
| 2026-11-05 14:07:38 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | -0.029 |  |
| 2026-11-05 14:06:58 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.060 |  |
| 2026-11-05 14:05:30 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:05:10 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-11-05 14:04:58 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-05 14:04:42 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.145 |  |
| 2026-11-05 14:04:40 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.095 |  |
| 2026-11-05 14:04:35 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:04:26 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-05 14:04:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:04:10 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.029 |  |
| 2026-11-05 14:03:33 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:03:15 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.055 |  |
| 2026-11-05 14:03:14 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.060 |  |
| 2026-11-05 14:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.030 |  |
| 2026-11-05 14:02:39 | Moragaswewa (Deduru Oya) | 3.45 | 🟢 Normal | -0.039 |  |
| 2026-11-05 14:02:35 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:02:12 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.186 |  |
| 2026-11-05 14:02:09 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-11-05 14:02:03 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:01:57 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-05 14:01:55 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-05 14:01:53 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2026-11-05 14:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:01:41 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 14:01:30 | Thanamalwila (Kirindi Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-11-05 14:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:01:27 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.032 |  |
| 2026-11-05 14:00:50 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:00:45 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.110 |  |
| 2026-11-05 14:00:33 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.036 |  |
| 2026-11-05 13:59:44 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | -0.067 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 14:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.030 |  |
| 2026-11-05 14:04:26 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-05 14:01:55 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-05 14:01:57 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-05 14:01:41 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 14:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:02:35 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:19:42 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:02:03 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:00:50 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:06:58 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:04:58 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-05 14:03:33 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:05:30 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:04:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:04:35 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:10:27 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.018 |  |
| 2026-11-05 13:07:29 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-11-05 14:01:30 | Thanamalwila (Kirindi Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-11-05 14:01:53 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2026-11-05 14:07:38 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | -0.029 |  |
| 2026-11-05 14:04:10 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.029 |  |
| 2026-11-05 14:01:27 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.032 |  |
| 2026-11-05 14:19:51 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | -0.034 |  |
| 2026-11-05 14:00:33 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.036 |  |
| 2026-11-05 14:09:54 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.038 |  |
| 2026-11-05 14:11:23 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.038 |  |
| 2026-11-05 14:02:39 | Moragaswewa (Deduru Oya) | 3.45 | 🟢 Normal | -0.039 |  |
| 2026-11-05 14:03:15 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.055 |  |
| 2026-11-05 14:03:14 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.060 |  |
| 2026-11-05 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.060 |  |
| 2026-11-05 14:02:09 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-11-05 13:59:44 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | -0.067 |  |
| 2026-11-05 14:04:40 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.095 |  |
| 2026-11-05 14:00:45 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.110 |  |
| 2026-11-05 14:04:42 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.145 |  |
| 2026-11-05 14:05:10 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-11-05 14:02:12 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)