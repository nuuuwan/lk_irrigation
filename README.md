# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_09:06:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 09:06:07 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.242 |  |
| 2026-02-24 09:05:55 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:05:26 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-02-24 09:05:18 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:04:49 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-02-24 09:04:39 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:04:20 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.068 |  |
| 2026-02-24 09:03:32 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2026-02-24 09:03:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:27 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-24 09:03:27 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 09:03:27 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.022 |  |
| 2026-02-24 09:03:25 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:13 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 09:03:08 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 09:03:05 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:02:53 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.121 |  |
| 2026-02-24 09:02:48 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-02-24 09:02:47 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:02:32 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:30 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 09:02:29 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:20 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:16 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:10 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:00 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2026-02-24 09:01:41 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:01:39 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-02-24 09:01:25 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2026-02-24 09:01:17 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:01:10 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:00:52 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:00:27 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-24 09:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 08:51:35 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 08:28:52 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.008 |  |
| 2026-02-24 08:17:53 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-02-24 08:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.068 |  |
| 2026-02-24 08:09:52 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 09:00:27 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-24 09:03:08 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 09:03:27 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-24 09:03:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 09:03:27 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 09:02:30 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 09:04:39 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:05:55 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:05 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-24 08:05:45 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:13 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:03:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:02:47 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 09:04:20 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 08:28:52 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.008 |  |
| 2026-02-24 09:02:29 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:32 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:01:41 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:01:17 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:05:18 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:16 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:20 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:01:10 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:00:52 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:02:10 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-24 09:01:39 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-02-24 08:08:30 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.012 |  |
| 2026-02-24 09:03:32 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2026-02-24 09:02:48 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-02-24 09:02:00 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2026-02-24 09:03:27 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.022 |  |
| 2026-02-24 09:04:49 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.028 |  |
| 2026-02-24 09:05:26 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-02-24 09:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.068 |  |
| 2026-02-24 09:01:25 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2026-02-24 09:02:53 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.121 |  |
| 2026-02-24 09:06:07 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)