# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_00:18:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 00:18:43 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.027 |  |
| 2026-03-17 00:11:38 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-17 00:10:19 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:10:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-17 00:08:55 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-17 00:08:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:08:23 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:07:39 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.016 |  |
| 2026-03-17 00:07:11 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:06:41 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 00:05:53 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:05:17 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:04:33 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-03-17 00:04:27 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-17 00:04:08 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:03:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:03:42 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-17 00:03:15 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:43 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:19 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:18 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.005 |  |
| 2026-03-17 00:02:17 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:11 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:07 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:02 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:51 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:37 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:19 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:15 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-17 00:01:10 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:06 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 00:01:15 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-16 23:05:12 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-17 00:10:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-17 00:03:42 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-17 00:08:55 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-17 00:06:41 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 00:11:38 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-17 00:07:11 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:19 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:03:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-16 23:06:52 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:37 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:02 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:11 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:05:53 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:04:08 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:51 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:07 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 23:03:21 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:43 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:10:19 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:17 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:08:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:03:15 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:01:10 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:08:23 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:19 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 21:00:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-17 00:02:18 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | -0.005 |  |
| 2026-03-17 00:01:06 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.010 |  |
| 2026-03-17 00:04:27 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:06:25 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-17 00:07:39 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.016 |  |
| 2026-03-17 00:04:33 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-03-17 00:18:43 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.027 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)