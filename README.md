# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_06:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **214,683 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 06:16:05 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.046 |  |
| 2026-07-24 06:14:58 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-07-24 06:14:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:08:49 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.069 |  |
| 2026-07-24 06:08:23 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.036 |  |
| 2026-07-24 06:06:17 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.029 |  |
| 2026-07-24 06:05:58 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:05:48 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 06:05:43 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:05:19 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-24 06:05:14 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-24 06:05:00 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:04:02 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:03:47 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-24 06:03:12 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-07-24 06:03:05 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:03:02 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:03:00 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:54 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:39 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:35 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:07 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.024 |  |
| 2026-07-24 06:01:59 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-24 06:01:55 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:14 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-24 06:01:11 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-24 06:00:54 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:00:39 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.006 |  |
| 2026-07-24 06:00:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2026-07-24 05:51:27 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.069 |  |
| 2026-07-24 05:45:50 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 06:01:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-24 06:01:11 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-24 06:03:47 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-24 06:05:19 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-24 06:05:48 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 06:03:05 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:54 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:03:00 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:04:02 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:03:02 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:25:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:01:53 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:05:58 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:14:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:39 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:14 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:35 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:01:55 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:00:54 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:01:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:05:00 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:02:07 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 06:00:39 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.006 |  |
| 2026-07-24 06:01:59 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-24 06:05:14 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-24 06:03:12 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-07-24 06:14:58 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-07-24 06:00:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2026-07-24 06:02:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.024 |  |
| 2026-07-24 06:06:17 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.029 |  |
| 2026-07-24 06:08:23 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.036 |  |
| 2026-07-24 05:04:29 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.038 |  |
| 2026-07-24 06:16:05 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.046 |  |
| 2026-07-24 06:08:49 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)