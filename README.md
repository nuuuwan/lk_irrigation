# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_06:24:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 06:24:55 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:19:42 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-11-05 06:18:36 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:10:50 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:09:56 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:09:35 | Moraketiya (Walawe Ganga) | 2.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-05 06:09:32 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.028 |  |
| 2026-11-05 06:09:21 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:08:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:07:02 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-05 06:06:23 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:04:56 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-05 06:04:36 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-11-05 06:04:22 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.201 |  |
| 2026-11-05 06:04:21 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-11-05 06:04:11 | Thanamalwila (Kirindi Oya) | 2.37 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-05 06:04:03 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-05 06:03:34 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-11-05 06:03:30 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.031 |  |
| 2026-11-05 06:03:23 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:03:14 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:03:10 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.049 |  |
| 2026-11-05 06:02:48 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.091 |  |
| 2026-11-05 06:02:45 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 06:02:28 | Urawa (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.367 |  |
| 2026-11-05 06:02:24 | Dunamale (Aththanagalu Oya) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-11-05 06:02:17 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.100 |  |
| 2026-11-05 06:01:44 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-11-05 06:01:19 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | -0.200 |  |
| 2026-11-05 06:01:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:01:11 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-11-05 06:01:10 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-05 06:01:02 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-05 06:01:00 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.013 |  |
| 2026-11-05 06:00:34 | Moragaswewa (Deduru Oya) | 3.73 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 05:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | 0.000 |  |
| 2026-11-05 06:19:42 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-11-05 06:04:56 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-05 06:04:11 | Thanamalwila (Kirindi Oya) | 2.37 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-05 06:04:03 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-05 06:09:35 | Moraketiya (Walawe Ganga) | 2.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-05 06:01:02 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-05 06:02:45 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 06:03:14 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:01:00 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:06:23 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:03:23 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:09:56 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:24:55 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:09:21 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:08:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:01:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:18:36 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 06:01:10 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-05 06:04:21 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-11-05 06:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.013 |  |
| 2026-11-05 06:03:34 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-11-05 06:07:02 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-05 06:04:36 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-11-05 06:09:32 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.028 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 06:01:44 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-11-05 06:02:24 | Dunamale (Aththanagalu Oya) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-11-05 06:03:30 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.031 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 06:03:10 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.049 |  |
| 2026-11-05 06:01:11 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-11-05 06:00:34 | Moragaswewa (Deduru Oya) | 3.73 | 🟢 Normal | -0.064 |  |
| 2026-11-05 06:02:48 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.091 |  |
| 2026-11-05 06:02:17 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.100 |  |
| 2026-11-05 06:01:19 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | -0.200 |  |
| 2026-11-05 06:04:22 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.201 |  |
| 2026-11-05 06:02:28 | Urawa (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.367 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)