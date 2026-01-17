# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_11:18:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 11:18:09 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:17:15 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-01-17 11:13:29 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:12:32 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-17 11:11:49 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:09:58 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-17 11:06:55 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:06:13 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.089 |  |
| 2026-01-17 11:05:44 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:05:38 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:05:21 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:05:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:58 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-01-17 11:04:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-17 11:04:33 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:26 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-17 11:04:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.049 |  |
| 2026-01-17 11:04:10 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:03:18 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:03:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:03:10 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-01-17 11:03:08 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-01-17 11:02:35 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-17 11:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:25 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:21 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 11:02:11 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-01-17 11:02:07 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:01:55 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:01:32 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-17 11:01:29 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-01-17 11:01:26 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:35:11 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:25:04 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 11:01:29 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-01-17 11:01:32 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-17 11:02:35 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-17 11:12:32 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-17 11:04:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-17 11:09:58 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-17 11:02:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 11:03:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:01:26 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:11 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:09:42 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:01:55 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:25 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:05:21 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:21 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:18:09 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:05:38 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:02:07 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:33 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:06:55 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:03:18 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:04:10 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:11:49 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:03:08 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:13:29 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:25:04 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:05:44 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:17:15 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-01-17 11:04:26 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-17 11:04:58 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-01-17 11:03:10 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-01-17 11:02:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-01-17 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-01-17 11:04:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.049 |  |
| 2026-01-17 11:06:13 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)