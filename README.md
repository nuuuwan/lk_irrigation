# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_10:06:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 10:06:15 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:05:39 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:05:24 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:05:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-03-26 10:04:46 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:04:39 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:04:05 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-26 10:04:02 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.089 |  |
| 2026-03-26 10:03:59 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.049 |  |
| 2026-03-26 10:03:31 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:03:19 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.060 |  |
| 2026-03-26 10:03:13 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:03:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:02:48 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-26 10:02:48 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-26 10:02:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:02:24 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:02:15 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-03-26 10:02:04 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 10:01:48 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:41 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:35 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-03-26 10:01:34 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:27 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:17 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-26 10:01:10 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.054 |  |
| 2026-03-26 10:01:02 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.050 |  |
| 2026-03-26 10:00:28 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:00:27 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-26 10:00:18 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:15:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 09:01:53 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-03-26 10:04:05 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-26 10:01:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 10:02:15 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 10:02:24 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:00:18 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:04:45 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:05:39 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:27 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:00:20 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:03:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:41 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:04:39 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:48 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:04:46 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:03:31 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:00:28 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:10 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:02:04 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:05:24 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:08:03 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:01:34 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:03:13 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:06:15 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 10:02:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 09:15:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-03-26 10:02:48 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-26 10:02:48 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-26 10:00:27 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-26 10:01:17 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-26 10:01:35 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-03-26 10:05:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-03-26 10:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-03-26 10:03:59 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.049 |  |
| 2026-03-26 10:01:02 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.050 |  |
| 2026-03-26 10:01:08 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.054 |  |
| 2026-03-26 09:08:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.058 |  |
| 2026-03-26 10:03:19 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.060 |  |
| 2026-03-26 10:04:02 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)