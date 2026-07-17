# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--17_14:15:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 14:15:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:15:15 | Moraketiya (Walawe Ganga) | 0.46 | 🟢 Normal | -0.008 |  |
| 2026-07-17 14:13:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:11:14 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:10:47 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-17 14:09:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:09:30 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:08:41 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:07:39 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.066 |  |
| 2026-07-17 14:07:31 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:07:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.059 |  |
| 2026-07-17 14:06:58 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.106 |  |
| 2026-07-17 14:06:39 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:05:35 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 14:04:35 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:04:01 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 14:03:22 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:03:21 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:57 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:37 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-17 14:02:23 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.249 |  |
| 2026-07-17 14:02:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-07-17 14:02:17 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-07-17 14:02:14 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:07 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-07-17 14:01:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-17 14:01:52 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:45 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:21 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:20 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:13 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:07 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.031 |  |
| 2026-07-17 14:00:46 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:00:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-17 14:00:29 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:00:27 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 14:02:17 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-07-17 14:02:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-07-17 14:10:47 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-17 14:01:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-17 14:04:01 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 14:05:35 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 14:01:45 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:37 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:09:30 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:13 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:00:29 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 12:07:20 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:00:46 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:03:22 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:04:35 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:52 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:06:39 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:09:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:11:14 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:20 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:03:21 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:07:31 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:08:41 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:15:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:14 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:02:57 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:01:21 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:13:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-17 14:15:15 | Moraketiya (Walawe Ganga) | 0.46 | 🟢 Normal | -0.008 |  |
| 2026-07-17 14:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-17 14:00:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-17 14:00:27 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-17 14:01:07 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.031 |  |
| 2026-07-17 14:02:07 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-07-17 14:07:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.059 |  |
| 2026-07-17 14:07:39 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.066 |  |
| 2026-07-17 14:06:58 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.106 |  |
| 2026-07-17 14:02:23 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.249 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)