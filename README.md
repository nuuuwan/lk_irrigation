# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_09:09:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,484 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 09:09:28 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-04 09:09:19 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:08:01 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:07:46 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:07:07 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-04 09:07:07 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:06:42 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:06:15 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.037 |  |
| 2026-09-04 09:05:21 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-04 09:05:17 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:04:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:04:16 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:03:53 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-09-04 09:03:52 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-09-04 09:03:43 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.055 |  |
| 2026-09-04 09:03:20 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-04 09:03:18 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 09:03:11 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.010 |  |
| 2026-09-04 09:03:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-04 09:02:57 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-04 09:02:51 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-09-04 09:02:49 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:36 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-09-04 09:02:33 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:31 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:30 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:30 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:10 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:01 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-09-04 09:01:59 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:01:59 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:01:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-09-04 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:00:57 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.167 |  |
| 2026-09-04 09:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:00:40 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:00:16 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 09:03:53 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-09-04 09:03:20 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-04 09:02:57 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-04 09:03:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-04 09:05:21 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-04 09:03:18 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 09:07:07 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-04 09:01:59 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:00:16 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:07:07 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:33 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:07:46 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:03:43 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:31 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:04:16 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:01:59 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:49 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:08:01 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:04:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:10 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:30 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:06:42 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:00:40 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:10:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:09:19 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:02:30 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:05:17 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 09:03:11 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.010 |  |
| 2026-09-04 09:09:28 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-04 09:02:36 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-09-04 09:02:01 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-09-04 09:02:51 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-09-04 09:06:15 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.037 |  |
| 2026-09-04 09:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.055 |  |
| 2026-09-04 09:01:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-09-04 09:00:57 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)