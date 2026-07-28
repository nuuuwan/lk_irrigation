# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_11:17:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 11:17:22 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:17:04 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:15:36 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:12:49 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:09:54 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-28 11:09:08 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:09:01 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:08:30 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.041 |  |
| 2026-07-28 11:07:53 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.081 |  |
| 2026-07-28 11:07:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-28 11:06:19 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-28 11:05:46 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 11:05:43 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-07-28 11:04:59 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:30 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 11:04:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:18 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:07 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:03 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-07-28 11:03:43 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:03:37 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:03:28 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-07-28 11:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.064 |  |
| 2026-07-28 11:02:43 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:41 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-07-28 11:02:27 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:16 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:00 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:56 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:24 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-07-28 11:01:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:00:48 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-28 11:00:30 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:00:30 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 11:02:41 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-07-28 11:07:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-28 11:09:54 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-28 11:06:19 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-28 11:00:48 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-28 11:04:30 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 11:05:46 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 11:02:16 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:09:08 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:00:30 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:00 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:17:22 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:17:04 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:27 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:43 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:12:49 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:09:01 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:01:56 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:15:36 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:02:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:18 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:07 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:03:37 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:04:59 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:03:43 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-28 11:05:43 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-07-28 11:03:28 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-07-28 11:04:03 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-07-28 11:01:24 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-07-28 11:00:30 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.016 |  |
| 2026-07-28 10:07:38 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.039 |  |
| 2026-07-28 11:08:30 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.041 |  |
| 2026-07-28 11:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.064 |  |
| 2026-07-28 11:07:53 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)