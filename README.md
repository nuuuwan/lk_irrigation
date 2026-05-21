# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_17:11:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 17:11:31 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:11:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-05-21 17:09:42 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-21 17:07:40 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-21 17:07:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:07:09 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-21 17:07:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-21 17:06:09 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:05:54 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:05:41 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.069 |  |
| 2026-05-21 17:04:56 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 17:04:22 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:04:07 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:34 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:29 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:24 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-05-21 17:03:18 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:13 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-05-21 17:02:59 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-21 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:47 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:44 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:02:32 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 17:02:21 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:09 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:02:05 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:01:43 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:01:33 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-05-21 17:01:29 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:01:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-21 17:01:01 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:00:31 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:00:09 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 16:59:36 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-21 16:43:54 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 17:07:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-21 17:03:24 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-05-21 17:07:09 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-21 17:07:40 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-21 17:09:42 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-21 17:01:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-21 16:59:36 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-21 17:02:32 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 17:00:09 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 17:04:56 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 17:00:31 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:01:01 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:02:05 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:18 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:06:35 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:02:09 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:05:54 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:04:07 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:43:54 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:07:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:02:44 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:04:22 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:29 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:00:42 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:03:34 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:11:31 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:01:43 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-21 17:11:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-05-21 17:06:09 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:21 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:01:29 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:47 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-21 17:02:59 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-21 17:01:33 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-05-21 17:03:13 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-05-21 17:05:41 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)