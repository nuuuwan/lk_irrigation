# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_01:22:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,087 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 01:22:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-11-05 01:18:55 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 01:17:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:11:19 | Kuda Oya (Kirindi Oya) | 4.10 | 🟢 Normal | -0.138 |  |
| 2026-11-05 01:09:37 | Thanamalwila (Kirindi Oya) | 3.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-05 01:09:36 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-05 01:08:37 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.045 |  |
| 2026-11-05 01:07:39 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-05 01:07:28 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 01:05:34 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-05 01:05:26 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 01:04:28 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.086 |  |
| 2026-11-05 01:04:17 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -1.861 |  |
| 2026-11-05 01:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-05 01:03:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-05 01:03:40 | Giriulla (Maha Oya) | 3.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-05 01:03:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.088 |  |
| 2026-11-05 01:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-05 01:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:03:33 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-05 01:03:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 01:03:19 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.021 |  |
| 2026-11-05 01:02:18 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-05 01:02:03 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.030 |  |
| 2026-11-05 01:01:57 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:39 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-05 01:00:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-11-05 01:00:26 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-05 01:00:18 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.618 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 01:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-05 00:09:03 | Urawa (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-05 01:03:33 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-05 01:02:18 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-05 01:09:37 | Thanamalwila (Kirindi Oya) | 3.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-05 01:03:40 | Giriulla (Maha Oya) | 3.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-05 01:09:36 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-05 01:00:26 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-05 01:05:34 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-05 01:07:28 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 00:02:01 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-05 01:03:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 01:05:26 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 01:18:55 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 01:01:57 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:04:47 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:10:03 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:17:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:39 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-05 01:01:09 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-05 01:03:19 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.021 |  |
| 2026-11-05 01:07:39 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-05 01:22:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-11-05 01:03:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 01:02:03 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.030 |  |
| 2026-11-05 00:11:22 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 01:08:37 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.045 |  |
| 2026-11-05 01:00:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-11-05 01:04:28 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.086 |  |
| 2026-11-05 01:03:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.088 |  |
| 2026-11-05 01:11:19 | Kuda Oya (Kirindi Oya) | 4.10 | 🟢 Normal | -0.138 |  |
| 2026-11-05 01:00:18 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.618 |  |
| 2026-11-05 01:04:17 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -1.861 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)