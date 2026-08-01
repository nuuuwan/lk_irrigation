# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_21:06:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,329 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 21:06:48 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-08-01 21:06:37 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.184 |  |
| 2026-08-01 21:05:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:05:36 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-01 21:05:27 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.079 |  |
| 2026-08-01 21:04:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:04:50 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.067 |  |
| 2026-08-01 21:04:23 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:04:22 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.059 |  |
| 2026-08-01 21:04:11 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:03:25 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-08-01 21:03:08 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.040 |  |
| 2026-08-01 21:02:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:50 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:43 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.168 |  |
| 2026-08-01 21:02:38 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-08-01 21:02:36 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:24 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:19 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.100 |  |
| 2026-08-01 21:02:16 | Hanwella (Kelani Ganga) | 5.12 | 🟢 Normal | -0.180 |  |
| 2026-08-01 21:01:46 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | -0.010 |  |
| 2026-08-01 21:01:33 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-08-01 21:01:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:01:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 21:01:09 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.041 |  |
| 2026-08-01 21:00:43 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 21:00:26 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-08-01 20:30:55 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:20:43 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.140 |  |
| 2026-08-01 20:20:05 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.067 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 21:00:26 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-08-01 21:00:43 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 21:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 21:02:36 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:05:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:04:11 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:01:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:39 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:08:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:09:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:54 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:04:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:01:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:24 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:04:23 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:06:44 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:02:50 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:01:09 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 21:05:36 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-01 21:01:46 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | -0.010 |  |
| 2026-08-01 21:02:38 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-08-01 21:06:48 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-08-01 21:01:33 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-08-01 21:03:08 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.040 |  |
| 2026-08-01 21:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.041 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 21:04:22 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.059 |  |
| 2026-08-01 21:03:25 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-08-01 21:04:50 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.067 |  |
| 2026-08-01 21:05:27 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.079 |  |
| 2026-08-01 21:02:19 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.100 |  |
| 2026-08-01 20:20:43 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.140 |  |
| 2026-08-01 21:02:43 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.168 |  |
| 2026-08-01 21:02:16 | Hanwella (Kelani Ganga) | 5.12 | 🟢 Normal | -0.180 |  |
| 2026-08-01 21:06:37 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.184 |  |
| 2026-08-01 20:05:34 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.398 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)