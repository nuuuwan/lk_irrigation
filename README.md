# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_22:04:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,972 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 22:04:55 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-09-04 22:04:28 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:04:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-04 22:03:33 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-09-04 22:03:31 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-09-04 22:03:08 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:03:06 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.030 |  |
| 2026-09-04 22:03:02 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:03:01 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-09-04 22:02:47 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:02:46 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-04 22:02:21 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:02:21 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 22:02:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-09-04 22:02:06 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:52 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:21 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:16 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:09 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 21:05:41 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-04 22:02:46 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-04 22:02:21 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 22:02:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:03:02 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:02:06 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:21 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:03:45 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:06:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:16 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:03:33 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:52 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:03:57 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:03:22 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:02:21 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:03:08 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:05:43 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:04:28 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:02:31 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:06:12 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:07:54 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:01:09 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:02:47 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 21:10:16 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-09-04 21:10:10 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-04 22:04:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-04 22:03:33 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-09-04 21:00:09 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-09-04 21:04:40 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.013 |  |
| 2026-09-04 22:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-09-04 22:03:31 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-09-04 22:03:01 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-09-04 22:03:06 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.030 |  |
| 2026-09-04 22:04:55 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-09-04 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-04 21:01:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.074 |  |
| 2026-09-04 21:09:23 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)