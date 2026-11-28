# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_16:13:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **328,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 16:13:40 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.062 |  |
| 2026-11-28 16:13:24 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.035 |  |
| 2026-11-28 16:11:42 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.066 |  |
| 2026-11-28 16:10:45 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-11-28 16:09:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-28 16:08:22 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-11-28 16:07:52 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-11-28 16:07:42 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.107 |  |
| 2026-11-28 16:07:23 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:07:15 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:06:53 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | -0.029 |  |
| 2026-11-28 16:06:46 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.028 |  |
| 2026-11-28 16:06:41 | Panadugama (Nilwala Ganga) | 5.17 | 🟡 Alert | -0.020 |  |
| 2026-11-28 16:06:05 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.048 |  |
| 2026-11-28 16:05:41 | Weraganthota (Mahaweli Ganga) | -1.68 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-11-28 16:05:32 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-28 16:05:15 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:04:54 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.029 |  |
| 2026-11-28 16:04:51 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.029 |  |
| 2026-11-28 16:04:30 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-28 16:04:07 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | 0.913 | 🔺 Rising |
| 2026-11-28 16:04:01 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:03:57 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.029 |  |
| 2026-11-28 16:03:19 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-28 16:03:19 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 16:03:10 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-11-28 16:03:09 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | -0.111 |  |
| 2026-11-28 16:02:40 | Moragaswewa (Deduru Oya) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-28 16:02:39 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-28 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-28 16:02:20 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-28 16:02:17 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-28 16:02:08 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.100 |  |
| 2026-11-28 16:01:58 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:01:49 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-28 16:01:10 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:00:59 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 16:06:41 | Panadugama (Nilwala Ganga) | 5.17 | 🟡 Alert | -0.020 |  |
| 2026-11-28 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-28 16:06:53 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | -0.029 |  |
| 2026-11-28 16:04:51 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.029 |  |
| 2026-11-28 16:04:07 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | 0.913 | 🔺 Rising |
| 2026-11-28 16:05:41 | Weraganthota (Mahaweli Ganga) | -1.68 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-11-28 16:04:30 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-28 16:03:19 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-28 16:09:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-28 16:03:19 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 16:05:32 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-28 16:01:58 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:05:15 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:07:23 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:04:01 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:01:49 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:01:10 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:07:15 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 16:07:52 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-11-28 16:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-28 16:02:39 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-28 16:02:20 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-28 16:10:45 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-11-28 16:08:22 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-11-28 16:02:40 | Moragaswewa (Deduru Oya) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-28 16:00:59 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-28 16:02:17 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-11-28 16:06:46 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.028 |  |
| 2026-11-28 16:04:54 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.029 |  |
| 2026-11-28 16:03:57 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.029 |  |
| 2026-11-28 16:03:10 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-11-28 16:13:24 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.035 |  |
| 2026-11-28 16:06:05 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.048 |  |
| 2026-11-28 16:13:40 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.062 |  |
| 2026-11-28 16:11:42 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.066 |  |
| 2026-11-28 16:02:08 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.100 |  |
| 2026-11-28 16:07:42 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.107 |  |
| 2026-11-28 16:03:09 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)