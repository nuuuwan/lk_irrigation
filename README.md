# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_18:30:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,747 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 18:30:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:06 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:11:32 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:10:52 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:10:27 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-05 18:09:31 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.049 |  |
| 2026-09-05 18:08:06 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-09-05 18:07:27 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-05 18:07:08 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:48 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:44 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-09-05 18:05:32 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:04 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:04:44 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:03:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.059 |  |
| 2026-09-05 18:03:33 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 18:03:31 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -2.250 |  |
| 2026-09-05 18:03:18 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-05 18:03:15 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -2.250 |  |
| 2026-09-05 18:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-05 18:03:00 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-05 18:02:48 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:27 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-09-05 18:02:20 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:12 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:12 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-05 18:02:12 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:10 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:06 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:33 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.067 |  |
| 2026-09-05 18:01:24 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:16 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:10 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:08 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.072 |  |
| 2026-09-05 18:00:34 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-09-05 18:00:22 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:00:09 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:00:08 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 18:05:44 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-09-05 18:07:27 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-05 18:02:12 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-05 18:03:18 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-05 18:03:00 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-05 18:03:33 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 18:02:06 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:00:08 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:12 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:03:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:12 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:11:32 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:48 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:00:22 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:48 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:00:09 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:04 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:06 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:07:08 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:33 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:30:30 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 17:03:18 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:10 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:02:20 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:10:52 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:10 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:24 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:01:16 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-05 18:10:27 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-05 18:00:34 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-09-05 18:08:06 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-09-05 18:02:27 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-09-05 18:09:31 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.049 |  |
| 2026-09-05 18:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.059 |  |
| 2026-09-05 18:01:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.067 |  |
| 2026-09-05 18:01:08 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.072 |  |
| 2026-09-05 18:03:31 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)