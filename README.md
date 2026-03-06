# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_11:21:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 11:21:14 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:19:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:16:24 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:11:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:10:26 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:10:25 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.053 |  |
| 2026-03-06 11:10:13 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-03-06 11:09:24 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-03-06 11:09:11 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-03-06 11:07:20 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:06:46 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:06:20 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.009 |  |
| 2026-03-06 11:06:09 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-06 11:05:48 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-06 11:05:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:04:49 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-06 11:04:37 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:04:27 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-03-06 11:04:13 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-06 11:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-03-06 11:03:16 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-06 11:03:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:55 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:48 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:54 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:49 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 11:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:20 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-03-06 11:01:17 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:16 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-06 11:01:15 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:00:38 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 11:04:27 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-03-06 11:04:49 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-06 11:06:09 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-06 10:06:00 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-06 11:03:16 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-06 11:05:48 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-06 11:04:13 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-06 11:01:49 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 11:00:38 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:54 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:16:24 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:21:14 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:19:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:04:37 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:07:20 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:05:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:03:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:48 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:55 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:17 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:02:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:06:46 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 10:06:17 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:01:15 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:10:26 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:11:40 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 11:09:24 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-03-06 11:09:11 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-03-06 11:06:20 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.009 |  |
| 2026-03-06 11:01:16 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-06 11:10:13 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-03-06 11:01:20 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-03-06 10:19:07 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.016 |  |
| 2026-03-06 11:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-03-06 11:10:25 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)