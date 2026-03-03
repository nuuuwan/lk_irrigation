# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_20:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 20:15:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:12:49 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:10:04 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-03-03 20:09:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:09:27 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:07:16 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.068 |  |
| 2026-03-03 20:07:03 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:06:31 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:05:52 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:05:48 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:49 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:04:48 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:35 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:27 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 20:03:49 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:43 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-03 20:03:26 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.117 |  |
| 2026-03-03 20:03:24 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:21 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:15 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:03 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:02:54 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:02:40 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:02:16 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-03-03 20:02:16 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.030 |  |
| 2026-03-03 20:02:01 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:38 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 20:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-03-03 20:01:22 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:11 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:07 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:00:53 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:00:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 20:03:43 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-03 20:04:27 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 20:01:38 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 20:00:53 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:21 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:02:40 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:49 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:05:52 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:12:49 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:07 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:15 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:11 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:09:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:03:24 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:00:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:35 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:48 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:06:31 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:07:03 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:01:22 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:15:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:02:01 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:05:48 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:04:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:02:54 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:09:27 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:04:49 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:03:03 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-03 20:10:04 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-03-03 20:02:16 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-03-03 20:02:16 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.030 |  |
| 2026-03-03 20:01:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-03-03 20:07:16 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.068 |  |
| 2026-03-03 20:03:26 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)