# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_22:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,006 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 22:15:18 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.009 |  |
| 2026-05-04 22:14:12 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:09:29 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.059 |  |
| 2026-05-04 22:07:20 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.082 |  |
| 2026-05-04 22:06:47 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:06:10 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 22:06:05 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:05:56 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-05-04 22:05:42 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-04 22:05:24 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-04 22:04:55 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:04:12 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:04:06 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 22:04:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-05-04 22:03:58 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-04 22:03:56 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:03:00 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.129 |  |
| 2026-05-04 22:02:59 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-05-04 22:02:49 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 22:02:13 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:01:53 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.051 |  |
| 2026-05-04 22:01:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-05-04 22:01:30 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-04 22:01:30 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:01:29 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:01:11 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-04 22:00:55 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:00:33 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-04 22:00:19 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 22:04:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-05-04 21:06:00 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-04 22:03:58 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-04 22:05:42 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-04 22:01:30 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-04 22:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 22:04:06 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 21:03:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 22:06:10 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 21:02:19 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 21:02:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:04:55 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:02:13 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:04:12 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:00:55 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:02:49 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:06:05 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:14:12 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:03:56 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:06:47 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-04 21:09:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:01:29 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:01:30 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:15:18 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.009 |  |
| 2026-05-04 22:01:11 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-04 22:00:33 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-04 22:05:24 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-04 20:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.024 |  |
| 2026-05-04 22:00:19 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-05-04 22:01:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-05-04 22:05:56 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-05-04 22:02:59 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-05-04 22:01:53 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.051 |  |
| 2026-05-04 22:09:29 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.059 |  |
| 2026-05-04 22:07:20 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.082 |  |
| 2026-05-04 22:03:00 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)