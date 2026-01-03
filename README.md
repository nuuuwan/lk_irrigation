# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_11:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 11:17:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-01-03 11:14:52 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.017 |  |
| 2026-01-03 11:08:35 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:08:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.035 |  |
| 2026-01-03 11:06:24 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:06:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-03 11:06:09 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.029 |  |
| 2026-01-03 11:05:57 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.058 |  |
| 2026-01-03 11:05:27 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:04:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:04:46 | Galgamuwa (Mee Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:04:43 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-03 11:04:37 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-03 11:03:54 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:51 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:36 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-01-03 11:03:24 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:19 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.014 |  |
| 2026-01-03 11:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-03 11:03:14 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:12 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:02:52 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-03 11:02:35 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-01-03 11:02:23 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.075 |  |
| 2026-01-03 11:02:22 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:02:17 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-01-03 11:02:07 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:02:04 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:01:59 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:01:53 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:01:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:01:20 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-01-03 11:01:11 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-03 11:00:52 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:00:43 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:00:32 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:00:16 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-03 10:26:27 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 11:04:37 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-03 11:04:43 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-03 11:06:16 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-03 11:02:52 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-03 11:01:11 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-03 11:01:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:00:43 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:02:22 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:14 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:02:04 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:54 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:51 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:12 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:04:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:03:24 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:01:59 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:08:35 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 11:17:32 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-01-03 11:05:27 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:06:24 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:04:46 | Galgamuwa (Mee Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:00:16 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:01:53 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:02:07 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:00:32 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:00:52 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-03 11:01:20 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-01-03 11:02:35 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-01-03 11:03:19 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.014 |  |
| 2026-01-03 10:19:54 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.015 |  |
| 2026-01-03 11:14:52 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.017 |  |
| 2026-01-03 11:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-03 11:02:17 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-01-03 11:03:36 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-01-03 11:06:09 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.029 |  |
| 2026-01-03 11:08:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.035 |  |
| 2026-01-03 11:05:57 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.058 |  |
| 2026-01-03 11:02:23 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)