# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_17:23:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,225 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 17:23:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:17:42 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:14:54 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 17:14:17 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:12:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:10:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:10:19 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:08:51 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-12 17:08:47 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-12 17:08:39 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:07:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:07:23 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:06:10 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 17:06:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:05:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:05:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:04:17 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-04-12 17:04:00 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 17:08:47 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-12 17:03:48 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-12 17:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-12 17:03:21 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-12 17:01:21 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 17:08:51 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-12 17:02:49 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 17:01:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 17:01:28 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 17:01:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 17:01:56 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 17:06:10 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 17:14:54 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 17:10:19 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:01:23 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:17:42 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:23:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:10:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:02:14 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:03:25 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:03:32 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-04-12 16:12:44 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:03:33 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:05:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:01:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:05:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:08:39 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:06:00 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:07:23 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:00:56 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:00:35 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:04:00 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:12:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:14:17 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 17:04:17 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-04-12 17:01:59 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.031 |  |
| 2026-04-12 17:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.049 |  |
| 2026-04-12 17:03:31 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.064 |  |
| 2026-04-12 17:00:40 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)