# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_04:48:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 04:48:57 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-04 04:41:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:14:32 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:11:34 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-04 04:11:33 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 04:09:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-07-04 04:08:51 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 3.176 | 🔺 Rising |
| 2026-07-04 04:08:33 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:08:17 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 3.176 | 🔺 Rising |
| 2026-07-04 04:08:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-07-04 04:07:34 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.096 |  |
| 2026-07-04 04:06:30 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-07-04 04:06:24 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-07-04 04:06:08 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.127 |  |
| 2026-07-04 04:05:36 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.069 |  |
| 2026-07-04 04:05:35 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:04:43 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:04:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:03:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-07-04 04:03:22 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-04 04:03:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.039 |  |
| 2026-07-04 04:02:42 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 04:02:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.498 | 🔺 Rising |
| 2026-07-04 04:02:18 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:02:01 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:02:00 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-07-04 04:01:43 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:01:17 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-04 04:01:03 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:00:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 04:08:51 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 3.176 | 🔺 Rising |
| 2026-07-04 04:02:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.498 | 🔺 Rising |
| 2026-07-04 04:06:30 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-07-04 04:09:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-07-04 04:48:57 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-07-04 04:11:33 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 04:01:17 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-04 04:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 04:00:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:02:42 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:02:01 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:04:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:14:32 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:04:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:05:35 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:02:18 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:06:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:08:33 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:03:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:04:43 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:01:03 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:41:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 04:01:43 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-04 04:06:24 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-04 04:11:34 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-04 04:03:22 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-04 00:03:46 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-07-04 04:08:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-07-04 04:03:37 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-07-04 04:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.039 |  |
| 2026-07-04 04:02:00 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-07-04 04:05:36 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.069 |  |
| 2026-07-04 04:07:34 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.096 |  |
| 2026-07-04 04:06:08 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)