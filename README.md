# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_08:15:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 08:15:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.017 |  |
| 2026-11-07 08:13:39 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.017 |  |
| 2026-11-07 08:11:57 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:11:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-11-07 08:10:44 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.019 |  |
| 2026-11-07 08:09:31 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.111 |  |
| 2026-11-07 08:07:11 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.068 |  |
| 2026-11-07 08:06:52 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -36.000 |  |
| 2026-11-07 08:06:51 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -36.000 |  |
| 2026-11-07 08:06:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:06:29 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 08:05:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-11-07 08:05:47 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-07 08:05:47 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.115 |  |
| 2026-11-07 08:05:32 | Holombuwa (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-07 08:05:02 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:04:55 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.066 |  |
| 2026-11-07 08:04:52 | Moraketiya (Walawe Ganga) | 1.97 | 🟢 Normal | -0.086 |  |
| 2026-11-07 08:04:37 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-11-07 08:04:27 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.102 |  |
| 2026-11-07 08:03:59 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 08:03:57 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | -0.211 |  |
| 2026-11-07 08:03:51 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 08:03:48 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-07 08:03:37 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.029 |  |
| 2026-11-07 08:03:18 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:03:16 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-07 08:03:01 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | -0.210 |  |
| 2026-11-07 08:02:58 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.049 |  |
| 2026-11-07 08:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.010 |  |
| 2026-11-07 08:02:33 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:02:33 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-07 08:02:23 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:02:07 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-07 08:01:59 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-07 08:01:49 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:01:34 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:00:08 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 08:04:37 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.000 |  |
| 2026-11-07 08:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.010 |  |
| 2026-11-07 08:03:59 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 08:06:29 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 08:03:51 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 08:05:47 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-07 08:02:23 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:01:49 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:05:02 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 08:06:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:11:57 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:11:47 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:01:34 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-07 08:03:48 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-07 08:05:32 | Holombuwa (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-07 08:03:16 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-07 08:00:08 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-11-07 08:02:07 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-11-07 08:15:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.017 |  |
| 2026-11-07 08:13:39 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.017 |  |
| 2026-11-07 08:10:44 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.019 |  |
| 2026-11-07 08:11:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-11-07 08:03:18 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:02:33 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-07 08:01:59 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-07 08:03:37 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.029 |  |
| 2026-11-07 08:02:33 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-07 08:02:58 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.049 |  |
| 2026-11-07 08:05:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-11-07 08:04:55 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.066 |  |
| 2026-11-07 08:07:11 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.068 |  |
| 2026-11-07 08:04:52 | Moraketiya (Walawe Ganga) | 1.97 | 🟢 Normal | -0.086 |  |
| 2026-11-07 08:04:27 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.102 |  |
| 2026-11-07 08:09:31 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.111 |  |
| 2026-11-07 08:05:47 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.115 |  |
| 2026-11-07 08:03:01 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | -0.210 |  |
| 2026-11-07 08:03:57 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | -0.211 |  |
| 2026-11-07 08:06:52 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)