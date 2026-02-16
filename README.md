# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_00:25:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 00:25:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:25:15 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:25:13 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:19:38 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-02-17 00:15:22 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:14:28 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-02-17 00:14:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-02-17 00:12:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:11:39 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:10:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-17 00:09:24 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-17 00:09:06 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:08:38 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:06:51 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:06:16 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:06:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:05:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:05:39 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:05:39 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-02-17 00:05:26 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 27.771 | 🔺 Rising |
| 2026-02-17 00:05:12 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-17 00:04:58 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:47 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-17 00:04:46 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-02-17 00:04:37 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-02-17 00:04:35 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.029 |  |
| 2026-02-17 00:04:16 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:15 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:13 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-02-17 00:03:47 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:03:47 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 00:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:03:41 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 00:03:41 | Thawalama (Gin Ganga) | 0.26 | 🟢 Normal | 27.771 | 🔺 Rising |
| 2026-02-17 00:02:36 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:02:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-17 00:02:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:01:50 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-02-17 00:01:41 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:01:38 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 23:39:24 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 00:05:26 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 27.771 | 🔺 Rising |
| 2026-02-17 00:19:38 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-02-17 00:04:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-02-17 00:04:47 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-17 00:02:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-17 00:03:41 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 00:03:47 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 00:10:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-16 23:20:24 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-17 00:02:36 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:01:41 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:16 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:11:39 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:03:59 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:25:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:08:38 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:06:16 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:09:06 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:04:58 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:06:51 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:01:38 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:05:39 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:05:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:06:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:01:36 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:15:22 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:02:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:03:47 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:12:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-17 00:09:24 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-17 00:05:12 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-17 00:01:50 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-02-16 23:12:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-17 00:05:39 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-02-17 00:04:37 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-02-17 00:04:46 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-02-17 00:04:35 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.029 |  |
| 2026-02-16 18:00:50 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)