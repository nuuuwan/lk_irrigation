# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_20:09:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 20:09:22 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-02-07 20:09:10 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.118 |  |
| 2026-02-07 20:08:51 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.011 |  |
| 2026-02-07 20:08:47 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:07:18 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-02-07 20:07:10 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:06:20 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -2.571 |  |
| 2026-02-07 20:05:58 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:05:43 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -2.571 |  |
| 2026-02-07 20:05:14 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:04:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:04:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:04:15 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-02-07 20:04:09 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:03:59 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 20:03:54 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-02-07 20:03:27 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:03:21 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:03:07 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 20:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:02:32 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-02-07 20:02:26 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:02:17 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:02:16 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:01:53 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 20:01:48 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:01:34 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:01:28 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:01:22 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-02-07 20:01:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-02-07 20:01:11 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:00:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:00:08 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-07 19:19:10 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 20:00:08 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-07 20:03:07 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 20:03:59 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 20:01:53 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 20:00:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:01:48 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:05:14 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:02:26 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:04:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:05:43 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:03:21 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:19:10 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:06:20 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:04:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:03:27 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:04:09 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:01:34 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:02:17 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:08:47 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 19:05:58 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 20:01:28 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 20:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:02:16 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:01:11 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:07:10 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-07 20:08:51 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.011 |  |
| 2026-02-07 20:04:15 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-02-07 19:13:21 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.017 |  |
| 2026-02-07 20:09:22 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-02-07 20:03:54 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-02-07 20:01:22 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-07 20:02:32 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-02-07 20:07:18 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-02-07 20:01:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-02-07 20:09:10 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.118 |  |
| 2026-02-07 20:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -2.571 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)