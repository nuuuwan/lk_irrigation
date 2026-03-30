# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_15:08:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 15:08:07 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-03-30 15:07:35 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:06:36 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-03-30 15:06:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.058 |  |
| 2026-03-30 15:05:47 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:05:43 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:05:01 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 15:04:38 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:04:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:04:10 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 15:03:53 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-03-30 15:03:40 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-03-30 15:03:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:03:25 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.041 |  |
| 2026-03-30 15:03:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:03:05 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:02:50 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:48 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:02:46 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:44 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 15:02:34 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:29 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:26 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:21 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:15 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:50 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:47 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-30 15:01:44 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:44 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:35 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 15:01:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:09 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:00:59 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:00:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:00:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:00:39 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:00:35 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:00:19 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.149 |  |
| 2026-03-30 15:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-30 15:00:07 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.064 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 15:00:07 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-30 15:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-30 15:01:47 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-30 15:04:10 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 15:05:01 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 15:01:35 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 15:02:44 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 15:01:44 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:50 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:29 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:00:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:09 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:50 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:07:35 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:00:59 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:03:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:34 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:21 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:46 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:03:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:05:47 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:05:43 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:44 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:04:38 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:01:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:15 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-30 15:04:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:00:35 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:02:48 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:03:05 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:00:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-03-30 15:06:36 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-03-30 15:08:07 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-03-30 15:03:40 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-03-30 15:03:53 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-03-30 15:03:25 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.041 |  |
| 2026-03-30 15:06:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.058 |  |
| 2026-03-30 15:00:19 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)