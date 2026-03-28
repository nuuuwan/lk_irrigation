# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_17:07:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,838 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 17:07:56 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:07:24 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:06:58 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-28 17:06:44 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:06:39 | Rathnapura (Kalu Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 17:04:53 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-28 17:04:41 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:35 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:25 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:10 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 17:03:58 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-28 17:03:57 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-28 17:03:57 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.146 |  |
| 2026-03-28 17:03:52 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-28 17:03:20 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:03:19 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:03:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:03:12 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:03:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:02:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:02:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2026-03-28 17:02:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:02:15 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:02:09 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:44 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:40 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:34 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:01:08 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:08 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:08 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:00:47 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:00:44 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-03-28 17:00:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-03-28 17:00:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:00:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 16:16:30 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 17:03:58 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-28 17:03:52 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-28 17:04:53 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-28 17:00:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 17:04:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 17:06:58 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-28 17:06:39 | Rathnapura (Kalu Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 17:03:20 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:25 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:08 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:02:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:03:19 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-28 16:02:50 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:35 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:41 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:07:24 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:40 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:08 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:07:56 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 16:05:37 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:06:44 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:44 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:02:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:03:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:03:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:04:10 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:00:47 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:08 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:02:09 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 17:01:34 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:03:12 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:02:15 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-28 17:00:44 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-03-28 16:07:44 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-03-28 16:08:04 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-03-28 17:00:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-03-28 17:02:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2026-03-28 17:03:57 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)