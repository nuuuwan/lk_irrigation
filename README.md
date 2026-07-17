# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--17_11:14:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,615 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 11:14:29 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:12:49 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:10:22 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-07-17 11:10:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-07-17 11:09:45 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-17 11:08:46 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:08:20 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:07:35 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:07:17 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:07:13 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-07-17 11:06:46 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:06:17 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:06:11 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:05:26 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:05:19 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:04:58 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-17 11:04:48 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:04:03 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 11:03:34 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-07-17 11:03:32 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.035 |  |
| 2026-07-17 11:03:29 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:03:07 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:03:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:03:00 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:02:41 | Putupaula (Kalu Ganga) | 0.05 | 🟢 Normal | -0.050 |  |
| 2026-07-17 11:02:31 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:02:27 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-17 11:02:21 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-17 11:02:18 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:02:13 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:34 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.214 |  |
| 2026-07-17 11:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:09 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:08 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-17 11:01:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:59 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:44 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:43 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:25 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:23 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 11:02:21 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-17 11:01:08 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-17 11:09:45 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-17 11:02:27 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-17 11:04:03 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-17 11:00:25 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:03:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:08:46 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:59 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:05:19 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:12:49 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:43 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:06:46 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:03:07 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:09 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:14:29 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:00:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:06:11 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:08:20 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:01:02 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:05:26 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:02:31 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:06:17 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:03:00 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:07:17 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:07:35 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:04:48 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:02:13 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-17 11:10:22 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-07-17 11:00:23 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-07-17 11:04:58 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-17 11:03:34 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-07-17 11:07:13 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-07-17 11:10:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-07-17 11:03:32 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.035 |  |
| 2026-07-17 11:02:41 | Putupaula (Kalu Ganga) | 0.05 | 🟢 Normal | -0.050 |  |
| 2026-07-17 11:01:34 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)