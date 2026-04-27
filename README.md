# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_06:32:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,180 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 06:32:39 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.002 |  |
| 2026-04-27 06:23:54 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.015 |  |
| 2026-04-27 06:21:45 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:19:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-27 06:09:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:08:03 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:07:34 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-27 06:07:10 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.191 |  |
| 2026-04-27 06:06:56 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-27 06:06:46 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 06:06:34 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:05:55 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-27 06:05:06 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 06:05:03 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-27 06:04:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:04:38 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 06:04:03 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:04:03 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.060 |  |
| 2026-04-27 06:03:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.025 |  |
| 2026-04-27 06:03:36 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:03:28 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-04-27 06:03:12 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-27 06:02:58 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-27 06:02:47 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:02:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-27 06:02:14 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.368 |  |
| 2026-04-27 06:01:55 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-27 06:01:43 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-27 06:01:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 06:01:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 06:01:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:00:54 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-04-27 06:00:41 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.038 |  |
| 2026-04-27 06:00:12 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.048 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 06:05:03 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-27 06:03:12 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-27 06:01:55 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-27 06:02:58 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-27 06:06:56 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-27 06:07:34 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-27 06:00:12 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-27 06:01:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 06:05:06 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 05:04:44 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 06:01:43 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-27 06:04:38 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 06:05:55 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-27 06:19:39 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-27 06:01:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 06:00:41 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 06:06:46 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 06:01:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:02:47 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:04:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:21:45 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:08:03 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:09:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:03:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:04:03 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:03:36 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 06:32:39 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.002 |  |
| 2026-04-27 06:02:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-27 06:23:54 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.015 |  |
| 2026-04-27 06:03:28 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-04-27 06:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.025 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-27 06:00:54 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-04-27 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.038 |  |
| 2026-04-27 06:04:03 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.060 |  |
| 2026-04-27 06:07:10 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.191 |  |
| 2026-04-27 06:02:14 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.368 |  |
| 2026-04-27 04:06:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)