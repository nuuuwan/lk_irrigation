# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_06:38:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,000 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 06:38:24 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.006 |  |
| 2026-05-25 06:13:01 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:10:25 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:09:23 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:08:22 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:08:11 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-25 06:06:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:05:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 06:05:14 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.088 |  |
| 2026-05-25 06:04:43 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:04:40 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-25 06:04:24 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 06:04:06 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:03:53 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 06:03:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 06:03:33 | Putupaula (Kalu Ganga) | 3.16 | 🟡 Alert | -0.021 |  |
| 2026-05-25 06:03:32 | Deraniyagala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-25 06:03:28 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-25 06:03:25 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-05-25 06:03:16 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-25 06:03:10 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-25 06:02:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:02:35 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:02:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:02:19 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.030 |  |
| 2026-05-25 06:02:14 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-25 06:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | -0.885 |  |
| 2026-05-25 06:01:53 | Ellagawa (Kalu Ganga) | 9.18 | 🟢 Normal | -0.021 |  |
| 2026-05-25 06:01:50 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:01:49 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-25 06:01:47 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.059 |  |
| 2026-05-25 06:01:38 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.174 |  |
| 2026-05-25 06:01:13 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-05-25 06:01:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:00:55 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 06:00:51 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 13.263 | 🔺 Rising |
| 2026-05-25 06:00:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-05-25 06:00:39 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:00:32 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 13.263 | 🔺 Rising |
| 2026-05-25 06:00:16 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.139 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 06:03:33 | Putupaula (Kalu Ganga) | 3.16 | 🟡 Alert | -0.021 |  |
| 2026-05-25 06:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | -0.885 |  |
| 2026-05-25 06:00:51 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 13.263 | 🔺 Rising |
| 2026-05-25 06:03:32 | Deraniyagala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-25 06:04:40 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-25 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-25 06:08:11 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-25 06:03:28 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-25 06:03:10 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-25 06:03:16 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-25 06:04:24 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 06:03:53 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 06:03:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 06:05:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 06:00:55 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 06:00:16 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:06:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:02:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:10:25 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:04:06 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:04:43 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:09:23 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:00:39 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:13:01 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:02:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:02:35 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 06:38:24 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.006 |  |
| 2026-05-25 06:01:49 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-25 06:02:14 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-25 06:03:25 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-05-25 05:03:18 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.018 |  |
| 2026-05-25 06:01:53 | Ellagawa (Kalu Ganga) | 9.18 | 🟢 Normal | -0.021 |  |
| 2026-05-25 06:02:19 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.030 |  |
| 2026-05-25 06:00:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-05-25 06:01:13 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-05-25 06:01:47 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.059 |  |
| 2026-05-25 06:05:14 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.088 |  |
| 2026-05-25 06:01:38 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)