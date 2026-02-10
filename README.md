# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_05:15:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 05:15:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-02-10 05:15:47 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:15:20 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-10 05:13:58 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:11:01 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-10 05:08:58 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-02-10 05:07:57 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-10 05:07:02 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-10 05:06:42 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:06:40 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:05:48 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:05:40 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.009 |  |
| 2026-02-10 05:05:30 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-10 05:05:23 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-02-10 05:04:58 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:04:43 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:04:16 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-10 05:04:00 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-10 05:03:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:03:11 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:59 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:53 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 05:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:44 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 05:02:40 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:20 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:01:51 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:01:37 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-10 05:01:25 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-10 05:01:24 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.176 |  |
| 2026-02-10 05:01:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.080 |  |
| 2026-02-10 05:01:06 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:00:47 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:40:58 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:35:44 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 04:01:12 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-02-10 05:07:02 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-10 05:11:01 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-10 03:07:34 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-10 04:09:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-10 05:01:25 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-10 05:07:57 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-10 05:15:20 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-10 05:05:30 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-10 05:02:53 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 05:02:44 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 04:01:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:03:11 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:40 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:04:43 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:59 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:13:58 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:05:48 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:06:42 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:00:47 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:03:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:02:20 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:01:51 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:01:06 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:15:47 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:10:14 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-10 05:05:23 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-02-10 05:05:40 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.009 |  |
| 2026-02-10 05:04:16 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-10 05:08:58 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-02-10 05:01:37 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-10 05:15:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-02-10 05:01:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.080 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-10 05:01:24 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)