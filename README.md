# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_10:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 10:12:12 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:11:24 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:10:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:09:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:09:04 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:08:57 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:07:22 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-18 10:06:13 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-02-18 10:05:56 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-18 10:05:31 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.137 |  |
| 2026-02-18 10:05:26 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:05:20 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-18 10:04:58 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 10:04:31 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:26 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-18 10:04:15 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:10 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:03:55 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.033 |  |
| 2026-02-18 10:03:46 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.070 |  |
| 2026-02-18 10:03:36 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:03:34 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:03:32 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 10:03:21 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 10:03:19 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.488 | 🔺 Rising |
| 2026-02-18 10:03:13 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:02:36 | Padiyathalawa (Maduru Oya) | 1.96 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-18 10:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-02-18 10:02:19 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.293 |  |
| 2026-02-18 10:02:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 10:02:13 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-02-18 10:01:46 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.005 |  |
| 2026-02-18 10:01:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:01:30 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:01:26 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:00:53 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:00:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:00:30 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 10:03:19 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.488 | 🔺 Rising |
| 2026-02-18 10:05:20 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-18 10:02:36 | Padiyathalawa (Maduru Oya) | 1.96 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-18 10:07:22 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-18 10:05:56 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-18 10:02:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 10:03:32 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 10:03:21 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 10:04:58 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 10:01:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:00:53 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:10:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:01:26 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:26 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:10 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:09:04 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:03:36 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:12:12 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:00:52 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:31 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:05:26 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:04:15 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:03:13 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:11:24 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:09:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:01:46 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.005 |  |
| 2026-02-18 10:01:30 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:00:30 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:08:57 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:03:34 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-18 10:04:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-18 10:02:13 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-02-18 10:03:55 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.033 |  |
| 2026-02-18 10:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-02-18 10:06:13 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-02-18 10:03:46 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.070 |  |
| 2026-02-18 10:05:31 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.137 |  |
| 2026-02-18 10:02:19 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.293 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)