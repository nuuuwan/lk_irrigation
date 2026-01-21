# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_09:12:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,514 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 09:12:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-01-21 09:09:30 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-21 09:09:06 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:07:24 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:07:14 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:05:08 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:05:01 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:04:50 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-21 09:04:28 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:04:26 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:04:08 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:04:07 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:03:53 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.092 |  |
| 2026-01-21 09:03:46 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-01-21 09:03:39 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-21 09:03:11 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.129 |  |
| 2026-01-21 09:03:08 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:03:07 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:03:05 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:50 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:02:45 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:30 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-21 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-01-21 09:02:22 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-21 09:02:19 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:09 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:07 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.397 |  |
| 2026-01-21 09:02:00 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-21 09:01:57 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:01:44 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:01:40 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:31 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:29 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 09:01:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:10 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:06 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:05 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 09:00:59 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:00:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 09:03:46 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-01-21 09:04:50 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-21 09:02:00 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-21 09:01:29 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 09:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 09:01:05 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 09:09:30 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-21 09:01:44 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:01:57 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:04:26 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:04:28 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:02:50 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 09:01:10 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:03:05 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:00:59 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:06 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:40 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:04:08 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:31 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:05:08 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:09:06 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:03:07 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:03:08 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:19 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:07:14 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:01:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:04:07 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:09 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:05:01 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:07:24 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:45 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 09:02:30 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-21 09:03:39 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-21 09:02:22 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-21 09:12:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-01-21 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-01-21 09:03:53 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.092 |  |
| 2026-01-21 09:03:11 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.129 |  |
| 2026-01-21 09:02:07 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.397 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)