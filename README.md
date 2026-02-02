# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_11:34:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,394 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 11:34:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.065 |  |
| 2026-02-02 11:19:48 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:16:29 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-02-02 11:13:21 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:11:24 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:11:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:11:09 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-02-02 11:09:58 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:09:03 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-02 11:07:17 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:06:47 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:06:19 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:06:07 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-02 11:06:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:05:46 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.115 |  |
| 2026-02-02 11:05:29 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-02-02 11:04:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.038 |  |
| 2026-02-02 11:04:38 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.213 |  |
| 2026-02-02 11:04:01 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 11:04:00 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-02-02 11:03:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 11:03:44 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:54 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-02-02 11:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:44 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:02:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:13 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:07 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.021 |  |
| 2026-02-02 11:02:01 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:02:01 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 11:01:52 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-02-02 11:01:36 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:01:22 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.058 |  |
| 2026-02-02 11:01:15 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-02 11:00:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 11:00:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.043 |  |
| 2026-02-02 11:00:30 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:00:20 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 11:06:07 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-02 11:09:03 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-02 11:01:15 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-02 11:04:01 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 11:02:01 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-02 11:00:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 11:03:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 11:01:36 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:00:20 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:53 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:19:48 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:07:17 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:06:47 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:09:58 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:00:30 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:06:19 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:02:13 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:05:29 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:11:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:03:44 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:13:21 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:11:09 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-02-02 11:11:24 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:02:01 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:06:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:02:44 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-02-02 11:04:00 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-02-02 11:16:29 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-02-02 11:02:07 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.021 |  |
| 2026-02-02 11:02:54 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-02-02 11:01:52 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-02-02 11:04:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.038 |  |
| 2026-02-02 11:00:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.043 |  |
| 2026-02-02 11:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-02-02 11:01:22 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.058 |  |
| 2026-02-02 11:34:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.065 |  |
| 2026-02-02 11:05:46 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.115 |  |
| 2026-02-02 11:04:38 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)