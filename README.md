# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_18:02:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 18:02:47 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:46 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | -0.032 |  |
| 2026-10-31 18:02:41 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:02:41 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:02:37 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.024 |  |
| 2026-10-31 18:02:25 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:24 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:56 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.052 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:01:48 | Thalgahagoda (Nilwala Ganga) | 1.58 | 🟡 Alert | -0.010 |  |
| 2026-10-31 18:01:45 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.084 |  |
| 2026-10-31 18:01:37 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 18:01:33 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:23 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.093 |  |
| 2026-10-31 18:01:11 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:09 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:01:08 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.041 |  |
| 2026-10-31 18:00:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:20 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-10-31 18:00:13 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-10-31 17:45:06 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 18:01:48 | Thalgahagoda (Nilwala Ganga) | 1.58 | 🟡 Alert | -0.010 |  |
| 2026-10-31 18:01:37 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 17:01:31 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 17:10:23 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-31 18:00:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:00:37 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:47 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:03:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:10:31 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:05:59 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:02:41 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:01:09 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:02:08 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:03:46 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-31 17:05:30 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:33 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:08:09 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:05:34 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:24 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-31 17:12:25 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:47 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:11 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:25 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:13 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:00:20 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-10-31 18:02:41 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:02:37 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.024 |  |
| 2026-10-31 17:09:01 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.027 |  |
| 2026-10-31 17:03:11 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-10-31 18:02:46 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | -0.032 |  |
| 2026-10-31 18:01:08 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.041 |  |
| 2026-10-31 18:01:56 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.052 |  |
| 2026-10-31 18:01:45 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.084 |  |
| 2026-10-31 17:05:43 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.092 |  |
| 2026-10-31 18:01:23 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.093 |  |
| 2026-10-31 17:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)