# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_00:36:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,365 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 00:36:54 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:33:29 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-14 00:26:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.004 |  |
| 2026-04-14 00:16:02 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:12:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:10:00 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 00:09:05 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:08:07 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-14 00:07:25 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-04-14 00:06:09 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-04-14 00:06:01 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-04-14 00:05:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-14 00:04:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-04-14 00:04:18 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:04:05 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-14 00:03:29 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:03:16 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-14 00:03:11 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-14 00:02:24 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:01:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:01:38 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.175 |  |
| 2026-04-14 00:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:01:30 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-04-14 00:01:29 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.065 |  |
| 2026-04-14 00:01:21 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.080 |  |
| 2026-04-14 00:01:16 | Katharagama (Menik Ganga) | -0.39 | 🟢 Normal | -0.012 |  |
| 2026-04-14 00:01:11 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:00:50 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:00:46 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:00:33 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -144.000 |  |
| 2026-04-14 00:00:32 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -144.000 |  |
| 2026-04-14 00:00:31 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -144.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 00:01:30 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-04-13 22:06:36 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-14 00:04:05 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-14 00:08:07 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-14 00:05:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-14 00:10:00 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-13 23:02:22 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-14 00:03:11 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-14 00:33:29 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 00:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:06:21 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:36:54 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:00:46 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:09:05 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:01:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:00:50 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:16:02 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 23:02:10 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:02:24 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:04:18 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:12:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:01:11 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-14 00:26:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.004 |  |
| 2026-04-14 00:07:25 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-14 00:03:16 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-14 00:01:16 | Katharagama (Menik Ganga) | -0.39 | 🟢 Normal | -0.012 |  |
| 2026-04-14 00:06:09 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-04-13 21:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-04-14 00:04:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-04-14 00:06:01 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-04-14 00:01:29 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.065 |  |
| 2026-04-13 21:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.079 |  |
| 2026-04-14 00:01:21 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.080 |  |
| 2026-04-13 21:10:02 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.098 |  |
| 2026-04-14 00:01:38 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.175 |  |
| 2026-04-14 00:00:33 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)