# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_09:01:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,689 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 09:01:37 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-01-19 09:01:25 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 09:01:19 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-19 09:01:14 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-01-19 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 09:00:14 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.031 |  |
| 2026-01-19 08:34:18 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:20:37 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:16:54 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:15:06 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.013 |  |
| 2026-01-19 08:13:49 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.018 |  |
| 2026-01-19 08:12:08 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-19 08:10:01 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:09:45 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.044 |  |
| 2026-01-19 08:08:14 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:07:49 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:07:39 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:06:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.087 |  |
| 2026-01-19 08:05:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.090 |  |
| 2026-01-19 08:05:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-19 08:05:15 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 08:05:01 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 08:05:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-19 08:01:21 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-19 08:02:19 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-19 08:03:30 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-19 08:04:20 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 08:05:15 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 08:02:53 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:00:41 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:03:46 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:10:01 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:04:46 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:16:54 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:01:11 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:20:37 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:01:12 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:07:49 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:07:39 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:01:48 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:04:29 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:34:18 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 09:01:19 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-19 09:01:25 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-19 08:12:08 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-19 08:01:55 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-01-19 08:01:16 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-01-19 08:01:09 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-01-19 09:01:37 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-01-19 08:13:49 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.018 |  |
| 2026-01-19 09:01:14 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-01-19 09:00:14 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.031 |  |
| 2026-01-19 08:05:01 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2026-01-19 08:02:32 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-01-19 08:09:45 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.044 |  |
| 2026-01-19 08:03:41 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.049 |  |
| 2026-01-19 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.050 |  |
| 2026-01-19 08:06:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.087 |  |
| 2026-01-19 08:05:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.090 |  |
| 2026-01-19 08:04:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)