# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_16:17:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,493 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 16:17:48 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:12:32 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:11:16 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-01-14 16:10:22 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:09:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-01-14 16:08:56 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:08:52 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:27 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:23 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:05:52 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:05:15 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:04:22 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:04:16 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:03:54 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-01-14 16:03:54 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:03:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:48 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:03:37 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:35 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:06 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 16:03:00 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:55 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.111 |  |
| 2026-01-14 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-01-14 16:02:13 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:07 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:05 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | -0.031 |  |
| 2026-01-14 16:02:01 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.103 |  |
| 2026-01-14 16:01:47 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-01-14 16:01:34 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-01-14 16:01:30 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:01:24 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:01:00 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:00:53 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:00:22 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 15:05:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-14 16:03:06 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 16:01:00 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:55 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:00:22 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:01:24 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:52 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:00:53 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:05:15 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:27 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:10:22 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:17:48 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:12:32 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:13 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:08:23 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:37 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:03:35 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:02:07 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:05:52 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 16:09:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-01-14 16:08:56 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:04:22 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:03:54 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:04:16 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:01:30 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:03:00 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:03:48 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-14 16:01:47 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-01-14 16:01:34 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:04:35 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-01-14 16:11:16 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-01-14 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.030 |  |
| 2026-01-14 16:02:05 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | -0.031 |  |
| 2026-01-14 16:03:54 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-01-14 16:02:01 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.103 |  |
| 2026-01-14 16:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)