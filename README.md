# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_15:09:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 15:09:34 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:08:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-21 15:08:23 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:07:38 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:06:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:06:21 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:06:06 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-21 15:05:34 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:05:33 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:05:12 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:04:56 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.144 |  |
| 2026-01-21 15:04:23 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-21 15:04:21 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-21 15:04:07 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:50 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:46 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:25 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:18 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-21 15:03:16 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:13 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.069 |  |
| 2026-01-21 15:03:09 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.082 |  |
| 2026-01-21 15:02:59 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-21 15:02:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:02:55 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-21 15:02:29 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:02:23 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-01-21 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 15:02:07 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:01:55 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 15:01:53 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:01:52 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 15:01:16 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 15:01:13 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:01:08 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:59 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:43 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:27 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-21 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:06 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 14:18:09 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 15:04:23 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-21 15:02:23 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-01-21 15:06:06 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-21 15:00:27 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-21 15:03:18 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-21 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 15:01:52 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 15:08:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-21 15:01:16 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-21 15:01:55 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 15:00:06 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:43 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:01:13 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:02:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:46 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:50 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:09:34 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:02:29 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:01:08 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:05:33 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-21 14:05:57 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:05:12 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:25 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:16 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:06:21 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:08:23 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:00:59 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:03:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:01:53 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:06:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:04:07 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:02:07 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 15:02:55 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-21 15:02:59 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-21 15:03:13 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.069 |  |
| 2026-01-21 15:03:09 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.082 |  |
| 2026-01-21 15:04:56 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)