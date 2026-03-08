# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_23:07:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 23:07:41 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:07:18 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -4.500 |  |
| 2026-03-08 23:07:14 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 23:06:46 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -4.500 |  |
| 2026-03-08 23:06:42 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:06:37 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.077 |  |
| 2026-03-08 23:06:17 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 23:06:15 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:04:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:04:34 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-08 23:04:22 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.059 |  |
| 2026-03-08 23:04:03 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-08 23:04:01 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.582 | 🔺 Rising |
| 2026-03-08 23:03:52 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-03-08 23:03:44 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.044 |  |
| 2026-03-08 23:03:41 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.023 |  |
| 2026-03-08 23:03:36 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-08 23:01:10 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:01:06 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:50 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-03-08 23:00:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:49 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:33 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:12 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-03-08 22:50:02 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.044 |  |
| 2026-03-08 22:23:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 23:04:01 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.582 | 🔺 Rising |
| 2026-03-08 23:03:36 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-08 23:06:17 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 23:04:03 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-08 23:07:14 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 22:00:28 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:01:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:01:10 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:33 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:06:42 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:06:05 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:04:28 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:01:06 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:05:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:49 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:00:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:04:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:06:15 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:07:41 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:03:06 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:05:36 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-08 22:23:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.007 |  |
| 2026-03-08 23:04:34 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-08 22:04:29 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-08 23:00:50 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-03-08 23:00:12 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-03-08 23:03:41 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.023 |  |
| 2026-03-08 23:03:52 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-03-08 22:00:27 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-03-08 23:03:44 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.044 |  |
| 2026-03-08 23:04:22 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.059 |  |
| 2026-03-08 23:06:37 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.077 |  |
| 2026-03-08 23:07:18 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)