# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_11:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,878 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 11:17:30 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-13 11:15:48 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:15:03 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-02-13 11:09:57 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-13 11:08:30 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-02-13 11:06:26 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.092 |  |
| 2026-02-13 11:06:16 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:05:42 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:05:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:05:08 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.098 |  |
| 2026-02-13 11:04:10 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:04:01 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:39 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 11:03:38 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:38 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-13 11:03:37 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-13 11:03:35 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-13 11:03:33 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-13 11:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.121 |  |
| 2026-02-13 11:03:04 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:03 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-13 11:02:38 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-02-13 11:02:26 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-13 11:02:17 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 11:02:16 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:15 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-02-13 11:02:04 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:01:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-13 11:01:53 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.068 |  |
| 2026-02-13 11:01:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:01:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-02-13 11:01:25 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:01:17 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-02-13 11:00:34 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 11:00:33 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 11:01:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-13 11:03:03 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-13 11:02:26 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-13 11:03:35 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-13 11:03:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-13 11:00:33 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-13 11:02:17 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 11:03:38 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-13 11:17:30 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-13 11:00:34 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 10:03:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 11:03:39 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 11:01:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:38 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:04:10 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:04:01 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:04 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:16 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:33 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:05:42 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:03:38 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:01:25 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:04 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:15 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-02-13 11:09:57 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-02-13 11:15:03 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-02-13 11:05:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:15:48 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:06:16 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:08:30 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-02-13 11:01:17 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-02-13 11:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-02-13 11:03:37 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-02-13 11:01:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-02-13 11:01:53 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.068 |  |
| 2026-02-13 11:06:26 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.092 |  |
| 2026-02-13 11:05:08 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.098 |  |
| 2026-02-13 11:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)