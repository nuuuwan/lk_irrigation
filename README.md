# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_03:19:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 03:19:35 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:10:24 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:08:20 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 03:06:49 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-03-10 03:06:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 03:06:11 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:05:49 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-10 03:05:04 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:04:44 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:21 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-03-10 03:03:16 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:10 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-10 03:03:10 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 03:02:56 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.205 |  |
| 2026-03-10 03:02:27 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:24 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:23 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:17 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.032 |  |
| 2026-03-10 03:02:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:01:47 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-10 03:01:32 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.052 |  |
| 2026-03-10 03:01:19 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-03-10 03:01:18 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:01:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-03-10 03:00:30 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-10 03:00:22 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:37:32 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.076 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 03:03:21 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-03-09 18:01:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 03:06:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 03:00:30 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-10 02:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-10 02:37:32 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-10 03:08:20 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 22:02:21 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-10 03:01:47 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-10 03:03:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 03:06:11 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:04:53 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:04:44 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:24 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:01:18 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-09 18:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:11:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:05:04 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:00:22 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:19:35 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:23 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:10 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:03:16 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:10:24 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:05:18 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:02:27 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:12:09 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:20:11 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.006 |  |
| 2026-03-10 03:05:49 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-10 03:03:10 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-10 03:06:49 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-03-10 03:01:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-03-10 03:01:19 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-03-10 03:02:17 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.032 |  |
| 2026-03-10 03:01:32 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.052 |  |
| 2026-03-09 18:01:53 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.075 |  |
| 2026-03-10 03:02:56 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)