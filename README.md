# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_17:05:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,617 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 17:05:40 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:05:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:05:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.088 |  |
| 2026-03-30 17:04:59 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 17:04:37 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:04:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:03:43 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:03:35 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:03:27 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-03-30 17:03:20 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-30 17:02:54 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-30 17:02:48 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:44 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-03-30 17:02:41 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.035 |  |
| 2026-03-30 17:02:30 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:15 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:15 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-03-30 17:01:59 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:01:49 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:01:28 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.043 |  |
| 2026-03-30 17:01:27 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:01:25 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2026-03-30 17:01:21 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:01:17 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-30 17:00:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:00:35 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:00:35 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 16:12:33 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 17:03:20 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-30 16:04:10 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-30 16:10:27 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-30 17:04:59 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 17:02:54 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-30 16:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 17:01:49 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:01:21 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 16:06:41 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:03:35 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:01:27 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:15 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-30 16:07:54 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:05:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:05:40 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:00:35 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 16:01:47 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:04:37 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:48 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:00:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:03:43 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:30 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:15 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:04:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 16:04:03 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:01:59 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-30 16:03:08 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:00:35 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:01:17 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-30 17:03:27 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-03-30 16:08:21 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.018 |  |
| 2026-03-30 16:08:49 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-03-30 17:02:44 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-03-30 17:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-03-30 15:08:07 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-03-30 17:02:41 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.035 |  |
| 2026-03-30 17:01:28 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.043 |  |
| 2026-03-30 17:05:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.088 |  |
| 2026-03-30 17:01:25 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)