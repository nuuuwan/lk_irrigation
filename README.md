# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_20:35:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,573 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 20:35:14 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:26:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-19 20:12:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:10:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-04-19 20:09:20 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:09:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.172 |  |
| 2026-04-19 20:09:04 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-04-19 20:08:44 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-19 20:07:28 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:07:07 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-04-19 20:07:03 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:06:38 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-19 20:06:02 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-19 20:05:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:05:26 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 20:05:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 20:04:48 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:04:45 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:04:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:04:21 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:04:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:04:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-04-19 20:03:58 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:03:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-19 20:03:27 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:45 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-19 20:02:34 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:30 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:29 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:23 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:01:58 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:00:52 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-19 20:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.075 |  |
| 2026-04-19 20:00:35 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:00:16 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-19 20:00:15 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 20:03:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-19 20:05:26 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 20:26:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-19 20:06:02 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-19 20:00:52 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-19 20:00:16 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-19 20:05:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 20:12:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:04:21 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:35:14 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:03:58 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:03:27 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:00:35 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:34 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:23 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:05:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:30 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:04:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:07:03 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:04:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:02:29 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:09:20 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-19 20:08:44 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-04-19 20:09:04 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-04-19 20:06:38 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-19 20:02:45 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-19 20:07:28 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:01:58 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:04:48 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:04:45 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.011 |  |
| 2026-04-19 20:10:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-04-19 20:07:07 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-04-19 20:04:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-19 20:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.075 |  |
| 2026-04-19 20:09:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)