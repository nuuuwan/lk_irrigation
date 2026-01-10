# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_03:20:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,323 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 03:20:04 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:20:03 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:20:01 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:18:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:13:25 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.147 |  |
| 2026-01-11 03:10:50 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-11 03:10:18 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:10:17 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:10:15 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:09:52 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-01-11 03:08:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-01-11 03:08:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:08:15 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:07:42 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:06:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-11 03:06:11 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:05:52 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 03:05:49 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-01-11 03:05:00 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 03:04:31 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:04:20 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.139 |  |
| 2026-01-11 03:04:16 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-11 03:03:41 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.050 |  |
| 2026-01-11 03:02:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-11 03:02:37 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:02:24 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:59 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:51 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:48 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:47 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-01-11 03:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-11 03:01:24 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:08 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 03:00:59 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:00:17 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:00:07 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:45:07 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 03:06:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-11 03:04:16 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-11 03:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-11 03:01:08 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 03:05:00 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 03:05:52 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 03:02:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:00:17 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:24 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:02:24 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:07:42 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:02:37 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:03:02 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 02:24:12 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:04:31 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:48 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:00:07 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:59 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:10:18 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:00:59 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:18:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:08:15 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:08:31 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:20:04 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:01:51 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 03:06:11 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:57:33 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.005 |  |
| 2026-01-11 03:08:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-01-11 03:09:52 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-01-11 03:10:50 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-11 03:01:47 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-01-11 03:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-11 03:05:49 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 03:03:41 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.050 |  |
| 2026-01-11 03:04:20 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.139 |  |
| 2026-01-11 03:13:25 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)