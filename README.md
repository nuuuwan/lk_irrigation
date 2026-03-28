# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_15:13:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,763 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 15:13:52 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.015 |  |
| 2026-03-28 15:11:26 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:08:09 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:07:22 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:05:29 | Rathnapura (Kalu Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-03-28 15:05:20 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:05:12 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2026-03-28 15:04:25 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:04:25 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:04:16 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:57 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:03:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-03-28 15:03:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:17 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:03:13 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:12 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:04 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:04 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:00 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:49 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:44 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:36 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:35 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-03-28 15:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:02:20 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 15:02:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:58 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:47 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:46 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:01:36 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:00:55 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:00:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:00:39 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-28 15:00:12 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.211 |  |
| 2026-03-28 15:00:04 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 15:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-28 15:02:20 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 15:07:22 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:58 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:04 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:47 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:08:09 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:00 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:04:16 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:13 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:12 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:04:25 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:04:25 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:00:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:04 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:44 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:05:20 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:11:26 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:00:39 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:00:55 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:01:36 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:49 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:02:36 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 15:03:57 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:03:17 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:01:46 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:01:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-03-28 15:13:52 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.015 |  |
| 2026-03-28 15:05:29 | Rathnapura (Kalu Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-03-28 15:03:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-03-28 15:02:35 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-03-28 15:05:12 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2026-03-28 15:00:12 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)