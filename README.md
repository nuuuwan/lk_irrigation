# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_06:13:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,128 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 06:13:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:11:59 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-03-21 06:10:58 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:10:37 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-21 06:09:35 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:07:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-21 06:07:07 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-21 06:05:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:05:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.186 |  |
| 2026-03-21 06:05:13 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 06:05:12 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:04:32 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:04:25 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-21 06:04:01 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:36 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-21 06:03:35 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.141 |  |
| 2026-03-21 06:03:26 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:19 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:01 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:02:54 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 06:02:54 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 16.800 | 🔺 Rising |
| 2026-03-21 06:02:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 16.800 | 🔺 Rising |
| 2026-03-21 06:02:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:02:31 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:02:24 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-21 06:02:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:02:13 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-21 06:01:45 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:01:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:01:26 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.164 |  |
| 2026-03-21 06:01:25 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:01:18 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.070 |  |
| 2026-03-21 06:01:12 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:00:59 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.028 |  |
| 2026-03-21 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 05:41:53 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 05:30:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 06:02:54 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 16.800 | 🔺 Rising |
| 2026-03-21 06:07:07 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-21 06:03:36 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-21 06:02:24 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-21 06:04:25 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 06:02:54 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 06:05:13 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 06:01:12 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:01:18 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:13:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:05:12 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:26 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:04:01 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 02:10:11 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:09:35 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:10:58 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-21 05:06:38 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:01:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:02:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:19 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:03:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:01:45 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:02:31 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-21 06:11:59 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-03-21 06:10:37 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-21 06:04:32 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:02:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:01:25 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:05:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-21 06:02:13 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-21 06:00:59 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.028 |  |
| 2026-03-21 06:07:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-21 06:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.070 |  |
| 2026-03-21 06:03:35 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.141 |  |
| 2026-03-21 06:01:26 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.164 |  |
| 2026-03-21 06:05:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)