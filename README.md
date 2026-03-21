# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_14:11:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 14:11:38 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:11:01 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:10:12 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-03-21 14:07:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-03-21 14:07:31 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-03-21 14:07:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:06:51 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.059 |  |
| 2026-03-21 14:06:44 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:06:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-03-21 14:05:26 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.101 |  |
| 2026-03-21 14:04:57 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-21 14:03:56 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.044 |  |
| 2026-03-21 14:03:52 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:03:44 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:03:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-03-21 14:02:59 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-21 14:02:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 14:02:53 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:02:36 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-21 14:02:32 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.050 |  |
| 2026-03-21 14:02:29 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:53 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-03-21 14:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:37 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:01:27 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.129 |  |
| 2026-03-21 14:01:16 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:01:11 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:01 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:00:57 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:00:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:00:16 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:59:21 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 13:23:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 14:10:12 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-03-21 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-21 14:02:36 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-21 14:02:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 13:59:21 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 14:01:11 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:03:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:00:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:02:53 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:07:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:02:29 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 13:02:48 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:37 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:53 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 12:01:39 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:00:16 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:11:01 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:11:38 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:03:44 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:00:57 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:01:01 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-21 14:07:31 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-03-21 14:04:57 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:03:52 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:01:16 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-21 13:02:59 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-21 14:07:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-03-21 14:02:59 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-21 13:13:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-03-21 14:06:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-03-21 14:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.029 |  |
| 2026-03-21 14:03:56 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.044 |  |
| 2026-03-21 14:02:32 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.050 |  |
| 2026-03-21 14:01:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-03-21 14:06:51 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.059 |  |
| 2026-03-21 14:05:26 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.101 |  |
| 2026-03-21 14:01:27 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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