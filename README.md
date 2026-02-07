# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_21:26:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 21:26:26 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.008 |  |
| 2026-02-07 21:19:41 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.060 |  |
| 2026-02-07 21:19:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:16:04 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:11:57 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-02-07 21:11:24 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.037 |  |
| 2026-02-07 21:11:09 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-02-07 21:10:13 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:08:50 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-02-07 21:08:27 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:08:15 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-02-07 21:07:40 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:06:59 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:06:27 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:06:07 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-07 21:05:46 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-07 21:05:23 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.085 |  |
| 2026-02-07 21:04:54 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:04:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-02-07 21:03:32 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:08 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 21:03:05 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.061 |  |
| 2026-02-07 21:02:59 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:02:51 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-07 21:02:50 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:02:45 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.068 |  |
| 2026-02-07 21:02:45 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:01:53 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.030 |  |
| 2026-02-07 21:01:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:01:34 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:00:47 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:00:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:00:07 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 21:11:57 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-02-07 21:02:51 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-07 21:06:07 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-07 21:05:46 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-07 21:03:08 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 21:00:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:11:09 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:01:34 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:16:04 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:07:40 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:32 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:06:59 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:12 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:03:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:19:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:01:43 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:04:54 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 21:26:26 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.008 |  |
| 2026-02-07 21:10:13 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:02:45 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:08:27 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:00:07 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:06:27 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:00:47 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:08:50 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-02-07 21:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-02-07 21:08:15 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-07 21:01:53 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.030 |  |
| 2026-02-07 21:11:24 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.037 |  |
| 2026-02-07 21:04:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-02-07 21:19:41 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.060 |  |
| 2026-02-07 21:03:05 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.061 |  |
| 2026-02-07 21:02:45 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.068 |  |
| 2026-02-07 21:05:23 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)