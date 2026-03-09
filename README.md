# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_13:18:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,475 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 13:18:05 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-03-09 13:12:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:11:05 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:08:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:08:06 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-09 13:07:25 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-03-09 13:06:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:06:01 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:05:52 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:05:24 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-09 13:05:15 | Thawalama (Gin Ganga) | 0.20 | 🟢 Normal | -48.414 |  |
| 2026-03-09 13:05:11 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:05:07 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-03-09 13:04:52 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:37 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.217 |  |
| 2026-03-09 13:04:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:18 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.107 |  |
| 2026-03-09 13:04:17 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -48.414 |  |
| 2026-03-09 13:04:03 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:58 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.088 |  |
| 2026-03-09 13:03:55 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:47 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:46 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 13:03:40 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:27 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-03-09 13:03:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 13:02:57 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-09 13:02:54 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-09 13:02:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:02:10 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:02:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-09 13:01:53 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:25 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.123 |  |
| 2026-03-09 13:01:11 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:07 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:03 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:00:43 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 13:05:07 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-03-09 13:02:54 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-09 13:05:24 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-09 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 13:00:43 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-09 13:03:46 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 13:03:40 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:53 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:08:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:03 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:12:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:02:10 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:55 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:05:11 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:47 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:52 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:02:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:11 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:03:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:03 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:01:07 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:11:05 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:06:01 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:06:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:08:06 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-09 13:02:57 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-09 13:02:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-09 13:07:25 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-03-09 13:18:05 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-03-09 13:03:27 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-03-09 13:03:58 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.088 |  |
| 2026-03-09 13:04:18 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.107 |  |
| 2026-03-09 13:01:25 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.123 |  |
| 2026-03-09 13:04:37 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.217 |  |
| 2026-03-09 13:05:15 | Thawalama (Gin Ganga) | 0.20 | 🟢 Normal | -48.414 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)