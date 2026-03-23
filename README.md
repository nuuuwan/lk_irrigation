# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_03:19:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,700 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 03:19:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-24 03:13:24 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:10:54 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:08:14 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:07:47 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-03-24 03:07:37 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.180 |  |
| 2026-03-24 03:05:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-24 03:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 03:04:33 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-24 03:04:29 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:04:21 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-24 03:04:19 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:04:09 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:03:42 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:03:09 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:03:08 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:03:08 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:52 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:36 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:31 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:02:19 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:13 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:01 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:57 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:01:40 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:35 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2026-03-24 03:01:34 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -36.000 |  |
| 2026-03-24 03:01:33 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:29 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:26 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -36.000 |  |
| 2026-03-24 03:01:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:00:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:38:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 03:05:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-24 03:19:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-24 03:04:21 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-24 03:04:33 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-24 03:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 03:03:42 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:00:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:01 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:03:09 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:57 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:01:38 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:29 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:04:19 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:40 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:13 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:01:33 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:52 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:04:09 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:04:29 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:13:24 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:28:11 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:25:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:03:08 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:02:36 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-24 01:06:43 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-03-24 03:08:14 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:10:54 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-24 02:07:06 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:02:31 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:01:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-24 03:07:47 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-03-23 21:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |
| 2026-03-24 03:07:37 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.180 |  |
| 2026-03-24 03:01:35 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)