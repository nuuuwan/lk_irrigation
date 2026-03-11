# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_04:30:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,026 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 04:30:21 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:29:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.007 |  |
| 2026-03-12 04:29:30 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:19:03 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:17:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-12 04:14:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-03-12 04:10:44 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:10:36 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-12 04:08:57 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-12 04:07:27 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-12 04:06:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 04:06:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:06:01 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:05:57 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:05:23 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:05:01 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:04:18 | Thawalama (Gin Ganga) | 0.80 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-12 04:04:02 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-12 04:03:51 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-12 04:02:07 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:48 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:45 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:35 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:31 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -0.013 |  |
| 2026-03-12 04:01:12 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:08 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 04:01:06 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:00:33 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:00:29 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.093 |  |
| 2026-03-12 04:00:18 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.046 |  |
| 2026-03-12 04:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:58:49 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:56:12 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:51:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.259 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 04:14:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-03-12 04:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-12 04:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-12 04:17:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-12 04:04:18 | Thawalama (Gin Ganga) | 0.80 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-12 04:04:02 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-12 04:10:36 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-12 03:00:16 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 04:01:08 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 04:06:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 04:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:48 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:45 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:02:07 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:12 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:33:13 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:23⌛ | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:30:21 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:05:57 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:05:23 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:06:01 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:08:57 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:35 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:03:51 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:10:44 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:19:03 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:06 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:06:30 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:00:33 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47⌛ | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:05:01 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 03:06:53 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:29:32 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.007 |  |
| 2026-03-12 04:07:27 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-12 04:01:31 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -0.013 |  |
| 2026-03-12 04:00:18 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.046 |  |
| 2026-03-10 18:02:53⌛ | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.088 |  |
| 2026-03-12 04:00:29 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.093 |  |
| 2026-03-12 03:12:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -35.426 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)