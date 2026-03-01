# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_23:13:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 23:13:13 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-01 23:09:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:08:38 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-01 23:06:08 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-01 23:05:33 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:18 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:15 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:08 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:04:35 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:04:32 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:04:19 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 23:03:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.717 |  |
| 2026-03-01 23:03:04 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:57 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-01 23:02:49 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-01 23:02:47 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:39 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:36 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-01 23:02:34 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:31 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 23:02:30 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:11 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:01:37 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-03-01 23:01:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-01 23:01:16 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:00:46 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:00:23 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-01 23:00:19 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-03-01 22:52:39 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-01 22:28:47 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 23:01:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-01 23:02:57 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-01 23:08:38 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-01 18:01:43 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-01 23:02:31 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 23:00:23 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-01 23:02:49 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-01 23:04:19 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 23:09:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-01 22:00:08 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:47 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:00:46 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:34 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 20:59:25 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 18:01:07 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:39 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 22:01:52 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-01 22:08:31 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 21:07:36 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:01:16 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:33 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:03:04 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:08 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:04:35 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 22:07:54 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:04:32 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:15 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:05:18 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:30 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:02:11 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-01 23:06:08 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-01 18:00:31 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-01 23:13:13 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-01 23:02:36 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-01 23:00:19 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-03-01 23:01:37 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-03-01 22:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-03-01 23:03:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.717 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)