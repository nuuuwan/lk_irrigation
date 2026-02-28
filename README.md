# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_04:14:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 04:14:52 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:07:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-03-01 04:07:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.057 |  |
| 2026-03-01 04:07:21 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-01 04:07:19 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-01 04:06:06 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:05:58 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-03-01 04:05:39 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:05:38 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:05:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:04:54 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.130 |  |
| 2026-03-01 04:04:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 04:03:47 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:03:24 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-03-01 04:03:23 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-03-01 04:03:05 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:58 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-01 04:02:08 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:08 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:07 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.168 |  |
| 2026-03-01 04:01:47 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-01 04:01:34 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:01:32 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:01:08 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-01 04:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:00:44 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-01 04:00:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.077 |  |
| 2026-03-01 04:00:25 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:56:44 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:56:20 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:46:57 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:46:29 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.130 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 04:03:24 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-03-01 04:07:21 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-01 00:16:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-28 18:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-01 04:00:44 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-01 04:04:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 04:01:47 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-01 03:02:09 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.003 |  |
| 2026-03-01 04:05:39 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:03:05 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:08 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:01:32 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:05:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:01:34 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:04:16 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:08:53 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:10:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:08 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:12 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 02:03:54 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:03:47 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:05:38 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:06:06 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:22:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:13:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:17:10 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:14:52 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:33 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:02:58 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:18 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 04:01:08 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-01 04:02:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-01 04:05:58 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-03-01 04:07:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-03-01 04:07:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.057 |  |
| 2026-03-01 04:00:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.077 |  |
| 2026-03-01 04:04:54 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.130 |  |
| 2026-03-01 04:02:07 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)