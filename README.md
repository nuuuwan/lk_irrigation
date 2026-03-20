# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_04:33:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,057 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 04:33:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:28:23 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:19:57 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-03-21 04:10:26 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.014 |  |
| 2026-03-21 04:10:01 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-03-21 04:08:56 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-03-21 04:08:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:08:03 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-21 04:06:14 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:04:59 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:04:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:04:44 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-21 04:04:30 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-21 04:04:20 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:03:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-03-21 04:02:58 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-21 04:02:54 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.012 |  |
| 2026-03-21 04:02:49 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:02:41 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:02:33 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-03-21 04:02:18 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-03-21 04:02:11 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-21 04:02:03 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:01:38 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:01:32 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.090 |  |
| 2026-03-21 04:01:30 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 04:01:30 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:01:13 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 04:00:48 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:00:42 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:41:11 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.127 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 04:03:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-03-21 04:04:30 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-21 04:04:44 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-21 04:08:03 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-21 04:02:11 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-21 04:01:30 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 04:01:13 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:01:30 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:02:41 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:06:14 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 04:08:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:01:38 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:00:42 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:02:03 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 02:10:11 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:04:20 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:03 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:04:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:28:23 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:00:48 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:33:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:02:49 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:32 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:04:59 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-21 04:19:57 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.008 |  |
| 2026-03-21 04:08:56 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-03-21 04:02:58 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-21 04:02:54 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.012 |  |
| 2026-03-21 04:02:33 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-03-21 04:10:26 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.014 |  |
| 2026-03-21 04:10:01 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-03-21 04:02:18 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-03-21 03:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-03-21 04:01:32 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.090 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-21 03:04:01 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)