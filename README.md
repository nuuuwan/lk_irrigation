# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_05:36:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,722 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 05:36:22 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -180.000 |  |
| 2026-03-15 05:36:21 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -180.000 |  |
| 2026-03-15 05:27:44 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.004 |  |
| 2026-03-15 05:19:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:09:53 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 05:08:20 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.051 |  |
| 2026-03-15 05:08:20 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 05:08:12 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 05:06:43 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:06:00 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 05:05:55 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.016 |  |
| 2026-03-15 05:05:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:04:26 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:03:45 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:03:37 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:03:34 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:03:31 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-03-15 05:03:23 | Dunamale (Aththanagalu Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-03-15 05:03:20 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:03:11 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-15 05:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-15 05:02:46 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:02:36 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:02:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:02:31 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-03-15 05:02:11 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 05:01:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-15 05:01:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:01:28 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-03-15 05:01:11 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:00:43 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.030 |  |
| 2026-03-15 05:00:31 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:00:13 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.136 |  |
| 2026-03-15 04:45:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 04:35:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-03-15 05:02:11 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 05:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-15 05:01:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-15 05:08:20 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 05:08:12 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 05:03:11 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-15 05:09:53 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 05:06:00 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 05:27:44 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.004 |  |
| 2026-03-15 05:19:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:02:36 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:02:11 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:02:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:01:11 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:00:31 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:02:46 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:05:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:03:37 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:20:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:04:26 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:06:43 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:14 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 05:03:45 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:01:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:03:34 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:03:20 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-03-15 05:05:55 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.016 |  |
| 2026-03-15 05:03:31 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-03-15 05:03:23 | Dunamale (Aththanagalu Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-03-15 05:00:43 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.030 |  |
| 2026-03-15 05:01:28 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-03-15 05:02:31 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-03-15 05:08:20 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.051 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-15 05:00:13 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.136 |  |
| 2026-03-15 05:36:22 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)