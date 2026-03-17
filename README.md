# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_09:05:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 09:05:47 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:05:36 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-17 09:04:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:04:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:04:41 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-03-17 09:04:15 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:04:08 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.077 |  |
| 2026-03-17 09:03:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-17 09:03:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:03:19 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 09:03:16 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 09:03:06 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:48 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:46 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-17 09:02:41 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.080 |  |
| 2026-03-17 09:02:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:06 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-03-17 09:02:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-03-17 09:01:59 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-17 09:01:11 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:01:04 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.055 |  |
| 2026-03-17 09:00:51 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.042 |  |
| 2026-03-17 09:00:44 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:00:33 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:21:54 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:20:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.067 |  |
| 2026-03-17 08:15:29 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-17 08:10:51 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 09:01:59 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-17 09:05:36 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-17 09:02:46 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-17 08:04:06 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 09:03:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-17 09:03:19 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 09:03:16 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 09:04:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:03:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:04:15 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:01:11 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:19 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:41 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:08:05 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:02:48 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:04:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:00:44 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:05:47 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:00:33 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 09:03:06 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:01:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:00 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:04:14 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:03:17 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:01:48 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-17 09:02:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-03-17 08:03:34 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-03-17 08:07:23 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-03-17 09:04:41 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-03-17 09:02:06 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.023 |  |
| 2026-03-17 08:05:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-03-17 09:00:51 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.042 |  |
| 2026-03-17 09:01:04 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.055 |  |
| 2026-03-17 08:20:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.067 |  |
| 2026-03-17 09:04:08 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.077 |  |
| 2026-03-17 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.080 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)