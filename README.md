# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_03:35:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 03:35:16 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:21:31 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:16:10 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-19 03:12:10 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:09:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-19 03:06:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-02-19 03:06:41 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-02-19 03:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-19 03:06:16 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.026 |  |
| 2026-02-19 03:05:26 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:05:16 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-19 03:05:01 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-19 03:03:57 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 03:03:30 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-19 03:02:50 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-19 03:02:38 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:02:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.028 |  |
| 2026-02-19 03:02:27 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-02-19 03:02:26 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2026-02-19 03:02:25 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:02:13 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:59 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-02-19 03:01:47 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:44 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-19 03:01:13 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.113 |  |
| 2026-02-19 03:00:54 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:00:49 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:00:18 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-02-19 02:43:25 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 03:06:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-02-19 01:21:54 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-19 03:05:01 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-19 03:16:10 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-19 03:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-19 03:01:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-19 03:03:57 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 02:18:25 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 03:02:50 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-19 03:01:44 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:02:25 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:10:40 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:05:26 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:00:54 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 01:05:04 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:21:31 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:35:16 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:02:38 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:00:49 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:12:10 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:47 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:02:13 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:01:59 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-02-19 03:09:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-19 03:05:16 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-19 03:03:30 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-19 03:02:27 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-02-19 03:00:18 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-02-19 03:06:16 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.026 |  |
| 2026-02-19 03:02:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.028 |  |
| 2026-02-19 03:06:41 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-02-19 02:06:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.060 |  |
| 2026-02-19 03:02:26 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2026-02-19 03:01:13 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)