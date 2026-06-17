# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_04:28:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,377 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 04:28:53 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-18 04:25:45 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-18 04:16:15 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:11:21 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-06-18 04:08:50 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-18 04:07:48 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-18 04:07:26 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:06:43 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:06:37 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.110 |  |
| 2026-06-18 04:06:32 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:06:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:05:25 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.023 |  |
| 2026-06-18 04:04:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 04:04:33 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.167 |  |
| 2026-06-18 04:04:32 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-18 04:04:22 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:04:20 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-06-18 04:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-06-18 04:04:18 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-06-18 04:04:16 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-06-18 04:04:04 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 04:03:49 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-18 04:03:38 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-18 04:03:09 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.051 |  |
| 2026-06-18 04:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.025 |  |
| 2026-06-18 04:02:37 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-18 04:02:30 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-18 04:02:24 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 04:02:15 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-06-18 04:02:11 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:02:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:01:39 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:01:06 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:00:26 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 04:28:53 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-18 04:04:32 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-18 04:04:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 04:07:48 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-18 04:08:50 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-18 04:25:45 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-18 04:03:49 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-18 04:02:30 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-18 04:00:26 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-18 04:03:38 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-18 04:02:24 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 04:04:04 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 04:02:37 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-18 04:06:32 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:01:06 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:03:53 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:04:22 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:07 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:06:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:02:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:06:43 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:02:11 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:07:26 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:16:15 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 04:02:15 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-06-18 04:11:21 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 04:04:18 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-06-18 04:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-06-18 04:04:16 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-06-18 04:05:25 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.023 |  |
| 2026-06-18 04:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.025 |  |
| 2026-06-18 04:04:20 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-06-18 04:03:09 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.051 |  |
| 2026-06-18 04:06:37 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.110 |  |
| 2026-06-18 04:04:33 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.167 |  |
| 2026-06-18 03:05:07 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)