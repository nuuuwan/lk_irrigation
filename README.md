# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_11:07:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 11:07:32 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.038 |  |
| 2026-04-30 11:07:18 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:06:16 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:06:01 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:05:25 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:05:22 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.021 |  |
| 2026-04-30 11:05:07 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:05:00 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-30 11:04:46 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:04:46 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-04-30 11:04:45 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-04-30 11:03:58 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-30 11:03:54 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-04-30 11:03:39 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:03:34 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 11:03:15 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:03:11 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:03:01 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:02:58 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-30 11:02:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:02:28 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.061 |  |
| 2026-04-30 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.080 |  |
| 2026-04-30 11:02:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-30 11:02:11 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-30 11:02:09 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:01:48 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:01:47 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-30 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:01:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:00:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:00:28 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 11:00:12 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 11:02:58 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-30 11:02:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-30 11:01:47 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-30 11:02:11 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-30 11:05:00 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-30 10:04:49 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-30 11:03:34 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 11:00:28 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 10:03:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 10:00:27 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 11:02:09 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:00:34 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 10:06:12 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:01:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:03:01 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:02:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:06:16 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:07:18 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:03:39 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:04:46 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-04-30 10:04:15 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:04:46 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:06:01 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:05:07 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:03:11 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:01:48 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:03:15 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:00:12 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:05:25 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-30 11:03:54 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-04-30 10:08:22 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-30 11:03:58 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-30 11:05:22 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.021 |  |
| 2026-04-30 11:04:45 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-04-30 10:11:21 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-04-30 11:07:32 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.038 |  |
| 2026-04-30 11:02:28 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.061 |  |
| 2026-04-30 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)