# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_04:12:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,630 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 04:12:02 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-22 04:09:36 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-22 04:08:14 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-22 04:08:08 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-04-22 04:08:03 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-04-22 04:06:55 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.128 |  |
| 2026-04-22 04:06:01 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-04-22 04:05:17 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-22 04:04:52 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.078 |  |
| 2026-04-22 04:04:19 | Thanamalwila (Kirindi Oya) | 2.35 | 🟢 Normal | -0.250 |  |
| 2026-04-22 04:04:09 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-22 04:03:37 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-22 04:03:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:03:30 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:03:07 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:02:53 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-22 04:02:41 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.049 |  |
| 2026-04-22 04:02:37 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-04-22 04:02:34 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-22 04:02:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:01:42 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.182 |  |
| 2026-04-22 04:01:10 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-22 04:01:10 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:00:51 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-22 04:00:34 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 04:00:28 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.168 |  |
| 2026-04-22 03:41:39 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.078 |  |
| 2026-04-22 03:32:58 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-22 04:04:09 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-22 04:03:37 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-22 04:09:36 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-22 04:05:17 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-22 04:12:02 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-22 04:01:10 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 04:00:34 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 23:01:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 03:04:32 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 04:02:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:06:01 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:02:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:05:11 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:01:10 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:03:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:03:07 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:12:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-22 04:03:30 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:06:47 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.006 |  |
| 2026-04-22 04:08:14 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-22 03:04:58 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.017 |  |
| 2026-04-22 04:02:34 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-22 04:02:53 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-22 04:08:03 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-04-22 04:00:51 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-22 04:02:37 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-04-22 04:08:08 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-04-22 04:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-04-22 03:01:07 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.044 |  |
| 2026-04-22 04:02:41 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.049 |  |
| 2026-04-22 04:04:52 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.078 |  |
| 2026-04-22 04:06:55 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.128 |  |
| 2026-04-22 03:01:14 | Kuda Oya (Kirindi Oya) | 2.68 | 🟢 Normal | -0.150 |  |
| 2026-04-22 04:00:28 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.168 |  |
| 2026-04-22 04:01:42 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.182 |  |
| 2026-04-22 04:04:19 | Thanamalwila (Kirindi Oya) | 2.35 | 🟢 Normal | -0.250 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)