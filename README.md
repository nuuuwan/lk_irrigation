# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_04:40:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 04:40:58 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:35:44 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.006 |  |
| 2026-02-10 04:31:01 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:28:48 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-10 04:16:13 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:10:14 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-10 04:09:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-10 04:06:45 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 04:06:23 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-10 04:05:33 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:05:15 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.005 |  |
| 2026-02-10 04:03:50 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:28 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:24 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:13 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:06 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-10 04:03:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:22 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 04:02:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:11 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:54 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:14 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-02-10 04:01:12 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-02-10 04:00:58 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:00:58 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.136 |  |
| 2026-02-10 04:00:56 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:00:53 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-02-10 04:00:52 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-02-10 04:00:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 04:01:12 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-02-10 03:07:34 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-10 04:09:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-10 03:05:21 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 03:15:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-10 04:06:23 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-10 04:06:45 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 04:02:22 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 03:04:54 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 04:28:48 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-10 03:01:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:05:33 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:54 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:31:01 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:00:56 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 03:25:49 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:00:58 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:13 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:16:13 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:11 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:28 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:02:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:00:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:01:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:40:58 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:50 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:03:24 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 04:05:15 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.005 |  |
| 2026-02-10 04:35:44 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.006 |  |
| 2026-02-10 04:10:14 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-10 04:03:06 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-10 04:00:52 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-02-10 04:01:14 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-10 04:00:58 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)