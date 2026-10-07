# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_13:14:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,388 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 13:14:03 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.064 |  |
| 2026-10-07 13:10:09 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-10-07 13:10:07 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:08:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-10-07 13:08:08 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.084 |  |
| 2026-10-07 13:06:43 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-10-07 13:06:41 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:05:32 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-10-07 13:05:29 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.025 |  |
| 2026-10-07 13:05:04 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-07 13:05:01 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.031 |  |
| 2026-10-07 13:04:54 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-10-07 13:03:38 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-07 13:03:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:03:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:03:25 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-07 13:03:15 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 13:03:11 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:02:51 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-10-07 13:02:48 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:02:43 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.011 |  |
| 2026-10-07 13:02:39 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:02:37 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-07 13:02:22 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.041 |  |
| 2026-10-07 13:02:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 13:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.102 |  |
| 2026-10-07 13:01:53 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.031 |  |
| 2026-10-07 13:01:25 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-10-07 13:01:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:01:21 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:01:16 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:00:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:00:54 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:00:42 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-10-07 13:00:37 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 13:08:08 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.084 |  |
| 2026-10-07 13:03:38 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-07 13:03:15 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 13:02:13 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 13:01:21 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:01:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:02:39 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:02:48 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:06:41 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:00:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:03:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:03:11 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:03:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:00:54 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:01:16 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-07 13:10:07 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 12:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.005 |  |
| 2026-10-07 13:08:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-10-07 13:10:09 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-10-07 13:03:25 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-07 13:06:43 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-10-07 13:02:37 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-07 13:02:43 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.011 |  |
| 2026-10-07 12:06:24 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-07 13:01:25 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-10-07 13:05:04 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-07 13:02:51 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-10-07 13:05:29 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.025 |  |
| 2026-10-07 13:00:37 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.030 |  |
| 2026-10-07 13:05:01 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.031 |  |
| 2026-10-07 13:01:53 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.031 |  |
| 2026-10-07 13:00:42 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-10-07 13:05:32 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-10-07 13:02:22 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.041 |  |
| 2026-10-07 12:02:40 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.050 |  |
| 2026-10-07 13:04:54 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-10-07 13:14:03 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.064 |  |
| 2026-10-07 13:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.102 |  |
| 2026-10-07 12:06:58 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)