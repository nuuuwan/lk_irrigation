# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_11:08:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,354 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 11:08:52 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.043 |  |
| 2026-01-04 11:08:16 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:07:51 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-04 11:07:16 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.018 |  |
| 2026-01-04 11:07:03 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:06:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-01-04 11:06:39 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:06:09 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-04 11:05:57 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -0.038 |  |
| 2026-01-04 11:05:46 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.038 |  |
| 2026-01-04 11:05:45 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:04:59 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:04:51 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:04:40 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-04 11:04:24 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-01-04 11:04:17 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:04:09 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:03:58 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 11:03:49 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:41 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.091 |  |
| 2026-01-04 11:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:21 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:13 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:02 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-01-04 11:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:02:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-04 11:02:22 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:02:10 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 11:02:03 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:01:48 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-01-04 11:01:44 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:41 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:01:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:19 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:19 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:01:10 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-04 11:01:07 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:05 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:17:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:16:03 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-01-04 10:15:57 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-04 10:13:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.043 |  |
| 2026-01-04 10:13:11 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-04 10:12:56 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 11:04:24 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-01-04 11:02:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-04 11:01:10 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-04 11:04:40 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-04 11:07:51 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-04 11:03:58 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 11:02:10 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 11:06:09 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-04 11:01:44 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:04:17 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:07 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:04:59 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:07:03 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:06:39 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:02:22 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:05:45 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:04:09 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:19 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:08:16 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:01:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-04 11:03:13 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:49 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:01:41 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:21 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:01:05 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-04 11:03:02 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-01-04 11:01:48 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-01-04 11:07:16 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.018 |  |
| 2026-01-04 11:06:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-01-04 11:02:03 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:04:51 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:01:19 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-01-04 11:05:46 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.038 |  |
| 2026-01-04 11:05:57 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -0.038 |  |
| 2026-01-04 11:08:52 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.043 |  |
| 2026-01-04 11:03:41 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.091 |  |
| 2026-01-04 10:03:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)