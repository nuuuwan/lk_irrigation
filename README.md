# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--22_08:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **52,383 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 08:10:24 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:10:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.061 |  |
| 2026-01-22 08:08:43 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:08:42 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:07:55 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.068 |  |
| 2026-01-22 08:07:08 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-22 08:05:52 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:05:49 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:05:24 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.028 |  |
| 2026-01-22 08:05:24 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-01-22 08:05:11 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-22 08:04:24 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:04:05 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.130 |  |
| 2026-01-22 08:04:02 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 08:03:53 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-22 08:03:28 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:03:26 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:03:26 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-01-22 08:03:11 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 08:02:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:02:03 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:02:01 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.152 |  |
| 2026-01-22 08:01:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:37 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:33 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:29 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 08:01:11 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:06 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:02 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 08:00:37 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 07:43:49 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.028 |  |
| 2026-01-22 07:28:55 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:26:52 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:25:28 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-22 07:22:44 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 08:03:11 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 08:00:37 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 08:04:02 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-22 07:14:07 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-22 08:05:11 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-22 08:01:02 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 08:01:15 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 08:02:01 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:37 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:29 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:06:12 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:33 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:10:24 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:03:28 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:08:42 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:02:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:06 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:26:52 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:05:49 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:02:03 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:05:52 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:03:26 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:08:43 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:04:24 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-22 08:01:11 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:04:18 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:13:46 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-22 08:03:53 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-22 08:07:08 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-22 08:03:26 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-01-22 08:05:24 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-01-22 08:05:24 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.028 |  |
| 2026-01-22 08:10:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.061 |  |
| 2026-01-22 08:07:55 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.068 |  |
| 2026-01-22 08:04:05 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.130 |  |
| 2026-01-22 08:01:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)