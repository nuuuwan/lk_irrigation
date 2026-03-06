# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_15:10:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,849 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 15:10:57 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:07:26 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-03-06 15:07:24 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:07:21 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:06:46 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:06:06 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:05:19 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:05:15 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:05:11 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:04:59 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-06 15:04:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-06 15:04:07 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:50 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:38 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:03:31 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:28 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 15:03:27 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:09 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:02:45 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:44 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-06 15:02:34 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:02:31 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:02:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:14 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 15:01:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:44 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:43 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:39 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:32 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.054 |  |
| 2026-03-06 15:01:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:31 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:26 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.085 |  |
| 2026-03-06 15:01:17 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:00:56 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:00:22 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-06 15:00:06 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 15:02:44 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-06 15:00:22 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-06 15:04:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-06 15:04:59 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-06 15:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 15:03:28 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 15:01:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:45 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:05:11 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:17 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:14 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:10:57 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:07:24 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:04:07 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:27 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:07:21 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:06:46 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:05:15 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:05:19 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:50 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:01:31 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:03:31 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:00:56 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:06:06 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:07:26 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-03-06 15:03:38 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:43 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:00:06 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:44 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:02:34 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:02:31 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:39 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:03:09 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-06 15:01:32 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.054 |  |
| 2026-03-06 15:01:26 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)