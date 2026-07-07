# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_22:41:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 22:41:31 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:14:00 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:12:11 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-07 22:09:37 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.055 |  |
| 2026-07-07 22:09:30 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:09:16 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:09:12 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:07:10 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:57 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 22:06:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:30 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-07-07 22:06:25 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:13 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-07 22:05:50 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:04:49 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2026-07-07 22:04:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:04:13 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:03:46 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-07 22:03:01 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:36 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-07-07 22:02:30 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:24 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:18 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:16 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.124 |  |
| 2026-07-07 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:52 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:45 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:36 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:12 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:00:56 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:00:47 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:00:42 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.021 |  |
| 2026-07-07 22:00:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 21:05:05 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-07-07 22:03:46 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-07 22:12:11 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-07 22:06:13 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-07 22:06:57 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:00:56 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:00:47 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:52 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:36 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:09:12 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:00:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:07:10 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:25 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:30 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:09:30 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:41:31 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:04:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:14:00 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:03:01 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:16 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:09:16 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:24 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:04:13 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:45 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:12 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:02:18 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:30 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-07-07 22:04:49 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2026-07-07 22:00:42 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.021 |  |
| 2026-07-07 22:02:36 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-07-07 21:02:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-07-07 22:09:37 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.055 |  |
| 2026-07-07 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)