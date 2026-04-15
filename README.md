# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_23:13:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,128 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 23:13:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.150 |  |
| 2026-04-15 23:10:24 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-15 23:08:51 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-04-15 23:06:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:06:04 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-04-15 23:05:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:05:30 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-15 23:04:44 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:04:11 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-15 23:03:42 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:03:34 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-15 23:03:03 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:02:56 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:02:48 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.012 |  |
| 2026-04-15 23:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:02:38 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-04-15 23:02:29 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:02:27 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:02:17 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-04-15 23:02:13 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 23:01:58 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:32 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-15 23:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:01:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:00:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:00:29 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-15 23:00:21 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.063 |  |
| 2026-04-15 23:00:12 | Wellawaya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.580 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 23:00:12 | Wellawaya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-04-15 22:02:24 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-04-15 23:00:29 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-15 23:01:32 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-15 23:03:34 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-15 23:05:30 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-15 23:04:11 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-15 23:02:13 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 22:40:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-15 22:13:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-15 22:00:58 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 23:02:56 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:04:44 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:00:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:03:42 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:02:27 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:05:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:06:28 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:08:10 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:03:03 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:01:58 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:01:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:01:30 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:02:29 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-15 23:02:38 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-04-15 23:02:48 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.012 |  |
| 2026-04-15 23:08:51 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-04-15 23:06:04 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-04-15 23:02:17 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 23:10:24 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-15 23:00:21 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.063 |  |
| 2026-04-15 23:13:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)