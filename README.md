# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_23:08:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,860 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 23:08:40 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:08:15 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-02-08 23:06:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:30 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:29 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:21 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:19 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.038 |  |
| 2026-02-08 23:05:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:04:37 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:04:01 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:03:19 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 23:03:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.119 |  |
| 2026-02-08 23:02:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-08 23:02:29 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.145 |  |
| 2026-02-08 23:01:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:01:39 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-08 23:01:29 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:01:28 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:01:17 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.133 |  |
| 2026-02-08 23:00:46 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:00:41 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-08 23:00:37 | Manampitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-08 23:00:10 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:44:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:30:45 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:22:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2026-02-08 22:22:52 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -36.000 |  |
| 2026-02-08 22:21:40 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.016 |  |
| 2026-02-08 22:20:55 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:17:05 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 22:01:53 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-02-08 23:02:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-08 23:00:41 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-08 22:06:25 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 23:03:19 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 23:01:29 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:00:10 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:21 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:04:01 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 21:12:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:03:44 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:00:46 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:03:44 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:30 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:01:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:04:37 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:08:40 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:06:59 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:20:55 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:44:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:01:28 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:29 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-08 23:00:37 | Manampitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-08 23:01:39 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-08 22:00:32 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-02-08 22:21:40 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.016 |  |
| 2026-02-08 22:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-02-08 23:08:15 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-02-08 23:05:19 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.038 |  |
| 2026-02-08 22:07:15 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.058 |  |
| 2026-02-08 23:03:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.119 |  |
| 2026-02-08 23:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.133 |  |
| 2026-02-08 23:02:29 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.145 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-08 22:22:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)