# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_07:04:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,843 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 07:04:27 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.066 |  |
| 2026-11-27 07:04:10 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -324.000 |  |
| 2026-11-27 07:04:10 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.149 |  |
| 2026-11-27 07:04:08 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | -324.000 |  |
| 2026-11-27 07:03:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-27 07:03:45 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-27 07:02:47 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-27 07:02:46 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-27 07:02:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.150 |  |
| 2026-11-27 07:02:19 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-27 07:02:11 | Kuda Oya (Kirindi Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:01:52 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:01:50 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.108 |  |
| 2026-11-27 07:01:27 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.002 |  |
| 2026-11-27 07:01:09 | Thanamalwila (Kirindi Oya) | 2.55 | 🟢 Normal | -0.084 |  |
| 2026-11-27 07:00:58 | Moragaswewa (Deduru Oya) | 3.57 | 🟢 Normal | -0.030 |  |
| 2026-11-27 07:00:48 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-27 07:00:38 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.139 |  |
| 2026-11-27 07:00:18 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.083 |  |
| 2026-11-27 06:26:13 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 07:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-27 07:03:45 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-27 06:03:07 | Moraketiya (Walawe Ganga) | 3.98 | 🟡 Alert | -0.048 |  |
| 2026-11-27 07:01:50 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.108 |  |
| 2026-11-27 07:02:46 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-27 07:00:48 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-27 06:03:03 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-27 06:03:55 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-27 06:08:57 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-27 06:04:30 | Badalgama (Maha Oya) | 4.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-27 06:14:14 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 06:01:43 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 05:46:21 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:02:19 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:01:52 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-27 06:07:31 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:02:11 | Kuda Oya (Kirindi Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:01:27 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.002 |  |
| 2026-11-27 07:03:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-27 06:02:25 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | -0.010 |  |
| 2026-11-27 07:02:47 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-27 06:05:09 | Thawalama (Gin Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-11-27 06:02:04 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.022 |  |
| 2026-11-27 07:00:58 | Moragaswewa (Deduru Oya) | 3.57 | 🟢 Normal | -0.030 |  |
| 2026-11-27 06:00:26 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.044 |  |
| 2026-11-27 06:02:29 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.049 |  |
| 2026-11-27 06:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.049 |  |
| 2026-11-27 06:04:53 | Giriulla (Maha Oya) | 4.34 | 🟢 Normal | -0.058 |  |
| 2026-11-27 07:04:27 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.066 |  |
| 2026-11-27 06:03:00 | Katharagama (Menik Ganga) | 0.44 | 🟢 Normal | -0.069 |  |
| 2026-11-27 06:03:00 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.072 |  |
| 2026-11-27 07:00:18 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.083 |  |
| 2026-11-27 07:01:09 | Thanamalwila (Kirindi Oya) | 2.55 | 🟢 Normal | -0.084 |  |
| 2026-11-27 07:00:38 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.139 |  |
| 2026-11-27 07:04:10 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.149 |  |
| 2026-11-27 07:02:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.150 |  |
| 2026-11-27 06:03:13 | Siyambalanduwa (Heda Oya) | 1.82 | 🟢 Normal | -0.369 |  |
| 2026-11-27 06:09:11 | Padiyathalawa (Maduru Oya) | 1.24 | 🟢 Normal | -216.000 |  |
| 2026-11-27 07:04:10 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)