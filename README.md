# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_13:17:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 13:17:27 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-03-03 13:14:16 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:10:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-03-03 13:10:06 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-03 13:09:42 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-03 13:05:57 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-03 13:05:25 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:05:17 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-03 13:05:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:05:04 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:04:33 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:25 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:05 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:01 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:00 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:03:56 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:53 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:23 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-03 13:03:11 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:03 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:02:38 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:02:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-03 13:02:33 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.050 |  |
| 2026-03-03 13:02:06 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:02:05 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.050 |  |
| 2026-03-03 13:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:53 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-03-03 13:01:42 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:21 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:21 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:18 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:00:41 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:00:20 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:00:12 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-03 13:00:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 13:03:23 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-03-03 13:02:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-03 13:10:06 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-03 13:05:57 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-03 13:00:12 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-03 13:09:42 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-03 13:05:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:00:20 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:03 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:42 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:14:16 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:11 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:02:38 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:21 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:01:21 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:05 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:00:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:25 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:05:25 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:56 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:00:41 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:03:53 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 12:08:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:01 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:04:33 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:17:27 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.008 |  |
| 2026-03-03 13:05:04 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:04:00 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:01:18 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:02:06 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-03 13:01:53 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-03-03 12:11:06 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.012 |  |
| 2026-03-03 13:10:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-03-03 13:05:17 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-03 13:02:05 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.050 |  |
| 2026-03-03 13:02:33 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)