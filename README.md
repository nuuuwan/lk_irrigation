# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_21:09:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,087 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 21:09:47 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.028 |  |
| 2026-02-05 21:08:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-05 21:08:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:08:00 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.026 |  |
| 2026-02-05 21:07:55 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-02-05 21:07:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-05 21:07:36 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | -0.065 |  |
| 2026-02-05 21:06:31 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 21:05:37 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.032 |  |
| 2026-02-05 21:05:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-05 21:05:16 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:05:10 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:04:52 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.105 |  |
| 2026-02-05 21:04:38 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:04:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:03:55 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.013 |  |
| 2026-02-05 21:03:53 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-02-05 21:03:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:03:41 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 1.914 | 🔺 Rising |
| 2026-02-05 21:03:25 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.090 |  |
| 2026-02-05 21:03:08 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:03:07 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:02:48 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 21:02:42 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:02:30 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:01:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 21:01:51 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 21:01:48 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.060 |  |
| 2026-02-05 21:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:00:32 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.042 |  |
| 2026-02-05 21:00:27 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:23:00 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 20:22:09 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.026 |  |
| 2026-02-05 20:21:35 | Padiyathalawa (Maduru Oya) | 1.95 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 21:03:41 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 1.914 | 🔺 Rising |
| 2026-02-05 21:07:55 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 21:08:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-05 21:01:52 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 21:06:31 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 21:01:51 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 21:02:48 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 21:00:27 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:02:30 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:03:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:02:42 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:04:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:03:08 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:03:07 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:05:16 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:05:10 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-05 18:04:13 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:08:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:04:38 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-05 21:05:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-05 18:05:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-05 21:03:53 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-02-05 21:03:55 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.013 |  |
| 2026-02-05 21:07:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-05 21:08:00 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.026 |  |
| 2026-02-05 21:09:47 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.028 |  |
| 2026-02-05 21:05:37 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.032 |  |
| 2026-02-05 21:00:32 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.042 |  |
| 2026-02-05 18:05:45 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.046 |  |
| 2026-02-05 21:01:48 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.060 |  |
| 2026-02-05 21:07:36 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | -0.065 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-05 21:03:25 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.090 |  |
| 2026-02-05 21:04:52 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.105 |  |
| 2026-02-05 20:18:29 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)