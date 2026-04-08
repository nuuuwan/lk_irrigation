# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_16:28:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 16:28:27 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:17:12 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.025 |  |
| 2026-04-08 16:15:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-08 16:10:41 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-04-08 16:10:16 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:07:32 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-08 16:07:26 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-08 16:07:07 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-04-08 16:06:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:06:18 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.083 |  |
| 2026-04-08 16:06:12 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:06:04 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-08 16:05:31 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:05:03 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.019 |  |
| 2026-04-08 16:04:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-08 16:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-08 16:04:32 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.014 |  |
| 2026-04-08 16:04:22 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-08 16:04:20 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 16:04:19 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-08 16:04:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:04:11 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:57 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:45 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-08 16:03:38 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:30 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:30 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-08 16:03:22 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:20 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:07 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:02:48 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-08 16:02:32 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-08 16:02:28 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:02:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:02:24 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:01:56 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:01:41 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:00:56 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:00:48 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.108 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 16:07:26 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-08 16:04:22 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-08 16:15:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-08 16:04:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-08 16:04:19 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-08 16:03:30 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-08 16:07:32 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-08 16:04:20 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 16:01:41 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:06:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:02:28 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:00:56 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:22 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:10:16 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:28:27 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:01:56 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:30 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:05:31 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:57 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:02:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:20 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:04:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:06:12 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:04:11 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:03:07 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-08 16:10:41 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-04-08 16:02:48 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-08 16:03:45 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-08 16:02:32 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-08 16:04:32 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.014 |  |
| 2026-04-08 16:07:07 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-04-08 16:05:03 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.019 |  |
| 2026-04-08 16:06:04 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-08 16:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-08 16:17:12 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.025 |  |
| 2026-04-08 15:30:43 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.034 |  |
| 2026-04-08 16:06:18 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.083 |  |
| 2026-04-08 16:00:48 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)