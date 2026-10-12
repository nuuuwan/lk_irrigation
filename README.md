# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_14:16:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,918 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 14:16:36 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.035 |  |
| 2026-10-12 14:14:19 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:12:04 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:11:56 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-12 14:10:25 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:09:18 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.019 |  |
| 2026-10-12 14:08:30 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:08:12 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-10-12 14:07:37 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.062 |  |
| 2026-10-12 14:07:34 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | -0.047 |  |
| 2026-10-12 14:07:26 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:05:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 14:05:48 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-12 14:05:32 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.032 |  |
| 2026-10-12 14:05:20 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-12 14:04:27 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.058 |  |
| 2026-10-12 14:04:16 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:04:07 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 14:03:47 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:03:40 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:03:26 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.059 |  |
| 2026-10-12 14:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | -0.030 |  |
| 2026-10-12 14:03:20 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:02:54 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:02:45 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.054 |  |
| 2026-10-12 14:02:42 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:02:40 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-12 14:02:34 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | -0.060 |  |
| 2026-10-12 14:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:02:24 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-12 14:02:22 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-10-12 14:01:55 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.041 |  |
| 2026-10-12 14:01:52 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:01:43 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-12 14:01:42 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:01:24 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:01:13 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:00:46 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-12 14:00:10 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:59:00 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 14:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | -0.030 |  |
| 2026-10-12 14:05:48 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-12 14:01:43 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-12 14:00:46 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-12 14:05:20 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-12 14:11:56 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-12 14:04:07 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 14:05:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 14:00:10 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:01:52 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:01:42 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:12:04 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:07:26 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:14:19 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:02:42 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:08:30 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-12 14:03:40 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:03:20 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:02:54 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:03:47 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:01:24 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:04:16 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:01:13 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-12 14:09:18 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.019 |  |
| 2026-10-12 14:02:24 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-12 14:02:40 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:00:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-10-12 14:02:22 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-10-12 14:05:32 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.032 |  |
| 2026-10-12 14:16:36 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.035 |  |
| 2026-10-12 14:08:12 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-10-12 14:01:55 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.041 |  |
| 2026-10-12 14:07:34 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | -0.047 |  |
| 2026-10-12 14:02:45 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.054 |  |
| 2026-10-12 14:04:27 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.058 |  |
| 2026-10-12 14:03:26 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.059 |  |
| 2026-10-12 14:02:34 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | -0.060 |  |
| 2026-10-12 14:07:37 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)