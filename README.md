# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_11:09:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 11:09:42 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:08:46 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.018 |  |
| 2026-04-15 11:07:26 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-04-15 11:07:16 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-15 11:06:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:06:29 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-04-15 11:06:09 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-04-15 11:06:07 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:04:22 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.117 |  |
| 2026-04-15 11:04:20 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 11:04:18 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:04:11 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-04-15 11:04:07 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:03:29 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:03:17 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:03:15 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:02:48 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-15 11:02:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:02:17 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:02:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-04-15 11:01:59 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-04-15 11:01:56 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:01:53 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:01:51 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:23 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:12 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:09 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:00:59 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 11:00:48 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:00:39 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-04-15 11:00:33 | Thanthirimale (Malwathu Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-04-15 11:00:06 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:30:28 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 11:02:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-04-15 11:07:26 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-04-15 11:02:48 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-15 11:00:59 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 10:02:38 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-15 10:12:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 11:07:16 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-15 11:04:20 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-15 11:00:06 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:51 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:06:07 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:09 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:06:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:03:15 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:56 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:00:48 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:02:17 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:02:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:03:29 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:23 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:01:12 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:09:42 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:06:09 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-04-15 10:06:05 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:03:17 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:04:07 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:01:53 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:04:18 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-15 11:08:46 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.018 |  |
| 2026-04-15 11:06:29 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-04-15 10:00:53 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:07:24 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-04-15 11:00:33 | Thanthirimale (Malwathu Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-04-15 11:00:39 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-04-15 11:04:11 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-04-15 11:01:59 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-04-15 10:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-04-15 11:04:22 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)