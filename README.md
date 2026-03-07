# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_14:16:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 14:16:07 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-07 14:12:03 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:09:25 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:09:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:08:47 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:07:40 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:07:05 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.020 |  |
| 2026-03-07 14:06:42 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-07 14:06:07 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-07 14:05:51 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:05:01 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-07 14:04:45 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:04:45 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:04:14 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:04:14 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:04:02 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:03:59 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:43 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:26 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:21 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:03:12 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:08 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:53 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:25 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:01 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:52 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:36 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 14:01:33 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.084 |  |
| 2026-03-07 14:01:13 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:00:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:00:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:00:30 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:00:16 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-07 14:00:15 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.020 |  |
| 2026-03-07 14:00:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 14:16:07 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-07 14:05:01 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-07 14:06:42 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-07 14:06:07 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-07 14:01:36 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 14:02:01 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:13 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:43 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:52 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:59 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:08:47 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:05:51 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:26 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:08 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:12 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:14:41 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:01:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:00:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:09:25 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:07:40 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:25 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:04:45 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:09:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:04:45 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:21 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:12:03 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:04:14 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:04:02 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:00:30 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:04:14 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:00:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-07 14:00:16 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-07 14:00:15 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.020 |  |
| 2026-03-07 14:07:05 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.020 |  |
| 2026-03-07 14:01:33 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)