# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_13:06:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 13:06:52 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:06:50 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:06:47 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 13:06:13 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.198 |  |
| 2026-01-09 13:05:23 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:04:47 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-01-09 13:04:30 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 13:04:27 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 13:04:08 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-09 13:03:08 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-01-09 13:02:49 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:46 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:02:45 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:31 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:30 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:02:21 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 13:02:17 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:13 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-01-09 13:02:06 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 13:01:49 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-09 13:01:48 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:46 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:45 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:23 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:22 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:01:09 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:01:07 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:00:28 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:00:24 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-09 13:00:13 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.034 |  |
| 2026-01-09 12:21:03 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.022 |  |
| 2026-01-09 12:17:33 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 13:01:49 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-09 13:00:24 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-09 12:04:35 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-09 13:02:13 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 13:02:06 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 13:04:30 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 13:04:27 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 13:02:21 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 13:06:47 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 13:02:17 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:07 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:23 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:05:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:49 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:45 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:17:33 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:05:23 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:00:28 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:45 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:06:52 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:22 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:02:31 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:06:50 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:12 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:46 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:48 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:01:09 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:02:30 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:02:46 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:01:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 13:04:47 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-01-09 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-01-09 13:04:08 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-09 12:21:03 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.022 |  |
| 2026-01-09 13:03:08 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-01-09 13:00:13 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.034 |  |
| 2026-01-09 12:01:33 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.189 |  |
| 2026-01-09 13:06:13 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.198 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)