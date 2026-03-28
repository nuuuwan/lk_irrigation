# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_14:09:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 14:09:42 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-28 14:09:36 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:09:02 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:08:39 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-03-28 14:08:37 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:07:42 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:07:40 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:07:25 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.093 |  |
| 2026-03-28 14:07:23 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:06:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.030 |  |
| 2026-03-28 14:06:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:05:55 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:04:55 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:03:58 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:03:48 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:03:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 14:03:42 | Rathnapura (Kalu Ganga) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-03-28 14:03:23 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.010 |  |
| 2026-03-28 14:03:20 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-28 14:03:07 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:43 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:41 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 14:02:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-28 14:02:35 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:35 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:32 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-28 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-03-28 14:02:08 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:01:59 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:01:49 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:01:37 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-28 14:01:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-28 14:00:45 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:00:44 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:00:23 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.101 |  |
| 2026-03-28 13:24:34 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.064 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 14:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-28 14:02:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-28 14:01:37 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-28 14:01:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-28 14:02:41 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-28 14:03:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 14:09:42 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-28 14:02:35 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:35 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 13:04:51 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:01:59 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:04:55 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:05:55 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:08:37 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:07:42 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:03:07 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:01:49 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:07:40 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:09:36 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:07:23 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:03:48 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:32 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:09:02 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:43 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:00:45 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:06:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:03:58 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:02:08 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 14:08:39 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-03-28 14:03:20 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-28 13:07:30 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-28 14:03:23 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.010 |  |
| 2026-03-28 13:00:41 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-03-28 14:03:42 | Rathnapura (Kalu Ganga) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-03-28 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-03-28 14:06:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.030 |  |
| 2026-03-28 13:00:44 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.052 |  |
| 2026-03-28 14:07:25 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.093 |  |
| 2026-03-28 14:00:23 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)