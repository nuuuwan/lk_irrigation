# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_13:15:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,308 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 13:15:40 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.109 |  |
| 2026-03-22 13:13:29 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-03-22 13:07:28 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:06:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:06:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-03-22 13:06:29 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:06:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:05:41 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-03-22 13:05:14 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:50 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-22 13:04:45 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:29 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:22 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:22 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.068 |  |
| 2026-03-22 13:03:44 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:03:43 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-22 13:03:32 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-22 13:03:25 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.067 |  |
| 2026-03-22 13:03:14 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-22 13:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:02:41 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-22 13:02:32 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-03-22 13:02:22 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-03-22 13:02:18 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-03-22 13:01:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:33 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:30 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-22 13:01:30 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 13:01:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:19 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:00:53 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.102 |  |
| 2026-03-22 13:00:45 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.123 |  |
| 2026-03-22 13:00:24 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 13:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-03-22 13:04:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-22 13:02:41 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-22 13:03:32 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-22 12:03:49 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-22 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 13:04:50 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:30 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:02:18 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:06:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:29 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:45 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:03:25 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:19 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:03:44 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:00:24 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:06:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:07:28 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:05:14 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:06:29 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:04:22 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:01:33 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 13:13:29 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-03-22 13:06:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-03-22 13:02:32 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-03-22 13:03:43 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-22 13:03:14 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-22 13:01:30 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-03-22 13:02:22 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-03-22 12:09:36 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.037 |  |
| 2026-03-22 13:05:41 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-03-22 13:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.067 |  |
| 2026-03-22 13:04:22 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.068 |  |
| 2026-03-22 13:00:53 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.102 |  |
| 2026-03-22 13:15:40 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.109 |  |
| 2026-03-22 13:00:45 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)