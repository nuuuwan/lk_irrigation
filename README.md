# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_06:15:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,451 measurements** from **39** stations.
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
| 2026-11-22 06:15:57 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:08:38 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:07:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.152 |  |
| 2026-11-22 06:06:47 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:06:08 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:05:22 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | -0.038 |  |
| 2026-11-22 06:05:09 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:04:42 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.030 |  |
| 2026-11-22 06:04:26 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-22 06:04:19 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:04:08 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 06:04:07 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.307 |  |
| 2026-11-22 06:03:34 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-11-22 06:03:11 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.020 |  |
| 2026-11-22 06:03:07 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 06:03:03 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.050 |  |
| 2026-11-22 06:02:58 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 06:02:52 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.042 |  |
| 2026-11-22 06:02:49 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:02:12 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:02:10 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.062 |  |
| 2026-11-22 06:02:09 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:01:36 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-11-22 06:01:35 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:01:34 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 06:01:28 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:01:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-22 06:01:06 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:01:06 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-22 06:00:54 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:00:54 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:00:32 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 06:00:11 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -36.000 |  |
| 2026-11-22 06:00:09 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -36.000 |  |
| 2026-11-22 05:57:21 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:46:46 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:46:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.307 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 06:01:06 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-22 06:04:26 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-22 06:01:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-22 06:00:32 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 06:04:08 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 06:02:58 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 06:03:07 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 06:01:34 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 06:01:35 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:01:28 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:06:08 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:04:07 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:15:57 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:08:38 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:01:46 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:02:12 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:04:19 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:00:54 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:06:47 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-22 06:02:49 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-22 05:19:04 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-11-22 06:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:00:54 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:01:06 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:05:09 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-22 06:01:36 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-11-22 06:03:11 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.020 |  |
| 2026-11-22 06:04:42 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.030 |  |
| 2026-11-22 06:05:22 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | -0.038 |  |
| 2026-11-22 06:03:34 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-11-22 06:02:52 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.042 |  |
| 2026-11-22 06:03:03 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.050 |  |
| 2026-11-22 06:02:10 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.062 |  |
| 2026-11-22 06:07:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.152 |  |
| 2026-11-22 06:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.307 |  |
| 2026-11-22 06:00:11 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)