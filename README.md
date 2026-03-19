# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_09:07:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 09:07:24 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:07:23 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-19 09:06:01 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:05:49 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-03-19 09:05:27 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:05:21 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:05:03 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-03-19 09:04:36 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:04:19 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 09:04:15 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:04:07 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:04:06 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.038 |  |
| 2026-03-19 09:04:03 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-19 09:03:31 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.059 |  |
| 2026-03-19 09:03:20 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:03:15 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 09:03:03 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-19 09:03:01 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-19 09:02:54 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-19 09:02:39 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 09:02:23 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:02:06 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:02:04 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | -0.113 |  |
| 2026-03-19 09:01:50 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 09:01:50 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:48 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.193 |  |
| 2026-03-19 09:01:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:42 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-03-19 09:01:35 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.080 |  |
| 2026-03-19 09:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.143 |  |
| 2026-03-19 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:18 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:06 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:00:51 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:00:25 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 09:01:42 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-03-19 08:06:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-03-19 09:03:03 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-19 09:07:23 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-19 09:02:39 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 09:03:01 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-19 08:06:03 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-19 08:01:36 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 09:04:19 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 09:01:50 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 09:03:15 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 09:01:50 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:04:15 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:02:06 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:00:25 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:05:27 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 08:09:56 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:07:24 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:04:07 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:18 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:02:23 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:04:36 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:01:06 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-19 09:05:21 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:03:20 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:06:01 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:00:51 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-19 09:02:54 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-19 09:05:03 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-03-19 09:04:03 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-19 09:04:06 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.038 |  |
| 2026-03-19 09:05:49 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-03-19 09:03:31 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.059 |  |
| 2026-03-19 09:01:35 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.080 |  |
| 2026-03-19 09:02:04 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | -0.113 |  |
| 2026-03-19 09:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.143 |  |
| 2026-03-19 09:01:48 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)