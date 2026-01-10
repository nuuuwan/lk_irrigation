# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_06:37:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,540 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 06:37:51 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 06:22:51 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:15:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 06:11:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:09:31 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-10 06:08:47 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:08:31 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 06:08:17 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:07:31 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-10 06:07:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:06:42 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-10 06:06:32 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:06:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:05:35 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 06:05:12 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:05:00 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-01-10 06:04:59 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:04:57 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.233 |  |
| 2026-01-10 06:04:41 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:04:39 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-10 06:04:06 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-10 06:04:04 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:03:47 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:03:33 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.024 |  |
| 2026-01-10 06:03:32 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.038 |  |
| 2026-01-10 06:03:09 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-10 06:02:25 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:01:57 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:01:54 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:01:45 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 06:01:33 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:01:31 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-10 06:01:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-01-10 06:01:09 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:00:50 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-01-10 06:00:47 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:00:21 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 06:04:39 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-10 06:01:31 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-10 06:01:45 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 06:03:09 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-10 06:04:06 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-10 06:06:42 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-10 06:15:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 06:08:31 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-10 06:07:31 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-10 06:09:31 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-10 06:05:35 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 06:37:51 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 06:02:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:03:47 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:06:32 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:04:04 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:06:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:22:51 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:08:17 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:01:54 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:04:41 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:05:12 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:02:25 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:07:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 06:11:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:04:59 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:01:57 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:00:47 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:01:09 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-10 06:00:21 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-01-10 06:00:50 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-01-10 06:05:00 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-01-10 06:03:33 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.024 |  |
| 2026-01-10 06:01:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-01-10 06:03:32 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.038 |  |
| 2026-01-10 06:04:57 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)