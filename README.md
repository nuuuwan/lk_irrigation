# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_06:12:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,573 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 06:12:13 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:11:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:10:32 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:10:13 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-31 06:08:37 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.063 |  |
| 2025-12-31 06:07:31 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2025-12-31 06:06:22 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:06:19 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:06:12 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:05:56 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:05:47 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | -0.002 |  |
| 2025-12-31 06:05:38 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:04:59 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2025-12-31 06:04:23 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:04:17 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.009 |  |
| 2025-12-31 06:04:16 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 06:04:12 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:04:08 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2025-12-31 06:04:06 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.022 |  |
| 2025-12-31 06:03:59 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:03:54 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-31 06:02:19 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:02:17 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 1.101 | 🔺 Rising |
| 2025-12-31 06:02:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2025-12-31 06:02:04 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:02:00 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.049 |  |
| 2025-12-31 06:01:35 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:01:32 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.104 |  |
| 2025-12-31 06:01:24 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:01:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:01:06 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:00:58 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 06:00:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.176 |  |
| 2025-12-31 06:00:29 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:00:27 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.235 |  |
| 2025-12-31 05:53:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 05:30:37 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.063 |  |
| 2025-12-31 05:26:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.176 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 06:02:17 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 1.101 | 🔺 Rising |
| 2025-12-31 06:03:54 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-31 06:10:13 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-31 06:01:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 06:04:16 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 06:00:58 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:06:22 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:04:23 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:11:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:04:12 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:01:35 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:06:19 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:05:56 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:12:13 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:02:19 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:10:32 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:01:06 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:05:38 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:01:24 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 06:05:47 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | -0.002 |  |
| 2025-12-31 06:04:17 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.009 |  |
| 2025-12-31 06:03:59 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:02:04 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:06:12 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-31 06:00:29 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-31 05:02:47 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2025-12-31 06:07:31 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2025-12-31 06:04:59 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2025-12-31 06:04:06 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.022 |  |
| 2025-12-31 06:02:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2025-12-31 06:04:08 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2025-12-31 06:02:00 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.049 |  |
| 2025-12-31 06:08:37 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.063 |  |
| 2025-12-31 06:01:32 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.104 |  |
| 2025-12-31 06:00:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.176 |  |
| 2025-12-31 06:00:27 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)