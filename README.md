# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_13:35:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,375 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 13:35:19 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:31:01 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:10:40 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.019 |  |
| 2026-01-14 13:09:38 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:08:29 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 13:06:43 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.048 |  |
| 2026-01-14 13:05:37 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.187 |  |
| 2026-01-14 13:05:26 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-14 13:05:12 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -18.000 |  |
| 2026-01-14 13:05:10 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -18.000 |  |
| 2026-01-14 13:04:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:04:44 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 13:04:27 | Thanthirimale (Malwathu Oya) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:04:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:04:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:03:49 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:03:49 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:03:26 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:03:24 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-01-14 13:03:15 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-01-14 13:03:12 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:03:12 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:52 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:52 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-14 13:02:43 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:02:29 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:20 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-14 13:02:11 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:01:32 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:21 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:14 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:02 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:00:45 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:00:14 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:00:14 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 13:02:20 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-14 13:00:14 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 13:08:29 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 13:04:44 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 13:02:52 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:00:14 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:29 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:21 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:03:12 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:09:38 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:03:49 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:14 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:32 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:02:43 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:04:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:00:45 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:04:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:35:19 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:31:01 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:01:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:05:26 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-14 13:03:49 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:03:12 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:11 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:01:02 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:52 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:02:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-14 13:03:24 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-01-14 13:10:40 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.019 |  |
| 2026-01-14 13:04:27 | Thanthirimale (Malwathu Oya) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:04:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:03:26 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:03:15 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-01-14 13:06:43 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.048 |  |
| 2026-01-14 13:05:37 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.187 |  |
| 2026-01-14 13:05:12 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)