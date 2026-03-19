# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_18:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,826 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 18:15:48 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.008 |  |
| 2026-03-19 18:13:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-03-19 18:10:20 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 18:08:58 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:08:40 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-19 18:07:06 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-19 18:05:53 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.124 |  |
| 2026-03-19 18:05:39 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:05:33 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:05:21 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 18:04:47 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:04:24 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:04:11 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:04:10 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-03-19 18:04:00 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 18:03:54 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:40 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:37 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-03-19 18:03:31 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:04 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 18:02:43 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-19 18:02:43 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.052 |  |
| 2026-03-19 18:02:27 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:02:26 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-03-19 18:02:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 18:02:05 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-03-19 18:01:51 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-03-19 18:01:50 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.133 |  |
| 2026-03-19 18:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:29 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:06 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:00:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:00:38 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-03-19 18:00:31 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:00:21 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:54:59 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:43:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 18:02:05 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-03-19 18:07:06 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-19 18:08:40 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-19 18:05:21 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 18:03:04 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 18:04:00 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 18:10:20 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 18:01:29 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:00:31 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:04:24 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:00:21 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:40 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:08:58 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:05:33 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:54 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:00:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:06 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:02:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:04:47 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:04:11 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:05:39 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:15:48 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.008 |  |
| 2026-03-19 18:03:31 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-19 18:03:37 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-03-19 18:02:43 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-19 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.021 |  |
| 2026-03-19 18:01:51 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-03-19 18:02:26 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-03-19 18:00:38 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-03-19 18:13:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-03-19 18:04:10 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-03-19 18:02:43 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.052 |  |
| 2026-03-19 18:05:53 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.124 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 18:01:50 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)