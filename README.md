# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_23:39:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 23:39:24 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:21:07 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:20:24 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-16 23:18:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:16:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.037 |  |
| 2026-02-16 23:12:53 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:12:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:09:16 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:08:56 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:07:06 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:06:12 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:06:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-16 23:05:06 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:04:30 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:04:27 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:04:26 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-16 23:04:00 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:03:53 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-02-16 23:03:34 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:03:08 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:02:38 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-02-16 23:02:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:02:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:02:02 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:01:55 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:54 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-02-16 23:01:53 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:43 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:40 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:12 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.042 |  |
| 2026-02-16 23:01:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-02-16 23:00:47 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.017 |  |
| 2026-02-16 23:00:21 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 23:06:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-16 23:04:26 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-16 23:00:21 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 23:20:24 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-16 23:01:40 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-16 22:02:59 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:43 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:05:06 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:03:59 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:09:16 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:04:00 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:06:12 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:53 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:39:24 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:08:56 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:12:53 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:21:07 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:03:34 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:02:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:07:06 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:01:36 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:01:55 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:03:08 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:04:30 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:18:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:04:27 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:12:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:02:02 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-16 22:03:35 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:03:53 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-02-16 23:00:47 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.017 |  |
| 2026-02-16 23:01:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-02-16 23:02:38 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-02-16 23:01:54 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-02-16 23:16:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.037 |  |
| 2026-02-16 23:01:12 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.042 |  |
| 2026-02-16 21:03:28 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.070 |  |
| 2026-02-16 18:00:50 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)