# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_23:10:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 23:10:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-04-25 23:09:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:08:51 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:08:15 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.119 |  |
| 2026-04-25 23:07:00 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:05:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-25 23:05:25 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.032 |  |
| 2026-04-25 23:05:21 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:04:42 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:04:40 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -54.000 |  |
| 2026-04-25 23:04:38 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -54.000 |  |
| 2026-04-25 23:04:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.078 |  |
| 2026-04-25 23:04:31 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-25 23:04:16 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:04:14 | Siyambalanduwa (Heda Oya) | 0.00 | 🟢 Normal | -0.420 |  |
| 2026-04-25 23:04:11 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:04:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:03:51 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:03:49 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:03:47 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:03:16 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-25 23:02:59 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-25 23:02:54 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:02:19 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:02:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:02:13 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:01:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:01:39 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:00:56 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:00:41 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:59:21 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:50:52 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:43:35 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:38:33 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-25 22:28:00 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 23:10:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-04-25 23:03:16 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-25 23:04:31 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-25 22:38:33 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-25 22:05:23 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 23:04:11 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:50:52 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:02:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:01:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:43:35 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:00:41 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:09:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:00:56 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:08:51 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:04:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:03:51 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:04:16 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 23:02:13 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:07:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-25 23:04:42 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:03:49 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:07:00 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:03:47 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:03:02 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:02:54 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:02:19 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:01:39 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:05:21 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-25 23:05:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-25 23:02:59 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 23:05:25 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.032 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 22:11:27 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.073 |  |
| 2026-04-25 23:04:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.078 |  |
| 2026-04-25 23:08:15 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.119 |  |
| 2026-04-25 23:04:14 | Siyambalanduwa (Heda Oya) | 0.00 | 🟢 Normal | -0.420 |  |
| 2026-04-25 23:04:40 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)