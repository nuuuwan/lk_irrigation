# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_17:34:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 17:34:44 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.007 |  |
| 2026-02-03 17:21:54 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-03 17:19:10 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-02-03 17:09:37 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-03 17:09:04 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:08:32 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-03 17:08:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:08:03 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-02-03 17:07:25 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:05:19 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:05:18 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:04:31 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 16.143 | 🔺 Rising |
| 2026-02-03 17:04:04 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:03:57 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-02-03 17:03:32 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-03 17:03:22 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:03:20 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-02-03 17:03:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-03 17:02:57 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:02:47 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-03 17:02:38 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-02-03 17:02:00 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:01:28 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:01:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.072 |  |
| 2026-02-03 17:01:06 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.012 |  |
| 2026-02-03 17:00:48 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 16.143 | 🔺 Rising |
| 2026-02-03 17:00:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.139 |  |
| 2026-02-03 17:00:22 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 17:04:31 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 16.143 | 🔺 Rising |
| 2026-02-03 17:03:57 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-02-03 17:09:37 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 17:21:54 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 17:08:32 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-03 17:03:32 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-03 17:02:00 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:01:28 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:09:04 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:07:25 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:03:22 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:02:57 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:05:19 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:08:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:04:04 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 17:34:44 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.007 |  |
| 2026-02-03 17:19:10 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 17:08:03 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-02-03 17:03:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-03 06:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-03 17:02:47 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-03 17:01:06 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.012 |  |
| 2026-02-03 17:02:38 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-03 17:03:20 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-02-03 06:04:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.064 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 17:00:22 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | -0.071 |  |
| 2026-02-03 17:01:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.072 |  |
| 2026-02-03 17:00:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.139 |  |
| 2026-02-03 06:01:58 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)