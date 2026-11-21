# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_07:21:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 07:21:42 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.002 |  |
| 2026-11-21 07:14:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:14:09 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-21 07:10:03 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-21 07:08:58 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:08:51 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.059 |  |
| 2026-11-21 07:08:34 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 07:08:10 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:07:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:07:01 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.071 |  |
| 2026-11-21 07:06:50 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-21 07:05:51 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-21 07:05:47 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.002 |  |
| 2026-11-21 07:05:47 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-21 07:05:29 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-21 07:05:14 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-11-21 07:04:59 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-21 07:04:32 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:04:14 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 07:04:04 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-11-21 07:03:55 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.062 |  |
| 2026-11-21 07:03:43 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.083 |  |
| 2026-11-21 07:03:36 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-21 07:03:27 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.677 |  |
| 2026-11-21 07:03:15 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-21 07:03:01 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-21 07:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-21 07:02:54 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-21 07:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.041 |  |
| 2026-11-21 07:02:31 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.118 |  |
| 2026-11-21 07:01:56 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:24 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 07:01:24 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-21 07:01:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:07 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-21 07:00:46 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-21 07:00:43 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:43 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:07 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 07:04:04 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-11-21 07:03:15 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-11-21 07:02:54 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-21 07:03:01 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-21 07:05:51 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-21 07:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-21 07:01:07 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-21 07:06:50 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-21 07:04:14 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 07:01:24 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 07:05:29 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-21 07:00:07 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 07:05:47 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-21 07:14:09 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-21 07:08:34 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 07:00:46 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-21 07:21:42 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.002 |  |
| 2026-11-21 07:05:47 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.002 |  |
| 2026-11-21 07:00:43 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:00:43 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:56 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:07:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:04:32 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:01:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:14:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:08:58 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 07:10:03 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-21 07:01:24 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-21 07:04:59 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-21 07:05:14 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-11-21 07:03:36 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-11-21 07:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.041 |  |
| 2026-11-21 07:08:51 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.059 |  |
| 2026-11-21 07:03:55 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.062 |  |
| 2026-11-21 07:07:01 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.071 |  |
| 2026-11-21 07:03:43 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.083 |  |
| 2026-11-21 07:02:31 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.118 |  |
| 2026-11-21 07:03:27 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.677 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)