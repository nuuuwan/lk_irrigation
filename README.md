# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_08:09:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 08:09:12 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:08:43 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.163 |  |
| 2026-04-07 08:08:03 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:07:17 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-04-07 08:06:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-04-07 08:06:11 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.077 |  |
| 2026-04-07 08:06:06 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:05:29 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:05:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-07 08:05:00 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.013 |  |
| 2026-04-07 08:04:41 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-04-07 08:04:10 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:04:07 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2026-04-07 08:03:56 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:42 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:38 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:35 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.097 |  |
| 2026-04-07 08:03:34 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 08:03:22 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-07 08:03:14 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.019 |  |
| 2026-04-07 08:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.069 |  |
| 2026-04-07 08:02:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-04-07 08:02:16 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:02:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:02:12 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | 9.931 | 🔺 Rising |
| 2026-04-07 08:02:06 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 08:02:05 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-04-07 08:02:03 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:01:54 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 08:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:01:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:01:14 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 9.931 | 🔺 Rising |
| 2026-04-07 08:01:10 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.031 |  |
| 2026-04-07 08:00:53 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:00:45 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:00:14 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:00:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:19:07 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 08:02:12 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | 9.931 | 🔺 Rising |
| 2026-04-07 08:03:22 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-07 08:05:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-07 08:01:54 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 08:02:06 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 08:03:34 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 08:00:14 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:00:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:02:03 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:05:29 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:12:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:08:03 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:06:06 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:42 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:04:32 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:09:12 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:02:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:38 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:02:16 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 07:05:37 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:00:45 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:56 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:07:17 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-04-07 08:04:10 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:00:53 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:01:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-07 08:04:41 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-04-07 08:05:00 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.013 |  |
| 2026-04-07 08:03:14 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.019 |  |
| 2026-04-07 08:06:23 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-04-07 08:02:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-04-07 08:01:10 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.031 |  |
| 2026-04-07 08:04:07 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2026-04-07 08:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.069 |  |
| 2026-04-07 08:02:05 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-04-07 08:06:11 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.077 |  |
| 2026-04-07 08:03:35 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.097 |  |
| 2026-04-07 08:08:43 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)