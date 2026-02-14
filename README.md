# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_12:08:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,822 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 12:08:08 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 12:06:13 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:52 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.050 |  |
| 2026-02-14 12:05:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:30 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-14 12:05:24 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:12 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:07 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:04:43 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:04:39 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:04:19 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-02-14 12:04:10 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:37 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | -0.005 |  |
| 2026-02-14 12:03:36 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-14 12:03:28 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-02-14 12:03:25 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:24 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-14 12:03:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:09 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:58 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.041 |  |
| 2026-02-14 12:02:49 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:44 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.070 |  |
| 2026-02-14 12:02:43 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:33 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:20 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:02:16 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.036 |  |
| 2026-02-14 12:02:00 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:01:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-14 12:01:47 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:01:39 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:01:12 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 12:01:07 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:00:45 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:00:37 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 12:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:00:13 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 12:04:19 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-02-14 12:01:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-14 12:05:30 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-14 12:00:13 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-14 12:03:24 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-14 12:03:36 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-14 12:00:37 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 12:01:12 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 12:08:08 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 12:02:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:49 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:00 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:01:39 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:43 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:24 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:09 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:07 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:04:10 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:02:33 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:04:39 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:04:43 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:00:45 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:25 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:05:12 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:06:13 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-14 12:03:37 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | -0.005 |  |
| 2026-02-14 12:02:20 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:01:07 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:02:16 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-14 12:03:28 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-02-14 12:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.036 |  |
| 2026-02-14 12:02:58 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.041 |  |
| 2026-02-14 12:05:52 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.050 |  |
| 2026-02-14 12:02:44 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)