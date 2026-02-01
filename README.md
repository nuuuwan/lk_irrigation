# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_07:07:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 07:07:32 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:07:31 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-01 07:07:25 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:06:53 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:06:41 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.056 |  |
| 2026-02-01 07:06:35 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-01 07:06:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-02-01 07:05:02 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.113 |  |
| 2026-02-01 07:04:53 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:04:49 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-01 07:03:40 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 07:03:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 07:03:21 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:03:10 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.011 |  |
| 2026-02-01 07:02:55 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:31 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:28 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:25 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-01 07:02:07 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-01 07:02:06 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:01:41 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:01:24 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.203 |  |
| 2026-02-01 07:01:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:01:19 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-02-01 07:01:10 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.099 |  |
| 2026-02-01 07:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:50:35 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:35:42 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-02-01 06:32:22 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:17:28 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-02-01 06:12:50 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.099 |  |
| 2026-02-01 06:12:16 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 06:11:32 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 07:01:19 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-02-01 06:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-02-01 07:06:09 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-02-01 06:03:17 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-01 07:04:49 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-01 06:12:16 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 07:06:35 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-01 07:02:25 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-01 06:10:19 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 07:03:40 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 07:07:31 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-01 07:03:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:03:24 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 06:05:28 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 07:02:06 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:28 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:01:41 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:07:15 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:04:53 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:31 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:11:32 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:03:21 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:07:32 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:55 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:02:23 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 06:50:35 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:01:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:06:53 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-01 07:02:07 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-01 07:03:10 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.011 |  |
| 2026-02-01 06:10:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-02-01 07:06:41 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.056 |  |
| 2026-02-01 07:01:10 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.099 |  |
| 2026-02-01 07:05:02 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.113 |  |
| 2026-02-01 06:01:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-02-01 07:01:24 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)