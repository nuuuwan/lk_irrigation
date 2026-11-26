# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_15:24:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 15:24:41 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.021 |  |
| 2026-11-26 15:20:12 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:17:51 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-11-26 15:15:57 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:14:41 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-11-26 15:14:01 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -36.000 |  |
| 2026-11-26 15:14:00 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -36.000 |  |
| 2026-11-26 15:13:59 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -36.000 |  |
| 2026-11-26 15:11:54 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 15:11:18 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-26 15:09:33 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.028 |  |
| 2026-11-26 15:08:52 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.101 |  |
| 2026-11-26 15:07:31 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:06:25 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:05:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:04:58 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-11-26 15:04:44 | Galgamuwa (Mee Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-26 15:04:11 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-26 15:03:49 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-26 15:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-11-26 15:03:20 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:03:05 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:02:53 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.063 |  |
| 2026-11-26 15:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.020 |  |
| 2026-11-26 15:02:43 | Moragaswewa (Deduru Oya) | 4.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-26 15:02:41 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.045 |  |
| 2026-11-26 15:02:40 | Giriulla (Maha Oya) | 2.81 | 🟢 Normal | -0.072 |  |
| 2026-11-26 15:02:38 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.657 | 🔺 Rising |
| 2026-11-26 15:02:26 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-26 15:02:25 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-11-26 15:02:23 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.101 |  |
| 2026-11-26 15:02:20 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 15:02:13 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:01:56 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.079 |  |
| 2026-11-26 15:01:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-26 15:01:48 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.101 |  |
| 2026-11-26 15:01:44 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:01:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:01:20 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:00:35 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:00:12 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 15:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.020 |  |
| 2026-11-26 15:01:48 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.101 |  |
| 2026-11-26 15:02:38 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.657 | 🔺 Rising |
| 2026-11-26 15:03:49 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-26 15:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-11-26 14:06:24 | Moraketiya (Walawe Ganga) | 2.50 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-11-26 15:02:26 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-26 15:02:43 | Moragaswewa (Deduru Oya) | 4.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-26 15:11:18 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-26 15:01:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-26 15:00:12 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 15:02:20 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 15:11:54 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 15:00:35 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:01:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:06:25 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:20:12 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:01:44 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:05:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:07:31 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:03:05 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:01:20 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:15:57 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:02:13 | Thanamalwila (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-26 15:17:51 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-11-26 15:14:41 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-11-26 15:04:58 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-11-26 15:04:44 | Galgamuwa (Mee Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-26 15:04:11 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-26 15:24:41 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.021 |  |
| 2026-11-26 15:02:25 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-11-26 15:09:33 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.028 |  |
| 2026-11-26 15:02:41 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.045 |  |
| 2026-11-26 15:02:53 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.063 |  |
| 2026-11-26 15:02:40 | Giriulla (Maha Oya) | 2.81 | 🟢 Normal | -0.072 |  |
| 2026-11-26 15:01:56 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.079 |  |
| 2026-11-26 15:02:23 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | -0.101 |  |
| 2026-11-26 15:08:52 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.101 |  |
| 2026-11-26 15:14:01 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)