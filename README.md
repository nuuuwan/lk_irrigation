# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_00:10:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,476 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 00:10:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-18 00:09:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-18 00:07:23 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:07:22 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:07:20 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:07:19 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:07:13 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:06:01 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:05:07 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:05:05 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-18 00:04:48 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:04:47 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-18 00:04:10 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:04:02 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-01-18 00:03:58 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-18 00:03:51 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:03:49 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:03:20 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:59 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:21 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:00 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:51 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 00:01:41 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:41 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-18 00:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:26 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-18 00:01:13 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:07 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:00:59 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-18 00:00:58 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-17 23:25:05 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:17:01 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:16:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:15:21 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-17 23:14:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 00:03:58 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-17 23:03:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-18 00:00:59 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-18 00:10:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-18 00:05:05 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-18 00:09:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-18 00:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 00:00:58 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-18 00:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:13 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:07 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:59 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:27 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:15:16 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:03:20 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:07:13 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:03:51 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:07:23 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:41 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:05:07 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:21 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:04:48 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:02:00 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:06:01 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:04:10 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:25:05 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:01:51 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:03:49 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:03:20 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-18 00:04:02 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-01-18 00:04:47 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-18 00:01:41 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-17 23:05:16 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-01-18 00:01:26 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-17 23:14:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.027 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)