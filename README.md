# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_04:05:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,447 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 04:05:14 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.059 |  |
| 2026-10-23 04:04:57 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:03:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:03:24 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-10-23 04:03:20 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | -0.052 |  |
| 2026-10-23 04:03:13 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-10-23 04:03:07 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:03:02 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:02:43 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 04:02:43 | Glencourse (Kelani Ganga) | 12.06 | 🟢 Normal | -0.098 |  |
| 2026-10-23 04:02:26 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:02:19 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 04:02:01 | Moragaswewa (Deduru Oya) | 5.30 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-23 04:02:00 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 04:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.413 | 🔺 Rising |
| 2026-10-23 04:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 04:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:01:39 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-10-23 04:01:29 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:01:19 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:01:13 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-10-23 04:01:09 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.113 |  |
| 2026-10-23 04:01:05 | Rathnapura (Kalu Ganga) | 4.41 | 🟢 Normal | -0.088 |  |
| 2026-10-23 04:01:03 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:00:43 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-23 04:00:24 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 04:02:01 | Moragaswewa (Deduru Oya) | 5.30 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-23 04:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.413 | 🔺 Rising |
| 2026-10-23 03:05:12 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-23 03:05:01 | Badalgama (Maha Oya) | 3.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-23 04:02:19 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 04:00:43 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-23 04:02:43 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 04:02:00 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 04:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 03:10:20 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-23 04:00:24 | Magura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 04:01:19 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:01:29 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:04:57 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:03:07 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:02:56 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:03:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:00:24 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:02:26 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-23 04:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:01:03 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:03:02 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-23 04:01:13 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-10-23 04:03:13 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-10-23 03:07:00 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-10-23 04:03:24 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-10-23 04:01:39 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-10-23 03:09:40 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.023 |  |
| 2026-10-23 03:07:32 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.031 |  |
| 2026-10-23 04:03:20 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | -0.052 |  |
| 2026-10-23 04:05:14 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.059 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-23 03:06:37 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.075 |  |
| 2026-10-23 03:13:45 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.078 |  |
| 2026-10-23 04:01:05 | Rathnapura (Kalu Ganga) | 4.41 | 🟢 Normal | -0.088 |  |
| 2026-10-23 04:02:43 | Glencourse (Kelani Ganga) | 12.06 | 🟢 Normal | -0.098 |  |
| 2026-10-23 04:01:09 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)