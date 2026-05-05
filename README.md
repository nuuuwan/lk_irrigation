# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_00:21:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 00:21:50 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.007 |  |
| 2026-05-06 00:10:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-06 00:09:13 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-06 00:08:32 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-06 00:08:18 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:08:03 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.015 |  |
| 2026-05-06 00:07:50 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-05-06 00:06:40 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-06 00:05:50 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:05:45 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.025 |  |
| 2026-05-06 00:05:17 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:05:10 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-06 00:05:10 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:04:13 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 00:04:04 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-06 00:03:47 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:03:29 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:03:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 00:03:06 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:02:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:02:31 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-06 00:01:59 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 6.771 | 🔺 Rising |
| 2026-05-06 00:01:53 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-05-06 00:01:52 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.244 |  |
| 2026-05-06 00:01:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -36.000 |  |
| 2026-05-06 00:01:47 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:01:46 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.020 |  |
| 2026-05-06 00:01:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:01:34 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:01:18 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:00:23 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 00:01:59 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 6.771 | 🔺 Rising |
| 2026-05-06 00:04:04 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-06 00:05:10 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-06 00:06:40 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-06 00:02:31 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-06 00:08:32 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 00:03:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 00:04:13 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 22:04:45 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 00:09:13 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-06 00:10:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-05 23:33:18 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-06 00:02:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:05:50 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-05 23:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 23:01:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-05 21:00:16 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 18:03:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:08:18 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:01:47 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:00:23 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:05:17 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:03:29 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:01:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:01:34 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 00:21:50 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.007 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:03:47 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:03:06 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:01:18 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-06 00:08:03 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.015 |  |
| 2026-05-05 21:12:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-05-06 00:01:46 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.020 |  |
| 2026-05-06 00:05:45 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.025 |  |
| 2026-05-05 23:33:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.028 |  |
| 2026-05-06 00:07:50 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-05-06 00:01:52 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.244 |  |
| 2026-05-06 00:01:53 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)