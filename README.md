# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_17:14:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,717 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 17:14:20 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:12:37 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:11:55 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-08 17:06:46 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-03-08 17:06:19 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.022 |  |
| 2026-03-08 17:05:54 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:05:32 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:05:24 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:05:15 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.041 |  |
| 2026-03-08 17:04:47 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-08 17:04:19 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-03-08 17:04:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:57 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-08 17:03:57 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:51 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:29 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:10 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-03-08 17:02:57 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:02:55 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-03-08 17:02:47 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:46 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:17 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:15 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:14 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:01:35 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-08 17:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.012 |  |
| 2026-03-08 17:00:58 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:00:47 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 17:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:00:32 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 17:00:29 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:00:26 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-08 17:00:08 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-08 16:27:33 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 17:04:19 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-03-08 17:00:26 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-08 17:00:08 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-08 17:04:47 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-08 17:01:35 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-08 17:00:32 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 17:00:47 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 17:02:17 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:15 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:51 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-08 14:02:03 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 16:11:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:10 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:14:20 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:00:29 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:05:54 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:57 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:04:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:03:29 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:46 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:00:58 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:12:37 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:02:47 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-08 17:11:55 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-08 17:06:46 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-03-08 17:05:24 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:05:32 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:02:57 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:02:14 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-08 17:03:57 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-08 17:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.012 |  |
| 2026-03-08 16:20:18 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.017 |  |
| 2026-03-08 17:02:55 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-03-08 17:06:19 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.022 |  |
| 2026-03-08 17:03:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-03-08 17:05:15 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)