# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_02:19:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 02:19:34 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-19 02:15:27 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:11:50 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:11:41 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-19 02:09:02 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-03-19 02:06:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:06:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:06:43 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:05:56 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-03-19 02:05:52 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:05:36 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-03-19 02:04:28 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.005 |  |
| 2026-03-19 02:03:15 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:03:07 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-19 02:03:04 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 02:03:00 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:54 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.069 |  |
| 2026-03-19 02:02:46 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:38 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:11 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:58 | Manampitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:40 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:27 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:25 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-03-19 02:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:00:56 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.239 |  |
| 2026-03-19 01:43:48 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 02:05:56 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-03-19 02:09:02 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-03-19 01:05:58 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-19 02:19:34 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-18 23:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 23:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-19 02:11:41 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-19 02:03:07 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-19 02:03:04 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 01:01:47 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 02:02:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:27 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:38 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:03:15 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 01:05:32 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:06:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:03:00 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:06:43 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:15:27 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:11:50 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:11 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:25 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:46 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:05:52 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 01:03:00 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:40 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:01:58 | Manampitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:06:51 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:04:28 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.005 |  |
| 2026-03-18 23:15:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-03-19 02:05:36 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-03-19 02:01:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-03-19 02:02:54 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.069 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-19 02:00:56 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)