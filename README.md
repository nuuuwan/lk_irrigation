# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_06:34:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 06:34:16 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.081 |  |
| 2026-01-06 06:23:25 | Padiyathalawa (Maduru Oya) | 2.30 | 🟢 Normal | -0.293 |  |
| 2026-01-06 06:16:21 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:15:59 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-01-06 06:15:07 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 06:15:06 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-06 06:10:29 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-06 06:10:12 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-06 06:09:57 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:08:26 | Weraganthota (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 06:08:00 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.093 |  |
| 2026-01-06 06:07:31 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:05:59 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 06:05:55 | Manampitiya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-01-06 06:05:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.032 |  |
| 2026-01-06 06:05:37 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.118 |  |
| 2026-01-06 06:04:49 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 06:04:48 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-06 06:04:43 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-06 06:04:14 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -180.000 |  |
| 2026-01-06 06:04:13 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -180.000 |  |
| 2026-01-06 06:03:45 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-06 06:03:42 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 06:03:42 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 06:03:08 | Siyambalanduwa (Heda Oya) | 3.76 | 🟢 Normal | 0.755 | 🔺 Rising |
| 2026-01-06 06:02:54 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 06:02:29 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:02:26 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-01-06 06:02:10 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-01-06 06:02:09 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.012 |  |
| 2026-01-06 06:01:47 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 06:01:38 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:01:12 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.112 |  |
| 2026-01-06 06:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 06:00:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:00:33 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-06 06:00:16 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 06:00:06 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 06:03:08 | Siyambalanduwa (Heda Oya) | 3.76 | 🟢 Normal | 0.755 | 🔺 Rising |
| 2026-01-06 06:02:10 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-01-06 06:05:55 | Manampitiya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-01-06 06:15:59 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-01-06 06:10:29 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-01-06 06:02:54 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 06:03:45 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-06 06:08:26 | Weraganthota (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 06:03:42 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-06 06:04:43 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-06 06:04:48 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-06 06:10:12 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-06 06:15:07 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 06:00:33 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-06 06:05:59 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 06:03:42 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 06:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 06:01:47 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 06:15:06 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-06 06:00:16 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 06:04:49 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 06:00:06 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:01:38 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:07:31 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:00:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:02:29 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:09:57 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 06:16:21 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-06 06:02:26 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-01-06 06:02:09 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.012 |  |
| 2026-01-06 06:05:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.032 |  |
| 2026-01-06 06:34:16 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.081 |  |
| 2026-01-06 06:08:00 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.093 |  |
| 2026-01-06 06:01:12 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.112 |  |
| 2026-01-06 06:05:37 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.118 |  |
| 2026-01-06 06:23:25 | Padiyathalawa (Maduru Oya) | 2.30 | 🟢 Normal | -0.293 |  |
| 2026-01-06 06:04:14 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)