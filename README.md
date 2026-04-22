# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_23:33:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,366 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 23:33:34 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-22 23:22:33 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-22 23:18:07 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-22 23:13:32 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:11:59 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-22 23:06:30 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-22 23:06:05 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.061 |  |
| 2026-04-22 23:05:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 23:05:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.012 |  |
| 2026-04-22 23:05:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 23:05:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.024 |  |
| 2026-04-22 23:04:37 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:04:36 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:03:58 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:02:57 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.042 |  |
| 2026-04-22 23:02:53 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:02:47 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:02:28 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:02:25 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.168 |  |
| 2026-04-22 23:01:53 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:01:52 | Thanamalwila (Kirindi Oya) | 3.55 | 🟢 Normal | -0.173 |  |
| 2026-04-22 23:01:44 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-04-22 23:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-04-22 23:01:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:01:32 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:01:28 | Kuda Oya (Kirindi Oya) | 2.71 | 🟢 Normal | -0.189 |  |
| 2026-04-22 23:01:24 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-04-22 23:01:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:01:18 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-22 23:01:07 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.085 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 23:01:44 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-04-22 23:18:07 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-04-22 23:22:33 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-22 23:01:07 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-22 22:12:31 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-22 23:11:59 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-22 23:05:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 23:06:30 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-22 23:05:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 22:05:30 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 23:33:34 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-22 23:02:47 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:01:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:03:58 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:04:36 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:01:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:01:53 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:04:37 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-22 23:13:32 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:19:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-22 23:02:28 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:01:32 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:02:53 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 23:05:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.012 |  |
| 2026-04-22 22:00:50 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-04-22 23:01:18 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-22 23:05:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.024 |  |
| 2026-04-22 23:02:57 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.042 |  |
| 2026-04-22 23:01:24 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-04-22 22:01:28 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.052 |  |
| 2026-04-22 23:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-04-22 23:06:05 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.061 |  |
| 2026-04-22 22:05:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.081 |  |
| 2026-04-22 23:02:25 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.168 |  |
| 2026-04-22 23:01:52 | Thanamalwila (Kirindi Oya) | 3.55 | 🟢 Normal | -0.173 |  |
| 2026-04-22 23:01:28 | Kuda Oya (Kirindi Oya) | 2.71 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)