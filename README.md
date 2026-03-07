# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_13:20:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 13:20:24 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-07 13:19:04 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:17:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-07 13:14:41 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:09:58 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:08:52 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-03-07 13:07:42 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.046 |  |
| 2026-03-07 13:07:37 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:06:48 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:06:10 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:05:51 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:05:28 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:05:16 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:04:42 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:04:30 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.247 |  |
| 2026-03-07 13:04:04 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:04:00 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 13:03:46 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:03:38 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:55 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:53 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 13:02:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:02:29 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-03-07 13:02:18 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:55 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:38 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:34 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:29 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:25 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:22 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 13:01:16 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:58 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:53 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:30 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:00:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:16 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 13:08:52 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-03-07 13:17:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-07 13:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 13:20:24 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-07 13:00:16 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 13:04:00 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 13:01:22 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 13:07:37 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:55 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:53 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:34 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:06:10 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:25 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:19:04 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:55 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:03:46 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:53 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:29 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-03-07 12:06:26 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:14:41 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:16 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:05:51 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:03:38 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:05:28 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:29 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:02:18 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:00:58 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:06:48 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:09:58 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:01:38 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-07 13:05:16 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:04:42 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:00:30 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:02:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:04:04 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-07 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-03-07 13:07:42 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.046 |  |
| 2026-03-07 13:04:30 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)