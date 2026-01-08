# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_23:22:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,374 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 23:22:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.007 |  |
| 2026-01-08 23:16:32 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-01-08 23:15:36 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.025 |  |
| 2026-01-08 23:10:46 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:07:52 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:06:37 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:55 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.057 |  |
| 2026-01-08 23:05:51 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:43 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-01-08 23:05:16 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:04:56 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:04:49 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.024 |  |
| 2026-01-08 23:04:20 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-08 23:03:49 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.974 |  |
| 2026-01-08 23:03:43 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:03:41 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:03:41 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-08 23:02:55 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:02:45 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:02:26 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-08 23:02:17 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-01-08 23:02:14 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-08 23:02:09 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:57 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:48 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-01-08 23:01:47 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.041 |  |
| 2026-01-08 23:01:35 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:32 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 23:01:31 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 23:01:48 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-01-08 23:04:20 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-08 23:02:14 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-08 23:02:26 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-08 23:01:32 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 23:01:35 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:07:52 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:55 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:51 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:03:41 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:02:55 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:04:56 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:16 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:05:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:31 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:03:43 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:02:09 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:06:37 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:10:46 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:01:57 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:02:45 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 23:22:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.007 |  |
| 2026-01-08 23:05:43 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 23:03:41 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-08 23:04:49 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.024 |  |
| 2026-01-08 23:15:36 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.025 |  |
| 2026-01-08 23:02:17 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 23:16:32 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-01-08 23:01:47 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.041 |  |
| 2026-01-08 23:05:55 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.057 |  |
| 2026-01-08 22:05:45 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.071 |  |
| 2026-01-08 21:03:07 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.078 |  |
| 2026-01-08 23:03:49 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.974 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)