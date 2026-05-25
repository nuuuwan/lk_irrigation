# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_01:25:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,721 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 01:25:19 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 01:21:44 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:15:29 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-26 01:14:37 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:09:55 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:08:25 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-26 01:08:15 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:08:14 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:06:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-05-26 01:06:16 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | -0.020 |  |
| 2026-05-26 01:06:08 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:05:19 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-05-26 01:04:54 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:04:30 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.031 |  |
| 2026-05-26 01:04:05 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-05-26 01:04:04 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:04:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:03:23 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-26 01:03:16 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:54 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-05-26 01:02:38 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:35 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.066 |  |
| 2026-05-26 01:02:22 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:01 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-05-26 01:01:56 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:01:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:18 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:05 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:00:47 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:00:46 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:59:59 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 00:21:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.023 |  |
| 2026-05-26 01:03:23 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-26 01:08:25 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-26 00:05:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 01:15:29 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-26 01:25:19 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 00:08:43 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-26 01:06:08 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:00:47 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:18 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:03:16 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:21:44 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:08:15 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:06:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:09:55 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:08:14 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:38 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:01:05 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:04:54 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-26 00:01:32 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:02:22 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 01:14:37 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:01:56 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:04:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-26 01:02:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-05-26 01:02:01 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-26 01:04:05 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-05-26 01:06:16 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-26 01:05:19 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-05-26 01:06:27 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-05-26 01:04:30 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.031 |  |
| 2026-05-26 01:02:35 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)