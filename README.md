# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_16:11:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,156 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 16:11:42 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-03-15 16:07:56 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-03-15 16:07:24 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:07:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:07:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:07:10 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-03-15 16:07:02 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-15 16:06:49 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:06:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 16:06:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-03-15 16:05:57 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:05:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:23 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 16:05:16 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:14 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:11 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 16:05:04 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-03-15 16:04:56 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-15 16:04:47 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:04:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:04:27 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-15 16:03:52 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:03:41 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:03:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-03-15 16:03:00 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.020 |  |
| 2026-03-15 16:02:55 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-15 16:02:39 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.113 |  |
| 2026-03-15 16:02:38 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:02:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:02:10 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:52 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:01:37 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:21 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:15 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:10 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:00:51 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:00:25 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.126 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 16:04:27 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-15 16:07:02 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-15 16:02:55 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-15 16:06:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 16:05:23 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 16:05:11 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 16:02:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:15 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:07:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:16 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:04:47 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:14 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:37 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:06:49 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:00:51 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:21 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:03:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:02:10 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:07:24 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:04 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-03-15 16:03:52 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:02:38 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:03:41 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:04:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:05:57 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:01:52 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:01:10 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:07:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-03-15 16:04:56 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-15 16:03:00 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.020 |  |
| 2026-03-15 16:07:10 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-03-15 16:07:56 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-03-15 16:06:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-03-15 16:11:42 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-03-15 16:02:39 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.113 |  |
| 2026-03-15 16:00:25 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)