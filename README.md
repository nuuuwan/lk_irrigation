# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_19:39:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,652 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 19:39:22 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-18 19:29:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:19:32 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:16:03 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:09:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:07:05 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 19:06:50 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:06:24 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-02-18 19:06:12 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-02-18 19:05:51 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:05:12 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:58 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:50 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-02-18 19:04:02 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-02-18 19:04:02 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:01 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 19:03:30 | Manampitiya (Mahaweli Ganga) | 3.05 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-02-18 19:03:28 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:03:23 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.058 |  |
| 2026-02-18 19:03:09 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 19:02:56 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:02:39 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:02:27 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-18 19:02:12 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:02:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:01:47 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 1.096 | 🔺 Rising |
| 2026-02-18 19:01:35 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-18 19:01:23 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:01:15 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-18 19:00:55 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.023 |  |
| 2026-02-18 19:00:50 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 19:00:49 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 19:03:30 | Manampitiya (Mahaweli Ganga) | 3.05 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-02-18 19:01:47 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 1.096 | 🔺 Rising |
| 2026-02-18 19:02:27 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-18 19:00:50 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 19:04:01 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 19:03:09 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 19:07:05 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 19:39:22 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-18 19:02:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:00:49 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:29:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:06:50 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:16:03 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:50 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:02 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:05:12 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:58 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:19:32 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:02:39 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:05:51 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:01:23 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:04:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:09:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:03:28 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:02:56 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:02:12 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-18 19:01:15 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-18 19:04:02 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-02-18 18:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-02-18 19:06:24 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-02-18 19:01:35 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-18 19:00:55 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.023 |  |
| 2026-02-18 19:06:12 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-02-18 19:03:23 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.058 |  |
| 2026-02-18 19:04:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)